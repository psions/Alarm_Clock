



from datetime import datetime
    
    
    
    
def set_alarm_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format, Try again."
    else:
        if int(alarm_time[0:2]) > 12:
            return "invalid Hour format, Try again"
        elif int(alarm_time[3:5]) > 59:
            return "invalid Minute format, Try again"
        elif int(alarm_time[6:8]) > 59:
                return " Invalid Second format, Try again"
        else:
            return "OK"



alarm_hour = alarm_time [0:2]
alarm_minute = alarm_time [3:5]
alarm_second = alarm_time [6:8]
alarm_period = alarm_time [9:].upper()


now = datetime.now()
current_hour = now.strftime("%I")
current_minute = now.strftime("%M")
current_second = now.strftime("%S")
current_period - now.strftime("%p")


while True:
    alarm_time =input("Enter time in 'HH:MM:SS AM/PM' format: ")

    validate = set_alarm_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f" Setting alarm for {alarm_time} ... ")
        break



if alarm_period == current_period:
    if alarm_hour == current_hour:
        if alarm_minute == current_minute:
            if alarm_second == current_second:
                print( "WAKE AND BAKE TIME!!")


while True:
    now = datetime.now()

    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_minute:
                if alarm_sec == current_second:
                    print("Wake AND BAKE TIME!")