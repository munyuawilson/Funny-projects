import time 


details=print('set the time>')
#get user input
year=int(input('year>'))
month=int(input('month>'))
today_date=int(input('date>'))
hour=int(input('Hour>'))
minutes=int(input('min>'))
#getting the future time in epoch(seconds)
alarm_time =(year,month,today_date,hour,minutes,0,0,362,0)
result=time.struct_time(alarm_time)
result_two=time.mktime(result)

#compare both 

time_now=time.time()
print(result_two,time_now)

while time_now != result_two:
    alarm_time =(year,month,today_date,hour,minutes,0,0,362,0)
    result=time.struct_time(alarm_time)
    result_two=time.mktime(result)
    if time_now == result_two:
        song=vlc.MediaPlayer("Element.mp3").play()
        input('')












