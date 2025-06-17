import os
#Created a function to check if the similar folder exists
def CheckPrevious(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
files =os.listdir()

CheckPrevious('Images')
CheckPrevious('Docs')
CheckPrevious('Media')

#sending images of mentioned type in images folder
imageExt=[".jpg", ".jpeg", ".png"]
images=[file for file in files if os.path.splitext(file)[1].lower in imageExt]

#sending documents of mentioned type in Docs folder
docExt=[".pdf",".pptx",".py",".cpp"]
images=[file for file in files if os.path.splitext(file)[1].lower in docExt]

#sending Videos of mentioned type in Media folder
medExt=[".mp4",".mp3",".flv"]
images=[file for file in files if os.path.splitext(file)[1].lower in medExt]

