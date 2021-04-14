import io
import os
import time
import tkinter as tk
from tkinter import *
from array import *
import csv

from google.cloud.vision_v1 import types
from tkcalendar import *
import instaloader
from instaloader import Post, NodeIterator
from instalooter.looters import ProfileLooter
from datetime import datetime
import json
from tkinter.filedialog import askopenfilename
# Imports the Google Cloud client library
from google.cloud import vision


import pandas as pd
from selenium import webdriver




# Instantiates a client
client = vision.ImageAnnotatorClient()
L = instaloader.Instaloader()

cartella = os.getcwd()
Hashtag = []
Profile = []
ProFace = []
#Liste per ontologia
ListaIndumenti = []
ClasseIndumenti = []
ListaCibo = []
ClasseCibo = []
IITA = []
FITA = []
NITA = []
HITA = []

df = pd.read_csv(cartella+"\\"+"Ontology"+"\\"+"Indumenti.csv")
ListaIndumenti = df["Indumento"].tolist()
ClasseIndumenti = df["Classe"].tolist()
dt = pd.read_csv(cartella+"\\"+"Ontology"+"\\"+"Food.csv")
ListaCibo = dt["Food"].tolist()
ClasseCibo = dt["Classe"].tolist()

ind  = pd.read_csv(cartella+"\\"+"Ita"+"\\"+"InduIta.csv")
IITA =ind["Indumenti"].tolist()
f = pd.read_csv(cartella+"\\"+"Ita"+"\\"+"FoodIta.csv")
FITA =f["Cibo"].tolist()
n = pd.read_csv(cartella+"\\"+"Ita"+"\\"+"Natureita.csv")
NITA =n["Nature"].tolist()
h = pd.read_csv(cartella+"\\"+"Ita"+"\\"+"HobbieIta.csv")
HITA =h["Hobbie"].tolist()

def AccO():
    try:
        try:
            username = "pupabot"
            password = "Pupabot.98"
            L.login(username, password)
            Profile.append(username)
            Profile.append(password)
            Sce_Ut()
        except (instaloader.exceptions.BadCredentialsException, instaloader.exceptions.InvalidArgumentException):
            window2 = tk.Tk()
            window2.geometry("600x200")
            window2.title("P.U.P.A.")
            window2.grid_columnconfigure(0, weight=1)
            Text_Out = tk.Label(window2, text="Username o password errate, riprovare. ", font="arial,15,bold")
            Text_Out.grid(row=1, column=0, sticky="N", padx=20, pady=20)
    except instaloader.exceptions.ConnectionException:
        window2 = tk.Tk()
        window2.geometry("600x200")
        window2.title("P.U.P.A.")
        window2.grid_columnconfigure(0, weight=1)
        Text_Out = tk.Label(window2,
                            text="Assicurarsi di avere autorizzato questo dispositivo per accedere a questo profilo.(Possibile soluzione accedere per la prima volta con questo dispositivo e inserire il codice di verifica.) ",
                            font="arial,15,bold")
        Text_Out.grid(row=1, column=0, sticky="N", padx=20, pady=20)


def Acc():
    if text_input.get() and text_input2.get():
        try:
            try:
                username = text_input.get()
                password = text_input2.get()
                L.login(username, password)
                Profile.append(username)
                Profile.append(password)
                Sce_Ut()
            except (instaloader.exceptions.BadCredentialsException, instaloader.exceptions.InvalidArgumentException):
                window2 = tk.Tk()
                window2.geometry("600x200")
                window2.title("P.U.P.A.")
                window2.grid_columnconfigure(0, weight=1)
                Text_Out = tk.Label(window2, text="Username o password errate, riprovare. ", font="arial,15,bold")
                Text_Out.grid(row=1, column=0, sticky="N", padx=20, pady=20)
        except instaloader.exceptions.ConnectionException:
            window2 = tk.Tk()
            window2.geometry("600x200")
            window2.title("P.U.P.A.")
            window2.grid_columnconfigure(0, weight=1)
            Text_Out = tk.Label(window2,
                                text="Assicurarsi di avere autorizzato questo dispositivo per accedere a questo profilo.(Possibile soluzione accedere per la prima volta con questo dispositivo e inserire il codice di verifica.) ",
                                font="arial,15,bold")
            Text_Out.grid(row=1, column=0, sticky="N", padx=20, pady=20)
    else:
        window2 = tk.Tk()
        window2.geometry("600x200")
        window2.title("P.U.P.A.")
        window2.grid_columnconfigure(0, weight=1)
        Text_Out = tk.Label(window2, text="Aggiungi le credenziali per accedere ! ", font="arial,15,bold")
        Text_Out.grid(row=1, column=0, sticky="N", padx=20, pady=20)


def Sce_Ut():
    welcome_label2 = tk.Label(window, text="Inserisci il nome dell'utente   : ", font="Helvetica,15")
    welcome_label2.grid(row=1, column=0, sticky="N", padx=20, pady=30)

    text_input.destroy()
    text_input2.destroy()
    search_botton.destroy()
    background_label.destroy()

    window.background2 = PhotoImage(file="Ricerca.png")
    window.background_label2 = tk.Label(image=window.background2)
    window.background_label2.place(x=0, y=0, relwidth=1, relheight=1)

    text_input4 = tk.Entry()
    text_input4.grid(row=2, column=0, sticky="WE", padx=200, pady=99)

    aux = StringVar()
    text_input5 = DateEntry(window, width=30, textvariable=aux, background="orange", foregroud="white", borderwidth=2,
                            year=2020)
    text_input5.grid(row=3, column=0, sticky="WE", padx=400, pady=16)

    aux1 = StringVar()
    text_input6 = DateEntry(window, width=30, textvariable=aux1, background="orange", foregroud="white", borderwidth=2,
                            year=2020)
    text_input6.grid(row=4, column=0, sticky="WE", padx=400, pady=18)

    search_botton2 = tk.Button(text="Cerca per data",
                               command=lambda: (Ver(text_input4.get(), text_input6.get(), text_input5.get())))
    search_botton2.grid(row=5, column=0, sticky="WE", padx=300, pady=0)
    search_botton3 = tk.Button(text="Cerca", command=lambda: (VerNUM(text_input4.get())))
    search_botton3.grid(row=6, column=0, sticky="WE", padx=300, pady=30)

    Open_botton = tk.Button(text="Apri file.Json", command=Open)
    Open_botton.grid(row=7, column=0, sticky="WE", padx=300, pady=0)

