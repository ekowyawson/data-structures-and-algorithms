import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_internals_modified():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    for item in hashtable._buckets():
        if item:
            actual.append(sorted(item['display'](), key=lambda x: hashtable.hash(x[0])))

    # Sort the expected list in the same way as actual to ensure the order does not affect comparison
    expected = sorted([
        [("silent", True), ("listen", "to me")],
        [("ahmad", 30)]
    ], key=lambda bucket: hashtable.hash(bucket[0][0]))

    assert actual == expected
