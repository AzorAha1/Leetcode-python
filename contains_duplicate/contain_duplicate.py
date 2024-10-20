from typing import List


def hasDuplicate(nums: List[int]) -> bool:
    """contain duplicate"""
    mynums = set()
    for num in nums:
        if num in mynums:
            return True
        else:
            mynums.add(num)
    return False