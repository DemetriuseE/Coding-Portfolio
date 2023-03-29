yes = 'yes'
no = 'no'


Bad
print(f"When i'm normally just feeling all around {C1}, I find it hard to gain hope in much of anything. Normally this feeling is given during time periods where I feel like I could have done more.")
print(f"Each time i'm feeling {C1}, I normally have a bodily response of feeling like i'm dragging along and on low energy.")
print("A great example of this would be wearing a military weighted vest and walking around during dehydration.")
print(f"I know it may be tough to see the light today {personal_name}, but would you mind telling me what's making you feel this way?")
print("(Type yes or no as a response and press [enter] to submit a response.)")
Bad_response_origin = input()
if Bad_response_origin == yes:
    print()
if Bad_response_origin == no:
    print("Would you mind describing to me what you feel when you feel bad using an analogy {personal_name}.")
    origin_response_no = input()
    if origin_response_no == no:
        print("Sorry for asking, but thank you for your responses.")
    if origin_response_no == yes:
        print(f"(Thank you {personal_name}. Please type your response then press [enter] once completed.)")
        origin_response_storytime = input()
    else:
        print(f"Thank you for spending time telling me this {personal_name}")
else:
    print(f"Let's continue with talking about how you're feeling {C1} {personal_name}.")
print(f"What do you normally do when you feel this way {personal_name}?")
expression_response_bad = input()
print(f"I find it interesting that you do {expression_response_bad}. Would you mind if i offered you some healthy tips for feeling bad?")
friendly_bad_advice_emotional_help = input()
if friendly_bad_advice_emotional_help == yes:
    print("Wonderful. These are some things I will suggest you try and hopefully come back with some habitually learned behaviors.")
    dealing_with_bad_list = {'Finding ways to express what has made me feel bad to a friend or loved one. ', 'Finding ways to cope with the feeling through information based articles ', 'Creating a method of prevention for what has happened.'}
    print (dealing_with_bad_list)
if friendly_bad_advice_emotional_help == no:
    print(f"I understand. Thank you for being such a great person {personal_name}. If you ever desire to tell me, i'll be waiting here {personal_name}.")
else:
    print(f"Thank you for talking to me today {personal_name}.")

Bored
print(f"I've experienced this a lot during childhood development. It's an experience I normally don't find myself in as much often due to taking precautionary methods to deal with it, but let's talk about you today {personal_name}")
print(f"Would you mind telling me 3 things that would spark even the slightest bit of curiosity in you today {personal_name}?")
curiosity_response = input()
if curiosity_response == yes:
    print("Wonderful {personal_name}. Tell me 3 things that would spark curiosity in you. (Type and press [enter] per each response)")
    curiosity_response_list = []
    curiosity_response_input_list = input()
    curiosity_response_list.append(curiosity_response_input_list)
    while range(curiosity_response_list) != 3:
        curiosity_response_input_list = input()
if curiosity_response == no:
    print("Understood. Thanks for at least talking to me today.")
while curiosity_response != yes or no:
    curiosity_response = input()
else:
    print(f"Let's continue {personal_name}.")
print("Whenever I cannot shake boredom, there are a couple of things I do to combat it.")
personal_bored_list = ["I search for new topics on youtube or social media to review" , "study philosphical dialogues and make a story out of them ", "or talk to friends about their hobbies to increase interest and reduce the feeling of being bored."]
print(personal_bored_list)
print("Do any of these selections sound good to you {personal_name}?")
print("(If yes, type a number between 1 to 3 and press [enter]. Otherwise just press enter to skip)")
personal_comparison_to_list_response = input()
if personal_comparison_to_list_response == 1:
    print(personal_bored_list[0])
if personal_comparison_to_list_response == 2:
    print(personal_bored_list[1])
if personal_comparison_to_list_response == 3:
    print(personal_bored_list[2])
else:
    print(f"Again, thank you so much today {personal_name}. You're a true trooper.")
print("As you go throughout the day I hope these statements help you to continue to ride the wave of inspiration.")
print("You have an abundance of potential waiting to be untapped as long as you're willing to take the steps necessary to focus on new things and new knowledge.")
print(f"I will always believe in you. Remain dignified {personal_name}.")

