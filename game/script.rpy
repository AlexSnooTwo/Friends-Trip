#Sprite main menu transformed
image sprite = At("gui/spritelogo.png", bounce)

#Transformation paramètre
transform bounce:
    alpha 0.0 xalign 0.0 yalign 0.0
    easein 3.0 alpha 1.0
    easein 2.0 yalign 0.5
    pause 3
    easein 4.0 xalign 0.0 alpha 0.0


label splashscreen:

    $ renpy.movie_cutscene('logoxixi.ogv')

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
define sncf = Character("Annonce")
#Ajouter 5 Filles, une chacun, deux pour kevin

define gui.dialogue_text_outlines = [ (0, "#00000080", 2, 2) ]
define gui.name_text_outlines = [ (0, "#00000080", 2, 2) ]

label start:

    scene black
    stop music fadeout 1

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
    # scene qui met en place un train, les personnages, bruit de train
    scene fab_train1
    play sound "audio/train.mp3" loop
    a "*{i}C'est marrant de se dire qu'on va refaire un voyage cette année.{/i}*"
    a "*{i}Se dire que l'Espagne de l'année dernière était le premier d'une longue
    série.{/i}*"
    a "*{i}Après tout c'est rare ces moments où on peut être réellement à quatre.{/i}*"
    a "*{i}D'habitude, y'en a toujours un de nous qui ne peut pas être présent.{/i}*"

    scene fab_train2
    f "On dirait qu'on va bientôt arriver à Bruxelles."
    f "Ça me fait penser que j'aurais du y passer depuis longtemps."
    f "J'ai promis à une pote de passer la voir en Belgique."
    f "J'avoue que l'ambiance déconnade autour d'une bière ça me parle."

    scene nils_fab_train
    n "J'aurais bien aimé te dire que moi aussi j'ai {b}ma{/b} Belge à voir."
    n "C'était bien parti avec ma colloque."
    n "Mais bon on reparlera pas de cette expérience romaine..."

    scene kev_alex_train
    k "Ben c'est difficile aussi."
    k "Avoir des discussions avec les gens là... Ouais."
    k "J'imagine qu'on a pas assez de ce {b}petit truc{/b} qui leur faut pour se sentir amusé."
    k "J'essaye de sociabiliser et tout mais... Ouais flemme à la fin, surtout que ça débouche souvent sur rien."

    scene fab_train2
    f "Ben voilà gros, toi aussi t'es un gros flemmard."
    f "Faut sortir de sa zone de confort un peu les gars."

    scene alex_train
    a "Parfois ça part juste d'une panne de PQ les mecs."
    a "Et ouais... {w}C'est ça qu'est bon!"
    a "D'ailleurs les gars en Allemagne on va au FKK hein."

    scene fab_train2
    f "Putain les gars, pas envie de refaire commme à Valence et vous voir vous dégonfler."

    scene kevin_train_cheeky
    k "Ben ça a rien à voir du coup là."

    scene alex_train
    a "C'est plus comme un espace de détente avec un spa, hamam, piscine."
    a "Avec des filles c'est vrai..."

    scene nils_fab_train
    n "Votre truc là. Je suis pas sûr d'y aller."

    scene kevin_train_cheeky
    k "C'est bon gros tu liras un bouquin à l'hotel."

    scene fab_train_cuck
    f "Les gars par contre calmez-vous j'ai une copine aussi."

    scene alex_train
    a "Ah grooos qu'est ce que tu me racontes tes histoires de cuck là."

    scene fab_train_cuck
    f "Ben gros à partir du moment où on a une copine pour toi on est un cuck."

    scene alex_train
    a "C'est pas ce que je voulais dire. Tu peux y aller comme moi et Kevin en mode détente."

    scene fab_train_cuck
    f "Ouais à ce moment là ça dépend."

    scene corridor_train
    sncf "Chers voyageurs bonjour."
    sncf "Nous vous informons que suite à un problème météo votre
    train arrivera à destination avec un retard de diz minutes."
    sncf "Nous vous prions de nous excuser. L'équipe SNCF vous souhaite une agréable fin de voyage à bord de nos TGV."

    scene nils_fab_train
    n "Problème météo? Il fait beau comme en été..."

    scene kevin_train_cheeky
    k "Et ben, dire que ça a pas toujours été aussi médiocre le service ferrovière."

    scene alex_train
    a "*{i}Rire{/i}*"

    scene nils_train_anger
    n "Par contre les gars commencez pas."
    n "Non mais parce que je vous connais avec vos blagues sur les trains."
    n "Je préfère prévenir, parce que sinon ça va vite dérailler."
    n "À tout moment je peux dire à mon pote cheminot de changer de direction."
    n "Et vous aimeriez pas que notre voyage direction Amsterdam se transforme en un aller simple transsibérien."

    scene alex_train
    a "Ça va on a rien dit..."

    scene corridor_train
    "{w}.{w}.{w}."

    scene fab_train2
    f "Nils tu penses quoi de la décroissance?"

    scene nils_train_anger
    n "La seule chose qui va croissante là maintenant c'est mon agacement."
    "{w}.{w}.{w}."

    stop sound fadeout 1
    scene station

    sncf "... et n'oubliez pas de laisser un commentaire sur l'appli' SNCF."




return
