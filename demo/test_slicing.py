##
## Need to install pytest with 'pip install pytest' to use these tests.
## Use the command 'pytest' to run the tests.
##


# Get the baz item using a positive index
def get_by_positive_index():
    list = ["foo", "bar", "baz", "bak", "toz"]
    return list[2]


def test_get_by_positive_index():
    assert get_by_positive_index() == "baz"


# Get the baz item using a negative index
def get_by_negative_index():
    list = ["foo", "bar", "baz", "bak", "toz"]
    return list[-3]


def test_get_by_negative_index():
    assert get_by_negative_index() == "baz"


# Slice the list with positive indexes to return ["bar", "baz", "bak"]
def slice_by_positive_index():
    list = ["foo", "bar", "baz", "bak", "toz"]
    return list[1:4]


def test_slice_by_positive_index():
    assert slice_by_positive_index() == ["bar", "baz", "bak"]


# Slice the list with positive indexes to return ["bar", "baz", "bak"]
def slice_by_negative_index():
    list = ["foo", "bar", "baz", "bak", "toz"]
    return list[-4:-1]


def test_slice_by_negative_index():
    assert slice_by_negative_index() == ["bar", "baz", "bak"]


# Slice the list to retrieve using only the left part ["bar", "baz", "bak"]
def slice_by_left_index():
    list = ["foo", "bar", "baz", "bak", "toz"]
    return list[1:]


# Slice the list to retrieve using only the left part ["bar", "baz", "bak", "toz"]
def test_slice_by_left_index():
    assert slice_by_left_index() == ["bar", "baz", "bak", "toz"]


# Slice the list to retrieve using only the left part ["bar", "baz", "bak", "toz"]
def slice_by_rigth_index():
    list = ["foo", "bar", "baz", "bak", "toz"]
    return list[:-3]


def test_slice_by_rigth_index():
    assert slice_by_rigth_index() == ["foo", "bar"]


# Copy the list with slice
def copy_list(list):
    return list[:]


def test_copy_list():
    list = ["foo", "bar", "baz", "bak", "toz"]
    assert copy_list(list) == list
    assert copy_list(list) is not list


# Retrieve ["foo", "baz", "toz"]
def slice_get_every_two_item():
    list = ["foo", "bar", "baz", "bak", "toz"]
    return list[::2]


def test_slice_get_every_two_item():
    assert slice_get_every_two_item() == ["foo", "baz", "toz"]


def reverse_list(list):
    return list[::-1]


def test_reverse_list():
    list = ["foo", "baz", "toz"]
    assert reverse_list(list) == [
        "toz",
        "baz",
        "foo",
    ]
