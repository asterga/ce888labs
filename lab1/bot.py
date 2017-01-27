from sopel import module
from emo.wdemotions import EmotionDetector


emo = EmotionDetector()
total_count = 0


@module.rule('')
def hi(bot, trigger):
    print(trigger, trigger.nick)
    #bot.say('Hi, ' + trigger.nick)
    #Find the number and type of each emotion in each message
    global emotions
    emotions = emotions.update(emo.detect_emotion_in_raw(str(trigger)))
    print(emotions)
    global total_count
    total_count =total_count + emotions['anger']+emotions['disgust']+emotions['fear']+emotions['joy']+emotions['sadness']+emotions['surprise']
    print('Updated emotions count: '+str(total_count))
    print(type(emotions))
