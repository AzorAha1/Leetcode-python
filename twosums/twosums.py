

def TwoSum(nums, target):
    """Two sum problem"""
    thenums = {}
    for index, value in enumerate(nums):
        remainder = target - value
        if remainder in thenums:
            return [thenums[remainder], index]
        thenums[value] = index
    return thenums
        