Busy
print("Being busy isn't an easy thing to remove. Often you make a lot of plans with others, set goals for yourself and stride to achieve them, and attempt to remain busy to prevent an idling mind.")
print("Although this is seen as 'productive' this can also lead to heavy amounts of burn out.")
print(f"{personal_name}, what has you so busy today?")
personal_business_response = input()
print(f"Thank you for your response {personal_name}.")
print(f"Now, think about what you would do if you didn't have to do all of {personal_business_response}.")
print("Speaking hypothetically, we should only focus on one thing at a time when dealing with the day. Allowing ourselves 5 minutes per hour to relax from the objective that we have to keep our minds maximized in production.")
print(f"{personal_name} for each thing that you accomplish today, reward yourself with a small minute to 2 minutes of relaxation.")
print("If you've gone for longer than 3-4 hours without doing small increments of this, please allow yourself approximately 5-10 minutes to view something that's stress-reducing.")
print()
print()
print("Often when I start to exhibit behaviors of being busy, I forget to pace myself.")
print(f"Are you finding it also difficult to pace yourself today {personal_name}.")
pacing_oneself_response = input()
if pacing_oneself_response == yes:
    print("It's common for people to experience this when they have a lot on their plate. They forget that reducing stress is a necessity in productivity for life.")
    print("I would like you to continue pacing yourself each and everyday.")
if pacing_oneself_response == no:
    print("I would like you to continue in the methods used, but increase them.")
while pacing_oneself_response != yes or no:
    pacing_oneself_response = input()
    if pacing_oneself_response == yes:
        print("It's common for people to experience this when they have a lot on their plate. They forget that reducing stress is a necessity in productivity for life.")
        print("I would like you to continue pacing yourself each and everyday.")
    if pacing_oneself_response == no:
        print("I would like you to continue in the methods used, but increase them.")
    else:
        print("Let's continue.")
else:
    print(f"Thank you so much for your responses today {personal_name}")
print(f"I hope you have a wonderful day today pacing yourself {personal_name}. Until next time.")


Stressed
print("Being stressed is not an easy emotional response to deal with.")
print(f"However, I will do my best to be here for you during this time today okay {personal_name}?")
print(f"Would you mind telling me in one sentence what is making you feel {C3}?")
print("(Type [yes] or [no] as a response. Otherwise press [(enter) to skip].)")
stressed_response = input()
if stressed_response == yes:
    print(f"Please tell me what's wrong {personal_name}.")
    print("(Thank you and press [enter] after your response.)")
    stressed_respone_story = input()
if stressed_response == no:
    print(f"That's alright. I appreciate you trying today {personal_name}.")
else:
    print("Let's continue with dealing with your stressing situation.")
print("We can start to feel overwhelmed when heightened bodily responses happen with specific events.")
print("Not only do those make it difficult for us, they also make it harder for us to focus on our current tasks.")
print("We start to stress ourselves to a point of no return and our body takes the toll.")
print("The only way we can slow this process is to start to process each stressing point with someone we trust. That way we can gather our thoughts and move with purpose.")
print("Do you have anyone whom you can talk to about your responses?")
talking_about_stress = input()
if talking_about_stress == yes:
    print(f"That is wonderful. I believe this would be a great time to talk to them about it. Will you go do that {personal_name}?")
    talking_about_stress_yes_response = input()
    if talking_about_stress_yes_response == yes:
        print(f"I'm proud of you {personal_name}. Make sure to ask for help in creating a gameplan and be receptive to it.")
    if talking_about_stress_yes_response == no:
        print(f"Well i'm always here for you {personal_name}. You can talk to me about it.")
    else:
        print("Let's talk about it briefly.")
if talking_about_stress == no:
    print("I'll be that person for you.")
while talking_about_stress != yes or no:
    talking_about_stress = input()
else:
    print(f"Thank you for expressing this to me today {personal_name}.")
print(f"{personal_name} please tell me 3 things you are currently stressed about.")
stressing_about_list = []
stressing_about_input = input()
while range(stressing_about_list) != 3:
    stressing_about_input = input()
    stressing_about_list.append(stressing_about_input)
