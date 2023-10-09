import sys

import userdb_csv

user_records = userdb_csv.read_csv_noheader(sys.argv[1])
for user in user_records:
    print(userdb_csv.format_user(user))
