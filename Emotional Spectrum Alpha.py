#All capitilized letters are primary emotions based on an emotional spectrum diagram given from a google search         Ex: A

#All letters with numbers have sub categories of primary emotions to help express sincere responses for user input      Ex: A1

#All Definitions are defined through Oxford dictionary or with their best emotional response definition.                Ex: A1_definition

#Emotional_input is used to describe a specific input after categorizing and labeling ones emotion                      Ex: emotional_input = 'Anger'

A = 'Anger'
B = 'Fearful'
C = 'Bad'
D = 'Sad'
E = 'Disgusting'
F = 'Happy'

#These are primary emotions exhibited by a quick emotional spectrum diagram. These 6 emotions will be the base of decision making for future code.

A1 = 'Let Down'
A2 = 'Humiliated'
A3 = 'Bitter'
A4 = 'Mad'
A5 = 'Aggressive'
A6 = 'Frustrated'
A7 = 'Distant'
A8 = 'Critical'

#All anger based responses based on the diagram given
A1_definition ="Failure to support or help someone as they had hoped or expected."
A2_definition ="Make (someone) feel ashamed and foolish by injuring their dignity and self-respect, especially publicly."
A3_definition ="(of people or their feelings or behavior) angry, hurt, or resentful because of one's bad experiences or a sense of unjust treatment."
A4_definition ="Mentally ill; insane."
A5_definition ="Ready or likely to attack or confront; characterized by or resulting from aggression."
A6_definition ="Feeling or expressing distress and annoyance, especially because of inability to change or achieve something"
A7_definition ="(of a person) not intimate; cool or reserved."
A8_definition ="Expressing adverse or disapproving comments or judgments."

#each anger correlating responses definition based on Oxford dictionary.

B1 = 'Fearful'
B2 = 'Scared'
B3 = 'Anxious'
B4 = 'Insecure'
B5 = 'Weak'
B6 = 'Rejected'
B7 = 'Threatened'

#Each fearful sub-emotion within the emotion


B1_definition ="Feeling afraid; showing fear or anxiety."
B2_definition ="Fearful; frightened."
B3_definition ="Experiencing worry, unease, or nervousness, typically about an imminent event or something with an uncertain outcome."
B4_definition ="(of a person) not confident or assured; uncertain and anxious."
B5_definition ="Liable to break or give way under pressure; easily damaged."
B6_definition ="Fail to show due affection or concern for (someone); rebuff."
B7_definition ="State one's intention to take hostile action against someone in retribution for something done or not done."

#each fearful sub-emotion defined

C1 = 'Bad'
C2 = 'Bored'
C3 = 'Busy'
C4 = 'Stressed'
C5 = 'Tired'

#Each bad response sub-emotion


C1_definition ="Not such as to be hoped for or desired; unpleasant or unwelcome."
C2_definition ="Feeling weary because one is unoccupied or lacks interest in one's current activity."
C3_definition ="Having a great deal to do."
C4_definition ="Experiencing mental or emotional strain or tension."
C5_definition ="In need of sleep or rest; weary."

#Each bad response sub-emotion defined

D1 = 'Sad'
D2 = 'Lonely'
D3 = 'Vulnerable'
D4 = 'Despair'
D5 = 'Guilty'
D6 = 'Depressed'
D7 = 'Hurt'

#each sad sub-emotion


D1_definition ="Feeling or showing sorrow; unhappy."
D2_definition ="(of a situation or period of time) sad and spent alone."
D3_definition ="Weak and easily hurt physically or emotionally."
D4_definition ="The feeling of having lost all hope"
D5_definition ="Feeling ashamed because you have done something that you know is wrong or have not done something that you should have done."
D6_definition ="Very sad and without hope."
D7_definition ="To feel painful."

#Each sad sub-emotion with their definitions

E1 = 'Disgusting'
E2 = 'Disapproving'
E3 = 'Disappointed'
E4 = 'Awful'
E5 = 'Repelled'

#each disgusting sub emotion


E1_definition ="Extremely unpleasant."
E2_definition ="Showing that you do not approve of somebody/something."
E3_definition ="Upset because something you hoped for has not happened or been as good, successful, etc. as you expected."
E4_definition ="Very bad or unpleasant."
E5_definition ="To drive, push or keep something away."

#each disgusting sub-emotion defined

