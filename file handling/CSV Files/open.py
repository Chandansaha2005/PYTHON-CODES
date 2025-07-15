#WAP to opena a csv file
import csv

with open("satyam.csv",'r') as file:
    x=csv.reader(file)
    for i in x:
        print(i)