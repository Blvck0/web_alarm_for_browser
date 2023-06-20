
import time

import webbrowser

set_alarm = input('Set alarm time as H:M:S')

url = input('Enter the website Url')

actual_time = time.strftime("%I:%M:%S")

while (actual_time != set_alarm):
    print('The alarm is ' + actual_time)
    actual_time = time.strftime("%I:%M:%S")
    time.sleep

    