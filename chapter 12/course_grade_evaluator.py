import pandas as pd

filename = input("Enter the name of the file: ")
data = pd.read_csv(filename, sep="\t")


class Student:
    def __init__(self, fname, lname, grades):
        self.fname = fname
        self.lname = lname
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)