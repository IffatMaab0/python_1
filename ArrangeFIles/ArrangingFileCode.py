import os
#Created a function to check if the similar folder exists
def CheckPrevious(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")       
    
files =os.listdir()
files.remove("ArrangingFileCode.py")
print(files)

CheckPrevious('Images')
CheckPrevious('Docs')
CheckPrevious('Media')
CheckPrevious('Others')

#sending images of mentioned type in images folder
imageExt=[".jpg", ".jpeg", ".png"]
images=[file for file in files if os.path.splitext(file)[1].lower() in imageExt]

#sending documents of mentioned type in Docs folder
docExt=[".pdf",".pptx",".py",".cpp"]
Docs=[file for file in files if os.path.splitext(file)[1].lower() in docExt]

#sending Videos of mentioned type in Media folder
medExt=[".mp4",".mp3",".flv"]
media=[file for file in files if os.path.splitext(file)[1].lower() in medExt]

others=[]
for file in files:
    ext=os.path.splitext(file)[1].lower()
    if (ext not in imageExt) and (ext not in docExt) and(ext not in medExt) and os.path.isfile(file):
        others.append(file)


move("Media",media)
move("Images",images)
move("Docs",Docs)
move("Others",others)

