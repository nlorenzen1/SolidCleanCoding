


'''
Classes and Methods should remain small and do one job (SRP)
Ideally, keep methods under 20 lines of code. Anymore and you're prob breaking SRP
Keep it elegant, let the code speak for itself, not the comments speaking for the code
'''

##Are comments really necssary with this code? Methods are small and simple and descriptive
class FileReader(object):
    def get_text_from_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read()

class TextChecker(object):
    def contains_text(self, input_text, val_to_check_for):
        return True if val_to_check_for in input_text else False


'''
Methods shouldn't exceed 3 input params.
It makes them confusing, and fragile/easy to break when updates are needed 
If more params are needed, pass a object
'''

#wrong
##Highly dangerous code if this method is used more than once 
##in code base and the input params change
def perform_important_descriptive_task(parm1, param2, param3, param4, param5):
    pass

#right:
class ConfigObject(object):
    def __init__(self):
        self.param1 = False
        self.param2 = True
        self.param3 = True
        self.param5 = False

##Config object may change, ideally appending to and only updating the methods that
##need the new params
def perform_important_descriptive_taskk(config_object):
    pass



'''
Be descriptive with complex logic and hide it in objects 

Avoid leaky abstractions
'''

#wrong
class Patient(object):
    def has_cough(self):
        pass
    def is_sneezing(self):
        pass
    def is_vomiting(self):
        pass
    
patient = Patient()

is_sick = False
if ((patient.has_cough) and (patient.is_sneezing)) or (patient.is_vomiting):
    is_sick = True

#right
class Patientt(object):
    def has_cough(self): #Could also be treated as private
        pass
    def is_sneezing(self): #Could also be treated as private
        pass
    def is_vomiting(self): #Could also be treated as private
        pass
    def is_sick(self): 
        return ((self.has_cough) and (self.is_sneezing)) or (self.is_vomiting)

patient = Patientt()
is_sick = patient.is_sick()





