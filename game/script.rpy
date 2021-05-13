# The script of the game goes in this file.
label splashscreen:

    play music "musics/OnlapRock.mp3"

    scene black
    with Pause(1)

    show text "Après un peu plus d'un an..." with dissolve
    with Pause(3)

    show text "De longues heures de travail..." with dissolve
    with Pause(3)

    show text "Xixi Fou vous présente officiellement..." with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)

    return
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define gui.dialogue_text_outlines = [ (0, "#00000080", 2, 2) ]
define gui.name_text_outlines = [ (0, "#00000080", 2, 2) ]

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

<<<<<<< HEAD
    e "Kevin tu es un salaud ouais mais toi tes un nazillon hehe"
=======
    e "You've created a new cum'Py g."
>>>>>>> Kevin

    e "plUS QUE D4ËTRE UN SALAUD? TU ES UN BEL ENCUL2!"
menu:
     "What should I do?"

     "Drink coffee.":
         "I drink the coffee, and it's good to the last drop."

     "Drink tea.":
         $ drank_tea = True

         "I drink the tea, trying not to make a political statement as I do."

label aftermenu:
    "JJJ"

return
    # This ends the game.
