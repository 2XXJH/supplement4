import os
import csv

def next_ten_numbers(num):
    return ",".join(str(num + i) for i in range(1, 11))





















def test_should_return_next_ten_numbers():
    assert next_ten_numbers(5) == "6,7,8,9,10,11,12,13,14,15"
    assert next_ten_numbers(0) == "1,2,3,4,5,6,7,8,9,10"
    assert next_ten_numbers(-3) == "-2,-1,0,1,2,3,4,5,6,7"

