import csv

class Person:
    def __init__(self, id, firstname, lastname, birth):
        self._id = id
        self._firstname = firstname
        self._lastname = lastname
        self._birth = birth

    @property
    def id(self):
        return self._id
    @property
    def firstname(self):
        return self._firstname
    @property
    def lastname(self):
        return self._lastname
    @property
    def birth(self):
        return self._birth

def read_csv_noheader(filename):
    f = open(filename, encoding='cp1252')
    rdr = csv.reader(f, delimiter=';', quotechar='"')

    for id, firstname, lastname, birth in rdr:
        u = {
            'id': int(id),
            'firstname': firstname,
            'lastname': lastname,
            'birth': birth,
            }
        yield u
        

def read_csv_header(filename):
    f = open(filename, encoding='cp1252')
    rdr = csv.DictReader(f, delimiter=';', quotechar='"')

    for record in rdr:
        id = record['ID']
        firstname = record['First name']
        lastname = record['Last name']
        birth = record['Date of Birth']

        u = {
            'id': int(id),
            'firstname': firstname,
            'lastname': lastname,
            'birth': birth,
            }

        yield u

def format_user(user):
    return f"ID:{user['id']}, Firstname:{user['firstname']}, Lastname:{user['lastname']}, Date of birth: {user['birth']}"

def _convert_users_from_dict_to_class(users):
    for user in users:
        u = Person(user['id'], user['firstname'], user['lastname'], user['birth'])
        yield u

def read_noheader_person(filename):
    users = read_csv_noheader(filename)
    return _convert_users_from_dict_to_class(users)

def read_header_person(filename):
    users = read_csv_header(filename)
    return _convert_users_from_dict_to_class(users)
