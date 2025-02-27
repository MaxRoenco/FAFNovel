
define e = Character("Eileen")

define e = Character("Eileen")

label start:
    scene bg room
    image SilverSexyWoman = "SilverSexyWoman.png"
    image SilverSexyWoman2 = "SilverSexyWoman2.png"
    show SilverSexyWoman 
    e "Hello very gorgeous guuyy."
    e "How are ?? UwU"
    $ player = renpy.input("What is your name beautiful guy: ")
    show SilverSexyWoman2
    e "I am horny of you [player]"

    return