F1 = 'Happy'
F2 = 'Optimistic'
F3 = 'Trusting'
F4 = 'Peaceful'
F5 = 'Powerful'
F6 = 'Accepted'
F7 = 'Proud'
F8 = 'Interested'
F9 = 'Content'
F10 = 'Playful'

#each happy sub-emotion

F1_definition ="Feeling or showing pleasure; pleased."
F2_definition ="Expecting good things to happen or something to be successful; showing this feeling."
F3_definition ="Tending to believe that other people are good, honest, etc."
F4_definition ="Quiet and calm; not worried or upset in any way."
F5_definition ="(of people) being able to control and influence people and events."
F6_definition ="Generally believed to be correct."
F7_definition ="Feeling pleased and satisfied about something that you own or have done, or are connected with."
F8_definition ="Giving your attention to something because you enjoy finding out about it or doing it; showing interest in something and finding it exciting."
F9_definition ="Being aware and accepting of overall circumstances."
F10_definition ="Full of fun; wanting to play."

#Each happy sub-emotion defined
print("Welcome to the Emotional spectrum identification. Thank you for runnnig this program. Throughout this, please type your responses based on the values seen before you.")
print("With whom do we have the honor of being able to talk to?")
personal_name = input()
print(f"Thank you {personal_name}.It is with great honor that we are able to have this conversation with you.")
print(f"I want {personal_name}(you) to know that this is a safe space and all information written down or responded to is to help navigate your emotions for future references.")
print()
print()
print(f"Hey {personal_name}, would you mind choosing an emotion from this list that you are currently experiencing: {A,B,C,D,E,F}?")


