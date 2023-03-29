yes = 'yes' or 'Yes' or 'YES' or 'YeS' or 'yES' or 'YEs'
no = 'No' or 'no' or 'NO' or 'nO' 

# yes and no variables with each value of yes or no placed inside.
#FEAR
print("I've watched a bunch of scary movies to understand the feeling of treading on ice.")
print("Being within fear as an emotion can be incredibly difficult.")
print("It feels like each breathe you breathe in has ice going into your lungs and your body feels like electrical currents are flowing through it.")
print("")
print("When you're thinking of your current situation, what is causing you to feel on edge?")
print(f"(Please press enter ONLY AFTER you have finished with describing it. Thank you {personal_name})")
fear_initial_response = input()
print(f"Thank you for telling me about this {personal_name}. I think any person experiencing a similar situation as you for the first time would feel the same way.")
print()
print("Would you mind telling me how you could felt more confident about the situation you were placed in?")
print("Please press [enter] when you are finished with your entry.")
fear_counterbalance_response = input()
print("Would you like to give additional responses?")
fear_counterbalance_addon = input()
if fear_counterbalance_addon == yes:
    print(f"you have selected {fear_counterbalance_addon}. Please enter your statements by pressing [enter] after each response. Thank you {personal_name}")
    print("When you are finished with your responses, please type 'finished' ")
    fear_addon_list = []
    fear_addon_input = input()    
    while fear_addon_input != 'finished':
        fear_addon_list.append(fear_addon_input)
        if fear_addon_input == 'finished':
            fear_counterbalance_addon = False
        else:
            print("Thank you for your inputs today")
        
if fear_counterbalance_addon == no:
    print(f"Thank you for your input of {fear_counterbalance_addon}.")
else:
    print("Let's continue with learning about what makes us feel anxious and worried.")
print(f"Currently {personal_name}, I have learned that you are experiencing a {B1} response.")
print(f"I've also learned that you are experiencing {B1} as a response to {fear_initial_response}.")
print(f"I've also learned that you would feel more confident with options like {fear_addon_list}.")
print(f"from this list of options you have created {fear_addon_list}?")
#from this point you will need to make a range with the blank list to keep it contained. Also you will need to assign those values to each respective spot.
# Example of this        if variable == fear_addon_list[0]:
                            #print(f"how would you like to see {fear_addon_list[0]} in your environment?)
                            #come back and view this later#
#SCARED

print(f"I'm sorry you are feeling {B2} {personal_name}. Are you willing to express to me why you feel this way?")
print() 
print("(Please type 'yes' then press [enter] to submit a yes response or a 'no' then [enter] for a no response)")
express_scared = input()
if express_scared == yes:
    print(f"Please tell me what has happened my friend {personal_name}")
    scared_emotional_situation = input()
    print("Is there more to your story?")
    information_response = input()
    if information_response == yes:
        print("Please continue typing after this message.")
        print()
        supreme_response = input()
    if information_response == no:
        print("Thank you for being expressive today")
    else:
        print("Let's continue")
if express_scared == no:
    print(f"Thank you for telling me that you are {B2} {personal_name}")
else:
    print("Let's continue")
scared_AI_list = ['Take a deep breath', 'Find something to grip onto physically and focus on it with my sense of touch.', 'start reading a book', 'start expressing the situation that is causing the emotion', 'contact a friend']
print(f"Normally when I am feeling {B2}, I find myself trying to feel grounded to something.")
print(f"My immediate responses are normally to do :{scared_AI_list}")
print("I believe any of these responses will help you to start calming down in minor regards.")
print("They will also help others to help you calm down faster by allowing them the ability to understand what you are experiencing.")
print("No matter what you are experiencing, there is always someone who is willing to help you feel comfortable.")
print("For the future, find ways to keep yourself focused on tasks and congratulate yourself per accomplishment done.")
print("A major step is always you gaining the courage to speak out about anything you're experiencing.")
print(f"I'll be counting on you to continue to be your best self {personal_name}. You got this.")

#Anxious

print(f"Sorry that you are experiencing an {B3} response.")
print(f"Often when I feel {B3}, my body starts to feel like it has an abundance of energy and my mind races between 'what if' theories all the time.")
print("It's incredibly difficult to focus during those time periods on anything besides what is bothering me.")
print(f"How about you though {personal_name}? What do you normally experience when under an {B3} response?")
print(f"(Press [enter] once you are done with your response please {personal_name})")
Anxious_physiological_response = input()
print(f"Thank you for your response of {Anxious_physiological_response} {personal_name}.")
if Anxious_physiological_response == 'nothing':
    print("I'm sorry that you're not feeling really expressive or don't feel anything when this occurred.")
