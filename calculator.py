#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Sunny
#
# Created:     17/04/2023
# Copyright:   (c) Sunny 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
first =input("first number")
operator =input (" enter operator (+,-,*,/,%) ")
second=input (" second number")

first =int(first)
second=int(second)
if operator == "+":
    print(first+ second)
elif operator =="-":
    print(first-second)
elif operator=="*":
    print(first*second)
elif operator =="/":
    print(first/second )
elif operator =="%":
    print(first%second)
else:
    print("invalid")