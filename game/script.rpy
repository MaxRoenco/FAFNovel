# Ведущий
define elena = Character("Elena R")

# Suspectors
define bozadji = Character("Artemie B")
define ilico = Character("Artemie I")
define maxim = Character("Maxim R")
define islam = Character("Islam A")

define kulev = Character("Kulev")
define bostan = Character("Bostan")
define furdui = Character("Furdui")
define cristofor = Character("Cristofor")
define gogoi = Character("Gogoi")

define policeman1 = Character("Bad Policemen")
define policeman2 = Character("Good Policemen")

default player = "Player"

default karma = 100

default quiz_score = 0

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
    $ renpy.music.set_volume(0.15, channel="music")
    $ renpy.music.set_volume(0.15, channel="sound")
    play music "funnyMusic2.mp3" loop fadein 0.5

    jump schoolStory
    # jump furduiLaboratory
    return

label schoolStory:
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

label utm:
    scene aula3 with fade
    show bostan:
        zoom 0.9
        # scary lauighing
    play sound "thunder.wav" fadein 0.5
    play music "troll.wav"  fadein 0.5
    bostan "Hello! Welcome to FAF. Bla bla bla... a very cool but cruel place."
    bostan "You should know that only 60%% of students survive here, so I will give you one last chance to change your mind."
    play music "creepyMusic.mp3" loop fadein 0.5
    menu:
        "Give up":
            jump give_up
        "Become part of the FAF community":
            play sound "thunder.wav" fadein 0.5
            play music "troll.wav"  fadein 0.5
            bostan "Congratulations!!! Today marks the beginning of the worst days of your life."
            bostan "Good luck surviving in FAF! UA-HA-HA-HA-HA"
            jump pc_class
    return

label give_up:
    play music "creepyMusic.mp3" loop fadein 0.5
    scene dark with fade
    show bostan with fade:
        zoom 0.6
        yalign 0.2
    bostan "You gave up too early. Better luck next time."
    return

label pc_class:
    hide bostan
    # heels
    show gogoi happy 2
    gogoi "You have a lecture with Mujik"
    show gogoi shocked
    gogoi "—oh, I mean Kulev"
    show gogoi smile 2
    gogoi "so don't be late and be obedient."
    hide gogoi
    show elena smile
    elena "You enter the classroom, but all the chairs are occupied except for one next to a dark-skinned guy of Jordanian appearance."
    hide elena
    menu: 
        "Leave the lecture because this dark-skinned guy looks creepy.":
            $ islamRelation -= 10
            $ karma -= 10
            jump leave_pc
        "Sit next to him despite his miserable appearance.":
            $ islamRelation += 10
            jump islamMeeting
    return

# islam meeting

label islamMeeting:
    show islam smile
    islam "Salam, Marhaba. Ke fac?"
    menu:
        "Hi, I don't speak Arabic. Do you understand English?":
            $ islamRelation -= 10
            show islam smile 2
            islam "Yeah, I speak English."
        "Hamdulillah, ce fac?":
            $ islamRelation += 10
            show islam shocked
            islam "Ooh, do you speak Arabic?"
            player "Yeah, of course!"
    show islam laugh
    islam "Nice to meet you. My name is Islam, and I am from Jordan."
    player "How did you end up in Moldova?"
    show islam smile
    islam "I'm here for education. Moldova has a very high level of programming education... (not really)."
    player "Yeah, I agree. Moldova is famous for its smart students. Tell me something about yourself."
    show islam smile 2
    islam "Alright. My family is not very rich, so I want to make money as soon as possible. I have some ideas about it."
    player "Do you know how to find a good job?"
    show islam
    islam "Mmm... not really. If my main plan fails, I'll look for a job."
    player "Can you tell me abo—"
    hide islam
    show kulev smile:
        yalign 0.5
    kulev "Hello, everyone. Today we will learn the C language."
    show kulev smile 2:
        yalign 0.5
    kulev "Let's start with a very simple task. Open your laptops and get started."
    hide kulev
    show elena smile
    elena "You open the task and see this..."
    hide elena
    # Here should be a photo of a difficult C programming task
    show islam laugh
    islam "Oh, this is very easy. Wait a bit; I'm almost finished."
    player "Bro, be my friend."
    hide islam
    jump next_class
    return

label leave_pc:
    elena "You are walking down the street when you see someone who was also at the initiation for FAFT students."
    play music "creepyMusic.mp3" loop fadein 0.5
    menu:
        "Approach him":
            $ bozadjiRelation += 10
            jump bozadjiMeeting
        "Move on":
            jump next_class
    return

# bozadji meeting

label bozadjiMeeting:
    # monkey money music
    play music "monkeyBusines.wav" loop fadein 0.5
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
    # heels
    show gogoi smile with fade
    gogoi "Today, after dinner, you have one more lecture with me in room 113"
    show gogoi smug
    gogoi "Don't be late!!"
    elena "You are walking down the corridor, and you see a curly blond guy sitting near room 113 with a very sad expression."
    play music "sadMusic.mp3" loop fadein 0.5
    menu:
        "Ask why he is so sad":
            $ ilicoRelation += 10
            jump ilicoMeeting
        "Move on":
            $ ilicoRelation -= 10
            jump gogoiLecture

