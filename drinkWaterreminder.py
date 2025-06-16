# import time
# import plyer

# def remind_to_drink():
#     plyer.notification.notify(
#         title = "Drink Water Reminder",
#         message = "Time to drink a glass of water 💧",
#         timeout = 10
#     )

# while True:
#     remind_to_drink()
#     time.sleep(3600) 


    #####using os module#### 


import os
import time

def remind_to_drink():
    os.system('msg * " Drink Water Reminder: Time to hydrate!"')

while True:
    remind_to_drink()
    time.sleep(1800) 