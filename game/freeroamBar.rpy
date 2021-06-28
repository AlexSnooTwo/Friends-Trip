default alexseen = False
default girlseen = False
default waitress = False
image animated_patrick:
    "patrick.png" with dissolve
    4
    "patrick2.png" with dissolve
    4
    "patrick3.png" with dissolve
    4
    "patrick4.png" with dissolve
    4
    "patrick5.png" with dissolve
    4
    repeat

screen freeroamBar():

    imagemap:
        idle "images/screen_bar.png"

        imagebutton:
            focus_mask True
            idle "images/sprites/alex_sprite.png"
            hover "images/sprites/alex_sprite_hover.png"
            xalign 1.035
            ypos 117
            action Jump("alexbar")

        imagebutton:
            focus_mask True
            idle "images/sprites/girl_sprite.png"
            hover "images/sprites/girl_sprite_hover.png"
            xalign 0.897
            yalign 0.1
            action Jump("kevinbar")

        imagebutton:
            focus_mask True
            idle "images/sprites/waitress_sprite.png"
            hover "images/sprites/waitress_sprite_hover.png"
            xalign 0.681
            yalign 0.489
            action Jump("nilsbar")

        imagebutton:
            focus_mask True
            idle "images/sprites/table_sprite.png"
            hover "images/sprites/table_sprite_hover.png"
            xalign 0.375
            yalign 0.55
            action Jump("finbar")
label alexbar:
    scene screen_bar
    if alexseen == True:
        f "Alexis a l'air déjà bien bourré."
        f "Je ferais mieux de faire autre chose."
        call screen freeroamBar
    else:
        scene counter_bar
        a "Hey mec. Tu viens faire des shots avec moi?!"
        a "Le serveur régale!"
        f "Pourquoi pas quelques-uns."
        f "Histoire d'avoir un peu d'energie."
        scene alex_bar2
        a "{i}*Gloups*{/i}"
        a "Ahhh!"
        scene alex_bar1
        a "Ça casse la gorge wala."
        f "What? Tu viens vraiment de dire ça?"
        a "Ayaaa!"
        f "Hey, tu penses qu'on pourrait demander au barman de mettre notre musique?"
        f "Comme à Grenade l'année dernière."
        a "On va pas faire danser grand monde mais au moins on dansera."
        scene bartender1
        a "Hey! Do you mean to play some songs from us?"
        f "Excellent."
        stop music
        play music "musics/sardines.mp3"
        scene animated_patrick
        "{i}Cliquer pour arrêter{/i}"
        $ alexseen = True
        call screen freeroamBar

label kevinbar:
    scene screen_bar
    if girlseen == True:
        "Ça reste encore un peu timide comme drague."
        "Au moins il à l'air d'entretenir la conversation."
        call screen freeroamBar
    else:
        scene counter_girl
        k "Euh.. Salut?!"
        $ girlseen = True
        call screen freeroamBar

label nilsbar:
    scene screen_bar
    if waitress == True:
        f "Nils a l'air de s'en tenir à bon compte."
        f "Je ne vais pas le déranger."
        call screen freeroamBar
    else:
        scene waitress_bar
        "Hallo Frau Blume."
        $ waitress = True
        call screen freeroamBar
