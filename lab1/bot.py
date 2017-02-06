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
   print("line read")
   print(trigger, trigger.nick)
   #bot.say('Hi, ' + trigger.nick)
   #Find the number and type of each emotion in each message
   emotions = emo.detect_emotion_in_raw(str(trigger))
   print(emotions)
   global total_count
   total_count =total_count + emotions['anger']+emotions['disgust']+emotions['fear']+emotions['joy']+emotions['sadness']+emotions['surprise']
   print('Updated emotions count: '+str(total_count))
  
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
	
   #The average number of emotions per message
   print("Average emotion per message: "+str(total_count/messages))
	
   #The average of each emotion
   print("Average anger emotion expressed per message: "+str(anger_count/messages))
   ave1 = anger_count/messages
   print("Average disgust emotion expressed per message: "+str(disgust_count/messages))
   ave2 = disgust_count/messages
   print("Average fear emotion expressed per message: "+str(fear_count/messages))
   ave3 = fear_count/messages
   print("Average joy emotion expressed per message: "+str(joy_count/messages))
   ave4 = joy_count/messages
   print("Average sadness emotion expressed per message: "+str(sadness_count/messages))
   ave5 = sadness_count/messages
   print("Average surprise emotion expressed per message: "+str(surprise_count/messages))
   ave6 = surprise_count/messages
	
   #Rolling averages for each emotion
   ave1 = ave1 + 0.1 * (emotions['anger'] - ave1)
   print("Rolling Average for anger: "+str(ave1))
   ave2 = ave2 + 0.1 * (emotions['disgust'] - ave2)
   print("Rolling Average for disgust: "+str(ave2))
   ave3 = ave3 + 0.1 * (emotions['fear'] - ave3)
   print("Rolling Average for fear: "+str(ave3))
   ave4 = ave4 + 0.1 * (emotions['joy'] - ave4)
   print("Rolling Average for joy: "+str(ave4))
   ave5 = ave5 + 0.1 * (emotions['sadness'] - ave5)
   print("Rolling Average for sadness: "+str(ave5))
   ave6 = ave6 + 0.1 * (emotions['surprise'] - ave6)
   print("Rolling Average for surprise: "+str(ave6))
	
	
	