def Open():
    try:
        filename = askopenfilename()
        if filename:
            with open(filename) as json_file:
                data = json.load(json_file)

            if 'Name' in data and 'Bio' in data and 'HashtagSelfie' in data and 'Selfie' in data and 'HashtagFriendly' in data and 'Friendly' in data and 'StatusClothes' in data and 'Clothes' in data and 'ClothesPred' in data and 'StatusFood' in data and 'HashtagFood' in data and 'Food' in data and 'FoodPred' in data and 'StatusNatural environmentAnimal' in data and 'HashtagNatural environment/Animal' in data and 'Natural environment/Animal' in data and 'StatusStatusHobbie Gadget' in data and 'HashtagHobbie/Gadget' in data and 'Hobbie/Gadget' in data:
                window3 = tk.Tk()
                window3.geometry("1000x600")
                window3.resizable(False, False)
                window3.title("P.U.P.A. risultati per utente: " + data['Name'])
                window3.grid_columnconfigure(0, weight=1)

                Text_Out = tk.Label(window3, text="Le preferenze di " + data['Name'] + " sono :\n", font="arial,15,bold")
                Text_Out.grid(row=0, column=0, sticky="N", padx=20, pady=20)
                textwidget = tk.Text(window3)
                textwidget.grid(row=2, column=0, sticky="WE", padx=10, pady=10)
                textwidget.insert(tk.END, "Biografia di :" + data['Name'] + "\n")
                textwidget.insert(tk.END, data['Bio'] + "\n")
                textwidget.insert(tk.END, "\n")
                textwidget.insert(tk.END, "Hashtag correlati ai selfie :"+"\n")
                textwidget.insert(tk.END, str(data['HashtagSelfie']) + "\n")
                textwidget.insert(tk.END, str(data['Selfie'])+ "\n")
                textwidget.insert(tk.END, "\n")
                textwidget.insert(tk.END, "Hashtag correlati a  foto in compagnia :"+"\n")
                textwidget.insert(tk.END, str(data['HashtagFriendly']) + "\n")
                textwidget.insert(tk.END, str(data['Friendly']) + "\n")
                textwidget.insert(tk.END, "\n")
                textwidget.insert(tk.END, "Sezione abbigliamento :"+"\n")
                textwidget.insert(tk.END, str(data['StatusClothes']) + "\n")
                textwidget.insert(tk.END, "Hashtag correlati alla categoria abbigliamento :" + "\n")
                textwidget.insert(tk.END, str(data['HashtagClothes']) + "\n")
                textwidget.insert(tk.END, "Le preferenze per la sezione abbigliamento sono :" + "\n")
                textwidget.insert(tk.END, str(data['Clothes']) + "\n")
                textwidget.insert(tk.END, str(data['ClothesPred']) + "\n")
                textwidget.insert(tk.END, "\n")
                textwidget.insert(tk.END, "Sezione cibi e bevande :"+"\n")
                textwidget.insert(tk.END, str(data['StatusFood']) + "\n")
                textwidget.insert(tk.END, "Hashtag correlati alla categoria cibi e bevande :" + "\n")
                textwidget.insert(tk.END, str(data['HashtagFood']) + "\n")
                textwidget.insert(tk.END, "Le preferenze per la sezione cibi e bevande sono :" + "\n")
                textwidget.insert(tk.END, str(data['Food']) + "\n")
                textwidget.insert(tk.END, str(data['FoodPred']) + "\n")
                textwidget.insert(tk.END, "\n")
                textwidget.insert(tk.END, "Sezione Ambiente e animali :"+"\n")
                textwidget.insert(tk.END, str(data['StatusNatural environmentAnimal']) + "\n")
                textwidget.insert(tk.END, "Hashtag correlati alla categoria ambiente e animali :" + "\n")
                textwidget.insert(tk.END, str(data['HashtagNatural environment/Animal']) + "\n")
                textwidget.insert(tk.END, "Le preferenze per la sezione ambiente e animali sono :" + "\n")
                textwidget.insert(tk.END, str(data['Natural environment/Animal']) + "\n")
                textwidget.insert(tk.END, "\n")
                textwidget.insert(tk.END, "Sezione hobbie e tempo libero :"+"\n")
                textwidget.insert(tk.END, str(data['StatusStatusHobbie Gadget']) + "\n")
                textwidget.insert(tk.END, "Hashtag correlati alla categoria hobbie e tempo libero :" + "\n")
                textwidget.insert(tk.END, str(data['HashtagHobbie/Gadget']) + "\n")
                textwidget.insert(tk.END, "Le preferenze per la sezione hobbie e tempo libero sono :" + "\n")
                textwidget.insert(tk.END, str(data['Hobbie/Gadget']) + "\n")
                textwidget.insert(tk.END, "\n")
            else:
                window2 = tk.Tk()
                window2.geometry("600x200")
                window2.title("P.U.P.A.")
                window2.grid_columnconfigure(0, weight=1)
                Text_Out = tk.Label(window2, text="Errore,inserire un file.json con la giusta struttura.", font="arial,15,bold")
                Text_Out.grid(row=1, column=0, sticky="N", padx=20, pady=20)
    except json.decoder.JSONDecodeError:
        window2 = tk.Tk()
        window2.geometry("600x200")
        window2.title("P.U.P.A.")
        window2.grid_columnconfigure(0, weight=1)
        Text_Out = tk.Label(window2, text="Errore,inserire un file con estensione .json.", font="arial,15,bold")
        Text_Out.grid(row=1, column=0, sticky="N", padx=20, pady=20)

def VerNUM(name):
    num = 30
    dir_name: str
    PROFILE_NAME: str
    posts: NodeIterator[Post]
    Time = time.strftime('%Y-%m-%d %H.%M.%S', time.localtime())
    count = 0
    c=0
    if name:
        try:
            try:
                PROFILE_NAME = name
                posts = instaloader.Profile.from_username(L.context, PROFILE_NAME).get_posts()
                #Prendo gli Hashtag dai 45 post più recenti
                for p in posts:
                    if p.is_video == False:
                        if p.typename == "GraphSidecar":
                            x = p.get_sidecar_nodes()
                            for i in x:
                                if i.is_video == False:
                                    c=c+1
                            while c>0:
                                ProFace.append(p)
                                c=c-1
                        else:
                            ProFace.append(p)
                        count = count + 1
                        for i in p.caption_hashtags:
                            if i not in Hashtag:
                                Hashtag.append(i)
                    if (count == num):
                        break

                looter = ProfileLooter(PROFILE_NAME)
                looter.login(Profile[0], Profile[1])
                looter.download(cartella + "\\"+"Users"+"\\"  + PROFILE_NAME + "--" + Time, media_count=num)
                try:
                    dir_name = cartella + "\\"+"Users"+"\\"  + PROFILE_NAME + "--" + Time
                    folder = os.listdir(dir_name)
                    for item in folder:
                        if item.endswith(".json") or item.endswith(".xz") or item.endswith(".txt"):
                            os.remove(os.path.join(dir_name, item))
                except FileNotFoundError:
                    window2 = tk.Tk()
                    window2.geometry("600x200")
                    window2.title("P.U.P.A.")
                    window2.grid_columnconfigure(0, weight=1)
                    Text_Out = tk.Label(window2, text="Quest'utente non ha aggiunto post ultimamente",
                                        font="arial,15,bold")
                    Text_Out.grid(row=1, column=0, sticky="N", padx=20, pady=20)

            except instaloader.exceptions.ProfileNotExistsException:
                window2 = tk.Tk()
                window2.geometry("600x200")
                window2.title("P.U.P.A.")
                window2.grid_columnconfigure(0, weight=1)
                Text_Out = tk.Label(window2, text="Profilo utente (%s) non esistente, riprova.\n" % PROFILE_NAME,
                                    font="arial,15,bold")
                Text_Out.grid(row=1, column=0, sticky="N", padx=20, pady=20)
        except RuntimeError:
            window2 = tk.Tk()
            window2.geometry("600x200")
            window2.title("P.U.P.A.")
            window2.grid_columnconfigure(0, weight=1)
            Text_Out = tk.Label(window2, text="Profilo utente (%s) privato, riprova.\n" % PROFILE_NAME,
                                font="arial,15,bold")
            Text_Out.grid(row=1, column=0, sticky="N", padx=20, pady=20)

        Ann_Imm(dir_name, PROFILE_NAME)

    else:
        window2 = tk.Tk()
        window2.geometry("600x200")
        window2.title("P.U.P.A.")
        window2.grid_columnconfigure(0, weight=1)
        Text_Out = tk.Label(window2, text="Errore,inserire il nome di un utente.", font="arial,15,bold")
        Text_Out.grid(row=1, column=0, sticky="N", padx=20, pady=20)


