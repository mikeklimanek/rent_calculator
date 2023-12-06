import time
from datetime import datetime, timedelta

def calculate_total_rent(initial_rent, rent_increases, years):
    current_time = datetime.now() - timedelta(days=365 * 3)
    total_rent = 0
    for year in range(years):
        for month in range(12):
            cumulative_increase = sum(amount for date, amount in rent_increases if date <= current_time)
            total_rent += initial_rent + cumulative_increase

            text = "{}: +{} CZK increase in comparison to initial rent, rent for this month was {:,}. CZK {:,} paid in total"
            print(text.format(current_time.strftime('%Y-%m'),cumulative_increase,cumulative_increase+initial_rent,total_rent))
            current_time += timedelta(days=30)
initial_rent = int(input("Enter your initial rent: "))

First_increase = int(input("Enter the first increase amount (f.e. 1000): "))
input_date = input("Enter date for first increase (format: YYYY MM DD): ")
increase1_date = datetime(Year1:=int(input_date.split()[0]), Month1:=int(input_date.split()[1]), Day1:=int(input_date.split()[2]))


Second_increase = int(input("Enter the second increase amount (f.e. 500): "))
input_date2 = input("Enter date for second increase (format: YYYY MM DD): ")
increase2_date = datetime(Year2:=int(input_date2.split()[0]), Month2:=int(input_date2.split()[1]), Day2:=int(input_date2.split()[2]))

rent_increases = [
    (increase1_date, First_increase),
    (increase2_date, Second_increase),
]
years = 3

calculate_total_rent(initial_rent, rent_increases, years)