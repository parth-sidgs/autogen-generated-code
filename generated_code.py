def find_median_sorted_arrays(nums1, nums2):
    """
    Finds the median of two sorted arrays.

    Args:
        nums1: The first sorted array.
        nums2: The second sorted array.

    Returns:
        The median of the two sorted arrays.

    Raises:
        ValueError: If both input arrays are empty.

    Time Complexity: O(log(min(m, n))) where m and n are the lengths of nums1 and nums2 respectively.
    Space Complexity: O(1)
    """
    m, n = len(nums1), len(nums2)

    if m > n:  # Ensure nums1 is the shorter array for efficiency
        nums1, nums2 = nums2, nums1
        m, n = n, m

    if m == 0:
        if n == 0:
            raise ValueError("Both input arrays cannot be empty.")
        if n % 2 == 0:
            return (nums2[n // 2 - 1] + nums2[n // 2]) / 2
        else:
            return nums2[n // 2]

    low, high = 0, m

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (m + n + 1) // 2 - partitionX

        maxLeftX = -float('inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == m else nums1[partitionX]

        maxLeftY = -float('inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == n else nums2[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (m + n) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1