label ilicoMeeting:
    # sad music
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
    # heels
    scene bg classroom with fade
    play music "funnyMusic2.mp3" loop fadein 0.5
    play sound "heels.wav" fadein 0.5
    gogoi "Hello, everyone. Today, we will analyze ourselves and reflect a bit."
    gogoi "I wrote down some activities on the table. Please choose one."
    gogoi "So, let's do an activity!"
    play sound "geese.mp3" fadein 0.5
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

label finishedFirstDay:
    play music "sadMusic.mp3" loop fadein 0.5
    # relax music
    elena "The last lecture of the day has ended, and everyone is heading home to relax."
    elena "Suddenly, you remember that you live in a dorm with a huge number of cockroaches."
    elena "You don’t even know who your roommate is."
    play sound "cristofor.mp3" fadein 0.5
    # islam change meeting with Maxim
    elena "You see a blond, athletic guy with entering the room."
    maxim "What's up? Is this room 318?"
    player "Umm... Yes. Who are you?"
    maxim "I live here. What about you? Who are you?"
    player "Oh, I live here too. You look like a very cool person. Why are you staying in a dorm?"
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
    jump secondDay

label maximStory:
    # sad music
    play music "creepyMusic.mp3" loop fadein 0.5
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
    jump secondDay
    # here

label secondDay:
    # funny music
    # dorm
    play music "funnyMusic1.mp3" loop fadein 0.5
    elena "You wake up and see how sweetly your neighbor sleeps, hugging his pillow like it's the last kebab in Chisinau."
    menu:
        "Wake up the neighbor and go to University":
            player "Hey, Maxim, wake up! We need to go to university, we have Cristofor's lecture."
            maxim "Omg, I don't even know who that is... fuck off."
            elena "You decide to apply the legendary *morning slap* technique to wake him up."
            elena "However, your neighbor turns out to be built like a bear and nearly performs a *UFC takedown* on you."
            elena "Just kidding... somehow you're still alive, and both of you head to university, slightly traumatized."
        "Go to University without your friend":
            elena "You quietly leave like a ninja, abandoning your comrade to his sweet dreams."
            $ maximRelation -= 10
            elena "But deep down, you feel the heavy burden of betrayal... or maybe that's just the kebab from last night."
        "Continue sleeping":
            $ karma -= 10
            elena "You embrace the warmth of your blanket, choosing to sleep through your responsibilities like a true IT student."
            elena "The universe doesn't forgive laziness... but at least your dreams are full of unlimited Wi-Fi and bug-free code."
    jump ilicoMeeting2


label ilicoMeeting2:
    # shizofrenia music
    # corridor
    elena "You go down the corridor and you see again this weird curly blond person around 113 cabinet."
    elena "But this time he is not upset, he has mad face expression."
    play music "creepyMusic.mp3" loop fadein 0.5
    menu:
        "Go to him and ask about his mood":
            $ ilicoRelation += 10
            player "Hi, how are you?"
            ilico "I am busy right now."
            elena "You see how he very fastly writes some weird simbols on his notebook with strengh and mad eyes."
            player "What are you doing?"
            ilico "I am improving my traiding strategy, I almost have the ideal market strategy BUT there is a small detail missing. I CAN'T FIND IT."
            player "What are you talking about?"
            elena "Actively swinging he plunges into his thoughts."
            ilico "MM... Arbitrage... Slippage... Pump and dump... Dark pools... OH! Maybe it's the liquidity trap?! No... NO! The flash crash paradox?!"
            elena "His eyes shine as he keeps muttering."
            ilico "AHH! It's the MARKET MAKER'S REVENGE! OR... OR... THE DEAD CAT BOUNCE?!"
            player "I have no idea what you're saying."
            ilico "HEDGE! HEDGE EVERYTHING! THE TREND IS YOUR FRIEND UNTIL IT'S NOT!"
            elena "He starts aggressively drawing candlestick patterns in the air."
            player "Are you okay?"
            ilico "OF COURSE NOT! I'M IN A BEAR MARKET OF EMOTIONS!"
            elena "You decide to leave him to his thoughts."
        "Move on":
            $ ilicoRelation -= 10
            ilico "MMMmMMmMMmMm"
    jump cristoforLecture

