import User

from learning_model import detect_emotion

user1 = User.User(1,'Test User',0,0)
method_dict ={
    "happy":user1.observe_happy,
    "angry":user1.observe_angry,
    "sad":user1.observe_sad,
    "hate":user1.observe_hate,
    "fear":user1.observe_fear,
    "depressed":user1.observe_depression
}


def user_input(msg1):
    detected_emotion = detect_emotion(msg1)
    if detected_emotion != 0:
        print("Emotion detected by the empathy model is -> "+detected_emotion)
        user1.emotion_dict[detected_emotion] += 10
        method_dict[detected_emotion]()

