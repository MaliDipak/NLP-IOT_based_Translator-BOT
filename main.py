import speech_recognition as sr
r = sr.Recognizer()
def audio2text(audiofileinput):
    with sr.AudioFile(audiofileinput) as source:
        audio = r.listen(source)
        try:
            print("Working on it....")
            text = r.recognize_google(audio)
            #   print(text)
            file = open("D:/PROJECTS AND PRESENTATIONS/SEMESTER PROJECT/PROJECT STAGE-I/PS-I Speech to Text/outputtext/output.txt", "w")
            a = file.write(text)
            file.close()  
            print("Done....")
        except:
            print("Sorry....Try Again.....")
