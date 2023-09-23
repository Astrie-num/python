#pthon program to display the calender of the given 
#month of the year


#import the calender module
import calendar

yy = 2020
mm = 1


# yy = int(input("Enter the year: "))
# mm = int(input("Enter the month: "))

#display the calender
print(calendar.month(yy, mm))