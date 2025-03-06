
# Ведущий
define elena = Character("Elena Romasenco")

# Suspectors
define bozadji = Character("Artemie Bozadji")
define ilico = Character("Artemie Ilico")
define maxim = Character("Maxim Roenco")
define islam = Character("Islam AbuKoush")

define kulev = Character("Kulev")
define bostan = Character("Bostan")
define furdui = Character("Furdui")
define cristofor = Character("Christofor")
define gogoi = Character("Gogoi")

default player = "Player"

default karma = 100

default bozadjiRelation = 0
default ilicoRelation = 0
default maximRelation = 0
default islamRelation = 0

image war:
    "war.jpg"
    xysize(1920,1080)

image dark:
    "dark.png"
    xysize(1920,1080)

image aula3:
    "aula3.jpg"
    xysize(1920,1080)

image Army = "Army.png"

image bbg:
    "images/bg boloto.jpg"
    xysize(1920,1080)

label start:
    scene aula3 with fade
    show elena happy with fade
    elena "Today is June 22, and you have just passed all your school exams."
    show elena smile
    elena "You were the best student in your area, and now all doors are open to you."
    show elena annoyed
    elena "Your mother insists that you go to Medical University. She knows you don't like biology, but nobody seems to care about that."
    show elena smug
    elena "Your father wants you to be a real MAN, so he insists that you join the army to harden your heart and soul."
    show elena smile 2
    elena "Your grandparents, being traditional, want you to become a good farmer and go to PTU."
    show elena laugh
    elena "On the other hand, you have always been inspired to become a great programmer..."
    show elena sleepy
    elena "Or maybe you just liked playing computer games. I'm not sure yet."
    show elena smug
    elena "You need to choose a path where you will conquer new heights."
    show elena happy
    elena "I hope you choose with your heart."
    hide elena happy
    menu start_choose:
        "Go to UTM and become a great programmer":
            jump utm
        "Go to USMF and become a great doctor":
            jump usmf
        "Go to PTU and become a skilled farmer":
            jump ptu
        "Go to the army and become a real MAN":
            jump war
    return

label utm:
    scene aula3 with fade
    show bostan:
        zoom 0.9
    bostan "Hello! Welcome to FAF. Bla bla bla... a very cool but cruel place."
    bostan "You should know that only 60%% of students survive here, so I will give you one last chance to change your mind."

    menu:
        "Give up":
            jump give_up
        "Become part of the FAF community":
            bostan "Congratulations!!! Today marks the beginning of the worst days of your life."
            bostan "Good luck surviving in FAF! UA-HA-HA-HA-HA"
            jump pc_class
    return

label give_up:
    scene dark with fade
    show bostan with fade:
        zoom 0.6
        yalign 0.2
    bostan "You gave up too early. Better luck next time."
    return

label pc_class:
    gogoi "You have a lecture with Mujik—oh, I mean Kulev—so don't be late and be obedient."
    elena "You enter the classroom, but all the chairs are occupied except for one next to a dark-skinned guy of Jordanian appearance."
    menu: 
        "Leave the lecture because this dark-skinned guy looks creepy.":
            $ islamRelation -= 10
            $ karma -= 10
            jump leave_pc
        "Sit next to him despite his miserable appearance.":
            $ islamRelation += 10
            jump islamMeeting
    return

label islamMeeting:
    islam "Salam, Marhaba. Ke fac?"
    menu:
        "Hi, I don't speak Arabic. Do you understand English?":
            $ islamRelation -= 10
            islam "Yeah, I speak English."
        "Hamdulillah, ce fac?":
            $ islamRelation += 10
            islam "Ooh, do you speak Arabic?"
            player "Yeah, of course!"
    islam "Nice to meet you. My name is Islam, and I am from Jordan."
    player "How did you end up in Moldova?"
    islam "I'm here for education. Moldova has a very high level of programming education... (not really)."
    player "Yeah, I agree. Moldova is famous for its smart students. Tell me something about yourself."
    islam "Alright. My family is not very rich, so I want to make money as soon as possible. I have some ideas about it."
    player "Do you know how to find a good job?"
    islam "Mmm... not really. If my main plan fails, I'll look for a job."
    player "Can you tell me abo—"
    kulev "Hello, everyone. Today we will learn the C language."
    kulev "Let's start with a very simple task. Open your laptops and get started."
    elena "You open the task and see this..."
    # Here should be a photo of a difficult C programming task
    islam "Oh, this is very easy. Wait a bit; I'm almost finished."
    player "Bro, be my friend."
    jump next_class
    return

