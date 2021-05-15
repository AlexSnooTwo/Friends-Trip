label splashscreen:

    play music "musics/OnlapRock.mp3"

    scene black
    with Pause(1)

    show text "Après un peu plus d'un an..." with dissolve
    with Pause(3)

    show text "Xixi Fou vous présente officiellement..." with dissolve
    with Pause(2)
    hide text with dissolve

    return

#Characters

define a = Character("Alexis", color= "#FF0000") #Red
define k = Character("Kevin", color= "#FFFF00") #Yellow
define n = Character("Nils", color= "#0000FF") #Blue
define f = Character("Fabrice", color= "#008000") #Green
#Ajouter 4 Filles, une chacun

define gui.dialogue_text_outlines = [ (0, "#00000080", 2, 2) ]
define gui.name_text_outlines = [ (0, "#00000080", 2, 2) ]

label start:

    scene black

    a "Salut les amis !"
    a "Bon je sais ce que vous vous dîtes."
    a "On est venus pour jouer nous! Pas pour t'entendre parler sur un fond noir!"
    a "Et c'est normal... Vous allez pouvoir le faire très bientôt."
    a "Avant ça j'aimerais dire que ce jeu appartient à une réalité parallèle."
    a "Dans cette réalité: pas de virus, pas de masques, pas de confinement!"
    a "Bon si j'étais taquin je dirais qu'il n'y a pas de virus ici non plus."
    a "Bref."
    a "On va donc pouvoir commencer."
    a "Et je voulais vous dire que si jamais on ne pouvait pas aller en Hollande
    pour quelconque raison."
    a "On y sera au moins allé ensemble, à travers ce jeu..."
    a "Allez! Accrochez-vous bien parce que ça commence!"

#Menu avec les sprites de chacun façon BADK fin épisode 3 avec choix en
#en surbrillance

menu player:
    "Qui joue?"

    "Nils":
        $ Nils = True
        n "Je suis un sale communiste et j'aime que les autres le sache."

    "Fabrice":
        $ Fabrice = True
        f "Dans ce jeu j'ai une petite bite."

    "Alexis":
        $ Alexis = True
        a "Je suis un nasillon, j'essaye de pas en faire tout un plat."

    "Kevin":
        $ Kevin = True
        k "J'ai une gueule d'homme des cavernes dans ce VN."

"Au moins je suis pas un juif"

label train:

    scene train #scene qui met en place un train, les personnages, bruit de train

    a "test"

return
