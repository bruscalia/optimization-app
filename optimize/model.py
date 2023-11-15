from typing import Any, List, Dict

import numpy as np
from scipy.optimize import linprog


# Solve knapsack
def solve_model(items: List[Dict[str, Any]], capacity: int) -> List[Any]:
    """The main optimization function called from the app

    Parameters
    ----------
    items : List[Dict[str, Any]]
        Knapsack items

    capacity : int
        Knapsack capacity

    Returns
    -------
    List[Any]
        List of items selected
    """
    costs = []
    weights = []
    labels = []
    for item in items:
        costs.append(item["cost"])
        weights.append(item["weight"])
        labels.append(item["item"])

    sol = linprog(
        -np.array(costs),
        A_ub=np.atleast_2d(weights),
        b_ub=np.array([capacity]),
        bounds=[(0, 1) for _ in range(len(costs))],
        integrality=[1 for _ in range(len(costs))]
    )
    output = [labels[i] for i in range(len(sol.x)) if np.isclose(sol.x[i], 1, atol=1e-1)]
    return output
