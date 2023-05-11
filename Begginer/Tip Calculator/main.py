import math as math
print("Welcome to the tip calculator!")
bill_total = float(input('What was the total sum of the bill? '))
number_people = int(input('Howmany people should split the bill? '))
tip_percent = float(input("What is the percent of the tip? "))/100
payment = bill_total*(1+tip_percent)/number_people
print(f'Each person should pay ${"{:.2f}".format(payment)}')
