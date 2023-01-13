import re
from typing import List

def checkForName(data : List[str]) -> None:
    print("Name of the users found in the file are: ")
    for line in data:
        if re.search(r"Mr\.|Ms\.|Mrs\.", line):
            print(line)

def checkForWebsite(data : List[str]) -> None:
    print("websites found in the file are: ")
    for line in data:
        if re.search(r"www\..+\.com", line):
            print(line)

def checkForMail(data : List[str]) -> None:
    print("Emails found in the file are: ")
    for line in data:
        if re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', line):
            print(line)

def checkForPhone(data : List[str]) -> None:
    print("Phone numbers found in the file are: ")
    for line in data:
        if re.search(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', line):
            print(line)

if __name__ == '__main__':
    listedData = []
    with open('regex.txt', 'r') as f:
        data = f.readlines()
        data = list(map(lambda x: x.strip(), data))
        for line in data:
            listedData.append(line)
    checkForName(listedData)
    checkForWebsite(listedData)
    checkForMail(listedData)
    checkForPhone(listedData)
