
import pytest

'''
Attempt to test how your codes behaves with unit tests
Test passing and failure situations
'''

def string_to_lst(input_str, delimiter):
    return input_str.split(delimiter)


def test_when_comma_seperated_string_is_given_then_a_lst_with_two_items_are_returned():
    assert len(string_to_lst("hello,world", ",")) == 2

def test_a_blank_str_returns_len_of_1():
    assert len(string_to_lst("", ",")) == 1


def test_a_null_str_returns_len_of_0():
    with pytest.raises(Exception):
        string_to_lst(None, ",")

'''
#uncomment to see a failure
def test_a_null_str_returns_len_of_0():
    assert len(string_to_lst(None, ",")) == 1
'''



'''
Don't test network/file/db calls.

SEPERATE your logic from the network/file/db calls to make testing easier

Refer back to Dependency Injection (D in SOLID) for helping with network/file/db calls abstraction
'''

### we are going to create a simple mock here b/c we may or maynot have a file
class FileReader(object):

    def get_text_from_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read()

class FileReaderMock(object):
    def __init__(self, mock_file_data):
        self.mock_file_data = mock_file_data

    def get_text_from_file(self, file_name):
        return self.mock_file_data 


##This class has no network/file/db calls so we can just test it as is
class TextChecker(object):

    def contains_text(self, input_text, val_to_check_for):
        return True if val_to_check_for in input_text else False

class Program(object):
    def __init__(self, file_reader, text_checker):
        self.file_reader = file_reader
        self.text_checker = text_checker

    def run(self, file_name, text_to_find):
        return self.text_checker.contains_text(self.file_reader.get_text_from_file(file_name),text_to_find)

###Let's test

def test_that_word_hello_is_detected():
    #First create an instance of the mock since we don't want to worry about a file:
    fr = FileReaderMock("Hello world\n")
    tc = TextChecker()
    program = Program(fr, tc)
    assert program.run("/madeupfile.txt", "Hello") == True


