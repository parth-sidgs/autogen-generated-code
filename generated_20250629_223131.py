from typing import Optional

class ListNode:
    """
    Represents a node in a singly linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverses a singly linked list.

    Args:
        head: The head of the linked list.

    Returns:
        The head of the reversed linked list.  Returns None if the input is None.
    """
    prev = None
    curr = head

    while curr:
        next_node = curr.next  # Store the next node temporarily
        curr.next = prev        # Reverse the current node's pointer
        prev = curr            # Move 'prev' one step forward
        curr = next_node      # Move 'curr' one step forward

    return prev


# Example usage and testing:
def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Helper function to convert a linked list to a Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


test_cases = [
    [],
    [1],
    [1, 2],
    [1, 2, 3, 4, 5]
]

for values in test_cases:
    original_list = create_linked_list(values)
    reversed_list = reverse_linked_list(original_list)
    print(f"Original List: {values}  Reversed List: {linked_list_to_list(reversed_list)}")
