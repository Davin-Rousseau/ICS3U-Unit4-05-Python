#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on October 2019
# This program asks user to enter how many numbers
# they want to add. User enters numbers that are
# to be added, but only positive integers are added


def main():
    answer = 0
    loop_counter = 0

    # input
    number = input("Enter how many numbers you want to add: ")
    print("")

    # process
    try:
        loop_c = int(number)
        for loop_counter in range(loop_c):
            numInput = input("Enter number: ")
            try:
                intCheck = int(numInput)
                if intCheck < 0:
                    continue
                else:
                    answer += intCheck
            except ValueError:
                print("Enter positive number. ")
        print("")
        print("The answer is: {}".format(answer))
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
