import os
files = os.listdir("clutteredFolder")
i=1
for file in files:
    if file.endswith(".png"):
        os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}.png")
        print(file)
        i=i+1
