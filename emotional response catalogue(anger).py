print("Often when I feel let down about something I normally go around and do something encouraging. Anything that normally excites my interest.")
print("What is something your normally find yourself doing that brings joy and excitement into your life?")
Let_down_input_response = input()
print(f"you said you do {Let_down_input_response}? I think that's awesome. Do you have any friends who also do those hobbies too?")
print ("Type yes or no as seen here for a response.")
hobby_response = input ()
if hobby_response == 'yes':
    hobby_response = True
    print(f"You should see if there are any new things that have come up for {Let_down_input_response}. Try socializing with your friends briefly if able or a stranger.")
    print("Venturing out and socializing about new things could bring about making new friends or feeling better about the information. Additionally, taking up those hobbies now might help you feel better.")
if hobby_response == 'no':
    hobby_response = False
    print(f"I'm sorry to here that {personal_name}. Being in a very unique hobby or not having too many friends can feel bad. However, there are ways to make friends without physical social interaction.")
    print("on Omegle, discord commmunity groups, and chatting sites you can find friends who share similar overall interest and slowly influence them to liking your primary hobby too.")
    print("As you continue to learn about people through a less anxious field of social interaction, try to tell others about {Let_down_input_response}. It may help make a new friend with your hobby too.")
else:
    print("I'm sorry, but the information you have submitted could not be understood. Would you mind telling me again?")
#What we just did was make a valid response within a sub-emotion. We need to do this for the other 41 of them.

print("Often when I feel humiliated I look for comedy sources that fit my style of humor. What youtubers or other social media influencers are you interested in viewing normally?")
humiliated_input_response = input()
print(f"I'm certain that there are some forms of entertainment that can help to reduce your feeling of {A2}. Let's try going to view some of {humiliated_input_response} new content.")
print("Are you able to chat with any friends about this {humiliated_input_response} social media influencer?")
print("Type 'yes' for yes and type 'no' for no")
socialization_response = input()
if socialization_response == 'yes':
    print(f"Wonderful. Trying to spend some time with others who may encourage viewing that {humiliated_input_response} may be beneficial right now.")
    print("Please continue to do and find more things that you can be social about and don't feel ashamed for asking for encouragement.")
if socialization_response == 'no':
    print("I'm sorry to hear that. Well, there are always wonderful people online that are willing to be encouraging in different avenues of life.")
    print("While reviewing your favorite person ({humiliated_input_response}), it might be good to also check out Eric Thomas. He offers great amounts of encouragement.")
else:
    print()
#humiliated response sequence

print("Being bitter about anything makes it incredibly difficult to listen to others. Instead i'd like to know what has made you bitter.")
print("Would you mind telling me what is currently driving you to a point of pure resentment?")
Bitter_cause_input_response = input()
print("I'm sincerely sorry that this has occurred to you. Would you mind telling me about the events that lead into {Bitter_cause_input_response}?")
Bitter_cause_story_response = input()
print("Would you mind if i made sure the information was correct so i can ensure you're being heard?")
print("If Yes type 'yes'. if No type 'no'.")
paraphrasing_story_response_input = input()
if paraphrasing_story_response_input == 'yes':
    print(f"It is to my understanding that {Bitter_cause_input_response} lead into you feeling misunderstood and misheard.")
    print(f"Also, because {Bitter_cause_story_response} has happened it makes it difficult for you to not feel resentment.")
if paraphrasing_story_response_input == 'no':
    print('Understood.')
else:
    print("Let's continue forward.")

print("Anyone who would have gone through a similar situation as you would feel the same. Let's focus on getting out of it {personal_name}.")
print("I believe you should go and talk with a close friend, family member, or even a member of the community that you trust.")
print("Talking with others when we hold very dark feelings and asking for guidance after being heard can help us feel better about it.")
#Bitter response sequence

Mad
print(f"Being {A4} about things is quite difficult and tricky to deal with. So i'd rather take some time out to get to know you.")
print(f"Would you mind telling me what has gotten you so {A4} today?")
print(f"(Please do not press enter until you are finished with each response. Thank you so much {personal_name}.)")
Mad_input_response = input()
print("It sounds like people weren't being as considerate about your feelings as you believe they should. How could they have been more considerate {personal_name}?")
print("(Please press enter after each response.)")
Mad_input_of_consideration1 = input()
Mad_input_of_consideration2 = input()
Mad_input_of_consideration3 = input()
Mad_input_of_consideration_list = [Mad_input_of_consideration1, Mad_input_of_consideration2, Mad_input_of_consideration3]
print(f"Thank you for responses {personal_name}.")
print(f"so far i have {Mad_input_of_consideration_list} as ways to help with being more considerate.")
print(f"{personal_name} would you mind telling me a story of when you exhibited {Mad_input_of_consideration1} within your life?")
print("(Please type 'yes' for Yes and 'no' for No)")
Mad_consideration_input_storytime_response = input()
if Mad_consideration_input_storytime_response == 'yes':
    print("Please tell me all about your experience with it.")
    print("(you may begin typing and press enter to store your response.)")
    Mad_input_lifetime_event1 = input()

