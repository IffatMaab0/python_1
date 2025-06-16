import os
folders= os.listdir("Data")
for folder in folders:
    print(os.listdir(f"data/{folder}"))