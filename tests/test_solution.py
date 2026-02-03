## Student Name: Vikram Singh Chauhan
## Student ID: 220914867

"""
Public test suite for the meeting slot suggestion exercise.

Students can run these tests locally to check basic correctness of their implementation.
The hidden test suite used for grading contains additional edge cases and will not be
available to students.
"""
import pytest
# Adjust this import based on your exact folder structure
# If solution.py is in a 'src' folder:
from src.solution import is_allocation_feasible
# If solution.py is in the same folder as this test file:
# from solution import is_allocation_feasible


def test_basic_feasible_single_resource():
    # Basic Feasible Single-Resource
    # Constraint: total demand <= capacity
    # Reason: check basic functional requirement
    resources = {'cpu': 10}
    requests = [{'cpu': 3}, {'cpu': 4}, {'cpu': 3}]
    assert is_allocation_feasible(resources, requests) is True

def test_multi_resource_infeasible_one_overloaded():
    # Multi-Resource Infeasible (one overload)
    # Constraint: one resource exceeds capacity
    # Reason: check detection of per-resource infeasibility
    resources = {'cpu': 8, 'mem': 30}
    requests = [{'cpu': 2, 'mem': 8}, {'cpu': 3, 'mem': 10}, {'cpu': 3, 'mem': 14}]
    assert is_allocation_feasible(resources, requests) is False

def test_missing_resource_in_availability():
    # Missing Resource in Requests
    # Constraint: request references unavailable resource
    # Reason: allocation must be infeasible
    resources = {'cpu': 10}
    requests = [{'cpu': 2}, {'gpu': 1}]
    assert is_allocation_feasible(resources, requests) is False

def test_non_dict_request_raises():
    # Non-Dict Request Raises Error
    # Constraint: structural validation
    # Reason: request must be a dict
    resources = {'cpu': 5}
    requests = [{'cpu': 2}, ['mem', 1]]  # malformed request
    with pytest.raises(ValueError):
        is_allocation_feasible(resources, requests)

# Additional 5 Test Cases

def test_empty_requests_always_feasible():
    # Empty Request List
    # Constraint: No demand
    # Reason: Should be feasible regardless of resources (0 <= capacity)
    resources = {'cpu': 10}
    requests = []
    assert is_allocation_feasible(resources, requests) is True

def test_exact_capacity_match():
    # Exact Boundary Condition
    # Constraint: Total demand == Total capacity
    # Reason: Should be feasible (limits are usually inclusive)
    resources = {'cpu': 10, 'mem': 16}
    requests = [{'cpu': 5, 'mem': 8}, {'cpu': 5, 'mem': 8}]
    assert is_allocation_feasible(resources, requests) is True

def test_floating_point_resources():
    # Floating Point Precision
    # Constraint: Use float values for resources
    # Reason: Ensure function handles 'Number' type correctly as per type hint
    resources = {'bandwidth': 10.5}
    requests = [{'bandwidth': 5.2}, {'bandwidth': 5.2}] # Total 10.4
    assert is_allocation_feasible(resources, requests) is True

def test_partial_resource_overlap():
    # Partial Resource Overlap
    # Constraint: Requests ask for different subsets of available resources
    # Reason: Ensure logic handles sparse dictionaries correctly (not all requests need all resources)
    resources = {'cpu': 10, 'gpu': 5, 'disk': 100}
    requests = [
        {'cpu': 5},           # Asks only for CPU
        {'gpu': 2, 'disk': 50} # Asks for GPU and Disk, no CPU
    ]
    assert is_allocation_feasible(resources, requests) is True

def test_zero_capacity_resource():
    # Zero Capacity Resource
    # Constraint: Resource exists but has 0 capacity
    # Reason: Any positive request for this resource should fail immediately
    resources = {'cpu': 0}
    requests = [{'cpu': 1}]
    assert is_allocation_feasible(resources, requests) is False
