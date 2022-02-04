#!/usr/bin/python3

import sys
import csv
from os.path import exists
from os.path import basename


def handleFileDoesNotExist(n):
    for i in range(1, n):
        if not exists(sys.argv[i]):
            print("file " + sys.argv[i] + " does not exists.")
            sys.exit()
        else:
            assert True


def handleNotEnoughArguments(n):
    if n < 3:
        print("Total arguments passed:", n - 1)
        for i in range(1, n):
            print(sys.argv[i], end=" ")
        print("csv-combiner needs at least 2 file names(arguments) to combine.")
        sys.exit()
    else:
        assert True


handleNotEnoughArguments(len(sys.argv))
handleFileDoesNotExist(len(sys.argv))

for i in range(1, len(sys.argv)):
    with open(sys.argv[i], 'r') as nFile:
        reader = csv.reader(nFile)
        if i == 1:
            basefilename = "filename"
        else:
            next(reader)
        for email, category in reader:
            print(email + "," + category + "," + basefilename)
            basefilename = basename(sys.argv[i])