def Ver(name, DateI, DateF):
    dir_name: str
    PROFILE_NAME: str
    posts: NodeIterator[Post]
    c = 0
    dateFormatter = "%m/%d/%y"
    Time = time.strftime('%Y-%m-%d %H.%M.%S', time.localtime())
    if not DateI or not DateF:
        DateF="2/09/20"
        DateI="1/09/20"
    I = datetime.strptime(DateI, dateFormatter)
    F = datetime.strptime(DateF, dateFormatter)
    if name:
        if DateI and DateF and I <= datetime.now() and F <= datetime.now() and F < I:
            try:
                try:
                    PROFILE_NAME = name
                    posts = instaloader.Profile.from_username(L.context, PROFILE_NAME).get_posts()

                    #Predno gli Hashtag dai post entro una certa data
                    for post in posts:
                        if post.is_video == False:
                            postdate = post.date
                            if postdate < I and postdate >= F:
                                if post.typename == "GraphSidecar":
                                    x = post.get_sidecar_nodes()
                                    for i in x:
                                        if i.is_video == False:
                                            c = c + 1
                                    while c > 0:
                                        ProFace.append(post)
                                        c = c - 1
                                else:
                                    ProFace.append(post)
                                for i in post.caption_hashtags:
                                    if i not in Hashtag:
                                        Hashtag.append(i)
                        if postdate < F:
                            break
                    looter = ProfileLooter(PROFILE_NAME)
                    Date = (I, F)
                    looter.download(cartella + "\\"+"Users"+"\\" + PROFILE_NAME + "--" + Time, media_count=None, timeframe=Date)
                    try:
                        dir_name = cartella + "\\"+"Users"+"\\"  + PROFILE_NAME + "--" + Time
                        folder = os.listdir(dir_name)
                        for item in folder:
                            if item.endswith(".json") or item.endswith(".xz") or item.endswith(".txt"):
                                os.remove(os.path.join(dir_name, item))
                    except FileNotFoundError:
                        window2 = tk.Tk()
                        window2.geometry("600x200")
                        window2.title("P.U.P.A.")
                        window2.grid_columnconfigure(0, weight=1)
                        Text_Out = tk.Label(window2, text="Quest'utente non ha aggiunto post ultimamente",
                                            font="arial,15,bold")
                        Text_Out.grid(row=1, column=0, sticky="N", padx=20, pady=20)

                except instaloader.exceptions.ProfileNotExistsException:
                    window2 = tk.Tk()
                    window2.geometry("600x200")
                    window2.title("P.U.P.A.")
                    window2.grid_columnconfigure(0, weight=1)
                    Text_Out = tk.Label(window2, text="Profilo utente (%s) non esistente, riprova.\n" % PROFILE_NAME,
                                    font="arial,15,bold")
                    Text_Out.grid(row=1, column=0, sticky="N", padx=20, pady=20)
            except RuntimeError:
                window2 = tk.Tk()
                window2.geometry("600x200")
                window2.title("P.U.P.A.")
                window2.grid_columnconfigure(0, weight=1)
                Text_Out = tk.Label(window2, text="Profilo utente (%s) privato, riprova.\n" % PROFILE_NAME,
                                    font="arial,15,bold")
                Text_Out.grid(row=1, column=0, sticky="N", padx=20, pady=20)

            Ann_Imm(dir_name, PROFILE_NAME)
        else:
            window2 = tk.Tk()
            window2.geometry("600x200")
            window2.title("P.U.P.A.")
            window2.grid_columnconfigure(0, weight=1)
            Text_Out = tk.Label(window2,
                                text="Errore,verificare di avere inserito entrambe le date nel modo giusto.",
                                font="arial,15,bold")
            Text_Out.grid(row=1, column=0, sticky="N", padx=40, pady=20)
            Text_Out1 = tk.Label(window2,
                                 text="Assicurarsi che la prima data inserita si minore rispetto alla seconda.",
                                 font="arial,15,bold")
            Text_Out1.grid(row=2, column=0, sticky="N", padx=40, pady=20)
            Text_Out2 = tk.Label(window2,
                                 text="Assicurarsi che la seconda data inserita si minore o uguale rispetto alla data odierna.",
                                 font="arial,15,bold")
            Text_Out2.grid(row=3, column=0, sticky="N", padx=40, pady=20)

    else:
        window2 = tk.Tk()
        window2.geometry("600x200")
        window2.title("P.U.P.A.")
        window2.grid_columnconfigure(0, weight=1)
        Text_Out = tk.Label(window2,
                            text="Errore,inserire il nome di un utente .",
                            font="arial,15,bold")
        Text_Out.grid(row=1, column=0, sticky="N", padx=40, pady=20)



