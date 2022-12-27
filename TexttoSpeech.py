import pyttsx3 #import pyttsx3 using pip install pyttsx3
speaker=pyttsx3.init()

speaker.setProperty("rate",125)
speaker.setProperty("volume",0.5)
duration=speaker.getProperty("volume")
speaker.save_to_file("this is a test","test.mp3")#its will save text to audio format
print(duration)

speaker.say("This is a text to speech of python") #it will speak the text  inside the say() function orelse parrameter

speaker.runAndWait()#it will run the speech