if Mad_consideration_input_storytime_response == 'no':
    print("Thank you for remaining so expressive.")
else:
    print("Lets continue with the next part.")
print(f"{personal_name} would you mind telling me a story of when you exhibited {Mad_input_of_consideration2} within your life?")
print("(Please type 'yes' for Yes and 'no' for No)")
Mad_consideration_input_storytime_response2 = input()
if Mad_consideration_input_storytime_response2 == 'yes':
    print("I really do love hearing other people's story. Thank you for being willing to express it to me.")
    print("(please begin typing at any moment. do NOT press enter until finished.)")
    Mad_input_lifetime_event2 = input()
if Mad_consideration_input_storytime_response2 == 'no':
    print("Thank you for telling me.")
else:
    print("Let's continue to move forward. All responses are appreciated.")
print(f"{personal_name} would you mind telling me a story of when you exhibited {Mad_input_of_consideration3} within your life?")
print("(Please type 'yes' for Yes and 'no' for No)")
Mad_consideration_input_storytime_response3 = input()
if Mad_consideration_input_storytime_response3 == 'yes':
    print("Wonderful. Well i'm sort of excited to hear about this. Would you mind telling me in great details. They are always appreciated.")
    Mad_input_lifetime_event3 = input()
if Mad_consideration_input_storytime_response3 == 'no':
    print("Understood.")
else:
    print("Thank you for expressing yourself today.")
#Mad responses

print("Normally being an offensive-styled person leads to people running away. Let's talk about how you've gotten to be this way.")
print()
print()
print("Would you mind expressing to me, what has gotten you to be so offensive in nature today?")
print("(Type 'yes' for YES and type 'no' for NO)")
aggression_response_input = input()
if aggression_response_input == 'yes':
    print("Tell me all about it. This is a safe environment and no emotion goes without being heard.")
    aggression_storytime_response= input()
if aggression_response_input == 'no':
    print("That's alright. Maybe next time.")
else:
    print("Let's continue.")
print("Can you describe what you're feeling within your body? I'll give a couple of examples:")
print("Normally when I feel aggressive, my heart feels like it's pounding outside of my chest, i'm less sensitive to touch, and I feel strong physically, but mentally vulnerable.")
aggression_physiology_input = input()
print(f"I'm certain that there are a lot of people who feel the same way when aggressive about things {personal_name}.")
print("Have you ever found a way to deal with that {aggression_physiology_input} in a constructive manner?")
print("('yes' for YES and 'no' for NO)")
dealing_with_aggression_response = input()
if dealing_with_aggression_response == 'yes':
    print("Wonderful. Well it may be time to persist in what is already known. However i challenge you to find even more ways to deal with it.")
if dealing_with_aggression_response == 'no':
    dealing_with_aggression_list = ["Reading a new book", "Spending time within a specific hobby", "Exercising without weights", "Going for a walk", "Watching television or other forms of media as a distraction until the emotion is less intense", "Thinking about future lifestyle choices"]
    print("I am going to provide you with a list of ways on how to deal with your aggression in a constructive manner below.")
    print("I challenge you to taking up one for a week whenever you feel aggressive about anything and see what is done at the end of the week.")
    print(f" Examples of how i've dealt with aggression are as followed: {dealing_with_aggression_list}.")
else:
    print(f"Remember. You are a rockstar {personal_name}. Don't make a decision that will cost you your future.")
#Aggression responses

frustrated
print(f"Being {A6} is not easy. each time I am {A6}, I'm normally confused and angry about my confusion.")
print(f"What about you, {personal_name}. Do you also feel the same?")
frustration_correlation_response = input()
if frustration_correlation_response == 'yes':
    print("I'm sorry that you are feeling {A6}, {personal_name}")
    print("I can completely understand why you feel that way.")
if frustration_correlation_response == 'no':
    print("Interesting. Would you mind telling me what you're experiencing {personal_name}?")
    print("(Please start typing and press enter once done. Thank you for your response too {personal_name})")
    frustration_difference_response = input()
    print()
    print("It's quite interesting and intelligent for you to give this response. It's greatly appreciated and it opens my eyes to new ways of viewing the emotional spectrum.")
    print()
    print("What advice would you give someone else exhibiting this behavior {frustration_difference_response}?")
    print("(Please start typing and press enter once done. Thank you for your response too {personal_name})")
    print()
    frustration_difference_teaching = input()
    print()
    print(f"How do you personally deal with being {A6} using {frustration_difference_teaching}?")
    print("(Please start typing and press enter once done. Thank you for your response too {personal_name})")
    personalized_frustration_method = input()
    print(f"Intersting. Thank you for telling me this {personalized_frustration_method}")


else:
    print("Thank you for your responses today {personal_name}")

Distant
print(f"Thank you for responding so often as of today. I know that you are feeling {A7}, but i'd like to want through how you got there.")
print(f"{personal_name}, would you mind telling me why you are currently experiencing a {A7} feeling?")
print(f"(Please start typing and press enter once done. Thank you for your response too {personal_name})")
distant_reactional_response = input()

