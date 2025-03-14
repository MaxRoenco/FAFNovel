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

image parking:
    "parking.png"
    xysize(1920,1080)

image usmf:
    "usmf.png"
    xysize(1920,1080)

image cab:
    "cab.png"
    xysize(1920,1080)

image coridor:
    "coridor.png"
    xysize(1920,1080)

image biblioteca:
    "coridor.png"
    xysize(1920,1080)

image Army = "Army.png"

image bbg:
    "images/bg boloto.jpg"
    xysize(1920,1080)

label start:
    $ renpy.music.set_volume(0.05, channel="music")
    $ renpy.music.set_volume(0.1, channel="sound")
    play music "funnyMusic2.mp3" loop fadein 0.5

    jump schoolStory
    # jump finishedFirstDay
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
    scene cab with fade
    hide bostan
    # heels
    show gogoi happy 2
    play sound "heels.wav" fadein 0.5
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
    scene aula3 with fade
    show islam smile
    play sound "islam.wav" fadein 0.5
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
    play music "cristofor.mp3" loop fadein 0.5
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
    scene parking with fade
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
    play music "monkeyBusines.wav" loop fadein 0.5

    show bozadji smile at center with dissolve
    
    player "Hello, I saw you at the previous lecture."
    
    show bozadji smile 2
    bozadji "Hello, yeah, I was there."
    
    player "Why aren't you at the PC lecture?"
    
    show bozadji
    bozadji "Because I'm busy right now. I'm heading to work."
    
    player "How did you get a job if you're only a first-year student? Also, why did you enroll in university if you already have a job?"
    
    show bozadji smug
    bozadji "I just used ChatGPT in interviews, that's all. As for university, I'm not really sure why I'm here—just for fun."
    
    player "Bro, you're a very weird person, but I respect strong-willed people."
    
    show bozadji smile 3
    bozadji "Thx, sorry, but I need to go. Goodbye."
    
    player "Goodbye."
    
    hide bozadji with dissolve
    
    $ bozadjiRelation += 10
    
    scene coridor with fade
    show elena smile at center with dissolve
    
    elena "You decide to return to the university and wait for the next lecture."
    
    hide elena with dissolve
    
    jump next_class

label next_class:
    scene cab with fade
    show gogoi smile with fade
    play sound "heels.wav" fadein 0.5
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
            # //
label ilicoMeeting:
    # sad music
    play music "sad_theme.wav" loop fadein 0.5
    
    scene cab with fade
    show ilico sad at center with dissolve
    
    player "Hi, why are you so upset?"
    
    ilico "I am very nervous about the upcoming exams... I can't find peace."
    
    player "Bro, it's only the first day of classes. We won't have an exam anytime soon."
    
    show ilico shocked
    ilico "Even after hearing that, I still have a bad feeling about this university."
    
    menu:
        "Let's go to Das Kebab. Maybe some kebab will improve your mood.":
            $ ilicoRelation += 10
            
            show ilico smile
            ilico "Alright, let's go and eat some delicious kebabs."
            
            player "Alright!"
            
            hide ilico with dissolve
            jump gogoiLecture
            
        "I'm going to develop schizophrenia soon because of people like this.":
            $ ilicoRelation -= 10
            
            show ilico sad
            "Ilico starts crying because of his worthless fate."
            
            player "OMG, I should have gone to medical school instead."
            
            hide ilico with dissolve
            jump gogoiLecture

# Gogoi's class

label gogoiLecture:
    scene cab with fade
    play music "funnyMusic2.mp3" loop fadein 0.5
    play sound "heels.wav" fadein 0.5

    show gogoi smile
    gogoi "Hello, everyone. Today, we will analyze ourselves and reflect a bit."

    show gogoi smug
    gogoi "I wrote down some activities on the table. Please choose one."

    show gogoi happy
    gogoi "So, let's do an activity!"

    play sound "geese.mp3" fadein 0.5
    menu:
        "Johari Window":
            show gogoi impressed
            gogoi "GREAT CHOICE! NOW, DO ALL OF THEM."
        "MBTI Personality Test":
            show gogoi impressed
            gogoi "GREAT CHOICE! NOW, DO ALL OF THEM."
        "Europass CV":
            show gogoi impressed
            gogoi "GREAT CHOICE! NOW, DO ALL OF THEM."
        "Emotional Intelligence":
            show gogoi impressed
            gogoi "GREAT CHOICE! NOW, DO ALL OF THEM."

    show gogoi smug
    player "Omg, my mental health is getting affected."

    jump finishedFirstDay


