# First we need to check for which function user wants.

logicFunction = input('Enter logic function name \'and,or,not\' :')

# ----------------------------------------------
# ------Check for any norm name error-----------
# ----and which function the user chose.--------
# ----------------------------------------------

if logicFunction == "and":

    conditionA = input("Enter value of condition A: ")  # the first number.

    # --------------------------------------------------------------
    # ------(now we need to check for any digit errors in (A).)-----
    # --------------------------------------------------------------

    if conditionA.isdigit():

        if conditionA in ["1", "0"]:

            # ------------------------------------------------
            # --------((A) checked now check (B).)------------
            # ------------------------------------------------

            conditionB = input("Enter value of condition B: ")  # the second number.

            if conditionB in ["1", "0"]:

                if conditionB.isdigit():

                    if conditionA == "1":

                        if conditionB == "1":
                            print('"and"logic function result is =', 1)

                        elif conditionB == "0":
                            print('"and" logic function result is =', 0)

                    elif conditionA == "0":

                        if conditionB == "1":
                            print('"and" logic function result is =', 0)

                        elif conditionB == "0":
                            print('"and" logic function result is =', 0)

                else:  # when (B) is out of the range.
                    print("either B is not a digit, has more than one digit, or is out of the 0,1 range")

            else:  # when (B) is not a digit.
                print("either B is not a digit, has more than one digit, or is out of the 0,1 range")

        else:  # when (A) is out of the range.
            print("either A is not a digit, has more than one digit, or is out of the 0,1 range")

    else:  # when (A) is not a digit .
        print("either A is not a digit, has more than one digit, or is out of the 0,1 range")
elif logicFunction == "or":

    conditionA = input("Enter value of condition A: ")  # the first number.

    # --------------------------------------------------------------
    # ------(now we need to check for any digit errors in (A).)-----
    # ------------------------(Again!)------------------------------

    if conditionA.isdigit():
        if conditionA in ["1", "0"]:

            conditionB = input("Enter value of condition B: ")  # the second number.

            if conditionB.isdigit():

                if conditionB in ["1", "0"]:

                    if conditionA == "1":

                        if conditionB == "1":

                            print('"or"logic function result is =', 1)

                        elif conditionB == "0":

                            print('"or"logic function result is =', 1)

                        else:

                            print("either B is not a digit, has more than one digit, or is out of the 0,1 range")

                    elif conditionA == "0":

                        if conditionB == "1":

                            print('"or"logic function result is =', 1)

                        elif conditionB == "0":

                            print('"or"logic function result is =', 0)

                else:  # when (B) is out of the range.
                    print("either B is not a digit, has more than one digit, or is out of the 0,1 range")

            else:  # when (B) is not a digit.
                print("either B is not a digit, has more than one digit, or is out of the 0,1 range")

        else:  # when (A) is out of the range.
            print("either A is not a digit, has more than one digit, or is out of the 0,1 range")

    else:  # when (A) is not a digit .
        print("either A is not a digit, has more than one digit, or is out of the 0,1 range")

elif logicFunction == "not":

    conditionA = input("Enter value of condition A: ")  # the first number and the only.

    # --------------------------------------------------------------
    # ------(now we need to check for any digit errors in (A).)-----
    # ----------------------(Again! "2")----------------------------

    if conditionA.isdigit():

        if conditionA in ["1", "0"]:

            if conditionA == "1":

                print('"not"logic function result is =', 0)

            elif conditionA == "0":

                print('"not"logic function result is =', 1)
        else:  # when (A) is not (1 or 0).
            print("either A is not a digit, has more than one digit, or is out of the 0,1 range")

    else:  # when (A) is not a digit.
        print("either A is not a digit, has more than one digit, or is out of the 0,1 range")

else:  # if the "logicFunction" input was not a logic function.
    print("Error:unknown logic function")