label cristoforLecture:
    scene bg classroom with fade
    show elena happy with fade
    # heels
    play music "funnyMusic2.mp3" loop fadein 0.5
    play sound "heels.wav" fadein 0.5
    gogoi "Good morning, Fafers!"
    gogoi "guess what? Cristofor will grade you based on your lab presentations for the second midterm!"
    gogoi "Good luck!"

    show elena smile
    gogoi "Today is an important day because we can finally present labs to Cristofor."
  
    scene bg classroom 118
    show elena angry

    gogoi "It's 8:15! WHERE IS CRISTOFOR?!"

    show elena annoyed
    player "Ugh, I didn’t sleep all night, and now this? I better ask Islam. Maybe he knows something. He’s always lurking around like a shadow anyway."

    # Scene 2: The Mysterious Sleepless Islam
    scene bg hallway with fade
    show islam sleepy

    player "Hey, Islam! How are you? Do you know where Cristofor is?"
    
    islam "بدلاً من أن أسرق بنكاً، قمت بعمله المعملي!!! وأين هو؟؟"
    play sound "islam.wav" fadein 0.5
    player "I didn’t sleep last night, but Islam..."
    player "I’m not sure if he slept this entire semester..."
    player "I wont disturb him... He is hallucinating and thinking he is in Jordania?"


    elena "Cristofor is late again. Typical."

    # Scene 3: The Late Bozadji
    # scene bg corridor with bozadji
    # show bozadji neutral with fade

    elena "Suddenly, the door open and walks Artiom Bozadji, late as always."
  
    player "Hi! Are you prepared to present your labs? And do you know where Cristofor is?"

    bozadji "Privet! Wait, what? He’s not here? Ugh, he’s wasting my time. I could be making money right now instead of waiting"
    play music "monkeyBusines.wav" loop fadein 0.5
    player "Totally agree with you"

    # Scene 4: The Mirage of Cristofor
    # scene bg hallway with fade
    show elena shocked
    
    elena "Just as you’re about to give up hope, you see a silhouette at the end of the corridor. Is it... Cristofor? Could it be?"
    play music "cristofor.mp3" loop fadein 0.5
    elena "Your heart skips a beat and you squint your sleep deprived eyes to get a better look."

    player "Wait... is that him? Or is it just a mirage? Am I hallucinating from lack of sleep?"

    elena "The silhouette stands still, unmoving. You realize it’s not Cristofor. It’s just a suspiciously Cristofor-shaped coat."

    player "kms"

    # Scene 5: Bozadji’s Disappearance
    # scene bg hallway with fade
    show elena annoyed

    elena "You turn to Bozadji to share your disappointment, but... he’s gone... Vanished..."
    play sound "creepyMusic.mp3" fadein 0.5
    elena "Bozadji dissapeared..."

    # Scene 6: The Discord Bomb
    # scene bg classroom with fade
    show elena shocked

    elena "Just as you’re about to give up and kys, your phone buzzes. It’s a notification from Discord. Cristofor has finally spoken."

    show cristofor discord
    cristofor "Good morning, everyone! Sorry for the delay. There was ahorrible traffic jam."
    cristofor "Anyway, here’s your choice for presenting the labs:"
    cristofor "- Next lesson at 15:00"
    cristofor "- Or at 17:30"
    cristofor "Choose wisely!"

    player "Wait, what? 15:00 or 17:30? That’s not a choice that’s a trap!"

    elena "But before you can react, the Discord bot auto-selects 21:00 for you. Congratulations! You’re now presenting your labs at 9 PM."
    play music "cristofor.mp3" loop fadein 0.5
    player "What the fistic?#$!?! With this timing, we’ll never be ready for the midterms!"

    # Scene 7: The Ilico Meltdown
    # scene bg classroom with fade
    show ilico stressed with fade

    elena "you hear a familiar voice"
  
    elena "It’s Artemie!!! You are heading to him to complain about laboratories!"
    play music "creepyMusic.mp3" fadein 0.5
    ilico "NOOOOOOOOOOOOOOO!"
    ilico " What if the market crashes before I present my labs?!"

    player "Hey, calm down. The only thing crashing right now is my will to live. What’s wrong?"

    ilico "I can’t focus on my labs because I’m too busy calculating the risk-reward ratio of presenting early versus late."
    player "I have no words..."

    # Scene 9: The Final 
    # scene bg classroom with fade
    show elena smile

    elena "As the clock strikes 21:00, Cristofor finally arrives"
    play sound "cristofor.mp3" fadein 0.5
    cristofor "Alright, let’s check these labs! All 15 groups at once!"

    show cristofor neutral with fade
    cristofor "I’ll ask each of you a question. If you answer correctly, you pass. If not... well, let’s just say the universe is cruel."
    play music "creepyMusic.mp3" loop fadein 0.5
    # The Probability Theory Question
    cristofor "First question: Which probability theory concept is the most important for understanding randomness?"
    cristofor "Choose wisely. Your grade depends on it."

    menu:
        "Pigeonhole Principle":
            cristofor "Incorrect! The correct answer is... Martingale. But since you tried, you tried :)"
            $ karma -= 10
        "Martingale":
            cristofor "Incorrect! The correct answer is... Probabilistic Deviation Propagation. But don’t worry, I’ll be generous, 5 is too a positive grade)"
            $ karma -= 10
        "Probabilistic Deviation Propagation":
            cristofor "Incorrect! The correct answer is... Pigeonhole Principle. Curlu-Curlu!"
            $ karma -= 10

    show elena shocked

    elena "Cristofor pulls out a giant slot machine and starts spinning it to determine your lab marks."

    cristofor "Next group! Same question. Choose wisely."

    cristofor "You got a huge marks lately"
    cristofor "Mr. Pumpkin asked me to do Gaussean Distribution"
    cristofor "Reverse Gaussean Distribution..."
    cristofor "80%% fail..."

    cristofor "The universe works in mysterious ways! Next group!"

    elena "You finally finish presenting your labs at 23:00. Your brain feels like..."
    elena "Sorry, Your brain feels nothing"
    play music "sadMusic.mp3" loop fadein 0.5
    player "I just spent hours presenting labs to a man who grades us with a slot machine. What am I even doing with my life?"
    player "If this is how it’s going to be, I’m never going to make money. I need to start doing something."
    player "Artemie is talking a lot about market and the big player is bank"
    player "Maybe I can do something useful to them?"
    player "Optimize database, Legacy system, slow transactions?"
    jump furduiLaboratory


# Merge Sort Lab Presentation Dialogue