label finishedFirstDay:
    play music "sadMusic.mp3" loop fadein 0.5
    # relax music
    
    scene dorm with fade
    show elena smile at center with dissolve
    
    elena "The last lecture of the day has ended, and everyone is heading home to relax."
    
    show elena smile 2
    elena "Suddenly, you remember that you live in a dorm with a huge number of cockroaches."
    
    show elena smug
    elena "You don't even know who your roommate is."
    
    play sound "cristofor.mp3" fadein 0.5
    hide elena with dissolve
    
    # Note: The comment about islam was changed to match the actual scene with Maxim
    
    show elena shocked at left with dissolve
    elena "You see a blond, athletic guy entering the room."

    hide elena
    
    show maxim smile at right with dissolve
    maxim "Hey there."
    
    show maxim smile 2
    maxim "Is this room 318?"
    
    player "Umm... Yes. Who are you?"
    
    show maxim smile
    maxim "My name is Maxim, I will be living in this room."
    
    player "Oh me too."
    
    player "Why did you decide to live in a dormitory?"
    
    show maxim smug
    maxim "Because there is a gym nearby, I need to live as close to it as possible."
    
    player "You look buff already, why do you need to train more?"
    
    show maxim angry
    maxim "ITS NEVER ENOUGH! I NEED TO BECOME EVEN STRONGER!"
    
    player "Uhhh.. alright, please don't kill me."
    
    show maxim smile 3
    maxim "Don't worry, I don't bully weak chushpan kids."
    
    show maxim smug
    maxim "Anyways, wanna go to the gym with me sometime? You look like a fricking tryapka."
    
    menu:
        "Nah, I don't want to become a gym rat.":
            $ maximRelation -= 10
            
            show maxim angry 2
            maxim "Pfft, well don't blame me when you get bullied."
            
        "Yes! I wanna be muscular like you.":
            $ maximRelation += 10
            
            show maxim laugh
            maxim "I like your enthusiasm, maybe you are not as weak as I thought."
            
            show maxim smile
            maxim "Maybe we can be friends?"
            
            hide maxim with dissolve
            hide elena with dissolve
            jump maximStory
    
    hide maxim with dissolve
    
    show elena smile at center with dissolve
    elena "You were very tired from today's events."
    
    show elena sleepy
    elena "You put your head on the pillow and instantly fell asleep."
    
    hide elena with dissolve
    jump secondDay

label maximStory:
    # sad music
    play music "relaxing_tune.mp3" loop fadein 0.5
    
    scene dorm with fade
    show maxim smile at center with dissolve
    
    menu:
        "Sure!":
            $ maximRelation += 10
            show maxim laugh
            maxim "Great! We're going to be gym buddies!"
        "Nah, I just need you to help me train.":
            $ maximRelation -= 10
            show maxim sad
            maxim "Oh, I see. That's fine too."
    
    show maxim smile 2
    maxim "Fine, I'm a bit tired. Let's go to sleep."
    
    player "Together???"
    
    show maxim shocked
    maxim "Ew, of course not! I'm not gay."
    
    hide maxim with dissolve
    jump secondDay

label secondDay:
    play music "noir_detective.mp3" loop fadein 0.5
    scene dorm with fade
    
    show elena smile at left with dissolve
    elena "You wake up to the sunlight filtering through the dusty dorm blinds like a scene from a low-budget detective movie."
    
    show elena smug
    elena "Your roommate Maxim is still asleep, hugging his protein shaker like it contains the secrets of the universe."
    
    # First clue about the robbery
    show elena shocked
    elena "Your phone buzzes with a UTM news alert: 'Local Bank Robbed - Authorities Suspect Student Involvement'"
    
    # Player notices something
    player "(That's strange... didn't Islam mention something about 'making money quickly' yesterday?)"
    
    show maxim smile at right with dissolve:
        zoom 0.9
    
    menu:
        "Wake up Maxim and show him the news":
            player "Hey, Muscle Mountain, wake up! Check out this crazy news!"
            
            show maxim sad
            maxim "Ughhh... what time is it? This better be important or I'll bench press you."
            
            player "Someone robbed Moldova National Bank yesterday. Police think it was a student."
            
            show maxim shocked
            maxim "Seriously? That's wild. Probably some desperate guy who couldn't afford the cafeteria prices."
            
            show maxim smug
            maxim "Though I did see Bozadji counting a lot of cash yesterday after class..."
            
            # New clue
            $ clue_bozadji_cash = True
            
            show elena smile 2
            elena "You make a mental note about Bozadji having suspicious amounts of cash."
            
            show maxim smile
            maxim "Anyway, we should get going. Cristofor's lecture starts in 30 minutes, and rumor has it he knows something about the robbery."
            
        "Let Maxim sleep and investigate alone":
            $ maximRelation -= 5
            
            hide maxim with dissolve
            
            show elena smile
            elena "You decide to let your muscle-bound roommate continue his beauty sleep. After all, crime waits for no one!"
            
            show elena shocked
            elena "As you get dressed, you notice a small mud stain on your roommate's shoes that wasn't there yesterday."
            
            # New clue
            $ clue_maxim_shoes = True
            
            player "(Hmm, that's odd. Wasn't the news report saying the robbers escaped through the muddy construction site?)"
            
            show elena smug
            elena "You quietly leave the room, your mind racing with possibilities and accusations that would make Sherlock Holmes proud... or concerned for your mental health."
            
        "Continue sleeping, crime can wait":
            $ karma -= 10
            
            hide maxim with dissolve
            
            show elena sleepy
            elena "You decide that becoming an amateur detective can definitely wait until after you've had your full eight hours. After all, Batman doesn't have to deal with morning classes."
            
            show elena shocked
            elena "Unfortunately, your dreams of peaceful slumber are interrupted by something even more terrifying than crime - your roommate's morning workout routine."
            
            show maxim angry at right with dissolve:
                zoom 0.9
            
            maxim "RISE AND GRIND, ROOMIE! IT'S CHEST DAY! ONE! TWO! THREE!"
            
            show elena annoyed
            elena "The entire room shakes with each push-up as Maxim counts loudly enough to wake the dead - or worse, hungover students."
            
            player "What time is it? And why does it feel like I'm in an earthquake simulator?"
            
            show maxim smile 3
            maxim "It's GAINS o'clock! I've already done 100 push-ups, 100 sit-ups, and I'm about to head out for a 10km run!"
            
            player "Are you training to be a hero for fun or something?"
            
            show maxim smug
            maxim "No time for jokes! There's an emergency assembly at school. Something about a crime and a special announcement."
            
            player "Ugh, fine. But this better be worth missing breakfast for."
            
            show maxim smile
            maxim "Don't worry, I made you a protein shake! It's only slightly chunky."
            
            show elena smug
            elena "You eye the mysterious brown liquid with the same suspicion normally reserved for UTM cafeteria food."
            
            player "I think I'd rather face the criminal."
    
    hide maxim with dissolve
    hide elena with dissolve
    jump ilicoMeeting2


