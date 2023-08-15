import os

import numpy as np
from skimage import measure

def save_obj(sample, file_name):
    path = "../samples"
    """ Use marching cubes to obtain the surface mesh and save it to an *.obj file """
    # convert volume to mesh
    sample = np.pad(sample, ((1, 1), (1, 1), (1, 1)))
    verts, faces, normals, values = measure.marching_cubes(sample, 0)
    # scale to normalized cube [-1.0, 1.0]^3
    verts /= sample.shape
    verts -= [0.5, 0.0, 0.5]
    verts *= 2.0
    # fix .obj indexing
    faces += 1

    # Save output as obj-file
    file_path = os.path.join(path, f'{file_name}.obj')
    with open(file_path, 'w') as f:
        for item in verts:
            f.write("v {0} {1} {2}\n".format(item[0], item[1], item[2]))
        for item in normals:
            f.write("vn {0} {1} {2}\n".format(item[0], item[1], item[2]))
        for item in faces:
            f.write("f {0}//{0} {1}//{1} {2}//{2}\n".format(item[0], item[1], item[2]))