# Scene Label
label furduiLaboratory:
    # Set the scene
    scene bg classroom  # Ensure you have a classroom background
    elena "Today you have lecture with Furdui, be prepared to his question.."
    # Initial interaction
    play sound "thunder.wav" fadein 0.5
    play music "troll.wav" fadein 0.5
    player "Good morning, Professor Furdui. I'm here to present my merge sort laboratory work."

    furdui "Ah, Elena. Another student hoping to pass with minimal effort, I see."

    player "No, professor. I've worked hard on this lab and I'm prepared to demonstrate my understanding."

    furdui "Hard work? In this generation? Let's see about that. Your punctuality is already a problem."

    player "I know I'm a bit late, but I promise my work meets the requirements."

    furdui "Late submissions are the first sign of academic negligence. But go on, convince me."
    play music "creepyMusic.mp3" loop fadein 0.5
    menu:
        "Apologize sincerely":
            player "I sincerely apologize for the delay. I understand the importance of deadlines."
            $ karma += 5
            furdui "At least you show some understanding."

        "Make an excuse":
            player "There were some unexpected complications with my computer..."
            $ karma -= 5
            furdui "Excuses, always excuses. The real world doesn't accept such nonsense."

    furdui "Before we discuss your merge sort implementation, you'll need to prove your understanding."

    player "I'm ready for any questions you have, professor."

    # Merge Sort Quiz
    furdui "Let's begin with a comprehensive quiz about merge sort. Each incorrect answer will cost you."

    # Question 1: Basic Concept
    player "First question: What is the primary strategy of the merge sort algorithm?"

    menu:
        "Divide and Conquer":
            player "Divide and Conquer! The algorithm breaks down the problem into smaller, more manageable sub-problems."
            $ quiz_score += 1
            $ karma += 3
            furdui "Correct. A promising start."

        "Bubble Sorting":
            player "Um... Bubble Sorting?"
            $ karma -= 5
            furdui "Incorrect. Bubble sort is an entirely different, less efficient sorting method."

        "Random Shuffling":
            player "Random Shuffling?"
            $ karma -= 5
            furdui "Completely wrong. This shows a fundamental misunderstanding."

    # Question 2: Time Complexity
    furdui "What is the time complexity of merge sort?"

    menu:
        "O(n²)":
            player "O(n²), like insertion sort?"
            $ karma -= 5
            furdui "Incorrect. Merge sort is more efficient than that."

        "O(n log n)":
            player "O(n log n)! It maintains this complexity in all cases - best, average, and worst."
            $ quiz_score += 1
            $ karma += 3
            furdui "Correct. You're showing some actual knowledge."

        "O(1)":
            player "O(1)?"
            $ karma -= 5
            furdui "Ridiculous. That's constant time, impossible for sorting."

    # Question 3: Implementation Details
    furdui "Describe the key steps in implementing merge sort."

    menu:
        "Recursively divide, sort sub-arrays, then merge":
            player "First, recursively divide the array into two halves, sort those sub-arrays, and then merge them back together."
            $ quiz_score += 1
            $ karma += 3
            furdui "Precise explanation. You've clearly studied."

        "Swap adjacent elements":
            player "Swap adjacent elements?"
            $ karma -= 5
            furdui "No! That's more akin to bubble sort. Completely incorrect."

        "Sort from left to right in one pass":
            player "Sort from left to right in one pass?"
            $ karma -= 5
            furdui "Absurd. Merge sort is not a single-pass algorithm."

                # Final Quiz Assessment
    if quiz_score >= 2:
        furdui "Not entirely terrible. Your theoretical understanding shows promise."
        $ karma += 10
    else:
        furdui "Your performance is disappointing. Theory is the foundation of practical implementation."
        $ karma -= 10

    # Closing Dialogue
    player "May I now present my actual implementation, professor?"

    furdui "Go ahead. But remember, theory without perfect implementation means nothing."

    # Final Karma and Score Determination
    if karma >= 60:
        furdui "You've barely scraped through. 8 out of 10. Do better next time."
    elif karma >= 50:
        furdui "Mediocre performance. 5 out of 10. Improvement is mandatory."
    else:
        furdui "Unsatisfactory. 3 out of 10. You need serious remedial work."
    jump cristoforLecture2

# Cristofor class

label cristoforLecture2:
    play music "cristofor.mp3" fadein 0.5
    elena "Today, you have another one lecture with Cristofor."  
    # 113 cabinet maybe, or think of something else  
    elena "You enter the classroom and see a very elegant person in a suit with long black hair."
    elena "Unexpectedly, Elena Gogoi enters with a frightened expression on her face."  
    play music "creepyMusic.mp3" loop fadein 0.5
    gogoi "There is news that one of the students from FAF took part in a bank robbery. The police are trying to find him, but all attempts have failed. He is very skilled at stealth."  
    gogoi "Today's lectures are canceled, so everyone is free. However, tomorrow all classes will take place as scheduled, so don't be late."  
    elena "You look around the room after hearing this news and notice some strange reactions."  
    elena "A curly blond student’s eyes dart around the room rapidly—though, to be fair, that might just be his usual behavior."  
    elena "A dark-skinned guy with a Jordanian appearance tries to hide his face under his sweater—maybe he just smelled something bad."  
    elena "However, you can’t see your neighbor, Maxim. He was at this lecture, but somehow, he has disappeared."  
    elena "And, of course, Bozadji, the first-year student who works in the cybersecurity department, is absent too."  
    elena "Each of these people seems weird and suspicious. Ugh, this is so exhausting. I'll just go home and relax..."  
    jump thirdDay  

