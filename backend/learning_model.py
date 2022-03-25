from locale import normalize
from empath import Empath
lexicon = Empath()
# emotion_category2 = ['fear', 'disgust', 'anger', 'violence', 'shame', 'love', 'rage', 'help', 'envy', 'joy']
# emotion_dict = Empath().analyze('He killed a guy' , categories=emotion_category2)
def detect_emotion(user_input):
    emotion_dict = Empath().analyze(user_input, normalize=True)
    # print(emotion_dict)
    key_list = []
    for key in emotion_dict:
        if emotion_dict[key] > 0:
            key_list.append(key)
            # print(key+":"+str("{:.2f}".format(emotion_dict[key])))


    major_emotion_dict = {
        "happy": ["cheerfulness", "optimism", "celebration", "party", "poitive_emotion"],
        "sad": ["emotional", "shame", "negative_emotion"],
        "depressed":["cold", "nervousness", "neglect", "shame", "pain", "timidity", "contentment"],
        "angry": ["hate", "aggression", "violence", "rage", "shame", "pain", "emotional"],
        "hate": ["hate", "envy", "negative_comment"],
        "fear": ["fear", "violence,pain", "negative_emotion"]
    }

    count_arr = [0,0,0,0,0,0]

    index2emo_dict = {

    }

    if len(key_list) == 0:
        return 0

    for key in key_list:
        for temp_key in major_emotion_dict:
            if key in major_emotion_dict["happy"]:
                count_arr[0] += 1
                index2emo_dict[0] = "happy"
            
            elif key in major_emotion_dict["sad"]:
                index2emo_dict[1] = "sad"
                count_arr[1] += 1
                
            elif key in major_emotion_dict["depressed"]:
                index2emo_dict[2] = "depressed"
                count_arr[2] += 1
                
            elif key in major_emotion_dict["angry"]:
                index2emo_dict[3] = "angry"
                count_arr[3] += 1
                
            elif key in major_emotion_dict["hate"]:
                index2emo_dict[4] = "hate"
                count_arr[4] += 1
                
            elif key in major_emotion_dict["fear"]:
                index2emo_dict[5] = "fear"
                count_arr[5] += 1
                


    max_val = max(count_arr)
    if max_val == 0:
        print(key+":"+str("{:.2f}".format(emotion_dict[key])))
        return 0
    index = count_arr.index(max_val)
    return (index2emo_dict[index])


# print(detect_emotion("Hurray we won"))