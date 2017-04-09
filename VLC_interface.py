# -*- coding: utf-8 -*-
import vlc
import os
import files
import soundcloud
client_id = "" #you need a soundcloud client id
Instance = vlc.Instance()
player = Instance.media_list_player_new()
client = soundcloud.Client(client_id=client_id)
print("This programme use the soundcloud lib. Check https://developers.soundcloud.com/ for more info")

def openFile():
    path = input("File path :")
    Media.add_media(path)
    player.set_media_list(Media)
    print(path," a bien été ajouté")
    print("P pour lancer la lecture ou o pour ouvrir plus de fichiers")

def openDir():
    def aide():
        print("")
        print(" AIDE :")
        print("  !o : valider")
        print("  !p : indiquer une nouvelle adresse complète")
        print("  !b : quitter le menu")
        print("  !? : afficher l'aide")
    if os.path.exists("/mnt/USB-HDD/Musique"):  #Look for the directory. Useful if you use a extrenal storage
        path = "/mnt/USB-HDD/Musique"
    else:                                       #use a other path
        path = "/home/pi/Music"
    while 1==1:
        print("")
        print("Adresse : ",path)
        print("------------------------------------------------")
        for dossier in os.listdir(path):
            print(dossier)
        print("------------------------------------------------")
        op = input("!? pour voir les options : ")
        try:
            if op[0] == "!":
                if op[1] == "o":
                    for file in os.listdir(path):
                        Media.add_media(path + "/" + file)
                    player.set_media_list(Media)
                    print(path," a bien été ajouté")
                    print("P pour lancer la lecture ou o pour ouvrir plus de fichiers")
                    break
                elif op[1] == "p":
                    path = input("Nouvelle adresse : ")
                    while os.path.exists(path) == False:
                        print("l'adresse n'éxiste pas")
                        path = input("Nouvelle adresse : ")
                elif op[1] == "?":
                    aide()
                elif op[1] == "b":
                    print("")
                    break
                else:
                    print("commande non reconnue")
            elif op[0] != "/":
                if os.path.exists(path + "/" + op):
                    path = path + "/" + op
            else:
                if os.path.exists(path + op):
                    path = path + op
        except:
            aide()

def openWeb():
    while True:
        print("1 : Radio")
        print("2 : SoundCould")
        web_mode = input("Faite un choix : ")
        try:
            web_mode =int(web_mode)
        except:
            print("Entrez un nombre")
        if web_mode == 1:
            source = "Radio.txt"
            break
        elif web_mode == 2:
            source = "SoundCloud.txt"
            break
    liste=[]
    names=[]
    file = files.lir(source)
    if file != False:
        for tmp in file:
            tmp2 = tmp.split(";")
            liste.append(tmp2[0])
            names.append(tmp2[1])
        i = 0
        for name in names:
            print(i," : ",name)
            i = i + 1
        while 1==1:
            op = input("Indice du nom entre 0 et " + str(i-1) + " : ")
            if web_mode == 1:
                try:
                    if int(op) < i:
                        Media.add_media(str(liste[int(op)]))
                        player.set_media_list(Media)
                        print(str(names[int(op)])," : ",str(liste[int(op)])," a bien été ajouté")
                        print("P pour lancer la lecture ou o pour ouvrir plus de fichiers")
                        break
                except:
                    print("Indiquez un nombre")
            if web_mode == 2:
                try:
                    if int(op) < i:
                        soundcloud_media = client.get("/resolve",url=liste[int(op)])
                        Media.add_media(soundcloud_media.stream_url+"?client_id="+client_id)
                        player.set_media_list(Media)
                        print(names[int(op)]," a bien été ajouté")
                        print("P pour lancer la lecture ou o pour ouvrir plus de fichiers")
                        break
                except:
                    print("Indiquez un nombre")
    else:
        print("Le fichier "+source+" n'existe pas")
        print("Créé le ou tapez l'adresse dans l'option d'ouverture f")

def openMedia():
    while 1==1:
        print("f : fichier seul")
        print("d : dossier entier")
        print("w : web")
        op = input("Option : ")
        if op == "f" or op == "F":
            openFile()
            break
        elif op == "d" or op == "D":
            openDir()
            break
        elif op == "w" or op =="W":
            openWeb()
            break
        else:
            print("f : fichier seul")
            print("d : dossier entier")
            print("w : web")

Media=Instance.media_list_new()
openMedia()
print(" AIDE:")
print("  P : play")
print("  p : pause")
print("  s : stop")
print("  o : ouvir")
print("  n : suivant")
print("  b : précédent")
print("  q : quitter")

while 1==1:
    op = input("? pour afficher l'aide :")
    if op == "?":
        print(" AIDE:")
        print("  P : play")
        print("  p : pause")
        print("  s : stop")
        print("  o : ouvir")
        print("  n : suivant")
        print("  b : précédent")
        print("  q : quitter")
    if op == "p":
        player.pause()
    if op == "P":
        player.play()
    if op == "s":
        player.stop()
        print("o pour ouvrir un fichier ou pl pour relancer la lecture")
    if op == "o":
        while 1==1:
            op = input("Nouvelle plyliste [o/n] : ")
            if op == "o" or op == "O":
                Media=Instance.media_list_new()
                openMedia()
                break
            elif op == "n" or op == "N":
                openMedia()
                break
    if op == "n":
        player.next()
    if op == "b":
        player.previous()
    if op == "q":
        player.stop()
        break

