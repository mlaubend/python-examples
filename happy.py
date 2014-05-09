def ishappy(number):
    #these are the initial conditions; if the number is already 1 or 4, a message
    #is printed and a bool is returned
    if number == 4:
            print(number)
            print("Not Happy :(")
            return False
    elif number == 1:
            print(number)
            print("Happy!")
            return True
    x = 0

    """this function breaks up the number into its corresponding digits by
    converting it into a string, slicing, and then converting back to an int
    in order to perform math operations"""
    while x!=1 or x!=4:
        digitsum = 0
        numberlength = len(str(number))
        for i in range(0,numberlength):
            digitsum += (int(str(number)[i])**2)
        print(digitsum)

        """checks whether or not the number is happy after each iteration of
        the loop"""
        if digitsum == 4:
            print("Not Happy :(")
            return False
            
        if digitsum == 1:
            print("Happy!")
            return True

        """necessary in order to update the loop """
        x = digitsum
        number = digitsum

ishappy(28)
