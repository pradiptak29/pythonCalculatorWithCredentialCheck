# pythonCalculatorWithCredentialCheck

# welcome message
print("----------------------------------------------------------------------------------------")
print("Hi there, my name is calculation_world; in short CW.\nMay I see your valid User ID and password, please?")
print("----------------------------------------------------------------------------------------")

# verifying user credentials
_id = input("User ID:\t")
if 'asterix_29' == _id.lower():
    b = input("Password:\t")
    print("----------------------------------------------------------------------------------------")
    print("Processing User ID...")
    print("Validating Password...")
    if 'pop12345xy' == b.lower():
        print("Hello,", _id)

        # main calculator function
        def calling():
            print("----------------------------------------------------------------------------------------")
            cont = input("Do you want to continue?\nPress\n Y for YES\n N for NO\n")
            if 'y' == cont.lower():
                print("----------------------------------------------------------------------------------------")
                job = input("What do you want me to do?")
                print("----------------------------------------------------------------------------------------")
                try:
                    jobin = int(job)
                    if jobin == 1:
                        addition()
                    elif jobin == 2:
                        subtraction()
                    elif jobin == 3:
                        product()
                    elif jobin == 4:
                        division()
                    else:
                        print("Sorry, invalid option!")
                    calling()
                except:
                    print("Sorry, invalid option!")
                    calling()
            elif 'n' == cont.lower():
                print("Thank You for using me.")
                print("----------------------------------------------------------------------------------------")
            else:
                print("Sorry, invalid option!")
                calling()

        # Addition
        def addition():
            print("**Section: Addition**")
            x = input("Give me a value:")
            y = input("Give me another value:")
            try:
                xval = float(x)
                yval = float(y)
                print("After addition we get: ", xval + yval)
            except:
                print("Syntax ERROR")
                addition()

        # Subtraction
        def subtraction():
            print("**Section: Subtraction**")
            x = input("Give me a value:")
            y = input("Give me another value which is to be subtracted:")
            try:
                xval = float(x)
                yval = float(y)
                print("After subtraction we get: ", xval - yval)
            except:
                print("Syntax ERROR")
                subtraction()

        # Multiplication
        def product():
            print("**Section: Multiplication**")
            x = input("Give me a value:")
            y = input("Give me another value:")
            try:
                xval = float(x)
                yval = float(y)
                print("After multiplication we get: ", xval * yval)
            except:
                print("Syntax ERROR")
                product()

        # Division
        def division():
            print("**Section: Division**")
            x = input("Give me a dividend:")
            y = input("Give me the divisor:")
            try:
                xval = float(x)
                yval = float(y)
                print("After division we get:", "\nResult:", xval / yval, "\nQuotient:", int(xval / yval),
                      "\nRemainder: ",
                      xval % yval)
            except:
                print("Syntax ERROR")
                division()

        # Options
        print("Welcome to calculation_world.")
        print("Type 1 for Addition\nType 2 for Subtraction\nType 3 for Multiplication\nType 4 for Division")

        calling()

    # Forget Password Section
    else:
        print("Incorrect Password.")
        print("Sorry", _id + ", you're not allowd.")
        forget_password = input("forgot password?\nPress\n Y for YES\n N for NO\n")
        if forget_password.lower() == 'y':
            _mail = input("Please enter the registered e-mail address:")
            if _mail.lower() == 'pop.9bakp@gmail.com':
                print("----------------------------------------------------------------------------------------")
                print("User ID: asterix_29\nPassword: pop12345xy")
            else:
                print("Sorry", _id + ", your e-mail address does not match. You're not allowed.")
                print("----------------------------------------------------------------------------------------")
                print("                    !!!Attention!!!\nA security alert has been sent to the registered email address.\n              Thank you "
                      "for your support.")
        elif forget_password.lower() == 'n':
            print("See you soon,", _id)
        print("----------------------------------------------------------------------------------------")
else:
    print("----------------------------------------------------------------------------------------")
    print("Unauthorized User ID.")
    print("Sorry", _id + ", you're not allowed.")
    print("----------------------------------------------------------------------------------------")
