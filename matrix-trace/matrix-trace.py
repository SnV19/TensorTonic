import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    A = np.asarray(A)
    return float(np.trace(A))