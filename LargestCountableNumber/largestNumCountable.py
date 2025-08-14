import sys
sys.set_int_max_str_digits(0)

num = 8099965799; power = num; count = 1

while(count < power):
    try:
        result = num ** count
        print(count+1, ":" ,result)
        count += 1
    except Exception as exec:
        print(exec)
        break

# num = -num
# print(num)
# num = -num