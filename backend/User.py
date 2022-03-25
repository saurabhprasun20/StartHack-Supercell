import string

class User:
    emotion_dict={}
    def __init__(self, id, name, level,point):
        self.id = id
        self.name = name
        self.level = level
        self.point = point
        self.intervention_type = None
        self.intervention_needed = False
        self.threshold = 50
        self.emotion_dict['happy']=0
        self.emotion_dict['sad']=0
        self.emotion_dict['depressed']=0
        self.emotion_dict['angry']=0
        self.emotion_dict['hate']=0
        self.emotion_dict['fear']=0
        

    def observe_happy(self):
        if self.emotion_dict['happy']>self.threshold:
            print("INTERVENTION STARTED")
            self.intervention_type = "happy"
            self.intervention_needed =True
            print(self.intervene_user_happy())
    
    def intervene_user_happy(self):
        happy_json = {
            "msg": "What a good work User1. Keep up the positive approach and spread the light",
            "duration":"10",
            "reward": "level up"
        }
        return happy_json
    
    def observe_depression(self):
        if self.emotion_dict['depressed']>self.threshold:
            print("INTERVENTION STARTED")
            self.intervention_type = "depressed"
            self.intervention_needed =True
            print(self.intervene_user_depression())
    
    def intervene_user_depression(self):
        depression_json = {
            "msg": "I can feel you are in pain. Maybe talk to your friends.",
            "duration":"10",
        }
        return depression_json

    def observe_sad(self):
        if self.emotion_dict['sad']>self.threshold:
            print("INTERVENTION STARTED")
            self.intervention_type = "sad"
            self.intervention_needed =True
            print(self.intervene_user_happy())
    
    def intervene_user_sad(self):
        sad_json = {
            "msg": "It looks like you are not haooy with something. Talk with your friends maybe",
            "duration":"10",
            "reward": "None"
        }
        return sad_json
    
    def observe_angry(self):
        if self.emotion_dict['angry']>self.threshold:
            print("INTERVENTION STARTED")
            self.intervention_type = "angry"
            self.intervention_needed =True
            print(self.intervene_user_angry())
    
    def intervene_user_angry(self):
        angry_json = {
            "msg": "Relax and breathe. Any heated argument makes the matter worse.",
            "duration":"10",
            "reward": "None"
        }
        return angry_json

    def observe_hate(self):
        if self.emotion_dict['hate']>self.threshold:
            print("INTERVENTION STARTED")
            self.intervention_type = "hate"
            self.intervention_needed =True
            print(self.intervene_user_hate())
    
    def intervene_user_hate(self):
        hate_json = {
            "msg": "Please refrain from using hate speech. Violation of these kind are taken seriously. ",
            "duration":"10",
            "reward": "None",
            "punishment": "Level down"
        }
        return hate_json

    def observe_fear(self):
        if self.emotion_dict['fear']>self.threshold:
            print("INTERVENTION STARTED")
            self.intervention_type = "fear"
            self.intervention_needed =True
            print(self.intervene_user_fear())
    
    def intervene_user_fear(self):
        fear_json = {
            "msg": "Be brave user. Talk to someone regarding your issue",
            "duration":"10",
            "reward": "None",
        }
        return fear_json
    
    

    
    