label ilicoMeeting2:
    # Play schizophrenia music
    # Scene: corridor
    scene coridor with fade
    show elena
    elena "You go down the corridor and you see again this weird curly blond person around cabinet 113."
    show elena annoyed
    elena "But this time he is not upset. He has a mad facial expression."
    play music "creepyMusic.mp3" loop fadein 0.5
    hide elena
    show ilico angry
    menu:
        "Go to him and ask about his mood":
            $ ilicoRelation += 10
            player "Hi, how are you?"
            ilico "I am busy right now."
            show elena shocked at right
            elena "You see how he very quickly writes some weird symbols on his notebook with strength and mad eyes."
            player "What are you doing?"
            show ilico angry 2 at left
            ilico "I am improving my trading strategy. I almost have the ideal market strategy BUT there is a small detail missing. I CAN'T FIND IT."
            player "What are you talking about?"
            show elena at right
            elena "Actively swinging, he plunges into his thoughts."
            show ilico shocked at left
            ilico "MM... Arbitrage... Slippage... Pump and dump... Dark pools... OH! Maybe it's the liquidity trap?! No... NO! The flash crash paradox?!"
            show elena shocked at right
            elena "His eyes shine as he keeps muttering."
            show ilico angry 2 at left
            ilico "AHH! It's the MARKET MAKER'S REVENGE! OR... OR... THE DEAD CAT BOUNCE?!"
            player "I have no idea what you're saying."
            show ilico angry at left
            ilico "HEDGE! HEDGE EVERYTHING! THE TREND IS YOUR FRIEND UNTIL IT'S NOT!"
            show elena shocked at right
            elena "He starts aggressively drawing candlestick patterns in the air."
            player "Are you okay?"
            show ilico shocked at left
            ilico "OF COURSE NOT! I'M IN A BEAR MARKET OF EMOTIONS!"
            show elena at right
            elena "You decide to leave him to his thoughts."
        "Move on":
            $ ilicoRelation -= 10
            show ilico smug
            ilico "MMMmMMmMMmMm"
    jump cristoforLecture
