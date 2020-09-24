'''
Single Responsiblity Principle
Open/Closed Principle
Liskov Subsitution Principle
I
D

A sub-class must must be appropriate for the super class.

"If it looks like a duck, quacks like a duck, but needs batteries, you prob have the wrong abstraction"

'''

#Wrong:
class Doctor(object):
    def __init__(self, npi_id):
        self.npi_id = npi_id
    
    def get_npi_id(self):
        return self.npi_id
    
    def perform_surgery(self):
        pass

class PlasticSurgeon(Doctor):
    pass


class Radiologist(Doctor):
    #Doesn't make sense for Radiologist to have perform_surgery
    pass



#Right:
class Doctorr(object):
    def __init__(self, npi_id):
        self.npi_id = npi_id
    
    def get_npi_id(self):
        return self.npi_id

class Surgeon(Doctor):
    def perform_surgery(self):
        pass

class PlasticSurgeonn(Surgeon):
    pass


class Radiologistt(Doctor):
    pass
    