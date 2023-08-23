import FreeCAD as App
import Mesh
import os

doc = App.ActiveDocument
parent_objects = [obj for obj in doc.Objects if obj.InList == []]
__objs__ = [obj for obj in parent_objects]

# Construct the new file path
file_path = FreeCAD.ActiveDocument.FileName
filename = "full_assembly.stl"
new_file_path = os.path.join(os.path.dirname(file_path), filename)

# Export using the new file path
Mesh.export(__objs__, new_file_path)

del __objs__
print("full_assembly.stl updated")
