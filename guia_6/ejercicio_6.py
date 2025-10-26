def print_1_to_10():
    num : int = 1
    while num <= 10:
        print(num)
        num += 1

#print_1_to_10()

def print_even_between_10_and_40():
    num = 10
    while num <= 40:
        print(num)
        num += 2
    
#print_even_between_10_and_40()

def print_eco():
    count = 0
    while count < 10:
        print("eco")
        count += 1

#print_eco()

def coundown(num:int):
    while num >= 1:
        print(num)
        num -=1
    print("Despegue")

#coundown(10)

def monitor_time_travel(departure_year,arrival_year : int):
    while arrival_year <= departure_year:
        print(f"Viajo un año al pasado, estamos en el año {departure_year}")
        departure_year -= 1
    
#monitor_time_travel(2010,2001)

def monitor_time_travel_20(departure_year : int):
    while departure_year >= -384:
        if departure_year < 0:
            print(f"Viajo 20 años al pasado, estamos en el año {departure_year*-1} ac")
        else:
            print(f"Viajo 20 años al pasado, estamos en el año {departure_year} dc")
        departure_year -= 20
    
monitor_time_travel_20(1000)