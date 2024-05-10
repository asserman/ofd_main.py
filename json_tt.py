# import re
# text = "привет лте 13/*21/*545646-** 54 "
# update_text = re.sub(r'[^а-яА-Я0-9]', '-', text )
# print(update_text)
#
# prime_number = [2, 3, 5]
# for num_pos, num in enumerate (prime_number, start=1):
#     print(f"Prime Numbers # {num_pos:_^3}, {num:_^5}")
# name = ("HomeWork", 'tuple')
# urgency = 5
# task_f = f"Name: {name}; Urgency Level: {urgency}"
# test = 'TITLE text'
#
# print(F'{test.title()}')
#
# task_ids = [1, 2 , 3]
# task_names = ['Do homework', 'Landry', 'Pay bills']
# task_ungrenies = [5, 3, 4]
# for i in range(3):
#     print(f'{task_ids[i]:^12}{task_names[i]:^12}{task_ungrenies[i]:^12}')
#
# def create_formatted_records(fmt):
#     for i in range(3):
#         task_id = task_ids[i]
#         name = task_names[i]
#         ungrency = task_ungrenies[i]
#         print(f'{task_id:{fmt}}{name:{fmt}}{ungrency:{fmt}}')
# create_formatted_records("'^12")
# create_formatted_records('>12')
#
# large_prime_number = 1000000007
# print(f'Use commas : {large_prime_number:,d}')
#
# large_prime_number1 = 1023
# print(f'Use commas : {large_prime_number1:b}')
# print(f'Use commas : {large_prime_number1:c}')
# for i in range( 4024):
#     if (f'{i:c}'=='А'):
#         print(i)
#         break
#     print(f'{i:c}', end='')
# decimal_number = 1.23456
# print(f'Two digits: {decimal_number:.2f}')
# print(f'Two digits: {decimal_number:.4f}')
# print(f'Two digits: {decimal_number:.1f}')
# sci_number = 0.00000000412733
# print(f'Sci notation: {sci_number:e}')
# print(f'Sci notation: {sci_number:.2e}')
#
# pct_number = 0.179323
# print(f'Percentage: {pct_number:%}')
# print(f'Percentage: {pct_number:.2%}')
#
# dict = {'name':"Vacuum", 'price': 130.675}
# price_text = f'{dict["name"]}: {{{dict["price"]:.2f}}}'
# assert price_text == 'Vacuum: {130.68}'
# print(price_text)
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()
for port in ports:
    print(port.device)
portin = ports[1].device
portout = ports[2].device
portin1 = ports[3].device

baudrate = 19200
ser1 = serial.Serial(portin, baudrate=baudrate)
ser2 = serial.Serial(portout, baudrate=baudrate)
# ser3 = serial.Serial(portin1, baudrate=baudrate)
while True:
    data = ser1.read(1)
    try:
        int(data)
    except:
        print()
        ser2.write(data)
    else:
        print(int(data), end='')
        ser2.write(data)
    # print( ser3.read())




