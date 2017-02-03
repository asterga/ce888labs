from sopel import module
from emo.wdemotions import EmotionDetector


emo = EmotionDetector()
total_count = 0
anger_count = 0
disgust_count = 0
fear_count = 0
joy_count = 0
sadness_count = 0
surprise_count = 0
messages = 0


@module.rule('')
def hi(bot, trigger):
    print(trigger, trigger.nick)
    #bot.say('Hi, ' + trigger.nick)
    #Find the number and type of each emotion in each message
    emotions = emo.detect_emotion_in_raw(str(trigger))
    print(emotions)
    global total_count
    total_count =total_count + emotions['anger']+emotions['disgust']+emotions['fear']+emotions['joy']+emotions['sadness']+emotions['surprise']
    print('Updated emotions count: '+str(total_count))
    print(type(emotions))
	global messages
	messages = messages + 1
	global anger_count
	anger_count = anger_count + emotions['anger']
	global disgust_count
	disgust_count = disgust_count + emotions['disgust']
	global fear_count
	fear_count = fear_count + emotions['fear']
	global joy_count
	joy_count = joy_count + emotions['joy']
	global sadness_count
	sadness_count = sadness_count + emotions['sadness']
	global surprise_count
	surprise_count = surprise_count + emotions['surprise']
	
	
