def Saturday():

    print("\n" )
    print("Now we are going to move onto your weekend pay")
    print("\n"  )

    sat_rate = input('Please enter your Saturday hourly rate?')

    try:
        sat_rate = float(sat_rate)

    except:
        print("Please type number")
        return Saturday()

    if sat_rate in {0}:
        print('You didnt work any extra on Saturday')
    elif sat_rate > 30:
        print('-Number needs to be between 1 to 30')
        return Saturday()
    else:
        sat_hours = input('How many hours did you work on Saturday?')



    sat_pay = int(sat_hours) * int(sat_rate)
    print("You worked " + str(sat_hours) + " hours and your Saturday was £" + str(sat_rate))
    print("\n" )
    print("Which gives you total pay of £" + str(sat_pay))
    print("\n" )

    print("\n")



#    if sat_rate in range(1-1000):
#        print("\n")
#        sat_hours = int(input('How many hours did you work on Saturday?'))

#        sat_hours = float(input("Please enter your hours worked on Saturday"))
#        sat_pay = sat_hours * float(sat_rate)

#        print("\n")

#    elif sat_rate in {0}:
#            print('You didnt work any extra')
#            return Saturday()

#    else:
#        return sat_rate
#sat_rate = Saturday()

#    else:
#        sat_rate.isdigit() == False
#        print("Quit")


    #sat_hours = float(input("Please enter your hours worked on Saturday"))


    #sat_pay = sat_hours * float(sat_rate)
