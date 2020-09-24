
'''
Single Responsiblity Principle
Open/Closed Principle
Liskov Subsitution Principle
Interface Seperation Principle
Dependency Inversion Principle

Inject yo Dependencies
    
'''


#Wrong:
class FileReader(object):

    def get_text_from_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read()


class TextChecker(object):

    def contains_text(self, input_text, val_to_check_for):
        return True if input_text in val_to_check_for else False


class Main(object):

    def run(self):
        fr1 = FileReader() #going to make it nearly impossible to unit test
        tc1 = TextChecker() #not impossible to test, but harder if you used interfaces to have different implementations
        return tc1.contains_text(fr1.get_text_from_file("/somewhere"),"Look for this")





#Right:

class FileReaderr(object):

    def get_text_from_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read()


class TextCheckerr(object):

    def contains_text(self, input_text, val_to_check_for):
        return True if val_to_check_for in input_text else False


class Mainn(object):
    def __init__(self, file_reader, text_checker):
        self.file_reader = file_reader
        self.text_checker = text_checker

    def run(self):
        return self.text_checker.contains_text(self.file_reader.get_text_from_file("/somewhere"),"Look for this")


