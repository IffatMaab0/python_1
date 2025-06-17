# import time
# import plyer

# Function to display reminder using system message
# def remind_to_drink():
#     plyer.notification.notify(
#         title = "Drink Water Reminder",
#         message = "Time to drink a glass of water 💧",
#         timeout = 10
#     )

# while True:
#     remind_to_drink()
#     time.sleep(3600)    # Sleep for 1800 seconds (30 minutes)


    #####using os module#### 


import os
import time

def remind_to_drink():
    os.system('msg * " Drink Water Reminder: Time to hydrate!"')

while True:
    remind_to_drink()
    time.sleep(1800)          # Sleep for 1800 seconds (30 minutes)