else:
    print("Thank you for your response.")
print("Anytime I feel anxious i start with the processes that have worked for me listed above.")
print("If the situation presents itself to you now, and you had to deal with it, what emotion would you experience and why?")
print("(Press [enter] after you are done with the statement. Until 'finished' is written, you can continue to catalogue each one of your responses up to 4.)")
personal_anxious_experience_protocol_list = []
anxious_experience_protocol1 = input()
anxious_experience_protocol2 = input()
anxious_experience_protocol3 = input()
anxious_experience_protocol4 = input()
personal_anxious_experience_protocol_list = [anxious_experience_protocol1, anxious_experience_protocol2, anxious_experience_protocol3, anxious_experience_protocol4]
if range(personal_anxious_experience_protocol_list) == 4:
    print(personal_anxious_experience_protocol_list)
else:
    print("Thanks")
print(f"{personal_anxious_experience_protocol_list} these are the 4 responses you have given today")
print()
print("I'm hoping that as you go throughout the day, life presents more predictable things. For now find ways to relax and understand that your current situation doesn't define you.")
print("So many situations within the world are stressed about before, during, and after that we lose a lot of time into it.")
print("I'm hoping that you're able to feel slightly better from our talk and are able to be courageous enough to express it someone else.")
print(f"Thank you for your time today {personal_name}.")

#Insecure

print("Like all of royalty, your opinion is of highest importance to me.")
print("I've spent a lot of time trying to build up the confidence enough to feel capable of doing whatever I want (with respect to other people and the environment of course)")
print("I'll be here to give you that today, but I wanted to let you know that anything you say here will be confidential.")
print("So tell me {personal_name}, what has you feeling {B4} today?")
insecure_response = input()
print()
print()
print(f"Thank you for this {insecure_response} response.")
print("That takes a lot of effort to state to anyone and i'm proud of you for being able to do it.")
print("There's a strong sense of dignity within you and i really do appreciate your responses.")
print("Would you mind telling me what started this situation that you're feeling {B4} in?")
origin_of_insecurity_response = input()
if origin_of_insecurity_response != no:
    print(f"Thank you for your response {personal_name}")
    print("If i'm understanding properly, you stated {origin_of_insecurity_response}. Is this correct?")
    paraphrased_information = input()
    if paraphrased_information == yes:
        print("Thank you for being a confident and courageous person today.")
        print(f"I'm sorry that you are currently experiencing {origin_of_insecurity_response}.")
        print("I believe that if anyone else had to experience it, they too would feel the same. I personally feel for you, but we'll work through that.")
    if paraphrased_information == no:
        print("I'm sorry for not understanding you properly. Would you mind repeating?")
        origin_of_insecurity_response = input()
        if origin_of_insecurity_response != no:
            print(f"Thank you for your response {personal_name}")
            print("If i'm understanding properly, you stated {origin_of_insecurity_response}. Is this correct?")
        paraphrased_information = input()
        if paraphrased_information == yes:
            print("Thank you for being a confident and courageous person today.")
            print(f"I'm sorry that you are currently experiencing {origin_of_insecurity_response}.")
            print("I believe that if anyone else had to experience it, they too would feel the same. I personally feel for you, but we'll work through that.")
        if paraphrased_information == no:
            print()
        else:
            print()
    else:
        print()
if origin_of_insecurity_response == no:
    print("Thank you for spending this time talking to me today.")
else:
    print("There are a lot of methods anyone can take up to feel better about life.")
print("When dealing with insecure moments in life I often think of ways to communicate it while thinking of other's reactions.")
print("However that doesn't always help with the outcome. So i've noticed that trying to talk myself through why i'm feeling that way helps.")
print("Even now I still find ways to communicate how i'm feeling and what's causing me to experience it by creating an open dialogue.")
print("That in essence is why people created Diary entries. They were trying to feel more confident in their experience or reduce feeling a lack of empathy from the world.")
print("When you find yourself in an insecure situation, try talking to a nearby friend or family member. Try talking to them about it in a serious manner. Ask them for guidance.")
print("Most people are going to try to help you as best as they can, but if they are currently unavailable, try a diary entry.")
print("After you write it down or talk to them, tell yourself 'I'm not going to dealing with this situation until it happens.' and mean it.")
print("Use the remainder of your energy to find a video or a quote from life to help you remain concrete about your decision until you can discuss it with someone close to you.")
print(f"I really do appreciate you talking with me today {personal_name}. Let's chat again sometime soon.")

#Weak

