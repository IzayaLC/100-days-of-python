#This is a simple TipCalculator

print('Hello! Welcome to the Tip Calculator!')
bill = float(input('How much is the bill? '))

tip = float(input('What percent tip would you like to pay? '))
num_people_paying = int(input('How many people will be split the bill? '))

tip_as_percent = tip/100
total_bill = bill * (1 + tip_as_percent)

individual_bill = round(total_bill/num_people_paying, 2)

print(f'Each person will have to pay: {individual_bill}')