"""
Data Preprocessing Utilities
============================

This module demonstrates how Sphinx handles multiple files within the same 
package (ml/processing.py).
"""

from typing import List
import numpy as np

def normalize_data(raw_data: List[float]) -> List[float]:
    """
    Normalizes a list of values to have zero mean and unit variance.

    Parameters
    ----------
    raw_data : List[float]
        The input data to be normalized.

    Returns
    -------
    List[float]
        The normalized dataset.
    """
    data_np = np.array(raw_data)
    return ((data_np - np.mean(data_np)) / np.std(data_np)).tolist()
