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
    scene fab_train1 with dissolve
    play sound "audio/train.mp3" loop
    a "*{i}C'est marrant de se dire qu'on va refaire un voyage cette année.{/i}*"
    a "*{i}Se dire que l'Espagne de l'année dernière était le premier d'une longue
    série.{/i}*"
    a "*{i}Après tout c'est rare ces moments où on peut être réellement à quatre.{/i}*"
    a "*{i}D'habitude, y'en a toujours un de nous qui ne peut pas être présent.{/i}*"

    scene fab_train2 with dissolve
    f "On dirait qu'on va bientôt arriver à Bruxelles."
    f "Ça me fait penser que j'aurais du y passer depuis longtemps."
    f "J'ai promis à une pote de passer la voir en Belgique."
    f "J'avoue que l'ambiance déconnade autour d'une bière ça me parle."

    scene nils_fab_train with dissolve
    n "J'aurais bien aimé te dire que moi aussi j'ai {b}ma{/b} Belge à voir."
    n "C'était bien parti avec ma colloque."
    n "Mais bon on reparlera pas de cette expérience romaine..."

    scene kev_alex_train with dissolve
    k "Ben c'est difficile aussi."
    k "Avoir des discussions avec les gens là... Ouais."
    k "J'imagine qu'on a pas assez de ce {b}petit truc{/b} qui leur faut pour se sentir amusé."
    k "J'essaye de sociabiliser et tout mais... Ouais flemme à la fin, surtout que ça débouche souvent sur rien."

    scene fab_train2 with dissolve
    f "Ben voilà gros, toi aussi t'es un gros flemmard."
    f "Faut sortir de sa zone de confort un peu les gars."

    scene alex_train with dissolve
    a "Parfois ça part juste d'une panne de PQ les mecs."
    a "Et ouais... {w}C'est ça qu'est bon!"
    a "D'ailleurs les gars en Allemagne on va au FKK hein."

    scene fab_train2 with dissolve
    f "Putain les gars, pas envie de refaire commme à Valence et vous voir vous dégonfler."

    scene kevin_train_cheeky with dissolve
    k "Ben ça a rien à voir du coup là."

    scene alex_train with dissolve
    a "C'est plus comme un espace de détente avec un spa, hamam, piscine."
    a "Avec des filles c'est vrai..."

    scene nils_fab_train with dissolve
    n "Votre truc là. Je suis pas sûr d'y aller."

    scene kevin_train_cheeky with dissolve
    k "C'est bon gros tu liras un bouquin à l'hotel."

    scene fab_train_cuck with dissolve
    f "Les gars par contre calmez-vous j'ai une copine aussi."

    scene alex_train with dissolve
    a "Ah grooos qu'est ce que tu me racontes tes histoires de cuck là."

    scene fab_train_cuck with dissolve
    f "Ben gros à partir du moment où on a une copine pour toi on est un cuck."

    scene alex_train with dissolve
    a "C'est pas ce que je voulais dire. Tu peux y aller comme moi et Kevin en mode détente."

    scene fab_train_cuck with dissolve
    f "Ouais à ce moment là ça dépend."

    scene corridor_train with dissolve
    sncf "Chers voyageurs bonjour."
    sncf "Nous vous informons que suite à un problème météo votre
    train arrivera à destination avec un retard de diz minutes."
    sncf "Nous vous prions de nous excuser. L'équipe SNCF vous souhaite une agréable fin de voyage à bord de nos TGV."

    scene nils_fab_train with dissolve
    n "Problème météo? Il fait beau comme en été..."

    scene kevin_train_cheeky with dissolve
    k "Et ben, dire que ça a pas toujours été aussi médiocre le service ferrovière."

    scene alex_train with dissolve
    a "*{i}Rires{/i}*"

    scene nils_train_anger with dissolve
    n "Par contre les gars commencez pas."
    n "Non mais parce que je vous connais avec vos blagues sur les trains."
    n "Je préfère prévenir, parce que sinon ça va vite dérailler."
    n "À tout moment je peux dire à mon pote cheminot de changer de direction."
    n "Et vous aimeriez pas que notre voyage direction Amsterdam se transforme en un aller simple transsibérien."

    scene alex_train with dissolve
    a "Ça va on a rien dit..."

    scene corridor_train with dissolve
    "{w}.{w}.{w}."

    scene fab_train2 with dissolve
    f "Nils tu penses quoi de la décroissance?"

    scene nils_train_anger with dissolve
    n "La seule chose qui va croissante là maintenant c'est mon agacement."
    "{w}.{w}.{w}."

    stop sound fadeout 1
    play music "musics/GoodTimes.MP3"
    scene station with dissolve
    sncf "...et n'oubliez pas de laisser un commentaire sur l'appli' SNCF."

    scene taxi with dissolve
    a "Bon ben go chercher les vélos les gars."

