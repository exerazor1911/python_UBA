def print_1_10():
    for i in range(1,11):
        print(i)

#print_1_10()

def print_even_between_10_and_40():
    for i in range (10,41,2):
        print(i)
    
#print_even_between_10_and_40()

def print_eco():
    for i in range(10):
        print("eco")

#print_eco()

def coundown(num:int):
    for i in range(num,0,-1):
        print(i)
    print("Despegue")

#coundown(10)

def monitor_time_travel(departure_year,arrival_year : int):
    for i in range (departure_year,arrival_year-1,-1):
        print(f"Viajo un año al pasado, estamos en el año {i}")
    
#monitor_time_travel(2010,2001)

def monitor_time_travel_20(departure_year : int):
    for i in range (departure_year,-385,-20):
        if i < 0:
            print(f"Viajo 20 años al pasado, estamos en el año {i*-1} ac")
        else:
            print(f"Viajo 20 años al pasado, estamos en el año {i} dc")
    
monitor_time_travel_20(1000)