label cristoforLecture:
    scene cab with fade
    show elena happy with fade
    # heels
    play music "funnyMusic2.mp3" loop fadein 0.5
    play sound "heels.wav" fadein 0.5
    hide elena
    show gogoi happy at right
    gogoi "Good morning, Fafers!"
    show gogoi smile at right
    gogoi "Guess what? Cristofor will grade you based on your lab presentations for the second midterm!"
    show gogoi happy 2 at right
    gogoi "Good luck!"

    show elena smile 2 at left
    show gogoi smile 2 at right
    gogoi "Today is an important day because we can finally present labs to Cristofor."
  
    scene cab with fade
    show elena angry at left
    show gogoi angry at right

    gogoi "It's 8:15! WHERE IS CRISTOFOR?!"

    show elena annoyed at left
    hide gogoi
    player "Ugh, I didn't sleep all night, and now this? I better ask Islam. Maybe he knows something. He's always lurking around like a shadow anyway."

    # Scene 2: The Mysterious Sleepless Islam
    scene cab with fade
    show islam

    player "Hey, Islam! How are you? Do you know where Cristofor is?"
    
    show islam sad
    islam "بدلاً من أن أسرق بنكاً، قمت بعمله المعملي!!! وأين هو؟؟"
    play sound "islam.wav" fadein 0.5
    player "I didn't sleep last night, but Islam..."
    show islam
    player "I'm not sure if he slept this entire semester..."
    player "I won't disturb him... He is hallucinating and thinking he is in Jordania?"
    hide islam
    show elena annoyed
    elena "Cristofor is late again. Typical."

    # Scene 3: The Late Bozadji

    show elena smug at right
    elena "Suddenly, the door opens and walks Artiom Bozadji, late as always."
  
    player "Hi! Are you prepared to present your labs? And do you know where Cristofor is?"

    show bozadji smug at left
    bozadji "Privet! Wait, what? He's not here? Ugh, he's wasting my time. I could be making money right now instead of waiting"
    play music "monkeyBusines.wav" loop fadein 0.5
    player "Totally agree with you"

    # Scene 4: The Mirage of Cristofor
    hide bozadji
    show elena shocked at right
    
    elena "Just as you're about to give up hope, you see a silhouette at the end of the corridor. Is it... Cristofor? Could it be?"
    play music "cristofor.mp3" loop fadein 0.5
    show elena sad at right
    elena "Your heart skips a beat and you squint your sleep-deprived eyes to get a better look."

    player "Wait... is that him? Or is it just a mirage? Am I hallucinating from lack of sleep?"

    show elena shocked at right
    elena "The silhouette stands still, unmoving. You realize it's not Cristofor. It's just a suspiciously Cristofor-shaped coat."

    player "kms"

    # Scene 5: Bozadji's Disappearance
    show elena annoyed at right

    elena "You turn to Bozadji to share your disappointment, but... he's gone... Vanished..."
    play sound "creepyMusic.mp3" fadein 0.5
    show elena shocked at right
    elena "Bozadji disappeared..."

    # Scene 6: The Discord Bomb
    scene cab with fade
    show elena shocked at right

    elena "Just as you're about to give up and kys, your phone buzzes. It's a notification from Discord. Cristofor has finally spoken."

    show cristofor smile at left
    cristofor "Good morning, everyone! Sorry for the delay. There was a horrible traffic jam."
    show cristofor smug at left
    cristofor "Anyway, here's your choice for presenting the labs:"
    cristofor "- Next lesson at 15:00"
    cristofor "- Or at 17:30"
    show cristofor smile 3 at left
    cristofor "Choose wisely!"

    player "Wait, what? 15:00 or 17:30? That's not a choice that's a trap!"

    show elena shocked at right
    show cristofor smile 2 at left
    elena "But before you can react, the Discord bot auto-selects 21:00 for you. Congratulations! You're now presenting your labs at 9 PM."
    play music "cristofor.mp3" loop fadein 0.5
    player "What the fistic?#$!?! With this timing, we'll never be ready for the midterms!"
    hide cristofor
    # Scene 7: The Ilico Meltdown
    scene cab with fade
    show ilico angry with fade

    show elena smile 2 at right
    elena "You hear a familiar voice"
  
    show elena happy at right
    elena "It's Artemie!!! You are heading to him to complain about laboratories!"
    play music "creepyMusic.mp3" loop fadein 0.5
    show ilico shocked at left
    ilico "NOOOOOOOOOOOOOOO!"
    show ilico angry 2 at left
    ilico "What if the market crashes before I present my labs?!"

    player "Hey, calm down. The only thing crashing right now is my will to live. What's wrong?"

    show ilico sad at left
    ilico "I can't focus on my labs because I'm too busy calculating the risk-reward ratio of presenting early versus late."
    player "I have no words..."
    hide ilico
    # Scene 9: The Final 
    scene cab with fade
    show elena smile 2 at right

    elena "As the clock strikes 21:00, Cristofor finally arrives"
    play sound "cristofor.mp3" fadein 0.5
    show cristofor smile at left
    cristofor "Alright, let's check these labs! All 15 groups at once!"

    show cristofor smug at left
    cristofor "I'll ask each of you a question. If you answer correctly, you pass. If not... well, let's just say the universe is cruel."
    play music "creepyMusic.mp3" loop fadein 0.5

    # The Probability Theory Question
    show cristofor smile 3 at left
    cristofor "First question: Which probability theory concept is the most important for understanding randomness?"
    show cristofor smug at left
    cristofor "Choose wisely. Your grade depends on it."

    menu:
        "Pigeonhole Principle":
            show cristofor laugh at left
            cristofor "Incorrect! The correct answer is... Martingale. But since you tried, you tried :)"
            $ karma -= 10
        "Martingale":
            show cristofor smile 2 at left
            cristofor "Incorrect! The correct answer is... Probabilistic Deviation Propagation. But don't worry, I'll be generous, 5 is too a positive grade)"
            $ karma -= 10
        "Probabilistic Deviation Propagation":
            show cristofor smile 3 at left
            cristofor "Incorrect! The correct answer is... Pigeonhole Principle. Curlu-Curlu!"
            $ karma -= 10

    show elena shocked at right

    elena "Cristofor pulls out a giant slot machine and starts spinning it to determine your lab marks."

    show cristofor smile at left
    cristofor "Next group! Same question. Choose wisely."

    show cristofor smile 2 at left
    cristofor "You got huge marks lately"
    show cristofor smug at left
    cristofor "Mr. Pumpkin asked me to do Gaussean Distribution"
    show cristofor smile 3 at left
    cristofor "Reverse Gaussean Distribution..."
    show cristofor laugh at left
    cristofor "80%% fail..."

    show cristofor smile at left
    cristofor "The universe works in mysterious ways! Next group!"

    show elena sad at right
    elena "You finally finish presenting your labs at 23:00. Your brain feels like..."
    show elena sleepy at right
    elena "Sorry, Your brain feels nothing"
    play music "sadMusic.mp3" loop fadein 0.5
    player "I just spent hours presenting labs to a man who grades us with a slot machine. What am I even doing with my life?"
    player "If this is how it's going to be, I'm never going to make money. I need to start doing something."
    player "Artemie is talking a lot about market and the big player is bank"
    player "Maybe I can do something useful to them?"
    player "Optimize database, Legacy system, slow transactions?"
    jump furduiLaboratory

