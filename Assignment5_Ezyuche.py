#ASSIGNMENT ONE

#write a code that will print out all the days of a particular month.
# The system should be able to prompt you for the year and month. 
# The value of the month should either be a number or the month name.

# import calendar
# months = ["January", "February", "March", "April", "May", "June", "July", 
#           "August", "September", "October", "November", "December"]
# year = int(input("Enter year: "))
# month_input = input("Enter month (number or name): ").strip().capitalize()

# # convert month name to number if needed

# if month_input.isdigit():
#     month = int(month_input)
# else:
#     month = months.index(month_input) +1

# #print all days of the month
# print(calendar.month(year,month))

#ASSIGNMENT TWO

#write a code to prin out a range of months in a year. 
# The system should be able to prompt you for a particular year, start month and end month, 
# after which it will print out the range of calendar for the period specified. 
# Both the start month and end month should be able to takein either the number of the month name

# import calendar
# months = ["January", "February", "March", "April", "May", "June", "July", 
#           "August", "September", "October", "November", "December"]

# #step 1: prompt for inputs
# year = int(input("Enter year: "))
# start_month = input("Enter month (number or name): ").strip().capitalize()                          
# end_month = input("Enter month (number or name): ").strip().capitalize()

# #step 2: convert month name to number if needed

# if start_month.isdigit():
#     start = int(start_month)
# else:
#     start = months.index(start_month) 

# if end_month.isdigit():
#     end = int(end_month)
# else:
#     end = months.index(end_month) 

# #step 3: print the calenders

# print(f"\nCalender for {calendar.month_name[start]} to {calendar.month_name[end]}, {year}\n")
# for month in range(start, end + 1):
#     print(calendar.month(year, month))


# ASSIGNMENT THREE 
# . okoro and sons company is organizing a lottery for the general public, 
# each person is required to buy a ticket and fill in his or her NIN. 
# The later found out that so many people bought and filled more than one ticket. 
# This is because they found out that there where many NINs of the same value 
# and this is against the companies policy: 
# Write a code which ensures that nobody wins this lottery more than ones. 


def lottery_system():

    # 1. Sample data
    all_tickets_nins = [
        "A234567", "B987654", "E111111", "A234567",
        "D222222", "B987654", "C333333"]
    
    print(f"Original list of tickets: {all_tickets_nins}")

    # 2. The core logic: convert list to a set to remove duplicates
    unique_nins_set = set(all_tickets_nins)

    # 3. Convert back to a list (optional)
    valid_lottery_entries = list(unique_nins_set)

    print(f"Valid (unique) entries: {valid_lottery_entries}")
    print("\n" + "=" * 30 + "\n")


