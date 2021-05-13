label splashscreen:

    play music "musics/OnlapRock.mp3"

    scene black
    with Pause(1)

    show text "Après un peu plus d'un an..." with dissolve
    with Pause(3)

    show text "Xixi Fou vous présente officiellement..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

#Characters

define a = Character("Alexis")
define k = Character("Kevin")
define n = Character("Nils")
define f = Character("Fabrice")

define gui.dialogue_text_outlines = [ (0, "#00000080", 2, 2) ]
define gui.name_text_outlines = [ (0, "#00000080", 2, 2) ]


label start:

    scene bg room

    show eileen happy


    a "Kevin tu es un salaud"
    k "Ouais mais toi tes un nazillon hehe"

menu:
     "What should I be"

     "Salaud.":
         "Je suis un salaud et j'aime que les autres le sache."

     "Nasillon.":
         $ Nasillon = True

         "Je suis un nasillon, j'essaye de pas en faire tout un plat"

label aftermenu:
    "J"

return
