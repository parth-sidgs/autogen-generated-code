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
        nums1, nums2, m, n = nums2, nums1, n, m

    if m == 0 and n == 0:
        raise ValueError("Both input arrays cannot be empty.")

    low, high = 0, m
    while low <= high:
        partition_x = (low + high) // 2
        partition_y = (m + n + 1) // 2 - partition_x

        max_left_x = nums1[partition_x - 1] if partition_x > 0 else -float('inf')
        min_right_x = nums1[partition_x] if partition_x < m else float('inf')

        max_left_y = nums2[partition_y - 1] if partition_y > 0 else -float('inf')
        min_right_y = nums2[partition_y] if partition_y < n else float('inf')


        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            if (m + n) % 2 == 0:
                return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
            else:
                return max(max_left_x, max_left_y)
        elif max_left_x > min_right_y:
            high = partition_x - 1
        else:
            low = partition_x + 1