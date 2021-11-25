def Sunday():
    sun_rate = input('Please enter your Sunday hourly rate?')

    try:
        sun_rate = float(sun_rate)

    except:
        print("please type number")
        return Sunday()

    if sun_rate in {0}:
        print('You didnt work any extra on Sunday')
    elif sun_rate > 30:
        print('number needs to be between 1 to 30')
        return Sunday ()
    else:
        sun_hours = float(input('How many hours did you work on Sunday?'))
        sun_hours = float(sun_rate)



    sun_pay = sun_hours * sun_rate

    print("You worked " + str(sun_hours)+ " hours and your sunday hourly pay rate was " + str(sun_rate))
    print("\n" )
    print("Which gives you a total of £" + str(sun_pay))
    print("\n" )
    print("This is the end of the program ;)")
    print("\n" )