# Scene Label
label furduiLaboratory:
    # Set the scene
    scene cab  # Ensure you have a classroom background
    show elena at left
    elena "Today you have lecture with Furdui, be prepared for his questions..."
    
    # Initial interaction
    play sound "thunder.wav" fadein 0.5
    play music "troll.wav" fadein 0.5
    
    show furudui at right
    player "Good morning, Professor Furdui. I'm here to present my merge sort laboratory work."

    show furudui smug at right
    furdui "Ah, Elena. Another student hoping to pass with minimal effort, I see."

    player "No, professor. I've worked hard on this lab and I'm prepared to demonstrate my understanding."

    show furudui angry at right
    furdui "Hard work? In this generation? Let's see about that. Your punctuality is already a problem."

    player "I know I'm a bit late, but I promise my work meets the requirements."

    show furudui angry 2 at right
    furdui "Late submissions are the first sign of academic negligence. But go on, convince me."
    play music "creepyMusic.mp3" loop fadein 0.5
    
    menu:
        "Apologize sincerely":
            player "I sincerely apologize for the delay. I understand the importance of deadlines."
            $ karma += 5
            show furudui smile at right
            furdui "At least you show some understanding."

        "Make an excuse":
            player "There were some unexpected complications with my computer..."
            $ karma -= 5
            show furudui angry at right
            furdui "Excuses, always excuses. The real world doesn't accept such nonsense."

    show furudui smug at right
    furdui "Before we discuss your merge sort implementation, you'll need to prove your understanding."

    player "I'm ready for any questions you have, professor."

    # Merge Sort Quiz
    show furudui smile 3 at right
    furdui "Let's begin with a comprehensive quiz about merge sort. Each incorrect answer will cost you."

    # Question 1: Basic Concept
    show furudui at right
    player "First question: What is the primary strategy of the merge sort algorithm?"

    menu:
        "Divide and Conquer":
            player "Divide and Conquer! The algorithm breaks down the problem into smaller, more manageable sub-problems."
            $ quiz_score += 1
            $ karma += 3
            show furudui smile at right
            furdui "Correct. A promising start."

        "Bubble Sorting":
            player "Um... Bubble Sorting?"
            $ karma -= 5
            show furudui laugh at right
            furdui "Incorrect. Bubble sort is an entirely different, less efficient sorting method."

        "Random Shuffling":
            player "Random Shuffling?"
            $ karma -= 5
            show furudui angry 2 at right
            furdui "Completely wrong. This shows a fundamental misunderstanding."

    # Question 2: Time Complexity
    show furudui smug at right
    furdui "What is the time complexity of merge sort?"

    menu:
        "O(n²)":
            player "O(n²), like insertion sort?"
            $ karma -= 5
            show furudui angry at right
            furdui "Incorrect. Merge sort is more efficient than that."

        "O(n log n)":
            player "O(n log n)! It maintains this complexity in all cases - best, average, and worst."
            $ quiz_score += 1
            $ karma += 3
            show furudui smile 2 at right
            furdui "Correct. You're showing some actual knowledge."

        "O(1)":
            player "O(1)?"
            $ karma -= 5
            show furudui shocked at right
            furdui "Ridiculous. That's constant time, impossible for sorting."

    # Question 3: Implementation Details
    show furudui smile 3 at right
    furdui "Describe the key steps in implementing merge sort."

    menu:
        "Recursively divide, sort sub-arrays, then merge":
            player "First, recursively divide the array into two halves, sort those sub-arrays, and then merge them back together."
            $ quiz_score += 1
            $ karma += 3
            show furudui smile at right
            furdui "Precise explanation. You've clearly studied."

        "Swap adjacent elements":
            player "Swap adjacent elements?"
            $ karma -= 5
            show furudui angry at right
            furdui "No! That's more akin to bubble sort. Completely incorrect."

        "Sort from left to right in one pass":
            player "Sort from left to right in one pass?"
            $ karma -= 5
            show furudui angry 2 at right
            furdui "Absurd. Merge sort is not a single-pass algorithm."

    # Final Quiz Assessment
    if quiz_score >= 2:
        show furudui smile 2 at right
        furdui "Not entirely terrible. Your theoretical understanding shows promise."
        $ karma += 10
    else:
        show furudui sad at right
        furdui "Your performance is disappointing. Theory is the foundation of practical implementation."
        $ karma -= 10

    # Closing Dialogue
    player "May I now present my actual implementation, professor?"

    show furudui smug at right
    furdui "Go ahead. But remember, theory without perfect implementation means nothing."

    # Final Karma and Score Determination
    if karma >= 60:
        show furudui smile at right
        furdui "You've barely scraped through. 8 out of 10. Do better next time."
    elif karma >= 50:
        show furudui at right
        furdui "Mediocre performance. 5 out of 10. Improvement is mandatory."
    else:
        show furudui angry at right
        furdui "Unsatisfactory. 3 out of 10. You need serious remedial work."
    
    jump cristoforLecture2

