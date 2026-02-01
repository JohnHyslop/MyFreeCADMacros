# MyFreeCADMacros
My FreeCAD Macros

## Description
This repository contains a collection of macros designed for use with FreeCAD, aimed at enhancing productivity and simplifying common tasks.  

---

## Macros

### 1. Check Interference Macro
The **Check Interference** macro allows users to identify and analyse interferences between selected bodies in the active FreeCAD document. It examines the geometry of the selected objects to determine if they intersect or overlap.  

If any interferences are detected, a message box will display the results, informing the user of the specific bodies involved.  

**Use Case:**  
- Validating assemblies.  
- Ensuring adequate clearances in complex models.  

**Usage:**  
1. Select the bodies you want to check.  
2. Run the macro.  
3. Read the message box for interference results.  

---

### 2. StitchCut Macro
The **StitchCut** macro is designed for creating evenly spaced “stitch cuts” along lines in sheet metal flat patterns. These cuts make it easier to fold the material by hand.  

**Features:**  
- Specify **Start & End Offset** (gap from the edges).  
- Automatically calculates **cut lengths** based on the number of cuts.  
- Users can define **number of cuts**, and optionally adjust cut lengths.  
- Inserts the cuts directly into the active sketch in FreeCAD.  

**Use Case:**  
- Hand-folding sheet metal parts accurately and efficiently.  

**Author:** John Hyslop

**Usage:**  
1. Enter **edit mode** on the sketch containing your fold line.  
2. Select the line you want to apply stitch cuts to.  
3. Run the macro and fill in the dialog prompts:  
   - Start & End Offset  
   - Number of cuts  
4. The macro will delete the original line and insert the evenly spaced stitch cuts.  

---

## How to Use These Macros
1. Copy the `.FCMacro` files into your FreeCAD macros folder or a dedicated subfolder.  
2. Open FreeCAD and navigate to `Macro → Macros...`.  
3. Select the macro you want to run and click **Execute**.  
4. Follow the prompts provided by each macro.  

---

## License
This repository is open for personal and educational use. Please give credit to the author if used in your projects.
