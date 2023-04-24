import requests,json
import os
import azure.cognitiveservices.speech as speechsdk
import music as mc

#定义声音音色默认普通话女生
voice_style = 'zh-CN-XiaoxiaoNeural'

def pretty_print_POST():
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    def say():
         print('你好')
    say()

def text_to_speech(text):
	# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription='5498c6ea93fd4d6eaa866dc84059aab1', region='eastus')
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    speech_config.speech_recognition_language="zh-CN"

    #广东女生 yue-CN-XiaoMinNeural
    #广东男生 yue-CN-YunSongNeural
    #广东传统男 zh-HK-HiuGaaiNeural
    #广东传统女 zh-HK-HiuMaanNeural
    #普通话女生 zh-CN-XiaoxiaoNeural
    #普通话男生 zh-CN-YunxiNeural
    #新闻男 zh-CN-YunyangNeural
    #讲故事男 zh-CN-YunyeNeural
    #讲故事童音女 zh-CN-XiaoshuangNeural
    #客服女 zh-CN-XiaoyanNeural
    #东北女 zh-CN-liaoning-XiaobeiNeural
    #四川男 zh-CN-sichuan-YunxiNeural
    #台湾女 zh-TW-HsiaoYuNeural
    #上海女 wuu-CN-XiaotongNeural
    #陕西女 zh-CN-shaanxi-XiaoniNeural
    #河南男 zh-CN-henan-YundengNeural

    # The language of the voice that speaks.
    global voice_style
    speech_config.speech_synthesis_voice_name=voice_style

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Get text from the console and synthesize to the default speaker.
    #print("Enter some text that you want to speak >")
    #text = input()

    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
    #还原音色
    voice_style = 'zh-CN-XiaoxiaoNeural'
    #speech_synthesizer.close()

def speech_to_text():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription='694263994ece49808e55780170859bd3', region='eastus')
    speech_config.speech_recognition_language="zh-CN"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    #print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return speech_recognition_result.text
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")	
    speech_recognizer.close()

def ask_chat_gpt(question):
	if question.startswith('播放'):
		mc.play_song(question.replace('播放',''))
		return '好的，正在为您播放{}'.format(question.replace('播放',''))
	elif question.startswith('暂停'):
		mc.pause_play()
		return '好的，播放已暂停'
	global voice_style
	#设置音色
	if question.startswith('用河南话'):
		voice_style = 'zh-CN-henan-YundengNeural'
	elif question.startswith('用粤语'):
		voice_style = 'yue-CN-XiaoMinNeural'
	elif question.startswith('用陕西话'):
		voice_style = 'zh-CN-shaanxi-XiaoniNeural'
	url = 'http://openai.spongeai.cn/v1/chat/completions'
    # Initializing JSON data
	json_datas = {"model": "gpt-3.5-turbo","messages": [{"role": "user", "content": question}], "temperature": 0.2 }

	headers = { 'Content-Type':'application/json','Authorization':'Token 91733bb042671dd0111124ab65809ca1d1794a9d'}
	response = requests.post(data=json.dumps(json_datas),headers=headers,url=url,timeout=15)
    
	# Printing the parsed values
	r_text = str(response.content.decode("unicode_escape"))
	#print(r_text)
	r_json = json.loads(r_text.replace("\n", "\\n"))
	return str(r_json['choices'][0]['message']['content'])
def sub_str(text):
	print(text.replace('播放',''))