# Cristofor class

label cristoforLecture2:
    play music "sadMusic.mp3" loop fadein 0.5
    play sound "heels.wav" fadein 0.5
    
    scene cab with fade
    show elena
    elena "Today, you have another lecture with Cristofor."  
    # 113 cabinet maybe, or think of something else  
    show elena smug
    elena "You enter the classroom and see a very elegant person in a suit with long black hair."
    
    play sound "cristofor.mp3" fadein 0.5
    show elena shocked
    elena "Unexpectedly, Elena Gogoi enters with a frightened expression on her face."
    hide elena
    show gogoi shocked with fade
    play music "creepyMusic.mp3" loop fadein 0.5
    gogoi "There is news that one of the students from FAF took part in a bank robbery. The police are trying to find him, but all attempts have failed. He is very skilled at stealth."

    show gogoi sad
    gogoi "Today's lectures are canceled, so everyone is free. However, tomorrow all classes will take place as scheduled, so don't be late."
    hide gogoi
    show elena smug
    elena "You look around the room after hearing this news and notice some strange reactions."
    
    show elena smile 2
    elena "A curly blond student's eyes dart around the room rapidly—though, to be fair, that might just be his usual behavior."
    
    show elena shocked
    elena "A dark-skinned guy with a Jordanian appearance tries to hide his face under his sweater—maybe he just smelled something bad."
    
    show elena annoyed
    elena "However, you can't see your neighbor, Maxim. He was at this lecture, but somehow, he has disappeared."
    
    show elena angry
    elena "And, of course, Bozadji, the first-year student who works in the cybersecurity department, is absent too."
    
    show elena sleepy
    elena "Each of these people seems weird and suspicious. Ugh, this is so exhausting. I'll just go home and relax..."
    
    jump thirdDay

label thirdDay:  
    # Dormitory  
    play music "sadMusic.mp3" loop fadein 0.5
    scene dorm with fade

    show maxim smile
    maxim "Good morning, my friend."  

    player "How did you get here?"  

    show maxim smug
    maxim "I was a bit busy yesterday because I was working on another project."  

    player "Oh, cool. Did you hear the latest news at the university?"  

    show maxim shocked
    maxim "Oh no, what are you talking about?"  

    player "Yesterday, one of the students from our group was involved in a bank robbery."  

    show maxim angry 2
    maxim "Oh, really?? I always knew that Arabic guy looked suspicious."  

    play music "creepyMusic.mp3" loop fadein 0.5
    menu:  
        "Yeah, he is very weird.":  
            $ islamRelation -= 10  
            $ maximRelation += 10  
            show maxim smug  
        "No, he is a good guy with a handsome appearance.":  
            $ islamRelation += 10  
            $ maximRelation -= 10  
            show maxim sad  
    hide maxim
    show elena smug with fade
    elena "Suddenly, you notice a Rolex watch on Maxim’s wrist. Hmm… very suspicious."  
    hide elena
    play sound "thunder.wav" fadein 0.5
    menu:  
        "Ask him about it?":  
            $ maximRelation -= 10  
            $ karma += 10  
            player "Where did you get that watch?"  

            show maxim sad
            maxim "*nervously scratches his head* Oh... I got my salary from my project yesterday... Never mind."  

        "Ignore this fact":  
            $ maximRelation += 5  
            $ karma -= 5  

    player "Let's go to the university and find out the latest news."  

    show maxim smile 2
    maxim "Yeah, let's go."  

    # University  
    jump universityFourthDay  