def Ann_Imm(dir_name, PROFILE_NAME):
    os.chdir(dir_name)
    ListImm = os.listdir()
    print(ListImm)
    Verifica = 0
    Confidence = array("d", [])
    imm = []
    topic = []
    Point = array("i", [])
    face = []
    i = 0
    c1 = 0
    c2 = 0
    ContaIMM=0
    selfie = 0
    friends = 0
    Elementi=0
    Totale=0
    HashtagSelfie = []
    HashtagFriends = []
    ContaHashFacce = 0
    BioData = ""
    SelfieStatus = ""
    FriendlyStatus = ""
    HashtagClothes = []
    Clothes = ""
    HashtagFood = []
    Food = ""
    HashtagNaturalenvironmentAnimal = []
    NaturalenvironmentAnimal = ""
    HashtagHobbieGadget = []
    HobbieGadget = ""
    StatusClothes = ""
    StatusFood = ""
    StatusNaturalenvironmentAnimal = ""
    StatusHobbieGadget = ""
    #Liste per preferenze
    IndumentiPref = []
    Indumenti = []
    FoodPref = []
    food = []
    Risultato = ""
    Risultato1 = []
    FP=""
    IP=[]
    Indice=0
    PT=0
    Lost=[]
    while Verifica == 0:
        if not ListImm:
            Verifica = 1
        else:
            str2 = ListImm.pop()
            imm.append(str2)

    for x in imm:
        file_name = os.path.abspath(dir_name + "\\" + x)
        ContaIMM = ContaIMM+1
        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations
        # parte per la face detection
        image = types.Image(content=content)
        response = client.face_detection(image=image)
        faces = response.face_annotations
        face.append(faces)
        # fine
        for label in labels:
            if label.description not in topic:
                topic.append(label.description)
                Confidence.append(label.score)
                c1 = c1 + 1
                Point.append(1)
                c2 = c2 + 1
            else:
                for x in topic:
                    if label.description == x:
                        Point[i] = Point[i] + 1
                        Confidence[i]=Confidence[i]+label.score
                    else:
                        i = i + 1
            i = 0
    for i in Point:
        Totale=Totale+i
    window2 = tk.Tk()
    window2.geometry("1000x600")
    window2.resizable(False, False)
    window2.title("P.U.P.A. risultati per utente: " + PROFILE_NAME)
    window2.grid_columnconfigure(0, weight=1)

    Text_Out = tk.Label(window2, text="Le preferenze di " + PROFILE_NAME + " sono :\n", font="arial,15,bold")
    Text_Out.grid(row=0, column=0, sticky="N", padx=20, pady=20)
    textwidget = tk.Text(window2)
    textwidget.grid(row=2, column=0, sticky="WE", padx=10, pady=10)
    Cont = 0
    Vuoto = 0
    topicspec = []
    pointspec = []
    Bio = instaloader.Profile.from_username(L.context, PROFILE_NAME).biography
    textwidget.insert(tk.END,"Biografia di :" + PROFILE_NAME + "\n")
    if len(Bio) > 0:
        textwidget.insert(tk.END, Bio + "\n")
        BioData = Bio
    else:
        textwidget.insert(tk.END, "L'utente " + PROFILE_NAME + " non ha una biografia da mostrare!" + "\n")
        BioData = "L'utente " + PROFILE_NAME + " non ha una biografia da mostrare!"
    textwidget.insert(tk.END, "\n")


    for i in face:
        if len(i) == 1:
            selfie = selfie + 1
            if ContaHashFacce<ProFace.__len__():
                for i in ProFace[ContaHashFacce].caption_hashtags:
                    if i not in HashtagSelfie:
                        HashtagSelfie.append(i)
        else:
            if len(i) > 1:
                friends = friends + 1
                if ContaHashFacce < ProFace.__len__():
                    for i in ProFace[ContaHashFacce].caption_hashtags:
                        if i not in HashtagFriends:
                            HashtagFriends.append(i)

        ContaHashFacce = ContaHashFacce + 1


    if selfie == 0 and friends == 0:
        textwidget.insert(tk.END, "L'utente " + PROFILE_NAME + " non ha foto di se o foto con altre persone!" + "\n")
        SelfieStatus = "L'utente " + PROFILE_NAME + " non ha foto di se o foto con altre persone!"
        FriendlyStatus = "L'utente " + PROFILE_NAME + " non ha foto di se o foto con altre persone!"
    else:
        if selfie == friends:
            textwidget.insert(tk.END, "L'utente " + PROFILE_NAME + " preferisce sia farsi selfie, che foto "+
                                                                   "in compagnia!" + "\n")
            SelfieStatus = "L'utente " + PROFILE_NAME + " preferisce sia farsi selfie, che foto in compagnia!"
            FriendlyStatus = "L'utente " + PROFILE_NAME + " preferisce sia farsi selfie, che foto in compagnia!"
        else:
            if selfie < friends:
                per = (friends * 100 / ContaIMM)
                textwidget.insert(tk.END, "L'utente " + PROFILE_NAME + " ama farsi foto in compagnia nel " + str(per)
                                  + "%" + " delle immagini !\n")
                if HashtagFriends.__len__()==0:
                    textwidget.insert(tk.END, "Nessun hashtag associato! " "\n")
                else:
                    textwidget.insert(tk.END, "Con associati questi hashtags : " + "\n")
                    for i in HashtagFriends:
                        textwidget.insert(tk.END, "#" + i + " ")
                    textwidget.insert(tk.END, "\n")
                textwidget.insert(tk.END, "\n")
                per = (selfie * 100 / ContaIMM)
                textwidget.insert(tk.END, "L'utente " + PROFILE_NAME + " ama farsi selfie nel " + str(per) + "%"
                                  + " delle immagini !\n")
                if HashtagSelfie.__len__()==0:
                    textwidget.insert(tk.END, "Nessun hashtag associato! " "\n")
                else:
                    textwidget.insert(tk.END, "Con associati questi hashtags : " + "\n")
                    for i in HashtagSelfie:
                        textwidget.insert(tk.END, "#" + i + " ")
                    textwidget.insert(tk.END, "\n")

                    SelfieStatus = "L'utente " + PROFILE_NAME + " ama farsi selfie nel " + str(per) + "% delle immagini !"
                    FriendlyStatus = "L'utente " + PROFILE_NAME + " ama farsi foto in compagnia nel " + str(per)+ "%" + " delle immagini !"
            else:
                per = (selfie * 100 / ContaIMM)
                textwidget.insert(tk.END, "L'utente " + PROFILE_NAME + " ama farsi selfie nel " + str(per) + "%" +
                                  " delle immagini ! \n")
                if HashtagSelfie.__len__()==0:
                    textwidget.insert(tk.END, "Nessun hashtag associato! " "\n")
                else:
                    textwidget.insert(tk.END, "Con associati questi hashtags : " + "\n")
                    for i in HashtagSelfie:
                        textwidget.insert(tk.END, "#" + i + " ")
                    textwidget.insert(tk.END, "\n")
                textwidget.insert(tk.END, "\n")
                per = (friends * 100 / ContaIMM)
                textwidget.insert(tk.END, "L'utente " + PROFILE_NAME + " ama farsi foto in compagnia nel " + str(per)
                                  + "%" + " delle immagini ! \n")
                if HashtagFriends.__len__()==0:
                    textwidget.insert(tk.END, "Nessun hashtag associato! " "\n")
                else:
                    textwidget.insert(tk.END, "Con associati questi hashtags : " + "\n")
                    for i in HashtagFriends:
                        textwidget.insert(tk.END, "#" + i + " ")
                    textwidget.insert(tk.END, "\n")
                SelfieStatus = "L'utente " + PROFILE_NAME + " ama farsi selfie nel " + str(per) + "% delle immagini !"
                FriendlyStatus = "L'utente " + PROFILE_NAME + " ama farsi foto in compagnia nel " + str(
                    per) + "%" + " delle immagini !"

    textwidget.insert(tk.END, "\n")
    Result = Capt_Hashtag("Hashtag_Moda.csv")
    HashtagClothes = Result
    textwidget.insert(tk.END,"Categoria Abbigliamento :"+ "\n")
    textwidget.insert(tk.END,
                      "Gli hashtag utilizzati dall'utente " + PROFILE_NAME + " per la categoria abbigliamento sono : " + "\n")
    if Result.__len__() != 0:
        for i in Result:
            textwidget.insert(tk.END, "#" + i + " ")
        textwidget.insert(tk.END, "\n")
    else:
        textwidget.insert(tk.END, "L'utente " + PROFILE_NAME + " non ha hashtag associati a questa categoria. " + "\n")

    textwidget.insert(tk.END, "Per la sezione abbigliamento " + PROFILE_NAME + " preferisce : \n")
    with open(cartella + "\\Food.csv", "r") as Nat:
        num = 0
        csv_reader = csv.reader(Nat)
        for row in csv_reader:
            y = row[0]
            for i in topic:
                if i == y:
                    PT = PT + Point[num]
                    if i in Lost:
                        Lost.remove(i)
                else:
                    if i not in Lost:
                        Lost.append(i)
                num = num + 1
            num = 0
    Nat.close()
    with open(cartella + "\\Nature.csv", "r") as Nat:
        num = 0
        csv_reader = csv.reader(Nat)
        for row in csv_reader:
            y = row[0]
            for i in topic:
                if i == y:
                    PT = PT + Point[num]
                    if i in Lost:
                        Lost.remove(i)
                else:
                    if i not in Lost:
                        Lost.append(i)
                num = num + 1
            num = 0
    Nat.close()
    with open(cartella + "\\Hobby.csv", "r") as Nat:
        num = 0
        csv_reader = csv.reader(Nat)
        for row in csv_reader:
            y = row[0]
            for i in topic:
                if i == y:
                    PT = PT + Point[num]
                    if i in Lost:
                        Lost.remove(i)
                else:
                    if i not in Lost:
                        Lost.append(i)
                num = num + 1
            num = 0
    Nat.close()
    with open(cartella + "\\Indumenti.csv", "r") as Nat:
        num = 0
        csv_reader = csv.reader(Nat)
        for row in csv_reader:
            y = row[0]
            for i in topic:
                if i == y:
                    topicspec.append(i)
                    pointspec.append(Point[num])
                    Elementi=Elementi+Point[num]
                    PT = PT + Point[num]
                    if i in Lost:
                        Lost.remove(i)
                else:
                    if i not in Lost:
                        Lost.append(i)
                num = num + 1
            num = 0
    Nat.close()
    print(topicspec)
    textwidget.insert(tk.END, "L'utente " + PROFILE_NAME + " ha preferenze in vestiti per :"+ str(Elementi) + ", in percentuale : "+ str(Elementi*100/PT) +"\n")
    StatusClothes = StatusClothes+"L'utente " + PROFILE_NAME + " ha preferenze in vestiti per :"+ str(Elementi) + ", in percentuale : "+ str(Elementi*100/PT)
    with open(cartella + "\\Indumenti.csv", "r") as Nat:
        csv_reader = csv.reader(Nat)
        for row in csv_reader:
            y = row[0]
            aux = IITA[Indice]
            for i in topic:
                if i == y:
                    if Point[Cont] >= ((max(pointspec)) / 5) or Point[Cont] >= 1:

                        textwidget.insert(tk.END, aux +" - Frequenza = " +str(Point[Cont])+ " - " + str(round(((Point[Cont]*100)/PT),2))+"%" + "\n")
                        Indumenti.append(i)
                        IndumentiPref.append(Point[Cont])
                        Clothes=Clothes+" "+aux +" - Frequenza = " +str(Point[Cont])+ " - " + str(round(((Point[Cont]*100)/PT),2))+"%"
                        Vuoto = Vuoto + 1
                Cont = Cont + 1
            Indice=Indice+1
            Cont = 0

        if Vuoto == 0:
            textwidget.insert(tk.END, "L'utente non ha particolari preferenze.  \n")
            Clothes = Clothes + "L'utente non ha particolari preferenze per la categoria Clothes"

    Nat.close()
    Risultato1 = PrefIndumenti(Indumenti,IndumentiPref)
    IP=Risultato1
    for i in Risultato1:
        textwidget.insert(tk.END, i + "\n")
    Vuoto = 0
    textwidget.insert(tk.END, "\n")

    Result = Capt_Hashtag("Hashtag_Food.csv")
    HashtagFood = Result
    textwidget.insert(tk.END, "Categoria cibi e bevande :" + "\n")
    textwidget.insert(tk.END,
                      "Gli hashtag utilizzati dall'utente " + PROFILE_NAME + " per la categoria cibo e bevande sono : " + "\n")
    if Result.__len__() != 0:
        for i in Result:
            textwidget.insert(tk.END, "#" + i + " ")
        textwidget.insert(tk.END, "\n")
    else:
        textwidget.insert(tk.END, "L'utente " + PROFILE_NAME + " non ha hashtag associati a questa categoria. " + "\n")

    textwidget.insert(tk.END, "Per la sezione cibo e bevande " + PROFILE_NAME + " preferisce : \n")
    topicspec.clear()
    pointspec.clear()
    Elementi=0
    with open(cartella + "\\Food.csv", "r") as Nat:
        num = 0
        csv_reader = csv.reader(Nat)
        for row in csv_reader:
            y = row[0]
            for i in topic:
                if i == y:
                    topicspec.append(i)
                    pointspec.append(Point[num])
                    Elementi = Elementi + Point[num]
                num = num + 1
            num = 0
    Nat.close()
    print(topicspec)
    Indice=0
    textwidget.insert(tk.END, "L'utente " + PROFILE_NAME + " ha preferenze in cibo per :" + str(
        Elementi) + ", in percentuale : " + str(Elementi * 100 / PT) + "\n")
    StatusFood = StatusFood+"L'utente " + PROFILE_NAME + " ha preferenze in cibo per :" + str(
        Elementi) + ", in percentuale : " + str(Elementi * 100 / PT)
    with open(cartella + "\\Food.csv", "r") as Nat:
        csv_reader = csv.reader(Nat)
        for row in csv_reader:
            y = row[0]
            aux = FITA[Indice]
            for i in topic:
                if i == y:
                    if Point[Cont] >= ((max(pointspec)) / 5) or Point[Cont] >= 1:
                        textwidget.insert(tk.END, aux + " - Frequenza = " + str(Point[Cont]) + " - " + str(
                            round(((Point[Cont] * 100) / PT), 2)) + "%" + "\n")
                        FoodPref.append(Point[Cont])
                        food.append(i)
                        Food = Food + " " + aux + " - Frequenza = " + str(Point[Cont]) + " - " + str(
                            round(((Point[Cont] * 100) / PT), 2)) + "%"
                        Vuoto = Vuoto + 1
                Cont = Cont + 1
            Indice = Indice + 1
            Cont = 0
        if Vuoto == 0:
            textwidget.insert(tk.END, "L'utente non ha particolari preferenze.  \n")
            Food = Food + "L'utente non ha particolari preferenze per la categoria Food"

    Nat.close()
    Risultato = PrefFood(food, FoodPref)
    FP=Risultato
    textwidget.insert(tk.END, Risultato + "\n")

    Vuoto = 0
    textwidget.insert(tk.END, "\n")
    Vuoto = 0

    Result = Capt_Hashtag("Hashtag_Ambient_Anim.csv")
    HashtagNaturalenvironmentAnimal=Result
    textwidget.insert(tk.END, "Categoria ambiente e animali :" + "\n")
    textwidget.insert(tk.END,
                      "Gli hashtag utilizzati dall'utente " + PROFILE_NAME + " per la categoria ambiente e animali sono : " + "\n")
    if Result.__len__() != 0:
        for i in Result:
            textwidget.insert(tk.END, "#" + i + " ")
        textwidget.insert(tk.END, "\n")
    else:
        textwidget.insert(tk.END, "L'utente " + PROFILE_NAME + " non ha hashtag associati a questa categoria. " + "\n")

    textwidget.insert(tk.END, "Per la sezione ambiente e animali " + PROFILE_NAME + " preferisce : \n")

    topicspec.clear()
    pointspec.clear()
    Elementi=0
    with open(cartella + "\\Nature.csv", "r") as Nat:
        num = 0
        csv_reader = csv.reader(Nat)
        for row in csv_reader:
            y = row[0]
            for i in topic:
                if i == y:
                    topicspec.append(i)
                    pointspec.append(Point[num])
                    Elementi = Elementi + Point[num]
                num = num + 1
            num = 0
    Nat.close()
    print(topicspec)
    Indice=0
    textwidget.insert(tk.END, "L'utente " + PROFILE_NAME + " ha preferenze in natura e animali per :" + str(
        Elementi) + ", in percentuale : " + str(Elementi * 100 / PT) + "\n")
    StatusNaturalenvironmentAnimal = StatusNaturalenvironmentAnimal+"L'utente " + PROFILE_NAME +\
                                     " ha preferenze in natura e animali per :" + str(
        Elementi) + ", in percentuale : " + str(Elementi * 100 / PT)
    with open(cartella + "\\Nature.csv", "r") as Nat:
        csv_reader = csv.reader(Nat)
        for row in csv_reader:
            y = row[0]
            aux = NITA[Indice]
            for i in topic:
                if i == y:
                    if Point[Cont] >= ((max(pointspec)) / 5) or Point[Cont] >= 1:
                        textwidget.insert(tk.END, aux + " - Frequenza = " +str(Point[Cont])+ " - " + str(round(((Point[Cont]*100)/PT),2)) + "%"+ "\n")
                        NaturalenvironmentAnimal=NaturalenvironmentAnimal+" "+aux +" - Frequenza = " +str(Point[Cont])+ " - " + str(round(((Point[Cont]*100)/PT),2))+"%"
                        Vuoto = Vuoto + 1
                Cont = Cont + 1
            Indice = Indice + 1
            Cont = 0
        if Vuoto == 0:
            textwidget.insert(tk.END, "L'utente non ha particolari preferenze.  \n")
            NaturalenvironmentAnimal = NaturalenvironmentAnimal + "L'utente non ha particolari preferenze per la categoria Naturalenvironment&Animal"

    Nat.close()
    textwidget.insert(tk.END, "\n")
    Vuoto = 0

    Result = Capt_Hashtag("Hashtag_interessi.csv")
    HashtagHobbieGadget = Result
    textwidget.insert(tk.END, "Categoria hobbie e tempo libero :" + "\n")
    textwidget.insert(tk.END,
                      "Gli hashtag utilizzati dall'utente " + PROFILE_NAME + " per la categoria passioni e intrattenimento sono : " + "\n")
    if Result.__len__() != 0:
        for i in Result:
            textwidget.insert(tk.END, "#" + i + " ")
        textwidget.insert(tk.END, "\n")
    else:
        textwidget.insert(tk.END, "L'utente " + PROFILE_NAME + " non ha hashtag associati a questa categoria. " + "\n")

    textwidget.insert(tk.END, "Per la sezione passioni e intrattenimento " + PROFILE_NAME + " preferisce : \n")

    topicspec.clear()
    pointspec.clear()
    Elementi=0
    with open(cartella + "\\Hobby.csv", "r") as Nat:
        num = 0
        csv_reader = csv.reader(Nat)
        for row in csv_reader:
            y = row[0]
            for i in topic:
                if i == y:
                    topicspec.append(i)
                    pointspec.append(Point[num])
                    Elementi = Elementi + Point[num]
                num = num + 1
            num = 0
    Nat.close()
    print(topicspec)
    Indice=0
    textwidget.insert(tk.END, "L'utente " + PROFILE_NAME + " ha preferenze in hobby per :" + str(
        Elementi) + ", in percentuale : " + str(Elementi * 100 / PT) + "\n")
    StatusHobbieGadget = StatusHobbieGadget + "L'utente " + PROFILE_NAME + " ha preferenze in hobby per :" + str(
        Elementi) + ", in percentuale : " + str(Elementi * 100 / PT)
    with open(cartella + "\\Hobby.csv ", "r") as Nat:
        csv_reader = csv.reader(Nat)
        for row in csv_reader:
            y = row[0]
            aux = HITA[Indice]
            for i in topic:
                if i == y:
                    if Point[Cont] >= ((max(pointspec)) / 5) or Point[Cont] >= 1:
                        textwidget.insert(tk.END, aux +" - Frequenza = " +str(Point[Cont])+ " - " + str(round(((Point[Cont]*100)/PT),2))+"%"+"\n")
                        HobbieGadget=HobbieGadget+" "+aux +" - Frequenza = " +str(Point[Cont])+ " - " + str(round(((Point[Cont]*100)/PT),2))+"%"
                        Vuoto = Vuoto + 1
                Cont = Cont + 1
            Indice = Indice + 1
            Cont = 0
        if Vuoto == 0:
            textwidget.insert(tk.END, "L'utente non ha particolari preferenze.  \n")
            HobbieGadget = HobbieGadget + "L'utente non ha particolari preferenze per la categoria Naturalenvironment&Animal"

    Nat.close()

    data = {}
    data['Name'] = PROFILE_NAME
    data['Bio'] = BioData
    data['HashtagSelfie'] = HashtagSelfie
    data['Selfie'] = SelfieStatus
    data['HashtagFriendly'] = HashtagFriends
    data['Friendly'] = FriendlyStatus
    data['StatusClothes'] = StatusClothes
    data['HashtagClothes'] = HashtagClothes
    data['Clothes'] = Clothes
    data['ClothesPred'] = IP
    data['StatusFood'] = StatusFood
    data['HashtagFood'] = HashtagFood
    data['Food'] = Food
    data['FoodPred'] = FP
    data['StatusNatural environmentAnimal'] = StatusNaturalenvironmentAnimal
    data['HashtagNatural environment/Animal'] = HashtagNaturalenvironmentAnimal
    data['Natural environment/Animal'] = NaturalenvironmentAnimal
    data['StatusStatusHobbie Gadget'] = StatusHobbieGadget
    data['HashtagHobbie/Gadget'] = HashtagHobbieGadget
    data['Hobbie/Gadget'] = HobbieGadget
    writeToJSONFile('JSON', PROFILE_NAME, data)

    #AnswerForm()
    WriteLost(Lost)
    Hashtag.clear()
    ProFace.clear()

