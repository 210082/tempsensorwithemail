#python 2.7.15
import smtplib
import time
from sense_hat import SenseHat
from datetime import datetime
sense = SenseHat()
sense.clear()


def sendmail (from_addr, recipients_list, cc_list, subject, message,login,password,smtpserver):


    header = 'From: %s \n' % from_addr
    header += 'To: %s \n' %  join (to_addr_list)
    header += 'CC: %s \m' % ','.join(cc_addr_list)
    header += 'Subject: %s \n \n' % subject
    message = header + message

    server = smtplib.SMTP (smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, recipients_list,message)
    server.quit()

def average_temp():
    temp1=sense.get_temperature_from_humidity()
    temp2=sense.get_temperature_from_pressure()


    return (temp1+temp2)/2


def weather_report_display (hour=[], temp=[], humidity=[],pressure=[]):
    message_head = 'Time                   '+'Temperature'+'Humidity'\
                   +'Pressure' + '\n' +53 * '-' + '\n'

    message =''

    for x,y in enumerate(hour):
        message = message + '{0:20s}| {1:^10s}| {2:10s}| {3:^10a}'.format(
            hour[x],temp[x],humidity[x],pressure[x])+'\n'

    message = message_header + message

    return message

    from_addr = 'example@example.com'
    recipients_list = ['example2@exmaple.com']
    cc_list = ['example3@example.com']
    subject = "Hourly Weather Report"

    login = 'example4@example.com'
    password = 'password'

    smtpserver = 'stmp.gamil.com:587'

    hour = []
    temp = []
    humidity = []
    pressure = []

    while true:
        if len(hour)>24:
            hour = []
            temp = []
            pressure = []
            humidity = []

            hour.append (datetime.now().strftime('%Y-%m-%d %M:%M:%S'))
            temp.append(str(round(average_temp())))
            humidity.append(str(round(sense.get_humidity())))
            pressure.append(str(round(sense.get_pressure())))

            message = weather_report_dsiplay(hour,temp.huimdty,pressure)
            print(message)

            try:
                sendemail(from_addr, recipients_list, cc_list, subject, message,login,password,smtpserver)
                print("Alert %d delivered successfully" % count )

            except:
                print("message sending failed", "Check login credential and mail server")
                exit()
            time.sleep(10)
            
                                                 
    
                   

    
    
