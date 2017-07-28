#Timesetter
import time
import win32api

try:
    import ntplib
    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')

except:
    print('Could not sync with time server.')


time_tuple = (  int(time.strftime('%Y',time.localtime(response.tx_time))), # Year
                int(time.strftime('%m',time.localtime(response.tx_time))), # Month
                int(time.strftime('%u',time.localtime(response.tx_time))), # Day of Week
                int(time.strftime('%d',time.localtime(response.tx_time))), # Day
                int(time.strftime('%H',time.localtime(response.tx_time)))-2, # Hour
                int(time.strftime('%M',time.localtime(response.tx_time))), # Minute
                int(time.strftime('%S',time.localtime(response.tx_time))), # Second
                  0, # Millisecond
              )
# Set the Time on Windows OS
win32api.SetSystemTime(time_tuple[0], time_tuple[1], time_tuple[2], time_tuple[3], time_tuple[4], time_tuple[5], time_tuple[6], time_tuple[7])