label leave_pc:
    elena "You are walking down the street when you see someone who was also at the initiation for FAFT students."
    menu:
        "Approach him":
            $ bozadjiRelation += 10
            jump bozadjiMeeting
        "Move on":
            jump next_class
    return

label bozadjiMeeting:
    player "Hello, I saw you at the previous lecture."
    bozadji "Hello, yeah, I was there."
    player "Why aren't you at the PC lecture?"
    bozadji "Because I'm busy right now. I'm heading to work."
    player "How did you get a job if you're only a first-year student? Also, why did you enroll in university if you already have a job?"
    bozadji "I just used ChatGPT in interviews, that's all. As for university, I'm not really sure why I'm here—just for fun."
    player "Bro, you're a very weird person, but I respect strong-willed people."
    bozadji "Thx, sorry, but I need to go. Goodbye."
    player "Goodbye."
    $ bozadjiRelation += 10
    elena "You decide to return to the university and wait for the next lecture."
    jump next_class

label next_class:
    gogoi "Today, after dinner, you have one more lecture with me in room 113, so don't be late."
    elena "You are walking down the corridor, and you see a curly blond guy sitting near room 113 with a very sad expression."
    menu:
        "Ask why he is so sad":
            $ ilicoRelation += 10
            jump ilicoMeeting
        "Move on":
            $ ilicoRelation -= 10
            jump gogoiLecture

label ilicoMeeting:
    player "Hi, why are you so upset?"
    ilico "I am very nervous about the upcoming exams... I can't find peace."
    player "Bro, it's only the first day of classes. We won't have an exam anytime soon."
    ilico "Even after hearing that, I still have a bad feeling about this university."
    menu:
        "Let's go to Das Kebab. Maybe some kebab will improve your mood.":
            $ ilicoRelation += 10
            ilico "Alright, let's go and eat some delicious kebabs."
            player "Alright!"
            jump gogoiLecture
        "I'm going to develop schizophrenia soon because of people like this.":
            $ ilicoRelation -= 10
            ilico "Starts crying because of his worthless fate."
            player "OMG, I should have gone to medical school instead."
            jump gogoiLecture
    return

# Gogoi's class

label gogoiLecture:
    scene bg classroom with fade
    gogoi "Hello, everyone. Today, we will analyze ourselves and reflect a bit."
    gogoi "I wrote down some activities on the table. Please choose one."
    gogoi "So, let's do an activity!"
    menu:
        "Johari Window":
            gogoi "GREAT CHOICE! NOW, DO ALL OF THEM."
        "MBTI Personality Test":
            gogoi "GREAT CHOICE! NOW, DO ALL OF THEM."
        "Europass CV":
            gogoi "GREAT CHOICE! NOW, DO ALL OF THEM."
        "Emotional Intelligence":
            gogoi "GREAT CHOICE! NOW, DO ALL OF THEM."
    player "Omg, my mental health get affected."
    jump finishedFirstDay
    return

label finishedFirstDay:
    elena "The last lecture of the day has ended, and everyone is heading home to relax."
    elena "Suddenly, you remember that you live in a dorm with a huge number of cockroaches."
    elena "You don’t even know who your roommate is."
    elena "You see a blond, athletic guy in an expensive suit with a Rolex on his wrist entering the room."
    maxim "What's up? Is this room 318?"
    player "Umm... Yes. Who are you?"
    maxim "I live here. What about you? Who are you?"
    player "Oh, I live here too. You look like a very rich person. Why are you staying in a dorm?"
    maxim "I have a very sad story about how I ended up here. Do you want to hear it?"
    menu:
        "Of course not, nobody cares about your story.":
            $ maximRelation -= 10
            maxim "Bro, you are a very rude person."
        "Yeah, I want to hear your story.":
            $ maximRelation += 10
            jump maximStory

    elena "You were very tired from today's events."
    elena "You put your head on the pillow and instantly fell asleep."

