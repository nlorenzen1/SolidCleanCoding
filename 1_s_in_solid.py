
'''
Single Responsiblity Principle
O
L
I
D

A class or method should have 1 job and 1 job only
'''
#Train your eyes to looks at the structure/setup first, then the implementation details

#Wrong:
class TextChecker(object):

    def read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read()

    def contains_text(self, input_text, val_to_check_for):
        return True if val_to_check_for in input_text else False



#Right:

#Single responsiblity to read files
class FileReader(object):

    def read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read()


#Single responsiblity to check for text
class TextCheckerr(object):

    def contains_text(self, input_text, val_to_check_for):
        return True if val_to_check_for in input_text else False

    