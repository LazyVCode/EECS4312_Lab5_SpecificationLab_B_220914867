## Student Name: Vikram Singh Chauhan
## Student ID: 220914867

from typing import Dict, List, Union

Number = Union[int, float]

def is_allocation_feasible(
    resources: Dict[str, Number],
    requests: List[Dict[str, Number]]
) -> bool:
    """
    Determine whether a set of resource requests can be satisfied given limited capacities.

    Args:
        resources : Mapping from resource name to total available capacity.
        requests : List of requests. Each request is a mapping from resource name to the amount required.

    Returns:
        True if the allocation is feasible, False otherwise.
        
    Constraints:
        1. Total demand for any resource cannot exceed its capacity.
        2. (New) At least one resource must remain unallocated (have spare capacity) after assignment.
           If the allocation consumes 100% of ALL available resources, it is invalid.
    """
    
    # 1. Calculate Total Demand
    total_demand: Dict[str, Number] = {}

    for req in requests:
        # Validation for the test_non_dict_request_raises test case
        if not isinstance(req, dict):
            raise ValueError("All requests must be dictionaries.")

        for resource_name, amount in req.items():
            # Check for invalid requests (asking for resources that don't exist)
            if resource_name not in resources:
                return False
            
            total_demand[resource_name] = total_demand.get(resource_name, 0) + amount

    # 2. Check Feasibility & Spare Capacity
    has_spare_capacity = False

    for resource_name, capacity in resources.items():
        demand = total_demand.get(resource_name, 0)

        if demand > capacity:
            return False  # Constraint 1 violation: Over-allocated
        
        if demand < capacity:
            has_spare_capacity = True  # Found a resource with breathing room

    # 3. Final Verification of New Requirement
    if len(resources) > 0 and not has_spare_capacity:
        return False

    return True
