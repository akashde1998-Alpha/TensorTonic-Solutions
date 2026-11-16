import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    y_p=np.asarray(y_pred, dtype=float)
    y_t=np.asarray(y_true, dtype=float)
    assert y_p.shape==y_t.shape
    y_e=(y_p-y_t)**2
    return float(np.mean (y_e))
    
    