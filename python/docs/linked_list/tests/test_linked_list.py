import pytest
from linked_lists.linked_list import LinkedList

@pytest.fixture
def linked_list():
    """Creates a new linked list instance for each test."""
    return LinkedList()

def test_insert_single(linked_list):
    """Test the insertion of a single element into the linked list.
    Validates that the head of the list is correctly assigned to
    the new element and that the next pointer of the head is None
    (indicating no subsequent elements).
    """
    linked_list.insert(1)
    assert linked_list.head.value == 1
    assert linked_list.head.next is None

def test_insert_multiple(linked_list):
    """Test the insertion of multiple elements into the linked list.
    Validates that the head of the list points to the most recently
    added element and that the elements are linked in the reverse
    order of their insertion.
    """
    linked_list.insert(1)
    linked_list.insert(2)
    assert linked_list.head.value == 2
    assert linked_list.head.next.value == 1

def test_includes_true(linked_list):
    """Test that the 'includes' method returns True for elements that are
    present in the list. Validates that the method correctly identifies
    existing elements.
    """
    linked_list.insert(1)
    linked_list.insert(2)
    assert linked_list.includes(1) is True
    assert linked_list.includes(2) is True

# Expected failure test
def test_includes_false(linked_list):
    """Test that the 'includes' method returns False for elements that are not
    present in the list. Validates that the method does not falsely identify
    non-existing elements.
    """
    linked_list.insert(1)
    assert linked_list.includes(3) is False

# Edge case tests
def test_to_string_empty(linked_list):
    """Test the string representation of an empty linked list. Validates that the
    method correctly represents an empty list as 'NULL'.
    """
    assert linked_list.to_string() == "NULL"

def test_insert_null(linked_list):
    """Validates that inserting nothing raises a TypeError.
    """
    with pytest.raises(TypeError):
        linked_list.insert()

# @pytest.mark.skip("todo")
def test_to_string_non_empty(linked_list):
    """Test the string representation of a non-empty linked list. Validates that
    the method correctly formats the string representation of the list, showing
    each element in the order they appear, ending with 'NULL'.
    """
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    assert linked_list.to_string() == "{ 3 } -> { 2 } -> { 1 } -> NULL"
