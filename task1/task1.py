import requests
import xml.etree.ElementTree as ET

def task1_solution():
    r = requests.get('https://coding-academy.pl/all_customers')
    return r

if __name__ == '__main__':
    root = ET.fromstring(task1_solution().content)
    pl_tst = open("test.txt", "w")
    for child in root:
        pl_tst.write(child.text + '\n')