def Capt_Hashtag(name):
    ListaHT = []
    ListSupp = []
    Cont = 0
    hashtag = []
    with open(cartella + "\\"+name, "r") as Reader:
        csv_reader = csv.reader(Reader)
        for row in csv_reader:
            y = row[0]
            hashtag.append(y)
    Reader.close()

    for i in Hashtag:
        if i != ".":
            for y in hashtag:
                if (i == y) or (y in i):
                    if i not in ListaHT:
                        ListaHT.append(i)
                        Cont = Cont + 1
                else:
                    if i not in ListSupp:
                        ListSupp.append(i)
        else:
            if Cont > 0:
                for i in ListSupp:
                    if i not in ListaHT:
                        ListaHT.append(i)
            Cont = 0
            ListSupp.clear()

    return ListaHT

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = cartella+'\\' + path + '\\' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

def PrefIndumenti(topicspec, IndumentiPref):
    a = 0
    b = 0
    Sport = 0
    Casual = 0
    Formal = 0
    Jewelry = 0
    Shoes = 0
    Undergarment = 0
    Glasses = 0
    Tot=0
    List=[]
    s=0
    #Result = "L'utente non ha preferenze per nessuna categoria di indumenti"
    for i in topicspec:
        for v in ListaIndumenti:
            if i==v:
                if ClasseIndumenti[b]=="Sport":
                    Sport = Sport + IndumentiPref[a]
                if ClasseIndumenti[b]=="Casual":
                    Casual = Casual + IndumentiPref[a]
                if ClasseIndumenti[b]=="Formal":
                    Formal = Formal + IndumentiPref[a]
                if ClasseIndumenti[b]=="Jewelry":
                    Jewelry = Jewelry + IndumentiPref[a]
                if ClasseIndumenti[b] == "Shoes":
                    Shoes = Shoes + IndumentiPref[a]
                if ClasseIndumenti[b] == "Undergarment":
                    Undergarment = Undergarment + IndumentiPref[a]
                if ClasseIndumenti[b] == "Glasses":
                    Glasses = Glasses + IndumentiPref[a]
            b = b+1
        b = 0
        a = a + 1
    Tot=Tot+Sport+Casual+Formal+Jewelry+Shoes+Undergarment+Glasses
    s = (Sport * 100) / Tot
    Result = "L'utente ama indossare indumenti per questa categoria:  Abbigliamento Sport - "+str(s)+"%"
    List.append(Result)
    s = (Casual * 100) / Tot
    Result = "L'utente ama indossare indumenti per questa categoria:Abbigliamento Casual - "+ str(s) +"%."
    List.append(Result)
    s = (Formal * 100) / Tot
    Result = "L'utente ama indossare indumenti per questa categoria:Abbigliamento Formali - "+str(s)+"%."
    List.append(Result)
    s = (Jewelry * 100) / Tot
    Result = "L'utente ama indossare indumenti per questa categoria: Gioielli - "+str(s)+"%."
    List.append(Result)
    s = (Shoes * 100) / Tot
    Result = "L'utente ama indossare indumenti per questa categoria: Scarpe - "+str(s)+"%."
    List.append(Result)
    s = (Undergarment * 100) / Tot
    Result = "L'utente ama indossare indumenti per questa categoria: Biancheria intima - "+str(s)+"%."
    List.append(Result)
    s = (Glasses * 100) / Tot
    Result = "L'utente ama indossare indumenti per questa categoria: Occhiali - "+str(s)+"%."
    List.append(Result)
    '''
    if Sport > Casual and Sport >Formal  and Sport >Jewelry and Sport >Shoes and Sport >Undergarment and Sport >Glasses:
        s=(Sport*topicspec.__len__())/100
        Result = "L'utente ama indossare indumenti per questa categoria:  Abbigliamento Sport."
    if Casual > Sport and  Casual >Formal  and Casual >Jewelry  and Casual >Shoes and Casual >Undergarment and Casual >Glasses:
        Result ="L'utente ama indossare indumenti per questa categoria:Abbigliamento Casual."
    if Formal > Sport  and Formal >Casual  and Formal >Jewelry  and Formal >Shoes and Formal >Undergarment and Formal >Glasses:
        Result = "L'utente ama indossare indumenti per questa categoria:Abbigliamento Formali."
    if Jewelry > Sport  and Jewelry >Formal and Jewelry >Casual  and Jewelry >Shoes and Jewelry >Undergarment and Jewelry >Glasses:
        Result =  "L'utente ama indossare indumenti per questa categoria: Gioielli ."
    if Shoes > Sport  and Shoes > Formal and Shoes >Jewelry  and Shoes >Casual and Shoes >Undergarment and Shoes >Glasses:
        Result =  "L'utente ama indossare indumenti per questa categoria: Scarpe."
    if Undergarment > Sport  and Undergarment >Formal  and Undergarment >Jewelry  and Undergarment >Shoes and Undergarment >Casual and Undergarment >Glasses:
        Result =  "L'utente ama indossare indumenti per questa categoria: Biancheria intima. "
    if Glasses > Sport  and Glasses >Formal  and Glasses >Jewelry and Glasses >Shoes and Glasses >Undergarment and Glasses >Casual:
        Result =  "L'utente ama indossare indumenti per questa categoria: Occhiali."
    '''
    return List

