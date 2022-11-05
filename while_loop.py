# Created by: Kaitlyn Ip
# Created on: Nov 2022
# This program uses a while loop


def main():
    # this function uses a while loop

    # this is to keep track of how many times you go through the loop
    loop_counter = 0
    answer = 0
    str_integer = input("Enter an integer: ")

    # input
    try:
        int_integer = int(str_integer)

        # process & output
        while loop_counter < int_integer:
            loop_counter = loop_counter + 1
            answer = answer + loop_counter
        print(
            "The sum of all the positive numbers from 1 to "
            + str(int_integer)
            + " "
            + "is {0}.".format(answer)
        )

    except ValueError:
        print("That is not a valid input.")


if __name__ == "__main__":
    main()
