
# Ведущий
define elena = Character("Elena")

# Suspectors
define bozadji = Character("Bozadji Artemie")
define ilico = Character("Ilico Artemie")
define maxim = Character("Roenco Maxim")
define islam = Character("Islam AbuKoush")

define bostan = Character("Bostan")
define furdui = Character("Furdui")
define cristofor = Character("Christofor")
define gogoi = Character("Goga")

default player = "Player"

image war:
    "war.jpg"
    xysize(1920,1080)

image aula3:
    "aula3.jpg"
    xysize(1920,1080)

image Army = "Army.png"

image bbg:
    "images/bg boloto.jpg"
    xysize(1920,1080)

label start:
    menu start_choose:
        elena "Today is June 22, and you have just passed all your school exams."
        elena "You were the best student in your area, and now all doors are open to you."
        elena "Your mother insists that you go to Medical University. She knows you don't like biology, but nobody seems to care about that."
        elena "Your father wants you to be a real MAN, so he insists that you join the army to harden your heart and soul."
        elena "Your grandparents, being traditional, want you to become a good farmer and go to PTU."
        elena "On the other hand, you have always been inspired to become a great programmer... or maybe you just liked playing computer games. I'm not sure yet."
        elena "You need to choose a path where you will conquer new heights."
        elena "I hope you choose with your heart."
        
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
    bostan "Hello! Welcome to FAF. Bla bla bla... a very cool but cruel place."
    bostan "You should know that only 60% of students survive here, so I'll give you one last chance to change your mind."
    
    menu optional_name:
        "Give up":
            jump give_up
        "Become part of the FAF community":
            bostan "Congratulations!!! Today marks the beginning of the worst days of your life."
            bostan "Good luck surviving in FAF!"
            jump next_class
    return


label usmf:
    bostan "Are you kidding me???????"
    bostan "Fine, it's your life, and only you decide who will manipulate you—me or this Medical University."
    elena "Don't pay attention to him. Bostan just doesn't like students from USMF or ASEM."
    bostan "Did you just say ASEM??? Those idiots will regret ever being born..."
    elena "Calm down, dear. You have a weak heart; you shouldn't get nervous."
    bostan "Fine, I'll go relax for a bit."
    
    elena "Let's continue. Unfortunately, you were accepted into Medical University."
    player "Why 'unfortunately'???"
    elena "You'll understand soon. HE-HE-HE-HE."
    
    elena "You attend your first lecture, where you meet a lot of cool friends and a very pleasant professor."
    elena "You actively participate in class, so the professor asks you to stay after the lecture."
    elena "Everyone leaves the auditorium, and only you and the professor remain."
    
    elena "Awkward silence... He gets closer and closer."  

    # elena "It turns out that the professor is obsessed with overloading students with medical research!"
    # elena "You try to leave, but he hands you a 500-page book and says you have to memorize it by tomorrow."
    # elena "No escape. No mercy. Only endless anatomy textbooks."
    # elena "Congratulations, you are now trapped in the world of sleepless nights and coffee addiction!"
    elena "It turns out that the teacher was a pedophile maniac"
    elena "You try to run away but with him was very big knife. You don't have any chances..."
    elena "You left only give up"
    elena "You were raped and killed"
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
    elena "Good choice, your father would be happy if not for what will happen next..."
    elena "You are strong beautiful guy, moreover very good physically prepared, because of it everyone want to communicate with oyu and be your friend."
    elena "But later everyone getting envies you, that you are the best on each exam."
    elena "Your fellow soldiers kicked you to death."
    elena "You are dead"
    return


label give_up:
    scene bg dark with fade
    bostan "You gave up too early. Better luck next time."
    return

label next_class:
    scene bg hallway with fade
    "You stand before an open door."
    menu:
        "Are you sure you want to come in?"
        "Yes, Come In":
            jump comein
        "No, Leave":
            jump leave
    return

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

# Gogoi class

label boba_class:
    scene bg classroom with fade
    gogoi "Blah blah blah... So, let's do an activity!"
    menu:
        "Johari Window":
            gogoi "GREAT CHOICE! NOW, DO ALL OF THEM."
        "MBTI Personality Test":
            gogoi "GREAT CHOICE! NOW, DO ALL OF THEM."
        "Europass CV":
            gogoi "GREAT CHOICE! NOW, DO ALL OF THEM."
        "Emotional Intellect":
            gogoi "GREAT CHOICE! NOW, DO ALL OF THEM."
    gogoi "GREAT CHOICE! NOW, DO ALL OF THEM."
    jump pistachio_class
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