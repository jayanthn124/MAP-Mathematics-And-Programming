# Mathematical Law of Opponods - Opposite Number Differences.

import math

def ReverseNumber(num, base):
    match base:
        case 2:
            number = bin(num)
        case 8:
            number = oct(num)
        case 10:
            number = num  
        case 16:
            number = hex(num)    
        case default:
            return 0
    number = num
    reversed_num = 0
    while number != 0:
        digit = number % base
        reversed_num = reversed_num * base + digit
        number //= base
    print("The Opposite Number for base: ", base, " is: ", reversed_num)
    if(num == reversed_num):
        return 0
    else:
        return reversed_num


def Opponod(num, base):

    # First Reverse the Number
    match base:
        case 2:
            number = bin(num)
            num = number
        case 8:
            print(oct(num))
            number = oct(num)[::-1]
            print(number)
            number = number[:2]
            print(int(number, 8))
            num = number
        case 10:
            number = num
            num = number  
        case 16:
            print(hex(num))
            number = hex(num)[::-1]
            print(number)
            num = number    
        case default:
            return 0
    # reversed_num = 0
    # while number != 0:
    #     digit = number % base
    #     reversed_num = reversed_num * base + digit
    #     number //= base
    # print("The Opposite Number for base: ", base, " is: ", reversed_num)

    # if(num == reversed_num):
    #     print("The Entered Number is a Palindrome Number.")
    # else:
    #     # The Difference - Opponod
    #     difference = reversed_num - num
    #     print("The Difference between it's Opposite Number is: ", difference)

    #     # Divisiblity by 9
    #     if((difference % 9) == 0):
    #         quotient = difference / 9
    #         print("The Law holds true. And the 9th multiples is: ", quotient)
    #     else:
    #         print("This Law is a Mathematical blunder.")


    
if __name__ == "__main__":
    # while(1):
        # Allow the User Inputs.
        num = int(input("Enter a non-palindrome number: "))
        # Apply the Law and verify.
        # Opponod(num,2) # Base-2
        Opponod(num,8) # Base-8
        # Opponod(num,10) # Base-10
        # Opponod(num,16) # Base-16