label maximStory:
    maxim "When I was a child, I had a best friend. We would constantly play, watch movies, and imagine that we would be rich and successful in the future."
    maxim "We even created a plan on how to achieve this success, but one day he told me that he was leaving with his family for another country."
    maxim "I lost my only friend, and it affected me deeply."
    maxim "After that, I became obsessed with making money. However, I can't make friends anymore."
    maxim "Not long ago, I earned a large sum of money, so I don’t need money anymore."
    maxim "But there's one goal I haven't achieved—I want to find good friends."
    maxim "Let's be friends?"
    menu:
        "Yeah, of course. I will help you with your goals.":
            $ maximRelation += 10
        "No, you sound like a little kid with psychological trauma.":
            $ maximRelation -= 10
    maxim "Fine, I'm a bit tired. Let's go to sleep."
    player "Together???"
    maxim "Ew, of course not! I'm not gay."

label comein:
    scene bg classroom with fade
    furdui "Okey."
    furdui "Hmm..."
    furduif "Uh-huh."
    furdui "You see this block of code?"
    player "Yes."
    furdui "Rewrite this using recursion in one for loop with customized radix sort. Also, display results in WebAssembly with real-time visualization. You have 7 minutes. Start working."
    player "May I ask a ques..."
    furdui "NO QUESTIONS! 5 and you are free."
    "You are defeated."
    jump new_day
    return

label leave:
    scene bg corridor with fade
    "You walk down the empty corridor. You see the door to the Programming Systems classroom."
    "Inside, students are crying during lab presentations, the room is on fire."
    return

# Cristofor class

label new_day:
    scene bg room_night with fade
    "After a sleepless night, traumatized by Furdui, you wake up."
    "Excited for a productive day, you check Outlook for your schedule."
    "BAM - Christofor. You decide to go to university."
    jump pistachio_class
    return

label pistachio_class:
    scene bg hallway with fade
    "You arrive at the class, but the door is locked."
    "You check your watch: 8:00 AM."
    "8:30... 8:50... 9:25..."
    "You see Pistachio's silhouette appear, then disappear."
    jump boba_class
    return

# Cristofor Labs

label pistachio_lab:
    scene bg lab with fade
    cristofor "What time do you want to present the labs?"
    menu:
        "8:00":
            jump wrong_choice
        "14:00":
            jump wrong_choice
        "18:00":
            jump wrong_choice
        "21:00":
            jump correct_choice
    return

label wrong_choice:
    "Wrong answer."
    jump pistachio_lab
    return

label correct_choice:
    "You stand in a queue of students with laptops. Outside, it's night, the stars and moon shine."
    return

