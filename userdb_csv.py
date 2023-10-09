import csv


def read_csv_header(filename):
    with open(filename, encoding='cp1252') as f:
        rdr = csv.DictReader(
            f,
            delimiter=';', 
            quotechar='"')

        for record in rdr:
            yield {
                'id': int(record['ID']),
                'firstname': record['First name'],
                'lastname': record['Last name'],
                'birth': record['Date of Birth'],
            }

def read_csv_noheader(filename):
    with open(filename, encoding='cp1252') as f:
        rdr = csv.reader(
            f,
            delimiter=';', 
            quotechar='"')

        for id, firstname, lastname, birth in rdr:
            yield {
                'id': int(id),
                'firstname': firstname,
                'lastname': lastname,
                'birth': birth,
            }
