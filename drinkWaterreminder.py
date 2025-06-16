import time
import plyer

def remind_to_drink():
    plyer.notification.notify(
        title = "Drink Water Reminder",
        message = "Time to drink a glass of water 💧",
        timeout = 10
    )

while True:
    remind_to_drink()
    time.sleep(3600) 