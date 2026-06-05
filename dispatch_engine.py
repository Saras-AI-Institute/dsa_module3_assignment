class Package:
    def __init__(self, package_id: int, weight: float):
        self.package_id = package_id
        self.weight = weight

def binary_search_package(warehouse_rack: list[Package], target_id: int) -> int:
    """
    Finds the index of the package with package_id == target_id.
    
    TODO:
    1. Implement standard Binary Search log(n) logic.
    2. If the target_id is found, return its index.
    3. CRITICAL THINKING: If it's NOT found, return the index where it SHOULD 
       be inserted to keep the warehouse_rack sorted.
    """
    # YOUR CODE HERE
    pass


def schedule_maximum_deliveries(intervals: list[tuple[int, int]]) -> int:
    """
    Given a list of tuples representing (start_time, end_time), return the MAXIMUM
    number of completely non-overlapping deliveries a single drone can fulfill.
    
    Example: [(1, 3), (2, 5), (3, 6)] -> Maximum is 2 deliveries: (1, 3) then (3, 6).
    
    TODO:
    1. Select the correct sorting strategy to allow a greedy choice.
    2. Sort the intervals list in-place or create a sorted copy.
    3. Iteratively pick windows that don't conflict with the last selected window's end time.
    """
    # YOUR CODE HERE
    pass