label universityFourthDay:
    # Scene: University with Policemen
    scene aula3 with fade
    play sound "policy.wav" fadein 0.5

    show elena shocked
    elena "The next day, the police arrive at the university, questioning students."
    hide elena
    
    show kulev smug at left
    kulev "Attention, everyone! The police are investigating last night's bank robbery. If you have any information, please cooperate."
    hide kulev
    
    player "This is getting serious..."

    # Islam A
    play sound "islam.wav" fadein 0.5
    show police
    kulev "Islam, where were you at the time of the robbery?"
    hide police

    show islam smug
    islam "I was praying at home and then working on my university labs."
    hide islam
    
    show kulev angry
    kulev "Can someone confirm this?"
    hide kulev
    
    show islam smug
    islam "Unfortunately, only Allah... Oh, and the teacher who has access to ELSE and can see my lab submission at that time."
    hide islam

    play music "creepyMusic.mp3" loop fadein 0.5
    show elena
    menu:
        elena "Do you think he's telling the truth or just a good liar?"
        "I BELIEVE HIM":
            $ islamRelation += 25
            show elena smile
            elena "A policeman heads to the Decanat to verify Islam's submission."
            hide elena
            if islamRelation > min(bozadjiRelation, ilicoRelation, maximRelation):
                show kulev smug
                kulev "Yes, there really was a submission at that time."
                hide kulev
                play music "funnyMusic2.mp3" loop fadein 0.5
            else:
                show kulev angry
                kulev "No, there are no submissions. You are lying."
                hide kulev
                play sound "thunder.wav" fadein 0.5
        "HE IS A LIAR":
            $ islamRelation -= 25
            hide elena
            show kulev smug
            kulev "We will verify this information."
            hide kulev

    # Artemie B
    show kulev smug
    kulev "Artemie B, where were you at the time of the robbery?"
    hide kulev

    show bozadji smug
    bozadji "I was working at the bank's cybersecurity department on the night shift."
    hide bozadji

    show kulev angry
    kulev "Can someone confirm this?"
    hide kulev

    show bozadji smug
    bozadji "Yes, the security cameras at the bank."
    hide bozadji

    show elena shocked
    elena "A policeman returns."
    hide elena

    show police
    policeman1 "Chief, all recordings from the cameras have been deleted."
    hide police

    show bozadji shocked
    bozadji "That can't be real! It's not my fault! Check my computer logs. My laptop is in my car, I'll go get it."
    hide bozadji

    show elena
    menu:
        elena "Do you believe him?"
        "I BELIEVE HIM":
            $ bozadjiRelation += 25
            hide elena
            if bozadjiRelation > min(islamRelation, ilicoRelation, maximRelation):
                scene parking_lot with fade
                show elena smile
                elena "Artemie B returns with his laptop, proving his innocence."
                hide elena
            else:
                scene empty_parking_lot with fade
                show elena shocked
                elena "Artemie B never returns... He was the thief!"
                hide elena
                play sound "thunder.wav" fadein 0.5
                jump retrospectiveBozadji
        "HE IS A LIAR":
            $ bozadjiRelation -= 25
            hide elena
            show kulev smug
            kulev "We will investigate further."
            hide kulev

    # Artemie I
    show kulev smug
    kulev "Artemie I, where were you at the time of the robbery?"
    hide kulev

    show ilico smug
    ilico "I was studying new trading strategies in the UTM library. You can ask Ms. Valentina, the security guard."
    hide ilico

    show kulev angry
    kulev "Ms. Valentina is on vacation for two weeks..."
    hide kulev

    show ilico shocked
    ilico "No, that isn't true! Maybe she took extra shifts. Go ask her."
    hide ilico

    show elena shocked
    elena "A policeman goes to Ms. Valentina."
    hide elena

    show elena
    menu:
        elena "Do you believe him?"
        "I BELIEVE HIM":
            $ ilicoRelation += 25
            hide elena
            if ilicoRelation > min(islamRelation, bozadjiRelation, maximRelation):
                show kulev smug
                kulev "Ms. Valentina confirmed that she saw you reading in the library."
                hide kulev
                play music "funnyMusic2.mp3" loop fadein 0.5
            else:
                show kulev angry
                kulev "Ms. Valentina denies even being at the university that night."
                hide kulev
                show elena shocked
                elena "Artemie I is the thief!"
                hide elena
                play sound "thunder.wav" fadein 0.5
                jump retrospectiveIlico
        "HE IS A LIAR":
            $ ilicoRelation -= 25
            hide elena
            show kulev smug
            kulev "We will confirm your alibi."
            hide kulev

    # Maxim R
    show police
    policeman1 "Maxim, where were you at the time of the robbery?"
    hide police

    show maxim smug
    maxim "I was delivering food for Glovo."
    hide maxim

    show police
    policeman1 "In what area?"
    hide police

    show maxim smug
    maxim "In the city center."
    hide maxim

    show police
    policeman1 "The bank that was robbed is in the city center. 😱😱😱 Someone saw you! Can you prove you were delivering food?"
    hide police

    show maxim shocked
    maxim "Maybe my manager can. You should contact him."
    hide maxim

    show elena
    menu:
        elena "Do you believe him?"
        "I BELIEVE HIM":
            $ maximRelation += 25
            hide elena
            if maximRelation > min(islamRelation, bozadjiRelation, maximRelation):
                show police
                policeman1 "The administrator confirmed that you were picking up orders at that time."
                hide police
            else:
                show police
                policeman1 "You don't even work for Glovo. No one knows you there!"
                hide police
                show elena shocked
                elena "Maxim R is the thief!"
                hide elena
                play sound "thunder.wav" fadein 0.5
                jump retrospectiveMaxim
        "HE IS A LIAR":
            $ maximRelation -= 25
            hide elena
            show kulev smug
            kulev "We will investigate further."
            hide kulev

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
    
    return

