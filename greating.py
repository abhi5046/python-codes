import time
timestamp=time.strftime("%H:%M:%S")
print(timestamp)
timestamp=int(time.strftime("%H"))

if(timestamp < 12):
    print("Good Morning")
elif(timestamp==12 & timestamp< 16):
    print("Good Afternoon")
elif(timestamp>=16 & timestamp<=20):
    print("Good Evening")
else:
    print("good night")

print("Thank You !!!")