print("Did it have anything to do with someone you were conversing with?")
print("(Please type 'yes' if YES or 'no' if NO)")
distant_person_experience_boolean = input()
if distant_person_experience_boolean == 'yes':
    print("Would you like to use an alias to refer to them as we go through everything?")
if distant_person_experience_boolean == 'no':
    print("Understood do you just feel like the world doesn't have any positive experiences for you?")
else:
    print("I'm really sorry this has been occuring for you. I'm having a hard time with becoming close to people too.")
print("Life can be strange, but working through {distant_reactional_response} is beneficial.")
print("I'd like to ask more questions if you're feeling up to it. Would you mind if i asked you further questions about this experience?")
print()
print("(Please start typing and press enter once done. Thank you for your response too {personal_name})")
distant_questioning_boolean = input()
if distant_questioning_boolean == 'yes':
    print("Thank you for being expressive today. It really does mean a lot and I hope that you are able to step on a good foot soon after this is all done.")
    print("(Please start typing and press enter once done. Thank you for your response too {personal_name})")
    distant_personalized_experience = input()
    print()
    print(f"Thank you for telling me {personal_name} about {distant_personalized_experience}.")
if distant_questioning_boolean == 'no':
    print("I can understand not wanting to express what's made you distant out of privacy. Thank you for sharing and being expressive through this.")
else:
    print("I'm having a difficult time understanding your input")
    while distant_questioning_boolean != 'yes' or 'no':
        distant_questioning_boolean = input()
print("Through many of these experiences shared or not shared I can tell that it's difficult and it bothers you. It would bother anyone.")
print(f"Whenever I start to experience {A7} as an emotion, i often find things to focus on that would make me happy.")
print("This would normally include: video games, socializing, philosophy, Youtube, Twitch, Xbox, Playstation, or other forms of social media and entertainment.")
print("I often feel like my body is colder than normal and everything I touch becomes frozen during this time period.")
print(f"When it comes to combating being {A7}, remain honest with yourself. Tell yourself it's okay to feel that way, but find a way to get out of the emotion.")
print("Go find things that make you happy and if the experience with the person has produced this cold feeling, talk with them about how it made you feel.")
print("9 times out of 10 talking with the person or talking about the experience helps us to feel comforted.")
print("Please never stop giving up on that.")
print(f"{personal_name} thank you for talking with me. You're a sweet and noble person. Remain courageous in discussing these issues with others.")
#Distant responses

print("Making decisions is difficult. We often believe others will make the same decision as us.")
print("Sometimes when we do this, we give our personalized expectations to those around us when they don't have the same life experiences as us.")
print('...')
print(f"So...{personal_name} what expectations did you give to someone else today?")
expectation_response = input()
print()
print(f"Thank you for that response {personal_name}.")
print("Would you like to give me more responses?")
print("(Please type 'yes' for YES and 'no' for NO)")
additional_expectation_responses = input()
if additional_expectation_responses == 'yes':
    print("Please add more expectations that you were giving people, an organization, or yourself")
    print("Once done, please type 'finished'.")
    critical_expectations = input()
    while critical_expectations != 'finished':
        critical_expectations = input()
        critical_expectations_list = []
        critical_expectations_list.append(critical_expectations)
    
if additional_expectation_responses == 'no':
    print(f"Thank you for this response {expectation_response}.")
else:
    print("I'm sorry, but I don't understand your input.")
print()
print("Let's work on expectations and why they are difficult to manage.")
print("Whenever we create expectations for ourself, we are setting rules and goals we wish to obtain.")
print("Whenever it is time for us to take accountability, we need to remain honest and evaluate true facts with emotional responses.")
print("Some people often struggle with giving themselves valid passes during stressful life periods and can be cynical towards themselves.")
print("How we combat this would be to allow ourselves to be forgiven while continuing to put our best foot forward as a habit.")
print("It won't be easy, but it is greatly beneficial.")
#self Critical
print("Whenever we have expectations for a specific establishments in society, we struggle to offer them grace periods.")
print("We believe we know what's best for everyone and everything and we often fail to account for any situation those establishments may be going through behind closed doors.")
print("In the same way that we are supposed to forgive ourselves, we should also be forgiving establishments that are trying their best too.")
print("Otherwise, we fail to remain considerate of all circumstances presenting themselves behind closed doors.")
#establishment critical
print("When we think of other people in a way that gives them our life experiences, we can often short change them in terms of consideration.")
print("Most people do not have the same situation and way of dealing with a situation based on their experiences.")
print("Whenever we find ourselves trying to correlate our experiences with other peoples experiences without taking this into consideration, we are being overly critical of them.")
print("Our best course of action is to take an understanding approach and allow them to express their life experiences.")
print("This will help us become less critical and more understanding as we continue to gather information.")
print("Being an active listener during this time period is the most effective way, while being forgiving too to their experiences and their behavior.")
print("The purpose of it, is to be able to communicate with other people your experiences and help in a constructive and humble life experiencing way.")
#People critical