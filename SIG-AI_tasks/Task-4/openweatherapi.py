import requests #This module allows us to send http requests from python
def weather(city):
    url = "https://open-weather13.p.rapidapi.com/city/"+ city + "/EN" 
    head_dict = {}
    head_dict["x-rapidapi-host"] = "open-weather13.p.rapidapi.com"
    head_dict["x-rapidapi-key"] = "723cabfb34msh1343ed360c54d70p194ae9jsn500bf4c6f6fc" # enter the api key provided in the readme file
    res = requests.get(url, headers=head_dict)
    res_dict = res.json()
    print( "Name: " , res_dict["name"]) 
    print("Temperature: " , res_dict["main"]["temp"]) 
    print( "Weather Description: " , res_dict["weather"][0]["description"]) 
    print("Wind Soeed:",res_dict["wind"]["speed"]) 
    print("Humidity",res_dict["main"]["humidity"]) 
    print("Location Coordinates")
    print("Longitude:",res_dict["coord"]["lon"])         
    print("Latitude",res_dict["coord"]["lat"])

#MAIN PROGRAM
while True:
    city = input("Which city's weather would you like to view?\n").strip() 
    weather(city)
    ch=input("Do you want to check the weather of another city?\n")
    if ch.lower()=="yes":
        pass
    elif ch.lower()=="no":
        print("Thank you for choosing our services")
        print("If you require any of our other services pls contact:7095419591 (lokesh)")
        break
#End of program