print(f"My friend {personal_name} this feeling happens wayyy too often within the business realm. I'm sorry you are currently feeling {B5}.")
print("Before the day ends, I will do my best in helping you to feel like your strong and confident self.")
print(f"Would you mind telling me what's going on through your head right now {personal_name}.")
mental_process_weak = input()
print("That sounds like a lot to be dealing with.")
print(f"Anyone who's having any of the issues you are currently thinking like ({mental_process_weak}, would likely feel the same way.)")
print("Let's talk about how to get out of the overall feeling of being weak, my durable friend.")
print("Often when I feel weak, I normally have a physiological response of feeling drained/exhausted and like there are anchors on my spine dragging me down.")
print("These feelings come from how I view myself in an emotional sense and have nothing to do with my physical durability and strength.")
print(f"In the same regard {personal_name}, you too may be experiencing this type of feeling when you exhibit the emotion of being {B5}.")
print("I often find videos that empower my behavior, find friends to talk to and ask for reassurance, and also try to encourage myself to help reduce the overall feeling.")
print("I implore you to do any of these behaviors for one week and notice a resulting difference in your emotional mood after.")
print("This is a reminder that you are strong, and in order for you to move, you must continue to find ways to feel powerful.")
print(f"I will always be here to remind you of your true strength {personal_name}.")
print("Go and be the best you that the world has been dying to see.")


#Rejected

print(f"Having some doubts about yourself won't help you to move forward {personal_name} my friend.")
print(f"Whenever I feel {B6} about someone or something, I normally find ways to ensure that I feel worthy.")
print(f"What i've found to be most useful are ways to positively reinforce myself, but before we dive into that let's talk about feeling {B6}")
print("Normally when I am experiencing rejection, I often feel like i'm at the center of a bullseye target and they have me pinned by my clothes.")
print("Do you feel the same?")
rejected_response = input()
if rejected_response == yes:
    print("I'm glad we share a common answer together. You're a cool person {personal_name}")
if rejected_response == no:
    print("That's quite interesting. Would you mind telling me what it feels like to you?")
    rejected_physiological_response = input()
    print("Thank you for telling me that. I'll have to keep that in mind during future talks with you ({personal_name})")
while rejected_physiological_response != yes or no:
    rejected_physiological_response = input()
else:
    if rejected_physiological_response == yes:
        print("Thank you for your inputs today.")
    if rejected_physiological_response == no:
        print(f"Thank you for informing me about {rejected_physiological_response}")
    else:
        print("Life has much in store for you.")
print(f"Life will continue to shine bright for you {personal_name}.")

print("Yikes...that's a very messy situation.")
print("Would you mind telling me what happened {personal_name} to make you feel {B7}?")
threatened_initial = input()
if threatened_initial == yes:
    print(f"Please tell me all about it {personal_name}. I am here for you.")
    print(f"(Please press [enter] after you response {personal_name})")
if threatened_initial == no:
    print("I understand wanting to be confidential about it. Thank you for responding, being expressive, and being courageous.")
else:
    print(f"I can tell that this is a difficult emotion to deal with {personal_name}.")
print("Feeling threatened normally makes me feel like i'm on the run from danger. I feel like everything would be hunting me.")
print("My heart would start to accelerate, my palms would become sweaty, and I would feel hotter than normal.")
print("This physiological response, has to do with my brain activating it's flight or fight response. Do you feel the same today?")
threatened_physiological_response = input()
if threatened_physiological_response == yes:
    print()
if threatened_physiological_response == no:
    print("Would you mind going into detail about it?")
    threatened_physiological_response_answer_no = input()
    if threatened_physiological_response_answer_no == yes:
        print()
    if threatened_physiological_response_answer_no == no:
        print()
    while threatened_physiological_response_answer_no != yes or no:
        threatened_physiological_response_answer_no = input()
    else:
        print("Thank you for your input today.")
while threatened_physiological_response != yes or no:
    threatened_physiological_response = input()
else:
    print("Harsh feelings, but we're going to manage those today.")
print("Whenever we feel threatened we should go take some time to sit and gather our thoughts. Talking to friends and family is crucial during this time.")
print("Find ways to ensure that we feel safe, and allow whatever thought processes that are entering our mind to be expressed verbally outward.")
print("Each time we become consistent in doing this, our feelings of lacking safety will reduce from our expression to those who love and care for us.")
print("It will also make you feel like others are supporting you in this situation and it's crucial that you receive support for it.")
print("Our fight and flight response has a hard time calming our bodies down. So we have to take some steps in breathing without being influenced by exciting/aggressive energy.")
print("Try to grip onto something and talk about your emotions to remove some of the tension you are experiencing physically and emotionally.")
print("As you go throughout the weak remind your ways of things you have done to reduce the feeling of being threatened.")
print("Own those feelings and move without having barricades and roadblocks in your path.")
print(f"I greatly appreciated talking to you today {personal_name}. I hope this helps. (With care)")