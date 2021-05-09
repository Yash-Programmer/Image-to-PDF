from PIL import Image
import os
import pyttsx3

eng = pyttsx3.init()

filename = 'Input_File.png'
image = Image.open(filename)
if image.mode == "RGBA":
    image = image.convert('RGB')
output = 'Output_File.pdf'
if not os.path.exists(output):
    image.save(output, 'PDF', resolution=100.0)

print('Your file is created successfully.')
OpenDocument = input('Do You want to open the file:  ')

if OpenDocument.lower() == 'no':
    print('no issues')
elif OpenDocument.lower() == 'yes':
    os.startfile(output)
    eng.say("We have open the file successfully")
    eng.runAndWait()
else:
    print('Invalid Input Command')