label thirdDay:  
    # Dormitory  
    play music "sadMusic.mp3" loop fadein 0.5
    maxim "Good morning, my friend."  
    player "How did you get here?"  
    maxim "I was a bit busy yesterday because I was working on another project."  
    player "Oh, cool. Did you hear the latest news at the university?"  
    maxim "Oh no, what are you talking about?"  
    player "Yesterday, one of the students from our group took part in a bank robbery."  
    maxim "Oh, really?? I always knew that Arabic guy looked like a robber."  
    play music "creepyMusic.mp3" loop fadein 0.5
    menu:  
        "Yeah, he is very weird.":  
            $ islamRelation -= 10  
            $ maximRelation += 10  
        "No, he is a good guy with a handsome appearance.":  
            $ islamRelation += 10  
            $ maximRelation -= 10  
    elena "Suddenly, you notice a Rolex watch on Maxim’s wrist. Hmm… very suspicious."  
    play sound "thunder.wav" fadein 0.5
    menu:  
        "Ask him about it?":  
            $ maximRelation -= 10  
            $ karma += 10  
            player "Where did you get that watch?"  
            maxim "*nervously scratches his head* Oh... I got my salary from my project yesterday... Never mind."  
        "Ignore this fact":  
            $ maximRelation += 5  
            $ karma -= 5  
    player "Let's go to the university and find out the latest news."  
    maxim "Yeah, let's go."  
    # University  
    jump universityFourthDay  


if karma <= 0:
        jump expelledUniversityStory

label universityFourthDay:
    # scene university with policemen
    play sound "policy.wav" fadein 0.5
    elena "The next day, the police arrive at the university, questioning students."
    kulev "Attention, everyone! The police are investigating last night's bank robbery. If you have any information, please cooperate."
    player "This is getting serious..."
    # Islam A
    play sound "islam.wav" fadein 0.5
    kulev "Islam, where were you at the time of the robbery?"
    islam "I was praying at home and then making labs for university."
    kulev "Can someone confirm this?"
    islam "Unfortunately, only Allah"
    islam "Oh, and the teacher who has access to ELSE and can see my lab submission at that time interval."
    play music "creepyMusic.mp3" loop fadein 0.5
    menu:
        elena "How do you think, is it true or is he a good liar?"
        "I BELIEVE HIM":
            $ islamRelation += 25
            elena "policeman2 goes to the Decanat to verify Islams submission."
            if islamRelation > min(bozadjiRelation, ilicoRelation, maximRelation):
                kulev "Yes, there really was a submission at that time."
            else:
                kulev "No, there are no submissions. You are a liar."
                play sound "thunder.wav" fadein 0.5
        "HE IS A LIAR":
            $ islamRelation -= 25
            kulev "We will verify this information."
    # Artemie B
    kulev "Artemie B, where were you at the time of the robbery?"
    bozadji "I was working at the bank s cybersecurity department on the night shift."
    kulev "Can someone confirm this?"
    bozadji "Yes, the security cameras at the bank."
    elena "policeman2 returns"
    policeman2 "Chief, all recordings from the cameras are deleted."
    bozadji "It can't be real, it's not my fault! Check my computer logs. My laptop is in my car, I'll go get it."
    menu:
        elena "How do you think, is it true or is he lying?"
        "I BELIEVE HIM":
            $ bozadjiRelation += 25
            if bozadjiRelation > min(islamRelation, ilicoRelation, maximRelation):
                scene parking_lot
                elena "Artemie B returns with the laptop, proving his innocence."
            else:
                scene empty_parking_lot
                elena "Artemie B never returns... He was the thief!"
                play sound "thunder.wav" fadein 0.5
                jump retrospectiveBozadji
        "HE IS A LIAR":
            $ bozadjiRelation -= 25
            kulev "We will investigate further."
    # Artemie I
    kulev "Artemie I, where were you at the time of the robbery?"
    ilico "I was studying new trading strategies in the UTM library. You can ask Ms. Valentina, the security guard."
    kulev "Ms. Valentina is on vacation for two weeks..."
    ilico "No, that isn't true! Maybe she took extra shifts. Go ask her."
    elena "Policeman goes to Ms. Valentina."
    menu:
        elena "Do you believe him?"
        "I BELIEVE HIM":
            $ ilicoRelation += 25
            if ilicoRelation > min(islamRelation, bozadjiRelation, maximRelation):
                kulev "Ms. Valentina confirmed that she saw you reading in the library."
            else:
                kulev "Ms. Valentina denies even being at the university that night."
                elena "Artemie I is the thief!"
                play sound "thunder.wav" fadein 0.5
                jump retrospectiveIlico
        "HE IS A LIAR":
            $ ilicoRelation -= 25
            kulev "We will confirm your alibi."
    # Maxim R
    policeman1 "Maxim, where were you at the time of robbery?"
    maxim "I was deliverying food at glovo"
    policeman1 "in what area?"
    maxim "in the city center of the town"
    policeman2 "the bank that was robbed is situated in the citycenter of the town😱😱😱, someone has seen you, can you prove that you were delivering the food?"
    maxim "Maybe my manager can, you should contant him"
    menu:
        elena "Do you believe him?"
        "I BELIEVE HIM":
            $ maximRelation += 25
            if maximRelation > min(islamRelation, bozadjiRelation, maximRelation):
                policeman2 "Administrator confirmed that you where picking up orders in that time-frimes"
            else:
                policeman2 "You dont even work at glovo, no-one knows you there"
                elena "Maxim R is the thief!"
                play sound "thunder.wav" fadein 0.5
        "HE IS A LIAR":
            $ maximRelation -= 25
            kulev "We will investigate further."

