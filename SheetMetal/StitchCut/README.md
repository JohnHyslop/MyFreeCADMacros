# StitchCut Macro

The StitchCut macro creates evenly spaced stitch cuts along a selected line in a sketch,  
primarily for sheet metal flat patterns to allow easier hand folding.

## Features
- Start & end offset from edges
- Automatic cut length calculation
- User-defined number of cuts
- Inserts cuts directly into the active sketch

## Usage
1. Enter **edit mode** on a sketch.
2. Select the line to apply stitch cuts to.
3. Run the macro.
4. Enter:
   - Start & End Offset
   - Number of cuts
   - **Cut Width**: Defines the thickness of each cut. A value of **0** means the cuts are represented as single lines (no thickness), while any other value applies the specified width.
5. The original line is replaced with stitch cuts.

## Author
John Hyslop

## FreeCAD Version
Tested on FreeCAD 1.02 and later.

## License
Free for personal and educational use. Please credit the author by including this README in your project or linking to the repository.

## Changelog
### Version 1.1 (February 2026)
- Now uses FreeCAD’s Persistent Configuration System
- Cut Widths can now be applied
- Updated Description: Improved clarity and added configuration options
- Renamed Macro to StitchCut.FCMacro for consistency
- Fixed errors and UI improvements: Replaced `QLineEdit` with `QSpinBox` and `QDoubleSpinBox` for better numeric input handling
- Added Open Transaction for Undo functionality

### Version 1.0 (March 2025)
- Initial release

## Last Updated
February 2026