label usmf:
    show bostan with fade:
        zoom 0.6
        yalign 0.2
    bostan "Are you kidding me???????"
    bostan "Fine, it's your life, and only you decide who will manipulate you—me or this Medical University."
    hide bostan
    show elena:
        zoom 0.7
        yalign 0.05
    elena "Don't pay attention to him. Bostan just doesn't like students from USMF or ASEM."
    hide elena
    show bostan:
        zoom 0.6
        yalign 0.2
    bostan "Did you just say ASEM??? Those idiots will regret ever being born..."
    hide bostan
    show elena sad:
        zoom 0.7
        yalign 0.05
    elena "Calm down, dear. You have a weak heart; you shouldn't get nervous."
    hide elena sad
    show bostan:
        zoom 0.6
        yalign 0.2
    bostan "Fine, I'll go relax for a bit."
    hide bostan
    show elena with fade:
        zoom 0.7
        yalign 0.05
    elena "Let's continue. Unfortunately, you were accepted into Medical University."
    player "Why 'unfortunately'???"
    show elena smug:
        zoom 0.7
        yalign 0.05
    elena "You'll understand soon. HE-HE-HE-HE."
    show elena laugh:
        zoom 0.7
        yalign 0.05
    elena "You attend your first lecture, where you meet a lot of cool friends and a very pleasant professor."
    show elena laugh:
        zoom 0.7
        yalign 0.05
    elena "You actively participate in class, so the professor asks you to stay after the lecture."
    show elena smile:
        zoom 0.7
        yalign 0.05
    elena "Everyone leaves the auditorium, and only you and the professor remain."
    show elena:
        zoom 0.7
        yalign 0.05
    elena "Awkward silence... He gets closer and closer."  
    show elena shocked:
        zoom 0.7
        yalign 0.05
    elena "It turns out that the professor is obsessed with overloading students with medical research!"
    elena "You try to leave, but he hands you a 500-page book and says you have to memorize it by tomorrow."
    show elena sad:
        zoom 0.7
        yalign 0.05
    elena "No escape. No mercy. Only endless anatomy textbooks."
    elena "Congratulations, you are now trapped in the world of sleepless nights and coffee addiction!"

    # elena "It turns out that the teacher was a pedophile maniac"
    # elena "You try to run away but with him was very big knife. You don't have any chances..."
    # elena "You left only give up"
    # elena "You were raped and killed"
    return

label ptu:
    elena "Good choice, but not the best one. HE-HE-HE-HE-HE."
    elena "At first, everything goes smoothly, but one day, you go on a picnic with friends."
    elena "The location for the party is near a lake."
    elena "You see the dirty water and try to touch it..."
    scene bbg with fade
    elena "But someone pushes you from behind, and you fall into the water. Unexpectedly, this isn't a lake—it's a marsh!"
    elena "You try to escape from the swamp, but all your movements only make things worse."
    elena "Everyone panics and tries to help you, but your head is almost underwater."
    elena "Three more seconds, and you can't breathe because your entire body is no longer under your control..."
    elena "All you can do is give up..."
    elena "You are dead."
    return

label war:
    show elena happy with fade
    elena "Good choice, your father would be happy!"
    show elena sleepy
    elena "If not for what will happen next..."
    show elena smile
    elena "You are strong attractive, muscular guy, and because of that everyone wants to talk to you and be your friend."
    show elena
    elena "But later everyone starts enving you, because you excel at every exam."
    show elena shocked
    elena "Your fellow soldiers kicked you to death."
    scene dark with fade
    show elena sad:
        zoom 0.7
        yalign 0.05
    elena "You are dead"
    return

# label final_choice:
#     scene bg calendar with fade
#     "It's December, the end of the semester."
#     menu:
#         "Stay home":
#             jump stay_home
#         "Meet the Big Boss":
#             jump big_boss
#     return

# label stay_home:
#     scene bg prayer with fade
#     "You pray to Bostan to cancel the quiz."
#     "Suddenly, in Discord, Catan announces:"
#     c "GUYS, WE HAVE A QUIZ TODAY."
#     "You rush to university."
#     jump big_boss
#     return

# label big_boss:
#     scene bg aula with fade
#     "You are in Amdaris, the final quiz begins."
#     "Absurd questions appear."
#     "A Gaussian distribution diagram appears, showing you are in the golden middle."
#     "Congratulations! You completed the first semester, but there are 7 more to go."
#     return


# label test:
#     scene bg room
#     image SilverSexyWoman = "SilverSexyWoman.png"
#     image SilverSexyWoman2 = "SilverSexyWoman2.png"
#     show SilverSexyWoman 
#     e "Hello very gorgeous guuyy."
#     e "How are ?? UwU"
#     $ player = renpy.input("What is your name beautiful guy: ")
#     define p = Character("[player]")
#     show SilverSexyWoman2
#     e "I am horny of you [player]"
#     return