#beginning of the program
user_input = input()
if user_input == A:
    print(f"from this selection {A1,A2,A3,A4,A5,A6,A7,A8} which one of these would best describe you?")
    emotional_input = input()
    if emotional_input == A1:
        print(f"I'm sorry that you feel {A1}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {A1}. {A1}'s definition is: {A1_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {A1}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case A1 is what we are checking.
    if emotional_input == A2:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {A2}. {A2}'s definition is: {A2_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {A2}. You are slightly influenced to make more decisions based on this.")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case A2 is what we are checking.
    if emotional_input == A3:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {A3}. {A3}'s definition is: {A3_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {A3}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case A3 is what we are checking.
    if emotional_input == A4:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {A4}. {A4}'s definition is: {A4_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {A4}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case A4 is what we are checking.
    if emotional_input == A5:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {A5}. {A5}'s definition is: {A5_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {A5}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case A5 is what we are checking.
    if emotional_input == A6:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {A6}. {A6}'s definition is: {A6_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {A6}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case A6 is what we are checking.
    if emotional_input == A7:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {A7}. {A7}'s definition is: {A7_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {A7}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case A7 is what we are checking.
    if emotional_input == A8:
        print(f"I'm sorry that you feel {emotional_input }. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {A8}. {A8}'s definition is: {A8_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {A8}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case A8 is what we are checking.
    else:
        print("Please give a value from this list:")
        #this nest is to see if they messed up. Must be edited to be adjusted sometime later. needs a while loop to check specific values.

if user_input == B:
    print(f"from this selection, how would you describe your emotion: {B1,B2,B3,B4,B5,B6,B7}")
    emotional_input = input()
    if emotional_input == B1:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {B1}. {B1}'s definition is: {B1_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {B1}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case B1 is what we are checking.
    if emotional_input == B2:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {B2}. {B2}'s definition is: {B2_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {B2}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case B2 is what we are checking.
    if emotional_input == B3:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {B3}. {B3}'s definition is: {B3_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {B3}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case B3 is what we are checking.
    if emotional_input == B4:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {B4}. {B4}'s definition is: {B4_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {B4}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case B4 is what we are checking.
    if emotional_input == B5:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {B5}. {B5}'s definition is: {B5_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {B5}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case B5 is what we are checking.
    if emotional_input == B6:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {B6}. {B6}'s definition is: {B6_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {B6}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case B6 is what we are checking.
    if emotional_input == B7:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {B7}. {B7}'s definition is: {B7_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {B7}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case B7 is what we are checking.
if user_input == C:
    print(f"from this selection, how would you describe your emotion: {C1,C2,C3,C4,C5}")
    emotional_input = input()
    if emotional_input == C1:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {C1}. {C1}'s definition is: {C1_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {C1}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case C1 is what we are checking.
    if emotional_input == C2:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {C2}. {C2}'s definition is: {C2_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {C2}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case C2 is what we are checking.
    if emotional_input == C3:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {C3}. {C3}'s definition is: {C3_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {C3}.You are slightly influenced to make more decisions based on this.")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case C3 is what we are checking.
    if emotional_input == C4:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {C4}. {C4}'s definition is: {C4_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {C4}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
    #This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case C4 is what we are checking.
    if emotional_input == C5:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {C5}. {C5}'s definition is: {C5_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {C5}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case C5 is what we are checking.

if user_input == D:
    print(f"from this selection, how would you describe your emotion: {D1,D2,D3,D4,D5,D6,D7}")
    emotional_input = input()
    if emotional_input == D1:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {D1}. {D1}'s definition is: {D1_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {D1}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case D1 is what we are checking.
    if emotional_input == D2:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {D2}. {D2}'s definition is: {D2_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {D2}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
    #This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case D2 is what we are checking.
    if emotional_input == D3:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {D3}. {D3}'s definition is: {D3_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {D3}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case D3 is what we are checking.
    if emotional_input == D4:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {D4}. {D4}'s definition is: {D4_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {D4}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case D4 is what we are checking.
    if emotional_input == D5:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {D5}. {D5}'s definition is: {D5_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {D5}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case D5 is what we are checking.
    if emotional_input == D6:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {D6}. {D6}'s definition is: {D6_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {D6}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case D6 is what we are checking.
    if emotional_input == D7:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {D7}. {D7}'s definition is: {D7_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {D7}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case D7 is what we are checking.
if user_input == E:
    print(f"from this selection, how would you describe your emotion: {E1,E2,E3,E4,E5}")
    emotional_input = input()
    if emotional_input == E1:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {E1}. {E1}'s definition is: {E1_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {E1}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case E1 is what we are checking.
    if emotional_input == E2:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {E2}. {E2}'s definition is: {E2_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {E2}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case E2 is what we are checking.
    if emotional_input == E3:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {E3}. {E3}'s definition is: {E3_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {E3}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case E3 is what we are checking.
    if emotional_input == E4:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {E4}. {E4}'s definition is: {E4_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {E4}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case E4 is what we are checking.
    if emotional_input == E5:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {E5}. {E5}'s definition is: {E5_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {E5}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case E5 is what we are checking.
if user_input == F:
    print(f"from this selection, how would you describe your emotion: {F1,F2,F3,F4,F5,F6,F7,F8,F9,F10}")
    emotional_input = input()
    if emotional_input == F1:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {F1}. {F1}'s definition is: {F1_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {F1}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case F1 is what we are checking.
    if emotional_input == F2:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {F2}. {F2}'s definition is: {F2_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {F2}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case F2 is what we are checking.
    if emotional_input == F3:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {F3}. {F3}'s definition is: {F3_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {F3}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case F3 is what we are checking.
    if emotional_input == F4:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {F4}. {F4}'s definition is: {F4_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {F4}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case F4 is what we are checking.
    if emotional_input == F5:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {F5}. {F5}'s definition is: {F5_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {F5}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case F5 is what we are checking.
    if emotional_input == F6:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {F6}. {F6}'s definition is: {F6_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {F6}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case F6 is what we are checking.
    if emotional_input == F7:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {F7}. {F7}'s definition is: {F7_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {F7}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case F7 is what we are checking.
    if emotional_input == F8:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {F8}. {F8}'s definition is: {F8_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {F8}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case F8 is what we are checking.
    if emotional_input == F9:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {F9}. {F9}'s definition is: {F9_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {F9}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case F9 is what we are checking.
    if emotional_input == F10:
        print(f"I'm sorry that you feel {emotional_input}. On a scale of 1-10 how would you describe it's intensity?")
        emotional_scale_input = int(input())
        print(f"So you have selected {F10}. {F10}'s definition is: {F10_definition}")
        if emotional_scale_input <= 10:
            print(f"It seems like you are exhibiting behaviors based on being {F10}.You are slightly influenced to make more decisions based on this")
        elif emotional_scale_input < 5:
            print('Try to find ways to reduce your feelings through verbal expression to a close loved one.')
        else:
            print('try another input please')
#This portion of the code will be asking users to make an input based on a 1-10 range. With it, the variable produces specific outputs. In this case F10 is what we are checking.
else:
    print("I'm sorry, but I don't understand your input. Would you mind trying again with the given values")
