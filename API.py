import requests
APIKEY="e3f5eae9141132f407e825c20a414bd6"
City=input("Enter a city to get its weather report..")
#city mumbai
data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKEY}")
responseData=data.json()
#print(responseData.weather)
print(responseData)
print()
print(f"{city}has temparature of=>",responseData["main"]["temp"],"k")
print(f"{city} has humidity of =>",responseData["main"]["humidity"],"%")