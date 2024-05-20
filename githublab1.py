# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days


Minutes = int(input("Enter the number of minutes:"))

total_day = Minutes//(60*24)
years = total_day//365

Remaining_days = total_day % 365

print(f"{Minutes} minutes is approximately {years} years and {remaining_days} days.")
