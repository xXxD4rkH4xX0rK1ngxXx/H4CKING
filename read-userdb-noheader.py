import sys
import userdb_csv

for record in userdb_csv.read_csv_noheader(sys.argv[1]):
    print(f'ID:{record["id"]}, Firstname:{record["firstname"]}, Lastname:{record["lastname"]}, Date of birth: {record["birth"]}')