label bikeshop:

    scene shop with dissolve
    k "C'est vraiment un magasin de vélo ça?"
    a "Je sais pas, je t'avais laissé nous en trouver un..."

    scene bikeshop_tenant with dissolve
    "Vendeur" "Bonjourr? Je sais vous aider peut-êtrre?"

    scene bikeshop_tenant2 with dissolve
    a "Bonjour Monsieur. J'aurais justement une question."

    scene bikeshop_tenant with dissolve
    "Vendeur" "Bien sûrr Monsieur."

    scene bikeshop_tenant2 with dissolve
    a "Pourquoi les Belges mettent-ils des bottes pour faire du vélo?"
    "..."
    a "Parce que le sida, ça s'attrape par les pédales."

    scene bikeshop_tenant with dissolve
    "Vendeur" "M'enfin Monsieur, je sais pas. C'est qu'on met pas de bottes ici."
    "Vendeur" "Je suis pas sûrr d'avoir compris Monsieur."
    "{i}Rires{/i}"

    scene bikeshop_tenant2 with dissolve
    a "Pas de soucis. Du coup on aimerait louer quatre vélos."
    f "Pour une semaine."

    scene bikeshop_tenant with dissolve
    "Vendeur" "Ça tombe bien, il m'en rreste justement quatre juste ici."

    scene bikeshop_bikes with dissolve
    f "Bon c'est clairement pas les meilleurs vélos du monde mais y'en a quatre."
    n "Ça tombe bien aussi, qu'ils correspondent à nos tailles respectives."
    n "C'est pas la moto d'Onizuka mais ça fera bien l'affaire."
    a "On aura pas mal au couilles j'espère avec ces selles."
    n "T'as mal au dos?"

    scene bikeshop_tenant with dissolve
    "Vendeur" "Ah oui Monsieur, vous avez raison, en plus ils sont à votre taille."
    "Vendeur" "Vous allez beaucoup rrouler?"

    scene bikeshop_tenant2 with dissolve
    k "On va au moins jusqu'à Amsterdam chef."
    f "On va aussi à Anvers."
    f "Vous penser qu'il faut y aller à l'endroit?"

    scene bikeshop_tenant with dissolve
    "Vendeur" "Ah oui monsieur, ça alors qu'il faut y aller à l'endroit!"
    "{i}Rires{/i}"

    scene bikeshop_tenant2 with dissolve
    a "Bon ben on vous les prend pour une semaine du coup."

    stop music fadeout 1
    play music "musics/all_the_roads.mp3"
    scene black with dissolve
    "Après quelques formalités administratives..."

label bikeroad:

    scene bikeroad1 with dissolve
    f "À fond les balloooooons!"
    n "La vache, dire que je parlais de faire le grand tour avec Hambourg!"
    "{i}Halètements{/i}"
    f "On va pas se mentir c'est un peu plat pour l'instant."
    a "Faut profiter tant qu'on a pas de reliefs pour faire des sprints!"
    f "Typiquement Alexis ça. À vouloir faire des sprints et être cramé après."
    a "Go go go!"

    scene bikeroad2 with dissolve
    k "Take it easy!"
    a "Direction Anvers!!!"
    n "On peut pas faire une pause les gars?"
    f "J'ai une impression de déjà vu."
    f "La musique, la scène..."
    a "T'entends une musique toi?"

    scene bikeroad3 with dissolve
    k "Hâte d'une petite bière là."
    n "Y'a pas eu de transition Kevin."
    n "Entre la phrase de Fabrice et la tienne."
    k "Ah. Euh, ouais."
    n "Tu devrais littéralement ouvrir ton bouquin de grammaire un jour."
    k "Ouais. Je suis victime de ma condition. Prolo' qui reproduit ses codes."
    n "T'appartiens quand même à une grande lignée d'Angleterre."
    k "Ah. Ouais ça. Tu parles de mon père alcoolique?"
    n "N'empêche qu'on doit aller voir ta famille dans le Westshire."
    f "Pour l'instant on va surtout esssayer d'arriver à Anvers."
    a "Le dernier arrivé à l'hotel a perdu!"

    scene bikeroad2 with dissolve
    $ renpy.pause ()

    scene black with dissolve
    "Après un trajet plus ou moins long et une bonne douche à l'hotel."

label bar:

    play music "musics/funkbar.mp3"
    scene anvers with dissolve

    f "Bon les gars choisissez un bar où je prends le premier qui vient."
    f "On tourne en rond depuis tout à l'heure."
    k "C'est bon j'en vois un qui a l'air pas mal sur google."

    scene waitress_bar with dissolve

    "Serveuse" "Hallo jongens! Welkom in de tofste bar van Antwerpen."
    f "What? J'ai pas fait allemand moi. Nils!"
    n "Je bite pas un mot de Batave, c'est pas de l'Allemand..."
    "Serveuse" "Bite?"
    "Serveuse" "Je peux parler Français aussi si vous voulez. J'ai vécu à Bruxelles."
    n "Euh."

    scene counter_bar with dissolve

    a "Hey les gars venez vite vous assoir le gars est déjà en train d'aroser le comptoir de bières!"

    scene waitress_bar with dissolve
    "Serveuse" "Dîtes moi directement pour d'autres boissons que la bière."
    "Serveuse" "Je vous apporterai ça."

    scene counter_bar with dissolve
    a "T'as pas plutôt vu la nana derrière? C'est pas la bière que j'ai envie de tirer."
    f "Nils on dirait que tu tombes pour la serveuse."
    n "On dirait que ce bar a de bonnes... {w}bières."
    f "Et toi Kevin ça pourrait bien être ta chance la fille derrière."

    scene counter_girl with dissolve
    k "Ouais."
    k "Ah ok."
    "*{i}Sueur{/i}*"

    scene barview with dissolve
    f "Bon on dirait bien que y'a que des couilles dans ce bar."
    n "Y'a surtout pas grand monde, rappelons nous de ne pas laisser Kevin nous
    choisir un bar pour la prochaine fois."

    call screen freeroamBar

label finbar:
    scene barview
    menu endbar:
        "Partir":
            n "Je suis un sale communiste et j'aime que les autres le sache."

        "Pas tout de suite":
            call screen freeroamBar
    "Test du screen"
    "Fin"

return
