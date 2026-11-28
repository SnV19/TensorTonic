import numpy as np

def normalize_3d(v: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as v.
    """
    v=np.asarray(v)
    norm = np.linalg.norm(v,axis=-1,keepdims=True) 
    return np.divide(
        v,
        norm,
        out = np.zeros_like(v,dtype = float), #initialization with zeros 
        where = norm !=0
    )