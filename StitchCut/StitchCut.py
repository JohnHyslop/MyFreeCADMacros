"""
StitchCut.py

Author: John Hyslop
Description: 
    This FreeCAD macro allows you to create evenly spaced "stitch cuts" along a selected 
    straight line in a sketch. The user can specify the start & end offsets, gap between cuts,
    and number of cuts. The macro will calculate the cut lengths and insert them directly
    into the sketch.

    Created with a little extra help from ChatGPT.
"""

import FreeCAD, FreeCADGui
from PySide import QtGui
import math, Part

# --- Dialog ---
class StitchCutDialog(QtGui.QDialog):
    def __init__(self, line_length, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Stitch Cut Parameters")
        self.line_length = line_length

        self.edge_offset_edit = QtGui.QLineEdit("3")  # Changed label
        self.gap_edit = QtGui.QLineEdit("3")
        self.num_cuts_edit = QtGui.QLineEdit("5")
        self.cut_length_display = QtGui.QLabel("0")

        layout = QtGui.QFormLayout()
        layout.addRow("Start & End Offset:", self.edge_offset_edit)
        layout.addRow("Gap between cuts:", self.gap_edit)
        layout.addRow("Number of Cuts:", self.num_cuts_edit)
        layout.addRow("Calculated Cut Length:", self.cut_length_display)

        buttons = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)

        # update calculation dynamically
        self.edge_offset_edit.textChanged.connect(self.update_cut_length)
        self.gap_edit.textChanged.connect(self.update_cut_length)
        self.num_cuts_edit.textChanged.connect(self.update_cut_length)
        self.update_cut_length()

    def update_cut_length(self):
        try:
            edge_offset = float(self.edge_offset_edit.text())
            gap = float(self.gap_edit.text())
            num = int(self.num_cuts_edit.text())
            usable = self.line_length - 2*edge_offset - (num - 1) * gap
            if usable <= 0:
                self.cut_length_display.setText("N/A")
            else:
                self.cut_length_display.setText(f"{usable/num:.3f}")
        except:
            self.cut_length_display.setText("Error")

    def getValues(self):
        try:
            edge_offset = float(self.edge_offset_edit.text())
            gap = float(self.gap_edit.text())
            num = int(self.num_cuts_edit.text())
            usable = self.line_length - 2*edge_offset - (num - 1) * gap
            if usable <= 0:
                return None
            cut_length = usable / num
            return edge_offset, gap, num, cut_length
        except:
            return None

# --- Get selected line ---
def get_selected_line():
    sel = FreeCADGui.Selection.getSelectionEx()
    if len(sel) != 1:
        QtGui.QMessageBox.critical(None, "Error", "Select exactly one line in a sketch.")
        return None, None
    sk = sel[0].Object
    if sk.TypeId != "Sketcher::SketchObject":
        QtGui.QMessageBox.critical(None, "Error", "Selection is not a sketch.")
        return None, None
    if len(sel[0].SubElementNames) != 1:
        QtGui.QMessageBox.critical(None, "Error", "Select exactly one edge.")
        return None, None
    edge_name = sel[0].SubElementNames[0]
    idx = int(edge_name.replace("Edge","")) - 1
    geo = sk.Geometry[idx]
    if geo.TypeId != 'Part::GeomLineSegment':
        QtGui.QMessageBox.critical(None, "Error", "Selected geometry is not a straight line.")
        return None, None
    return sk, idx

# --- Main macro ---
def stitch_cut():
    sk, idx = get_selected_line()
    if not sk:
        return

    line = sk.Geometry[idx]
    p1 = line.StartPoint
    p2 = line.EndPoint

    vec = p2.sub(p1)
    length = vec.Length
    direction = vec.normalize()

    dlg = StitchCutDialog(length)
    if dlg.exec_() != QtGui.QDialog.Accepted:
        return

    values = dlg.getValues()
    if not values:
        QtGui.QMessageBox.critical(None, "Error", "Invalid parameters, cuts won't fit.")
        return
    edge_offset, gap, num_cuts, cut_length = values

    # Remove original line
    sk.delGeometry(idx)

    # Add stitch cuts
    for i in range(num_cuts):
        start_dist = edge_offset + i*(cut_length + gap)
        end_dist = start_dist + cut_length
        if end_dist > length - edge_offset:
            end_dist = length - edge_offset
        ptA = FreeCAD.Vector(p1.x + direction.x*start_dist,
                             p1.y + direction.y*start_dist,
                             p1.z + direction.z*start_dist)
        ptB = FreeCAD.Vector(p1.x + direction.x*end_dist,
                             p1.y + direction.y*end_dist,
                             p1.z + direction.z*end_dist)
        sk.addGeometry(Part.LineSegment(ptA, ptB), False)

    sk.Document.recompute()
    QtGui.QMessageBox.information(None, "Done", "Stitch cuts applied!")

# --- Run ---
stitch_cut()

