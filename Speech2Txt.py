# import the module
import speech_recognition as sr
whatsapp_file = open("Whatsapp.txt")
whatsapp_data = whatsapp_file.readlines()
whatsapp_dic = {}
for line in whatsapp_data:
    whatsapp_dic[line.split()[0]] = line.split()[1]


def txt_emptylines(filename):
   with open(filename) as f_input:
      data = f_input.read().rstrip('\n')

   with open(filename, 'w') as f_output:
      f_output.write(data)


def listen():
   # create the recognizer
   r = sr.Recognizer()
   # define the microphone
   mic = sr.Microphone(0)
   # record your speech
   with mic as source:
      audio = r.listen(source)
   # speech recognition
   result = r.recognize_google(audio)
   # export the result
   #with open('my_result.txt', 'w') as file:
   #   file.write("Recognized text:")
   #   file.write("\n")
   #   file.write(result)
   #print("Exporting process completed!")
   whatsapp_update("SPIDERMAN SIGN/Whatsapp/","send_whatsapp_message_mic/", result)

def whatsapp_update(gesture, function, params):
   new_function = function + params

   key = {i for i in whatsapp_dic if whatsapp_dic[i] == new_function}
   if key:
      del whatsapp_dic[key.pop()]

   whatsapp_dic[gesture] = new_function

   # todo: check if the another function has the same sign to avoid overwritten
   txt = ""
   for key, value in whatsapp_dic.items():
      txt += f"{key} {value}\n"

   open("Whatsapp.txt", "w+").write(txt)
   txt_emptylines("Whatsapp.txt")