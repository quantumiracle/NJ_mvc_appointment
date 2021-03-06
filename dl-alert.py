import urllib.request
import re
import time
from bs4 import BeautifulSoup
from datetime import datetime
# import winsound
import os

# location_arr = ['101','102','103','104','105','106','107','108','109','110','111','112','113','114','115','116','117','118','119','120','121','122','123']  # for renew
location_arr = ['186','187','188','189','190','191','192','193','194','195','196','197','198','199','200','201','202','203','204','205','206','207','208']  # for initial
locationname_arr = ['Lawrenceville','Bayonne','North Cape May','Camden','Cardiff','Salem','Delanco','Eatontown','SouthPlainfield','Edison','Flemington','Toms River','Freehold','Lodi','Vineland','Newark','North Bergen','Wayne','Oakland','Paterson','Thorofare','Rahway','Randolph']
# base_url_link='https://telegov.njportal.com/njmvc/AppointmentWizard/11/'  # for renew
base_url_link='https://telegov.njportal.com/njmvc/AppointmentWizard/15/'  # for initial

required_months = ['August','September', 'October']

# def beep():
## this only works on windows
#     winsound.Beep(1500, 500)
#     winsound.Beep(4500, 500)
#     winsound.Beep(2500, 500)
#     winsound.Beep(1500, 500)
#     winsound.Beep(4500, 500)
#     winsound.Beep(2500, 500)

def beep():
    # works on ubuntu
    os.system('beep -f %s -l %s' % (1500, 500))
    os.system('beep -f %s -l %s' % (4500, 500))
    os.system('beep -f %s -l %s' % (2500, 500))
    os.system('beep -f %s -l %s' % (1500, 500))
    os.system('beep -f %s -l %s' % (4500, 500))
    os.system('beep -f %s -l %s' % (2500, 500))


def job():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("\n\n\nDate Time: ", dt_string, "\n\n")
    i=0
    found=0
    
    
    for location in location_arr:
        print(location)
        with urllib.request.urlopen(base_url_link+location) as response:
            page_html = response.read()
        soup = BeautifulSoup(page_html ,'lxml')
        unavailable=soup.find('div',attrs={'class': 'alert-danger'})
        if unavailable is not None :
            print('No appointments are available in '+locationname_arr[i])
            dt_string=""
        else:
            dates_html = soup.find('div',attrs={'class': 'col-md-8'})
            # print(dates_html)
            date_string = dates_html.find('label',attrs={'class': 'control-label'})
            if set(required_months) & set(date_string.text.split()):
                print("Matching required months")
                date_string=re.sub('Time of Appointment for ', '', date_string.text)
                date_string=re.sub(':', '', date_string)
                message = 'DL Renew Dates: '+locationname_arr[i]+' / ('+location+') : '+date_string
                print(message)
                beep()
                found=1
        i=i+1
        
while True :
    try:
        job()
    except:
        print("Something went wrong")
        time.sleep(60)
    else:
        time.sleep(60)
    