label retrospectiveBozadji:
    scene bg dark with fade
    play music "sadMusic.mp3" loop fadein 0.5

    elena "Now that you think about it, something doesn’t add up..."

    scene bg university_night with fade
    show bozadji with dissolve

    elena "Bozadji—a first-year student—casually lands a job in the cybersecurity department of a bank? Yeah, right."
    elena "You always thought he was just a guy who lucked out by using ChatGPT in interviews, but now... things are looking way too convenient."
    
    scene bg lecture_hall with fade
    show gogoi shocked with dissolve
    
    elena "Then came that lecture, the one where Gogoi burst in, looking like she just realized the exam was today instead of next week."
    gogoi "A bank robbery! A student from FAF is involved! The police can’t find him!"
    
    scene bg empty_classroom with fade
    elena "And who was suspiciously absent? Bozadji."
    
    scene bg police_station with fade
    show kulev  with dissolve

    kulev "Bozadji, where were you at the time of the robbery?"
    
    show bozadji  with dissolve
    bozadji "I was working the night shift at the bank's cybersecurity department."
    
    elena "Oh, how convenient. A cybersecurity guy working *at the exact bank that got robbed*? That’s like finding out the guy in charge of the cookie jar is also the only one with crumbs on his shirt."
    
    show police  with dissolve
    policeman2 "Chief, all the recordings from the security cameras are deleted."
    
    show bozadji surprised with dissolve
    bozadji "It can't be real, it's not my fault! Check my computer logs! My laptop is in my car, I'll go get it."
    
    scene parking with fade
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
    
    return

label retrospectiveMaxim:
    play music "sadMusic.mp3" loop fadein 0.5
    scene black with fade
    show text "Retrospective: The Buff Bandit - How Maxim Lifted More Than Just Weights" with fade
    
    "Looking back, it all makes perfect sense. The signs were as obvious as the vein popping out of Maxim's forehead during his 'just one more rep' moments."
    
    "From the day you met him, something about Maxim was... off. Not in the usual 'gym bro' way - though there was plenty of that too. It was something else."
    
    scene dorm_flashback with fade
    
    "Remember when you first met? 'I need to be close to the gym,' he said. What gym is conveniently located near Moldova National Bank? That's right - FitLife Center, the 24-hour establishment that would make the perfect alibi."
    
    show maxim flex with fade
    maxim "ITS NEVER ENOUGH! I NEED TO BECOME EVEN STRONGER!"
    
    "Stronger for what, Maxim? For carrying bags of cash? For breaking into bank vaults? For fighting off security guards?"
    
    "Then there was his mysterious 'project' - the one he was always 'working on.' Strange how this project never had a name, a deadline, or any tangible results beyond a sudden influx of cash."
    
    scene dorm_morning with fade
    
    "The morning after the robbery, you found mud on his shoes. The escape route through the construction site behind the bank would have been muddy after the previous night's rain."
    
    "And then, the most damning evidence of all..."
    
    scene dorm_night with fade
    show maxim sleep_talking with dissolve
    
    "Remember that night you heard him sleep-talking? You thought it was just another dream about protein powder and bench press PRs."
    
    maxim "Ungh... need to lift... the vault... door... heavier than... expected..."
    
    "At the time, you dismissed it as typical gym-rat sleep babble. Who hasn't dreamt of lifting improbably heavy objects?"
    
    "But now it all connects. The sudden appearance of a Rolex watch. The mysterious late-night 'workouts' that left him exhausted but with no visible pump. The way he always seemed to have cash despite claiming to be a broke student."
    
    scene university_corridor with fade
    
    "And let's not forget his reaction when you told him about the robbery:"
    
    show maxim nervous with dissolve
    maxim "Oh, really?? I always knew that Arabic guy looked like a robber."
    
    "Classic misdirection. Point the finger at someone else - preferably someone who already faces unfair stereotypes. The oldest trick in the criminal playbook."
    
    scene gym with fade
    
    "All those hours 'training' - was he actually casing the joint? Was each rep a rehearsal for the big heist? Was his protein shake bottle actually filled with lock-picking tools?"
    
    "They say the perfect criminal is the one you'd never suspect. And who would suspect the guy whose personality was 90% gym references and 10% protein calculations?"
    
    "The police were looking for a mastermind hacker or a desperate student. They weren't looking for someone whose biceps were bigger than their student debt."
    
    scene police_lineup with fade
    
    "In the end, it wasn't his training regimen that failed him - it was his cover story. No Glovo manager remembered him because Maxim had never delivered anything except, apparently, a perfect bank heist."
    
    "So next time you meet someone whose life revolves suspiciously around 'getting those gains,' maybe ask yourself: what kind of gains are they really after?"
    
    "After all, in Maxim's case, his biggest lift wasn't at the gym - it was at Moldova National Bank."
    
    return

label usmf:
    scene usmf with fade
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
    show elena smug
    elena "Good choice, but not the best one. HE-HE-HE-HE-HE."
    
    show elena smile
    elena "At first, everything goes smoothly, but one day, you go on a picnic with friends."
    
    show elena smile 2
    elena "The location for the party is near a lake."
    
    show elena smile
    elena "You see the dirty water and try to touch it..."
    
    scene bbg with fade
    
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
    play music "funnyMusic2.mp3" loop fadein 0.5
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