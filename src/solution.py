## Student Name: Vikram Singh Chauhan
## Student ID: 220914867

"""
Stub file for the is allocation feasible exercise.

Implement the function `is_allocation_feasible` to Determine whether a set of resource requests can be satisfied 
given limited capacities. Take into account any possible constraints. See the lab handout
for full requirements.
"""
    
from typing import Dict, List, Union

Number = Union[int, float]

def is_allocation_feasible(
    resources: Dict[str, Number],
    requests: List[Dict[str, Number]]
) -> bool:
    """
    Determine whether a set of resource requests can be satisfied given limited capacities.

    Args:
        resources : Dict[str, Number], Mapping from resource name to total available capacity.
        requests : List[Dict[str, Number]], List of requests. Each request is a mapping from resource name to the amount required.

    Returns:
        True if the allocation is feasible, False otherwise.
    
    Raises:
        ValueError: If a request in the list is not a dictionary.
    """
    
    # Dictionary to track the total amount needed for every requested resource
    total_demand: Dict[str, Number] = {}

    # 1. Sum up the total demand for each resource type across all requests
    for req in requests:
        # Validation: Ensure the request is actually a dictionary (to satisfy test specs)
        if not isinstance(req, dict):
            raise ValueError("Invalid request format: each request must be a dictionary.")

        for resource_name, amount in req.items():
            # Accumulate demand
            current_total = total_demand.get(resource_name, 0)
            total_demand[resource_name] = current_total + amount

    # 2. Check if the total demand exceeds the available capacity for any resource
    for resource_name, amount_needed in total_demand.items():
        # Get the available capacity; if the resource isn't listed, capacity is 0
        available_capacity = resources.get(resource_name, 0)
        
        # If demand is greater than capacity (or if capacity is 0 because it doesn't exist)
        if amount_needed > available_capacity:
            return False

    return True
