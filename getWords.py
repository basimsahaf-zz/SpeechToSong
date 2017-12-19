from __future__ import print_function
import json
import os
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
from secret import myusername, mypassword

speech_to_text = SpeechToTextV1(
    username = myusername,
    password = mypassword,
    x_watson_learning_opt_out=False
)

#print(json.dumps(speech_to_text.models(), indent=2))

#print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

fileArray = [];

for files in os.listdir("./mp3"):
    fileArray.append(files)

print("================================")
print("Total files: " + str(len(fileArray)))
print("================================")

print("================================")
print("Started")
print("================================")
for i in range(0, len(fileArray)):
    with open(join(dirname(__file__), './mp3/' + fileArray[i]),'rb') as audio_file:
        print("Currently on file no: " + str(i))
        with open(str(i) + '.txt','w') as newJson:
            try:
                newJson.write(json.dumps(speech_to_text.recognize(audio_file, content_type='audio/mp3', timestamps=True, word_confidence=True), indent=2))
            except:
                continue

    print("================================")
    print("Done with file " + str(i));
    print("Remaining files: " + str(fileArray - i))
    print("================================")