if range(stressing_about_list) == 3 or 'finished':
    tuple(stressing_about_list)
else:
    print(f"Thank you {personal_name}.")
print("Out of all of these things that you have told me about, which one is the most stressing to you?")
print("1, 2 or 3")
print("(Type the number that corresponds with the most intense stressful situation and press [enter].)")
numerical_stress_response = input()
if numerical_stress_response == 1:
    print(f"It seems that you have chosen {stressing_about_list[0]} as your most concerning issue. You should definitely reward yourself after doing this.")
if numerical_stress_response == 2:
    print(f"It seems that you have chosen {stressing_about_list[1]} as your most concerning issue. You should definitely reward yourself after doing this.")
if numerical_stress_response == 3:
    print(f"It seems that you have chosen {stressing_about_list[2]} as your most concerning issue. You should definitely reward yourself after doing this.")
else:
    print("Thank you for telling me today.")
print("If you continue to reward yourself for major tasks on a daily basis (hobbies, goals, dates for self, and self-loving qualities) you will notice a great amount of feeling relief.")
print("The feeling of giving yourself purpose, moving with that purpose, and achieving it later will be a conditional requirement for you to feel less stress.")
print("Over time, you will deem it to be greatly worthy of doing and try to implement it into your life.")
print(f"I'm hoping that if you come back again {personal_name} you feel any of these emotions {F1,F2,F3,F4,F5,F6,F7,F8,F9,F10}. Until then, see ya :) ")

Tired
print("Often this feeling comes with a great deal of consideration to sleep patterns.")
print("Often people who are slugging along all the time likely need more sleep.")
print(f"Do you get a minimum of 8 hours of sleep daily{personal_name}?")
sleep_8_at_night = input()
if sleep_8_at_night == yes:
    print("There may be underlying health concerns there and I suggest going to see a primary physician for a further diagnosis.")
if sleep_8_at_night == no:
    print("It is suggested that you find ways to get as close to 8 hours of sleep every day.")
    print("How many hours of sleep do you get per night?")
    hours_of_sleep_less_than_8 = input()
    while hours_of_sleep_less_than_8 != int(input()):
        try:
            ValueError("Please try to give a value between 0 and 8.")
            
        except:
            pass
    if hours_of_sleep_less_than_8 <= 4:
        #Questionaire based response between each of the variables given.
        print("Anyone receiving less than 1 REM cycle of sleep (REM needs 4 hours minimum to start) needs more sleep during their sleep time.")
    if hours_of_sleep_less_than_8 > 4 and hours_of_sleep_less_than_8 < 6:
        print("I believe a sufficient nap is in order. Find a way to either receive a boost within the day using caffeine or find a way to nap for 1 hour and a half as a set time.")
    else:
        print("Please consult your primary physician.")
print(f"Do you work an overnight job {personal_name}")
overnight_job_boolean = input()
if overnight_job_boolean == yes:
    print("Working overnights does some wild things to our physiology. It's best to try and rest in bed for the time you allot to sleep so your body can feel less fatigue overall.")
    print("Additionally, try to find a job that has ways for you to get more consistent nightly sleep.")
if overnight_job_boolean == no:
    print("Consult your primary care doctor.")
else:
    print("Thank you and think about a quick trip to the hospital for a check in if anything is wrong.")
print("Most times what I feel when i'm tired is the essence of something pushing down upon my shoulders. I feel like i'm chained to life and nothing I do gives me more energy, but drains it faster.")
print("I normally try to sleep additionally if this happens or ask myself if i slept for 8 hours that night before. Both of these play significant roles on the body and are the common issues that happen.")
print("If those answers become a check, then consulting your primary care doctor for some help, will actually offer a new way to deal with the problem.")
print(f"That's why I will heavily suggest that {personal_name}.")
print("I'm hoping the quick sleep schedule fixes, consistent sleep, and napping methods become a way for you to continue to feel less tired and further energized.")
print(f"You can always do great things if you treat yourself as best as you can emotionally and physically. I'll be rooting for your success {personal_name}")