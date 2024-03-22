import numpy as np

def improved(vec, step=1):
    return np.mean(vec * np.roll(vec, step))