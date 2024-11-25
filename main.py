import os
import csv

def next_ten_numbers(num):
    """
    Generate the next 10 numbers as a comma-delimited string starting from the given number.

    Args:
        num (int): The starting number.

    Returns:
        str: A comma-delimited string of the next 10 numbers.
    """
    return ",".join(str(num + i) for i in range(1, 11))





















def test_should_return_next_ten_numbers():
    assert next_ten_numbers(5) == "6,7,8,9,10,11,12,13,14,15"
    assert next_ten_numbers(0) == "1,2,3,4,5,6,7,8,9,10"
    assert next_ten_numbers(-3) == "-2,-1,0,1,2,3,4,5,6,7"

def test_list_to_comma_string():
    assert list_to_comma_string(["a", "b", "c"]) == "a,b,c"
    assert list_to_comma_string(["1", "2", "3"]) == "1,2,3"
    assert list_to_comma_string([]) == ""
