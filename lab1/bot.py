from sopel import module
from emo.wdemotions import EmotionDetector

emo = EmotionDetector()

@module.rule('')
def hi(bot, trigger):
    print(trigger, trigger.nick)
    bot.say('Hi, ' + trigger.nick)
	
	#count is used for every trigger, make  a data structure to store counts and their respective triggers
	count = emo.detect_emotion_in_row(str (trigger))
	