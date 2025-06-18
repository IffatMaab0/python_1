import time
currentTime= time.strftime('%H : %M : %S')
print("the time is " , currentTime)
hour=int(time.strftime("%H"))
if (5<= hour and hour<=11):
    print("Good Morning!")
elif(hour==12):
    print("Good Noon!") 
elif(12< hour and hour<=16):
    print("Good AfterNoon!")
elif(16<hour and hour<=19):
    print("Good Evening!")
else:
    print("Good Night!" )         




