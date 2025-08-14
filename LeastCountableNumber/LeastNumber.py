import sys
sys.set_int_max_str_digits(0)

num = 8099965799; power = 8099965799; count = power
while(count <= power):
    try:
        result = (1/float(num)) ** (1/float(count))
        print(count, ":" ,result)
        count += 1
    except Exception as exec:
        print(exec)
        break