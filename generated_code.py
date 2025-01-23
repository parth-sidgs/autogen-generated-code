"""
Finds the median of two sorted arrays.

Args:
    nums1: The first sorted array.
    nums2: The second sorted array.

Returns:
    The median of the two sorted arrays.
"""
def findMedianSortedArrays(nums1, nums2):
    """
    This function finds the median of two sorted arrays using binary search.

    The approach is to partition both arrays such that all elements in the left partitions 
    are smaller than or equal to all elements in the right partitions.  We adjust the 
    partition point in the smaller array using binary search until this condition is met.

    Time Complexity: O(log(min(m, n))) - Binary search on the smaller array.
    Space Complexity: O(1)
    """

    m, n = len(nums1), len(nums2)
    # Ensure nums1 is the smaller array for efficient binary search
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m

    low, high = 0, m

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (m + n + 1) // 2 - partitionX  # Calculate partition point in nums2

        maxLeftX = nums1[partitionX - 1] if partitionX > 0 else float('-inf')
        minRightX = nums1[partitionX] if partitionX < m else float('inf')

        maxLeftY = nums2[partitionY - 1] if partitionY > 0 else float('-inf')
        minRightY = nums2[partitionY] if partitionY < n else float('inf')

        if maxLeftX <= minRightY and maxLeftY <= minRightX:  # Correct partitions found
            if (m + n) % 2 == 0:  # Even number of elements
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            else:  # Odd number of elements
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:  # Move partitionX to the left
            high = partitionX - 1
        else:  # Move partitionX to the right
            low = partitionX + 1

    return None  # Should never reach here if arrays are sorted

