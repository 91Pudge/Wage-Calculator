import time


def Rate1():
    rate = input('Please enter your hourly rate:')
    try:
        rate = float(rate)
    except:
        print("-Please type a number")
        return Rate1()

    if rate in {0}:
        print("you didnt work any hours")
        return Rate1()
    elif rate > 60:
        print("are you sure!!")






    weekly =  int(rate) * 37.5

    print(f"Your  £{rate} per hour, multipled by 37.5 hours worked is--", weekly)
    print("\n" * 3 )



    time.sleep(2)
