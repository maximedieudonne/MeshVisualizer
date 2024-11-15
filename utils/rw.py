import nibabel as nb
import numpy as np
import trimesh

def load_mesh(gifti_file):
    """
    load gifti_file and create a trimesh object
    :param gifti_file: str, path to the gifti file on the disk
    :return: the corresponding trimesh object
    """
    g = nb.load(gifti_file)
    coords, faces = g.get_arrays_from_intent(
        nb.nifti1.intent_codes['NIFTI_INTENT_POINTSET'])[0].data, \
        g.get_arrays_from_intent(
            nb.nifti1.intent_codes['NIFTI_INTENT_TRIANGLE'])[0].data
    metadata = g.meta.metadata
    metadata['filename'] = gifti_file
    return trimesh.Trimesh(faces=faces, vertices=coords,
                           metadata=metadata, process=False)

# Fonction pour lire un fichier GIFTI (scalars.gii)
def read_gii_file(file_path):
    try:
        gifti_img = nb.load(file_path)
        scalars = gifti_img.darrays[0].data
        return scalars
    except Exception as e:
        print(f"Erreur lors du chargement de la texture : {e}")
        return None



