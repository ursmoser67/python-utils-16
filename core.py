from typing import List, Union

def calculate_average(values: List[Union[int, float]]) -> float:
    """
    Calculate the average of numbers in a list.
    
    Args:
        values: A list of integers or floats.
    
    Returns:
        The average as a float.
    """
    if not values:
        return 0.0
    return sum(values) / len(values)

def find_max(values: List[Union[int, float]]) -> Union[int, float]:
    """
    Find the maximum number in a list.
    
    Args:
        values: A list of integers or floats.
    
    Returns:
        The maximum value in the list.
    """
    if not values:
        raise ValueError("The list must not be empty.")
    return max(values)

def find_min(values: List[Union[int, float]]) -> Union[int, float]:
    """
    Find the minimum number in a list.
    
    Args:
        values: A list of integers or floats.
    
    Returns:
        The minimum value in the list.
    """
    if not values:
        raise ValueError("The list must not be empty.")
    return min(values)