
'''
Fail fast, don't send error messages
'''
#Wrong
class FileReader(object):
    def get_text_from_file(self, file_name):
        try: 
            with open(file_name, 'r') as f:
                return f.read()
        except Exception as e:
            print(e)
            return False

fr = FileReader()
text = fr.get_text_from_file('/a_file_that_does_not_exist')
if text:
    pass #do some work


#right
class FileReaderr(object):
    def get_text_from_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read()

try:
    fr = FileReader()
    text = fr.get_text_from_file('/a_file_that_does_not_exist')
except Exception as e:
    print("Hit the following error:", e)


'''
Avoid sending returning and passing in nulls!
'''
#wrong:
def get_users_from_db():
    #potentially returns none
    return None

def process_users():
    users = get_users_from_db()
    if users:
       for user in users:
           pass #do some work on users

#right:

#wrong:
def get_users_from_dbb():
    return [] #returns a empty list if the previous lines of code calling the db has zero users

def process_userss():
    users = get_users_from_dbb()
    for user in users:
        pass #do some work on users




