define e = Character("Elena")
define b = Character("Bostan")
define ba = Character("Bozadji Artemie")
define ia = Character("Ilico Artemie")
define f = Character("Furdui")
define k = Character("Christofor")
define p = Character("Pistachio")
define g = Character("Goga")
define c = Character("Catan")

default player = "Player"

label start:
    scene bg room
    menu start_choose:
        "Choose UTM if you want to be rich, successful and sexy man"
        "UTM":
            jump utm
        "ASEM":
            jump asem
        "PTU":
            jump ptu
        "WAR":
            jump war
    return


label utm:
    scene bg room with fade
    b "Welcome, freshmen! You are about to embark on the most important journey of your life. Choose wisely!"
    menu optional_name:
        "Give up":
            jump give_up
        "Go to the next class":
            jump next_class
    return

label asem:
    b "OMG are you freak???????"
    return

label ptu:
    image boloto = "boloto.png"
    scene boloto
    ia "You are dead"
    return

label war:
    image Army = "Army.png"
    image war = "war.png"
    scene bg war
    show Army
    ba "You are dead"
    return



label give_up:
    scene bg dark with fade
    b "You gave up too early. Better luck next time."
    return

label next_class:
    scene bg hallway with fade
    "You stand before an open door."
    menu:
        "Are you sure you want to leave?"
        "Yes, Leave":
            jump leave
        "No, Stay":
            jump stay
    return

label leave:
    scene bg classroom with fade
    f "Okey."
    f "Hmm..."
    f "Uh-huh."
    f "You see this block of code?"
    player "Yes."
    f "Rewrite this using recursion in one for loop with customized radix sort. Also, display results in WebAssembly with real-time visualization. You have 7 minutes. Start working."
    player "May I ask a ques..."
    f "NO QUESTIONS! 5 and you are free."
    "You are defeated."
    jump new_day
    return

label stay:
    scene bg corridor with fade
    "You walk down the empty corridor. You see the door to the Programming Systems classroom."
    "Inside, students are crying during lab presentations, the room is on fire."
    return

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

label boba_class:
    scene bg classroom with fade
    g "Blah blah blah... So, let's do an activity!"
    menu:
        "Johari Window":
            g "GREAT CHOICE! NOW, DO ALL OF THEM."
        "MBTI Personality Test":
            g "GREAT CHOICE! NOW, DO ALL OF THEM."
        "Europass CV":
            g "GREAT CHOICE! NOW, DO ALL OF THEM."
        "Emotional Intellect":
            g "GREAT CHOICE! NOW, DO ALL OF THEM."
    g "GREAT CHOICE! NOW, DO ALL OF THEM."
    jump pistachio_class
    return

label pistachio_lab:
    scene bg lab with fade
    p "What time do you want to present the labs?"
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
    return

label correct_choice:
    "You stand in a queue of students with laptops. Outside, it's night, the stars and moon shine."
    return

label final_choice:
    scene bg calendar with fade
    "It's December, the end of the semester."
    menu:
        "Stay home":
            jump stay_home
        "Meet the Big Boss":
            jump big_boss
    return

label stay_home:
    scene bg prayer with fade
    "You pray to Bostan to cancel the quiz."
    "Suddenly, in Discord, Catan announces:"
    c "GUYS, WE HAVE A QUIZ TODAY."
    "You rush to university."
    jump big_boss
    return

label big_boss:
    scene bg aula with fade
    "You are in Amdaris, the final quiz begins."
    "Absurd questions appear."
    "A Gaussian distribution diagram appears, showing you are in the golden middle."
    "Congratulations! You completed the first semester, but there are 7 more to go."
    return


label test:
    scene bg room
    image SilverSexyWoman = "SilverSexyWoman.png"
    image SilverSexyWoman2 = "SilverSexyWoman2.png"
    show SilverSexyWoman 
    e "Hello very gorgeous guuyy."
    e "How are ?? UwU"
    $ player = renpy.input("What is your name beautiful guy: ")
    define p = Character("[player]")
    show SilverSexyWoman2
    e "I am horny of you [player]"
    return