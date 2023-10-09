import sys
import userdb_csv

for record in userdb_csv.read_csv_noheader(sys.argv[1]):
    userdb_csv.print_user(record)
