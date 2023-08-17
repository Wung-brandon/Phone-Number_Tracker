from tkinter import *
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz


root = Tk()
root.title("Phone Number Tracker")
root.geometry("365x584+300+200")
root.resizable(False,False)

def Track():
    enter_number = entry.get()
    number = phonenumbers.parse(enter_number)
    #country
    locate = geocoder.description_for_number(number,'en')
    country.config(text=locate)
    #TimeZone of the country
    location = timezone.time_zones_for_number(number)
    zone.config(text=location)
    #Service provider of the country
    service_provider = carrier.name_for_number(number,'en')
    sim.config(text=service_provider)
    #longitude and latitude
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(locate)
    
    lng = location.longitude
    lat = location.latitude
    longitude.config(text=lng)
    latitude.config(text=lat)
    
    #time showing in phone 
    time = TimezoneFinder()
    result = time.timezone_at(lng=location.longitude,lat=location.latitude)
    
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M%p")
    clock.config(text=current_time)
    
    
#icon imaage
#icon = PhotoImage(file=r"C:\Users\WK. BRANDON\Desktop\Tracking\icon.png.png")
#root.iconphoto(False,icon)

#logo
#logo = PhotoImage(file=r"C:\Users\WK. BRANDON\Desktop\Tracking\icon.png.png")
#label(root,image = logo).place(x=20,y=70)
#num = PhotoImage(file=r"C:\Users\WK. BRANDON\Desktop\Tracking\neumorphic-rectangle-button-free-png (1).png")
#Label(root,image = num).place(x=5,y=160)

#heading
heading = Label(root,text="Track Number",justify="center", font=('ariel',15,'bold'))
heading.place(x=110,y=110)

#bottom
#bottom = PhotoImage(file=r"C:\Users\WK. BRANDON\Desktop\Tracking\pngtree-search-bar-png-and-icon-png-image_7771045.png")
#Label(root,image=bottom).place(x=-50,y=100)

#entry
entry = StringVar()
enter_number = Entry(root,textvariable=entry,width=20,justify="center",bd=0,background="blue", font=('ariel',20,'bold'))
enter_number.place(x=35,y=230)

#search button
#search_image = PhotoImage(file=r"C:\Users\WK. BRANDON\Desktop\Tracking\icon.png.png")
search = Button(root,text="Search",justify='center', borderwidth=0,cursor="hand2",font=('ariel',15,'bold'),background="blue",bd=0,command=Track)
search.place(x=150,y=300)

#label(information)
country = Label(root,text="Country",fg="black",bg="white",font=('arial',10,'bold'))
country.place(x=50,y=390)

sim = Label(root,text="Service Provider",fg="black",bg="white",font=('arial',10,'bold'))
sim.place(x=200,y=390)

zone = Label(root,text="TimeZone",fg="black",bg="white",font=('arial',10,'bold'))
zone.place(x=50,y=430)

clock = Label(root,text="Phone Time",fg="black",bg="white",font=('arial',10,'bold'))
clock.place(x=200,y=430)

longitude = Label(root,text="Longitude",fg="black",bg="white",font=('arial',10,'bold'))
longitude.place(x=50,y=470)

latitude = Label(root,text="Latitude",fg="black",bg="white",font=('arial',10,'bold'))
latitude.place(x=200,y=470)


root.mainloop()





