from flask import Flask,render_template,request,jsonify
import speech_recognition as sr
import requests
import json
from watson_developer_cloud import ConversationV1
ls = []
url = "https://gateway.watsonplatform.net/conversation/api"

username = "5b68a8cb-60f9-4d12-a206-fbf7ff0eb02e"
password = "A4KMYxxX6wRl"


conversation = ConversationV1(
    username= username,
    password= password,
    version='2017-04-21')

workspace_id = '2e430183-83e5-4d95-a22e-fb8da606d693'



app = Flask(__name__)

@app.route('/')
def dir1():
    return render_template("sentiment.html")


@app.route('/speechRecog')
def speechRecog():
	speech = speechRecog_main()
	text_message = speech
	response = conversation.message(workspace_id=workspace_id, message_input={'text': text_message})
	response = json.dumps(response, indent=2)
	response = json.loads(response)
	print(response)
	print(response["output"]["text"])	
	#print response.status_code
	#print response.text

	return jsonify(text_message, response["output"]["text"])







def speechRecog_main():

		mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
		sample_rate = 48000
		chunk_size = 2048
		r = sr.Recognizer()
		 

		mic_list = sr.Microphone.list_microphone_names()

		for i, microphone_name in enumerate(mic_list):
		    if microphone_name == mic_name:
		        device_id = i
        
		with sr.Microphone(device_index = i, sample_rate = sample_rate, 
		                        chunk_size = chunk_size) as source:

		    r.adjust_for_ambient_noise(source)
		    print ("Say Something")
		    audio = r.listen(source)
		         
		    try:
		        text = r.recognize_google(audio)
		        print(text)
		        return text
		     

		     
		    except sr.UnknownValueError:
		        print("Google Speech Recognition could not understand audio")
		     
		    except sr.RequestError as e:
		        print("Could not request results from Google Speech Recognition service; {0}".format(e))





@app.route('/get_message')
def get_message():

	message_input = request.args.get('message_input',0 ,type=str)
	text_message = message_input
	response = conversation.message(workspace_id=workspace_id, message_input={'text': text_message})
	response = json.dumps(response, indent=2)
	response = json.loads(response)
	print(response)
	print(response["output"]["text"])	
	#print response.status_code
	#print response.text

	return jsonify(response["output"]["text"])



if __name__ == '__main__':
    app.run()
