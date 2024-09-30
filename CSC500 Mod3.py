# Part 1

charge = float(input('What is cost of the meal purchased? '))
tip = 0.18*charge
tax = 0.07*charge

total = round(charge + tip + tax,2)

print(f'With tax and tip, the total cost of your meal is ${total}.')

# Part 2

current_time = float(input('What is the current time in hours? '))
set_alarm = float(input('How many hours until you want the alarm to go off? '))

alarm_time = int((current_time+set_alarm)%24)

print(f"Alarm set! It will go off at {alarm_time} o'clock.")