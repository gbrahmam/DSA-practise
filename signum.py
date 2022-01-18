# Fill in the following function.
# Please do not change the function name.
def signum(number):
    # you can start from here.
    if number>0:
        return 1
    elif number<0:
        return -1
    elif int(number) == 0:
        return 0


### Please do not edit the code below this line.

if __name__ == "__main__":
    test_input = float(input())
    print(signum(test_input))