import re

#Coverting to 24-hour time system
def convert_to_twfour(stime):
    zone = re.findall('[PM,AM]+',stime)
    time = re.findall('[0-9]+:+[0-9]+',stime)
    if zone[0] == 'PM':
        dok = time[0]
        pos = dok.find(':')
        ltime = dok[:pos]
        rtime = dok[pos:]
        ntime = int(ltime) + 12
        new_time = str(ntime)+ rtime
    else :
        new_time = time[0]
    return new_time

#Convert to 12-hour (PM,AM format)
def convert_to_zone(time):
    temp_time = int(time[:time.find(':')])
    temp_min = time[time.find(':'):]
    if  temp_time >= 12:
        ltime = 12
        if temp_time > 12:
            ltime = temp_time - 12
        con_time = str(ltime)+temp_min+' PM'
    elif temp_time < 12:
        ltime = temp_time
        if ltime == 0:
            ltime = 12
        con_time = str(ltime)+temp_min +' AM'
    return con_time

#Compute the final day
def compute_day(day,dayspassed):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    fday = (days.index(day) + dayspassed) % 7
    return days[fday]

#add_time function:Gets the input, converts the time to 24_hour format
# computes final time and day,converts it again in 12 hour format  and prints it.
def add_time(stime , dur , sday=None):


    ch_time = convert_to_twfour(stime)
    numB = int(ch_time[ch_time.find(':')+1:]) + int(dur[dur.find(':')+1:])
    divnumB = numB % 60

    remainder = numB // 60
    numA = int(ch_time[:ch_time.find(':')]) + int(dur[:dur.find(':')]) + remainder
    numB = str(divnumB)
    if int(numB) < 10 :
        numB='0' + numB
    cur_hour = str(numA % 24)
    days_passed = numA // 24
    conv_time = convert_to_zone(cur_hour+':'+numB)
    final_answer = conv_time
    if sday is not None:
        final_day = compute_day(sday,days_passed)
        final_answer = final_answer + ', '+final_day
    if days_passed == 0:
        final_answer = final_answer
    elif days_passed == 1:
        final_answer = final_answer + ' (next day)'
    else:
        final_answer = final_answer +' (' + str(days_passed)+' days later)'

    print(final_answer)


start_time = input('Type a start time in the 12-hour clock format (ending in AM or PM): ')
dur = input("Type the duration in the format hours:mins(minutes must be less than 60: ")
day = input('Type the day of the week(of start time) optionally:')
if day is not None:
    add_time(start_time,dur,day)
else:
    add_time(start_time, dur)
