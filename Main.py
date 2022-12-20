
import open3d
import numpy as np

mesh = open3d.io.read_triangle_mesh("C:/Users/aidan/Downloads/cube.ply")
print(mesh)
#print(np.asarray(mesh.vertices))
print(np.asarray(mesh.triangles))
print(np.asarray(mesh.vertices))


mesh.compute_vertex_normals()
open3d.visualization.draw_geometries([mesh])