def PrefFood(topicspec, FoodPref):
    a = 0
    b = 0
    Fish = 0
    Fruits = 0
    Rice = 0
    Alcoholic_beverage = 0
    Bread = 0
    Chicken = 0
    Pasta = 0
    Drink = 0
    Meat = 0
    Sweet = 0
    Pizza = 0
    Vegetable = 0
    Salad = 0
    Chocolate = 0
    Japan = 0
    Fried = 0
    Egg = 0
    Cheese = 0
    Result = "L'utente non ha preferenze per nessuna categoria di cibi"

    for i in topicspec:
        for v in ListaCibo:
            if i == v:

                if ClasseCibo[b]=="Fish":
                    Fish = Fish + FoodPref[a]
                if ClasseCibo[b]=="Fruits":
                    Fruits = Fruits + FoodPref[a]
                if ClasseCibo[b]=="Rice":
                    Rice = Rice + FoodPref[a]
                if ClasseCibo[b]=="Alcoholic beverage":
                    Alcoholic_beverage = Alcoholic_beverage + FoodPref[a]
                if ClasseCibo[b]=="Bread":
                    Bread = Bread + FoodPref[a]
                if ClasseCibo[b] == "Chicken":
                    Chicken = Chicken + FoodPref[a]
                if ClasseCibo[b] == "Pasta":
                    Pasta = Pasta + FoodPref[a]
                if ClasseCibo[b] == "Drink":
                    Drink = Drink + FoodPref[a]
                if ClasseCibo[b]=="Meat":
                    Meat = Meat + FoodPref[a]
                if ClasseCibo[b]=="Sweet":
                    Sweet = Sweet + FoodPref[a]
                if ClasseCibo[b]=="Pizza":
                    Pizza = Pizza + FoodPref[a]
                if ClasseCibo[b]=="Vegetable":
                    Vegetable = Vegetable + FoodPref[a]
                if ClasseCibo[b]=="Salad":
                    Salad = Salad + FoodPref[a]
                if ClasseCibo[b]=="Chocolate":
                    Chocolate = Chocolate + FoodPref[a]
                if ClasseCibo[b]=="Japan":
                    Japan = Japan + FoodPref[a]
                if ClasseCibo[b]=="Fried":
                    Fried = Fried + FoodPref[a]
                if ClasseCibo[b]=="Egg":
                    Egg = Egg + FoodPref[a]
                if ClasseCibo[b]=="Cheese":
                    Cheese = Cheese + FoodPref[a]
            b = b + 1
        b = 0
        a = a + 1
    if Fish > Fruits and Fish >Rice and Fish >Alcoholic_beverage and Fish >Bread and Fish >Chicken and Fish >Pasta and Fish >Drink and Fish >Meat and Fish >Sweet and Fish >Pizza and Fish >Vegetable and Fish >Salad and Fish >Chocolate and Fish >Japan and Fish >Fried and  Fish >Egg :
        Result = "L'utente ama i cibi per questa categoria: Pesce e affini ."
    if Fruits > Fish and Fruits >Rice and Fruits >Alcoholic_beverage and Fruits >Bread and Fruits >Chicken and Fruits >Pasta and Fruits >Drink and Fruits >Meat and Fruits >Sweet and Fruits >Pizza and Fruits >Vegetable and Fruits >Salad and Fruits >Chocolate and Fruits >Japan and Fruits >Fried and  Fruits >Egg :
        Result ="L'utente ama i cibi per questa categoria: Frutta ."
    if Rice > Fruits and  Rice >Fish and  Rice >Alcoholic_beverage and  Rice >Bread and  Rice >Chicken and  Rice >Pasta and  Rice >Drink and  Rice >Meat and  Rice >Sweet and  Rice >Pizza and  Rice >Vegetable and  Rice >Salad and  Rice >Chocolate and  Rice >Japan and  Rice >Fried and  Rice >Egg:
        Result = "L'utente ama i cibi per questa categoria: Riso e affini. "
    if Alcoholic_beverage > Fruits and Alcoholic_beverage >Rice and Alcoholic_beverage >Fish and Alcoholic_beverage >Bread and Alcoholic_beverage >Chicken and Alcoholic_beverage >Pasta and Alcoholic_beverage >Drink and Alcoholic_beverage >Meat and Alcoholic_beverage >Sweet and Alcoholic_beverage >Pizza and Alcoholic_beverage >Vegetable and Alcoholic_beverage >Salad and Alcoholic_beverage >Chocolate and Alcoholic_beverage >Japan and Alcoholic_beverage >Fried and  Alcoholic_beverage >Egg :
        Result =  "L'utente ama i cibi per questa categoria: Bevande alcoliche . "
    if Bread > Fruits and Bread >Rice and Bread >Alcoholic_beverage and Bread >Fish and Bread >Chicken and Bread >Pasta and Bread >Drink and Bread >Meat and Bread >Sweet and Bread >Pizza and Bread >Vegetable and Bread >Salad and Bread >Chocolate and Bread >Japan and Bread >Fried and Bread >Egg:
        Result =  "L'utente ama i cibi per questa categoria: Pane e affini ."
    if Chicken > Fruits and Chicken >Rice and Chicken >Alcoholic_beverage and Chicken >Bread and Chicken >Fish and Chicken >Pasta and Chicken >Drink and Chicken >Meat and Chicken >Sweet and Chicken >Pizza and Chicken >Vegetable and Chicken >Salad and Chicken >Chocolate and Chicken >Japan and Chicken >Fried and  Chicken >Egg :
        Result =  "L'utente ama i cibi per questa categoria:  Carne di pollo ."
    if Pasta > Fruits and Pasta >Rice and Pasta >Alcoholic_beverage and Pasta >Bread and Pasta >Chicken and Pasta >Fish and Pasta >Drink and Pasta >Meat and Pasta >Sweet and Pasta >Pizza and Pasta >Vegetable and Pasta >Salad and Pasta >Chocolate and Pasta >Japan and Pasta >Fried and  Pasta >Egg :
        Result =  "L'utente ama i cibi per questa categoria: Pasta. "
    if Drink > Fruits and  Drink >Rice and  Drink >Alcoholic_beverage and  Drink >Bread and  Drink >Chicken and  Drink >Pasta and  Drink >Fish and  Drink >Meat and  Drink >Sweet and  Drink >Pizza and  Drink >Vegetable and  Drink >Salad and  Drink >Chocolate and  Drink >Japan and  Drink >Fried and   Drink >Egg :
        Result =  "L'utente ama i cibi per questa categoria: Bevande non alcoliche ."
    if Meat > Fruits and Meat >Rice and Meat >Alcoholic_beverage and Meat >Bread and Meat >Chicken and Meat >Pasta and Meat >Drink and Meat >Fish and Meat >Sweet and Meat >Pizza and Meat >Vegetable and Meat >Salad and Meat >Chocolate and Meat >Japan and Meat >Fried and Meat >Egg:
        Result = "L'utente ama i cibi per questa categoria: Carne e affini ."
    if Sweet > Fruits and Sweet >Rice and Sweet >Alcoholic_beverage and Sweet >Bread and Sweet >Chicken and Sweet >Pasta and Sweet >Drink and Sweet >Meat and Sweet >Fish and Sweet >Pizza and Sweet >Vegetable and Sweet >Salad and Sweet >Chocolate and Sweet >Japan and Sweet >Fried and Sweet >Egg:
        Result = "L'utente ama i cibi per questa categoria: Dolci ."
    if Pizza > Fruits and Pizza >Rice and Pizza >Alcoholic_beverage and Pizza >Bread and Pizza >Chicken and Pizza >Pasta and Pizza >Drink and Pizza >Meat and Pizza >Sweet and Pizza >Fish and Pizza >Vegetable and Pizza >Salad and Pizza >Chocolate and Pizza >Japan and Pizza >Fried and Pizza >Egg:
        Result = "L'utente ama i cibi per questa categoria: Pizza e affini ."
    if Vegetable > Fruits and Vegetable >Rice and Vegetable >Alcoholic_beverage and Vegetable >Bread and Vegetable >Chicken and Vegetable >Pasta and Vegetable >Drink and Vegetable >Meat and Vegetable >Sweet and Vegetable >Pizza and Vegetable >Fish and Vegetable >Salad and Vegetable >Chocolate and Vegetable >Japan and Vegetable >Fried and Vegetable >Egg:
        Result = "L'utente ama i cibi per questa categoria: Verdure ."
    if Salad > Fruits and Salad > Rice and Salad > Alcoholic_beverage and Salad > Bread and Salad > Chicken and Salad > Pasta and Salad > Drink and Salad > Meat and Salad > Sweet and Salad > Pizza and Salad > Vegetable and Salad > Fish and Salad > Chocolate and Salad > Japan and Salad > Fried and Salad > Egg:
        Result = "L'utente ama i cibi per questa categoria: Insalate ."
    if Chocolate > Fruits and Chocolate >Rice and Chocolate >Alcoholic_beverage and Chocolate >Bread and Chocolate >Chicken and Chocolate >Pasta and Chocolate >Drink and Chocolate >Meat and Chocolate >Sweet and Chocolate >Pizza and Chocolate >Vegetable and Chocolate >Salad and Chocolate >Fish and Chocolate >Japan and Chocolate >Fried and Chocolate >Egg:
        Result = "L'utente ama i cibi per questa categoria: Cioccolata ."
    if Japan > Fruits and Japan >Rice and Japan >Alcoholic_beverage and Japan >Bread and Japan >Chicken and Japan >Pasta and Japan >Drink and Japan >Meat and Japan >Sweet and Japan >Pizza and Japan >Vegetable and Japan >Salad and Japan >Chocolate and Japan >Fish and Japan >Fried and Japan >Egg:
        Result = "L'utente ama i cibi per questa categoria: Cibo giapponese o asiatico ."
    if Fried > Fruits and Fried >Rice and Fried >Alcoholic_beverage and Fried >Bread and Fried >Chicken and Fried >Pasta and Fried >Drink and Fried >Meat and Fried >Sweet and Fried >Pizza and Fried >Vegetable and Fried >Salad and Fried >Chocolate and Fried >Japan and Fried >Fish and Fried >Egg:
        Result = "L'utente ama i cibi per questa categoria: Cibo fritto (es.Pollo fritto ,panzerotti etc)."
    if Egg > Fruits and Egg >Rice and Egg >Alcoholic_beverage and Egg >Bread and Egg >Chicken and Egg >Pasta and Egg >Drink and Egg >Meat and Egg >Sweet and Egg >Pizza and Egg >Vegetable and Egg >Salad and Egg >Chocolate and Egg >Japan and Egg >Fried and Egg >Fish:
        Result = "L'utente ama i cibi per questa categoria: Uova ."
    if Cheese > Fruits and Cheese >Rice and Cheese >Alcoholic_beverage and Cheese >Bread and Cheese >Chicken and Cheese >Pasta and Cheese >Drink and Cheese >Meat and Cheese >Sweet and Cheese >Pizza and Cheese >Vegetable and Cheese >Salad and Cheese >Chocolate and Cheese >Japan and Cheese >Fried and  Cheese >Egg and Cheese > Fish:
        Result = "L'utente ama i cibi per questa categoria: Formaggi e affini ."
    return Result