label retrospectiveIlico:
    play music "sadMusic.mp3" loop fadein 0.5
    scene black with fade
    show text "Retrospective: The Curious Case of Artemie I and the Market Maker’s Revenge" with fade
    
    "Now that you think back, the signs were all there. The frantic scribbling in the notebook, the wild eyes, the desperate search for the missing piece of his strategy—what if it was never about trading at all?"
    "What if, hidden between terms like 'liquidity trap' and 'dead cat bounce,' there was something more... tangible? Something like... a heist plan?"
    
    "At first, it seemed like just another one of Ilico's existential meltdowns—one of many, really. The guy had been stressed since day one, convinced exams were lurking behind every corner like debt collectors."
    "But then there was that day in the corridor. The way he muttered about arbitrage and slippage while violently stabbing his notebook with his pen, his pupils dilated like a day trader who just shorted Tesla at the wrong time."
    
    show ilico stressed with fade
    ilico "THE MARKET MAKER'S REVENGE!"
    
    "He had shouted, eyes glinting with dangerous enthusiasm. It seemed like gibberish at the time—like most of his monologues—but what if it wasn’t?"
    "What if, hidden in those notes, there were calculations far beyond your comprehension? What if, amidst all the candlestick patterns and Fibonacci sequences, there was a blueprint... not for a trading strategy, but for an escape route?"
    
    scene lecture_hall with fade
    # show gogoi worried
    
    gogoi "A student from FAF took part in a bank robbery!"
    
    "The words echoed through the room, bouncing off the walls and crashing directly into your already overworked brain. And then... the reactions."
    
    show ilico nervous
    "Ilico's eyes darted around the room at hyperspeed. But then again, that was kind of his default setting."
    
    show jordanian_student suspicious
    "A Jordanian-looking guy was pulling his sweater up to his nose. Suspicious? Maybe. But given how the lecture hall smelled after a full day of classes, understandable."
    
    show maxim missing
    "Maxim, your neighbor? Gone. Just—poof. Evaporated like your motivation after the first week of university."
    
    show bozadji absent
    "Bozadji, the cybersecurity guy? Also missing. Classic hacker move."
    
    "Was it all just a coincidence? Maybe. But maybe, just maybe, the real market he was analyzing wasn't the financial one—it was the underground one."
    "And maybe, just maybe, the only thing he was hedging... was his getaway."
    
    "Either way, one thing is certain: next time someone starts frantically sketching stock patterns in the air, you might want to check if a bank heist just went down."
    jump lifeAfterThief

label retrospectiveBozadji:
    scene bg dark with fade
    play music "sadMusic.mp3" loop fadein 0.5

    elena "Now that you think about it, something doesn’t add up..."

    scene bg university_night with fade
    show bozadji neutral with dissolve

    elena "Bozadji—a first-year student—casually lands a job in the cybersecurity department of a bank? Yeah, right."
    elena "You always thought he was just a guy who lucked out by using ChatGPT in interviews, but now... things are looking way too convenient."
    
    scene bg lecture_hall with fade
    show gogoi shocked with dissolve
    
    elena "Then came that lecture, the one where Gogoi burst in, looking like she just realized the exam was today instead of next week."
    gogoi "A bank robbery! A student from FAF is involved! The police can’t find him!"
    
    scene bg empty_classroom with fade
    elena "And who was suspiciously absent? Bozadji."
    
    scene bg police_station with fade
    show kulev neutral with dissolve

    kulev "Bozadji, where were you at the time of the robbery?"
    
    show bozadji neutral with dissolve
    bozadji "I was working the night shift at the bank's cybersecurity department."
    
    elena "Oh, how convenient. A cybersecurity guy working *at the exact bank that got robbed*? That’s like finding out the guy in charge of the cookie jar is also the only one with crumbs on his shirt."
    
    show policeman2 neutral with dissolve
    policeman2 "Chief, all the recordings from the security cameras are deleted."
    
    show bozadji surprised with dissolve
    bozadji "It can't be real, it's not my fault! Check my computer logs! My laptop is in my car, I'll go get it."
    
    scene bg parking_lot with fade
    elena "He ran off to fetch it."
    elena "You waited."
    elena "And waited."
    elena "And... he never came back."
    
    scene bg dark with fade
    elena "Now it all makes sense."
    elena "Works in cybersecurity? Check."
    elena "Has access to bank systems? Check."
    elena "Knows how to wipe security footage? Big check."
    elena "Magically disappears when asked to prove innocence? Yeah, that’s a wrap."
    
    scene bg city_night with fade
    elena "Bozadji didn’t just *get* a job at the bank. He was planning something all along."
    elena "Maybe university *was* just for fun. But hacking into a bank? That was the *real* assignment."
    
    jump lifeAfterThief


label usmf:
    show bostan with fade:
        zoom 0.6
        yalign 0.2
    play music "sadMusic.mp3" loop fadein 0.5
    play sound "thunder.wav" fadein 0.5
    bostan "Are you kidding me???????"
    bostan "Fine, it's your life, and only you decide who will manipulate you—me or this Medical University."
    play sound "troll.wav" fadein 0.5
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
    play music "creepyMusic.mp3" loop fadein 0.5
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
    scene dark with fade
    show elena sad:
        zoom 0.7
        yalign 0.05
    elena "You are dead"
    return

