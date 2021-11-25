import time





def worked_hours():



    print("\n" )
    print("Welcome to the Wage Calculator.")
    print("\n" )


    print('Did you work more than 37.5 hours. Yes or No?')
    hours_worked = str(input('>'))

    if hours_worked in {"YES", "Yes", "y", "Y", "yes"} :
        print("\n")
        print ("Great, Please proceed")
        print("\n")
    elif hours_worked in {"no", "No", "N", "n", "NO"}:
        print ("OK, See you soon, You need to work harder.")
        print ("Program restarting!!")
        time.sleep(2)
        print("\n")

        worked_hours()
    else:
        hours_worked.isalpha() == False
        print('Program quiting, Enter Yes or No!!')
        print("\n" )
        worked_hours()