def WriteLost(Lost):
    f = open(cartella + "\\"+"toADD"+"\\" + "Add.csv", "a")
    for i in Lost:
        f.write("{}\n".format(i))
    f.close()

def AnswerForm():
    web = webdriver.Chrome()
    web.get("https://docs.google.com/forms/d/e/1FAIpQLSeV4D2JGawDTNW7g25Kj0_6pxN3d74Qb44Vb14H_8wCgVXTvQ/viewform")

window = tk.Tk()
window.geometry("900x600")
window.title("P.U.P.A.")
window.grid_columnconfigure(0, weight=1)
window.resizable(False, False)
background = PhotoImage(file="Insta.png")
background_label = tk.Label(image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

window.iconbitmap('PUPA.ico')

text_input = tk.Entry()
text_input.grid(row=1, column=0, sticky="WE", padx=300, pady=200)

text_input2 = tk.Entry(show="*")
text_input2.grid(row=2, column=0, sticky="WE", padx=300, pady=0)

search_botton = tk.Button(text="Accedi", command=Acc)
search_botton.grid(row=3, column=0, sticky="WE", padx=350, pady=20)

search_botton = tk.Button(text="Accedi come ospite", command=AccO)
search_botton.grid(row=4, column=0, sticky="WE", padx=350, pady=20)

if __name__ == "__main__":
    window.mainloop()
