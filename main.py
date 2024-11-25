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

def list_to_comma_string(lst):
    """
    Convert a list of strings into a single comma-delimited string.

    Args:
        lst (list): A list of strings.

    Returns:
        str: A comma-delimited string of the input list.
    """ 
    return ",".join(lst)

def write_to_csv(headers, data, file_name):
    """
    Write headers and data to a CSV file.

    Args:
        headers (list): List of headers for the CSV file.
        data (str): Comma-delimited string containing the data rows.
        file_name (str): The name of the file where the CSV will be written.

    Returns:
        None
    """ 
    rows = data.split(",")
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerow(rows)

def test_should_return_next_ten_numbers():
    assert next_ten_numbers(5) == "6,7,8,9,10,11,12,13,14,15"
    assert next_ten_numbers(0) == "1,2,3,4,5,6,7,8,9,10"
    assert next_ten_numbers(-3) == "-2,-1,0,1,2,3,4,5,6,7"

def test_list_to_comma_string():
    assert list_to_comma_string(["a", "b", "c"]) == "a,b,c"
    assert list_to_comma_string(["1", "2", "3"]) == "1,2,3"
    assert list_to_comma_string([]) == ""

def test_write_to_csv(tmp_path):
    headers = ["Number"]
    data = "6,7,8,9,10,11,12,13,14,15"
    file_name = tmp_path / "test.csv"
    
    write_to_csv(headers, data, file_name)
    
    # Verify the file content
    with open(file_name, mode="r") as file:
        lines = file.readlines()
        assert lines[0].strip() == "Number"
        assert lines[1].strip() == "6,7,8,9,10,11,12,13,14,15"
