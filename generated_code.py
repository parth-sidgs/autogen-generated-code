        from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merges k sorted linked lists into one sorted linked list.

    Args:
        lists: A list of k sorted linked lists.

    Returns:
        The head of the merged sorted linked list, or None if the input list is empty or all lists are None.
    """

    if not lists or all(lst is None for lst in lists):
        return None

    import heapq

    # Min-heap to store the current smallest nodes from each list.
    min_heap = []

    # Add the head of each non-null list to the heap.
    for lst in lists:
        if lst:
            heapq.heappush(min_heap, (lst.val, id(lst), lst))  # Use id(lst) to avoid comparison issues with equal values

    # Create a dummy head for the merged list.
    dummy_head = ListNode()
    current = dummy_head

    # Iterate while the heap is not empty.
    while min_heap:
        # Get the node with the smallest value from the heap.
        _, _, smallest_node = heapq.heappop(min_heap)

        # Append the smallest node to the merged list.
        current.next = smallest_node
        current = current.next

        # If the smallest node has a next node, add it to the heap.
        if smallest_node.next:
            heapq.heappush(min_heap, (smallest_node.next.val, id(smallest_node.next), smallest_node.next))

    return dummy_head.next



