import sys
sys.path.append('/Applications/FreeCAD.app/Contents/Resources/lib')  # Adjust as needed
sys.path.append('/Applications/FreeCAD.app/Contents/Resources/lib/python3.8/site-packages')  # Adjust Python version and path as needed

import FreeCAD
import Mesh

# Check if a file path argument was provided
if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    print("Please provide the path to the FreeCAD file.")
    sys.exit(1)

output_dir = "stls"  # Update this path if needed

FreeCAD.openDocument(input_file)

def is_top_level_obj(obj):
    """Check if an object is a top-level object."""
    return not any(obj in child.InList for child in FreeCAD.ActiveDocument.Objects)

for obj in FreeCAD.ActiveDocument.Objects:
    # Check if object is a Part and is top-level
    # print(obj.TypeId)
    # print(obj.Label)
    if obj.TypeId.startswith('App::Part'):
        mesh = Mesh.Mesh(obj.Shape.tessellate(1.0))  # 1.0 is the tolerance, adjust as needed
        output_path = output_dir + "/" + obj.Label + ".stl"
        mesh.write(output_path)

FreeCAD.closeDocument(FreeCAD.ActiveDocument.Name)