label ptu:
    play music "sadMusic.mp3" loop fadein 0.5
    play sound "thunder.wav" fadein 0.5
    show elena smug
    elena "Good choice, but not the best one. HE-HE-HE-HE-HE."
    
    show elena smile
    elena "At first, everything goes smoothly, but one day, you go on a picnic with friends."
    
    show elena smile 2
    elena "The location for the party is near a lake."
    
    show elena smile
    elena "You see the dirty water and try to touch it..."
    
    scene bbg with fade
    play music "creepyMusic.mp3" loop fadein 0.5
    show elena shocked
    elena "But someone pushes you from behind, and you fall into the water. Unexpectedly, this isn't a lake—it's a marsh!"
    
    show elena sad
    elena "You try to escape from the swamp, but all your movements only make things worse."
    
    show elena shocked
    elena "Everyone panics and tries to help you, but your head is almost underwater."
    
    show elena sad
    elena "Three more seconds, and you can't breathe because your entire body is no longer under your control..."
    
    show elena sleepy
    elena "All you can do is give up..."
    
    scene dark with fade
    show elena sad:
        zoom 0.7
        yalign 0.05
    elena "You are dead"
    return

label war:
    show elena happy with fade
    elena "Good choice, your father would be happy!"
    show elena sleepy
    elena "If not for what will happen next..."
    play music "creepyMusic.mp3" loop fadein 0.5
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

label expelledUniversityStory:
    scene bg classroom with fade
    play music "sadMusic.mp3" loop fadein 0.5
    
    show elena annoyed with dissolve
    elena "Well, it was only a matter of time before this happened..."
    
    show elena sad
    elena "After consistently making poor choices, irritating your professors, and alienating your classmates, you've been summoned to the Dean's office."
    
    scene bg deans_office with fade
    show cristofor neutral with dissolve
    
    cristofor "I've reviewed your academic record and behavior reports. The university has standards that must be maintained."
    
    cristofor "Your performance has been... disappointing, to put it mildly."
    
    show cristofor serious
    cristofor "Therefore, effective immediately, you are expelled from the Faculty of Computers, Informatics and Microelectronics."
    
    player "But... but... I can improve! Give me another chance!"
    
    cristofor "The universe works in mysterious ways! But in your case, quite predictably. Goodbye."
    
    scene bg outside_university with fade
    play sound "thunder.wav" fadein 0.5
    
    show elena shocked
    elena "And just like that, your university career is over. You stand outside the gates, your belongings in a small box."
    
    show elena smug
    elena "What will you do now? Your options are limited..."
    
    menu:
        "Try to get into another university":
            jump another_university
        "Look for a job":
            jump find_job
        "Return home in shame":
            jump return_home

label another_university:
    scene bg other_university with fade
    play music "creepyMusic.mp3" loop fadein 0.5
    
    show elena smile
    elena "You apply to several other universities, hoping for a fresh start."
    
    show elena shocked
    elena "But it seems your reputation precedes you! The academic community is smaller than you thought."
    
    show bostan:
        zoom 0.6
        yalign 0.2
    bostan "YOU? Again? UA-HA-HA-HA-HA! I've already sent emails to ALL universities in Moldova about you."
    
    show elena sad
    elena "No university in Moldova will accept you now. Your academic future here is finished."
    
    jump life_after_expulsion

label find_job:
    scene bg office with fade
    play music "funnyMusic1.mp3" loop fadein 0.5
    
    show elena smile
    elena "With no degree and limited skills, your job options are... restricted."
    
    show elena smug
    elena "After seventeen rejections, you finally land an interview."
    
    show bozadji neutral
    bozadji "Wait, don't I know you from somewhere? Weren't you that student who got expelled from FAF?"
    
    player "Uh... no?"
    
    bozadji "I'm certain it was you. I respect your attempt to lie though – shows initiative. Unfortunately, we require honest employees."
    
    hide bozadji
    show elena sad
    elena "Back to the job hunt..."
    
    jump life_after_expulsion

label return_home:
    scene bg family_home with fade
    play music "sadMusic.mp3" loop fadein 0.5
    
    show elena sad
    elena "You return to your family home, where your mother greets you with tears."
    
    elena "Your father doesn't speak to you for three weeks."
    
    elena "Your grandparents keep saying 'we told you so' regarding their farmer suggestion."
    
    show elena smile
    elena "Eventually, they forgive you, but the disappointment lingers in their eyes."
    
    jump life_after_expulsion

label life_after_expulsion:
    scene bg small_apartment with fade
    play music "creepyMusic.mp3" loop fadein 0.5
    
    show elena neutral
    elena "Five years later..."
    
    show elena smile
    elena "Life has settled into a routine. You work at a small convenience store, making just enough to pay rent."
    
    show elena smug
    elena "One day, while scrolling through social media, you see updates from your former classmates."
    
    show islam smile at left
    elena "Islam has started a successful tech company in Jordan."
    
    show maxim at right
    elena "Maxim is now a crypto millionaire."
    
    show ilico at left
    elena "Artemie I has become a renowned financial analyst."
    
    show bozadji at right
    elena "And Bozadji? Well, he works for a major cybersecurity firm... or maybe he's still robbing banks. It's unclear."
    
    hide islam
    hide maxim
    hide ilico
    hide bozadji
    
    show elena sad
    elena "As you close your laptop, you wonder what might have been if you had made different choices..."
    
    show elena smile
    elena "But hey, at least you're not in a swamp or shot dead in the army, right?"
    
    scene dark with fade
    show text "THE END - EXPELLED ENDING" with dissolve
    pause 3.0
    
    return

