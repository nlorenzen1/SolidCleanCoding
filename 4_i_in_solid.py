
'''
Single Responsiblity Principle
Open/Closed Principle
Liskov Subsitution Principle
Interface Seperation Principle
D

Make fine grained interfaces that are client specific. Avoid big interfaces 
    
'''


#Wrong:
class IParser(object):
    def parse_html(self):
        raise NotImplementedError

    def parse_json(self):
        raise NotImplementedError

    def parse_text(self):
        raise NotImplementedError



##################Right:

class IParserr(object):
    def parse(self):
        raise NotImplementedError

class HTMLParser(IParserr):
    def parse(self):
        #implement specific parsing logic
        pass

class JSONParser(IParserr):
    def parse(self):
        #implement specific parsing logic
        pass


class TextParser(IParserr):
    def parse(self):
        #implement specific parsing logic
        pass