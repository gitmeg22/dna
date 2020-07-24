import csv
import sys
from sys import argv, exit
import re


def main():

    # Check for correct number of args
    check_args()

    # Open Text file... 'sequences/1.txt'... type(sequence) = '_io.TextIOWrapper'
    textfile = open(argv[2], "r")

    # Create variable to read sequence... type(list) = 'str'
    sequence = textfile.read()

    # Open CSV file into a Dictionary... type(csvfile) = 'csv.DictReader'
    csvfile = csv.DictReader(open(argv[1]))

    # Create List of Headers/Fieldnames from CSV file... type(headers) = 'list'... discard first header 'name' b/c is not a STR
    headers = csvfile.fieldnames[1:]
        # headers = reader.fieldnames[1:]

    # STR max counts
    strCounts = {}

    # Find maximum count of consecutive STRs from headers list in sequence string
    findMaxSTR(headers, sequence, strCounts)

    # print(strCounts)

    for row in csvfile:
        for k, v in row.items():
            print(k, v)


    textfile.close()


# Find maximum count of consecutive STRs from headers list in sequence string
def findMaxSTR(list, string, dictionary):
    for STR in list:
        # Use regex to find all instances of STR in the sequence
        group = re.findall(rf'(?:{STR})+', string)
        # Find largest grouping of STR in all instances
        largest = len(max(group, key=len)) // len(STR)
        # Add STR as Key and Largest as Value to dictionary
        dictionary[STR] = largest


# Check for correct number of args
def check_args():
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)


main()


#####

# 1st cmd line arg = name of CSV file (STR counts for list of individuals)
# 2nd cmd line arg = name of text file (DNA sequence to identify)

# if incorrects # of cmd line args
# print error msg

# if correct # of cmd line args

# open CSV file (arg 1) and read contents into memory

# 1st row of CSV file = column names
# 1st col of CSV file = name
# remaining cols = STR sequences

# open DNA sequence file and read contents into memory



# for each STR (in 1st line of CSV file)
    # compute longest run of consecutive repeats of the STR in the DNA sequence to identify

# Compare the STR counts against each row in the CSV file

# if the STR counts match exactly with an individual in CSV file
    # print name

    # STR counts will not match more than one name
    # if STR counts do not match any name
        # print "No match"







# Info on DictReader fieldnames to read headers of csv file
# https://stackoverflow.com/questions/28836781/reading-column-names-alone-in-a-csv-file/35963291

# https://stackoverflow.com/questions/3873361/finding-multiple-occurrences-of-a-string-within-a-string-in-python




# USING CONDENSED OPENING OF CSVFILE INSTEAD
# Open CSV file into a Dictionary
# with open(argv[1]) as csvfile:
#     # type(csv_reader) = 'csv.DictReader'
#     csv_reader = csv.DictReader(csvfile)

# headers = csv_reader.fieldnames
# print(type(csv_reader))