label lifeAfterThief:
    scene bg classroom with fade
    play music "funnyMusic1.mp3" loop fadein 0.5
    
    show elena smile
    elena "Several weeks have passed since the bank robbery case was resolved."
    elena "Life at FAF has returned to its usual chaotic rhythm - endless labs, complex assignments, and slightly unsettling professors."
    
    show cristofor neutral
    cristofor "The universe has a strange way of balancing itself. One student commits a crime, another helps solve it."
    cristofor "Perhaps you're more suited for detective work than computer science?"
    
    player "I just tried to be observant..."
    
    cristofor "Observant enough to earn yourself a few bonus points on your next exam. The universe rewards those who maintain order."
    
    hide cristofor
    show gogoi happy
    
    gogoi "After the excitement of the robbery investigation, today we're going to do something REALLY fun!"
    gogoi "Let's analyze how the recent events affected our group dynamics through a series of team-building exercises!"
    
    play sound "geese.mp3" fadein 0.5
    player "Of course. Because what's more fun than processing trauma through team-building?"
    
    # Scene: Check on remaining classmates
    scene bg hallway with fade
    
    # If Islam wasn't the thief
    if islamRelation > min(bozadjiRelation, ilicoRelation, maximRelation):
        show islam smile
        islam "You know, after everything that happened, I've decided to focus entirely on my studies."
        islam "My family sent me here for education, not drama. I plan to honor that."
        
        player "What about making money quickly? You mentioned having ideas..."
        
        show islam laugh
        islam "Ah, that. I'm starting a halal kebab delivery service targeting students. First month's business is already booming!"
        
        player "That's... surprisingly wholesome."
        
        islam "What did you think I meant? Bank robbery? استغفر الله!"
        hide islam

    # If Ilico wasn't the thief
    if ilicoRelation > min(islamRelation, bozadjiRelation, maximRelation):
        show ilico smile
        ilico "The market has been incredibly volatile lately. Perfect conditions for my new trading strategy!"
        
        player "Still chasing that perfect formula?"
        
        ilico "I've refined it! Now I'm only having panic attacks once per week instead of daily."
        
        player "Progress!"
        
        ilico "By the way, want to invest in my new cryptocurrency? It's called AnxietyCoin. When I'm stressed, the value goes up."
        
        player "I'll... think about it."
        hide ilico

    # If Maxim wasn't the thief
    if maximRelation > min(islamRelation, bozadjiRelation, ilicoRelation):
        show maxim
        maxim "I've been thinking a lot about what happened. Money isn't everything, you know?"
        
        player "That's quite philosophical coming from you."
        
        maxim "True friendship is what matters. By the way, do you want to invest in my new friendship bracelet business? Only 50 euros per bracelet."
        
        player "I thought money wasn't everything?"
        
        maxim "It isn't. But my Rolex collection won't expand itself."
        hide maxim

    # If Bozadji wasn't the thief
    if bozadjiRelation > min(islamRelation, ilicoRelation, maximRelation):
        show bozadji neutral
        bozadji "After the whole bank incident, they promoted me at the cybersecurity department. Ironic, right?"
        
        player "They promoted you for failing to prevent a robbery?"
        
        bozadji "No, for designing a new security system that would have prevented it. I'm implementing it next month."
        
        player "That's... convenient."
        
        bozadji "ChatGPT is a miracle worker. Don't tell my boss."
        hide bozadji

    # Final scene with Furdui
    scene bg classroom with fade
    show furdui
    
    furdui "I hear you've been quite the detective. Impressive for someone who struggles with basic sorting algorithms."
    
    player "Thank you... I think?"
    
    furdui "Don't let it distract you from your studies. Being able to solve crimes won't help you pass my exams."
    
    player "Of course, professor."
    
    furdui "Now, since you've helped resolve this situation, I'll give you an opportunity. A simple extra credit assignment."
    
    player "What is it?"
    
    furdui "Implement a search algorithm that could have found our thief more efficiently. You have until tomorrow."
    
    player "But... that's impossible!"
    
    furdui "Life is impossible. Programming is merely implausible. Get to work."
    
    show elena laughing behind furdui
    elena "And just like that, life at FAF returns to normal - impossible deadlines, eccentric professors, and the constant feeling that you're one assignment away from a complete breakdown."
    
    elena "But hey, at least you solved a bank robbery. That should look great on your CV... right next to 'survived FAF first semester'."
    
    # Graduation scene - flash forward
    scene bg graduation with fade
    play music "funnyMusic2.mp3" loop fadein 0.5
    
    show elena happy
    elena "Four years later..."
    
    elena "Against all odds, you've survived FAF. The bank robbery investigation is now just another colorful story from your university days."
    
    show bostan:
        zoom 0.6
        yalign 0.2
    
    bostan "Congratulations. I genuinely didn't expect you to make it. But here you are, proving that even the most hopeless cases can graduate sometimes."
    
    player "Thank you, professor. That means a lot coming from you."
    
    bostan "Don't get emotional. 40% of your graduating class is still missing. Probably still working on my assignments from second year."
    
    hide bostan
    show cristofor neutral
    
    cristofor "As you embark on your journey into the real world, remember: debugging your life is just like debugging code. The errors are usually between the keyboard and the chair."
    
    player "I'll remember that, professor."
    
    cristofor "And if you ever decide to rob a bank, at least use a better algorithm than your classmate did. Efficiency matters, even in crime."
    
    scene black with fade
    show text "THE END - DETECTIVE ENDING" with dissolve
    pause 3.0
    
    return
