from count_evens import number_of_evens
   

def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)


def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)


def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)


def test_between(collection, item):
    minimum, maximum = min(collection), max(collection)
    assert minimum < item and item < maximum, "{0} not between {1} and {2}".format(item, minimum, maximum)

if __name__ == '__main__':
    test_are_equal(number_of_evens([1,2,3,4,5]), 2)
    test_not_equal(number_of_evens([1,2,3,4,5]), 3)
    test_is_in([1,2,3,4,5], 5)
    test_between([1,2,3,4,5], 4)
    print('All tests passed!')