
import time

import webbrowser

set_alarm = input('Set alarm time as H:M:S \n')

url = input('Enter the website Url \n')

actual_time = time.strftime("%I:%M:%S")

while (actual_time != set_alarm):
    print('The time is ' + actual_time)
    actual_time = time.strftime("%I:%M:%S")
    time.sleep

if (actual_time == set_alarm):
    print('Your Website is about to open')
    webbrowser.open(url)

    