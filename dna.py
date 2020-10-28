from sys import argv, exit
import csv
import re

# check if there are the required amount of command line args.
if len(argv) != 3:
    print("Error")
    exit(1)

database = argv[1]
dna = argv[2]

# Open txt and read to a string
with open(dna, "r") as ptr_dna:
    dna_str = ptr_dna.readline()

# dna str's for large.csv and small.csv
dna_list = ['AGATC', 'TTTTTTCT', 'AATG', 'TCTAG', 'GATA', 'TATC', 'GAAA', 'TCTG']
if database == "databases/small.csv":
    dna_list = ['AGATC', 'AATG', 'TATC']

# makes list of names
names = []
with open(database, "r") as ptr_database:
    reader = list(csv.reader(ptr_database))
    for line in reader:
        names.append(line[0])  # name"s list have "name" inside, it causes some '+1's and '-1's in loop's :(
    reader.remove(reader[0])  # remove list wiwh "name" and str's

    for i in range(0, len(reader)):
        mark = True  # marks true if all str are fits till the reader's line end

        for j in range(1, len(dna_list)+1):

            # sequence we search in dna_str that repeats reader[i][j] times
            var = dna_list[j-1]*(int(reader[i][j])) 
            # sequence we search in dna_str that repeats only reader[i][j] times and no +1 more
            var_check = dna_list[j-1]*((int(reader[i][j]))+1)
            # search_check is bool that means var repeat only reader[i][j] times and no +1 more
            search_check = not re.search(var_check, dna_str)

            if re.search(var, dna_str) and search_check == True:
                pass
            else:
                mark = False
                break

        if mark == True:
            print(names[i+1])
            break

    if mark == False:
        print('No match')
