import tkinter as tk
import random
import time
import pygame
resetear=0
def reset():
    global resetear
    resetear=1
    texto_cuenta_regresiva.set('')
    texto_palabras.set('')
    texto_tiempo.set('')
    boton_reset.config(state=tk.DISABLED)
    boton_jugar.config(state=tk.NORMAL)
    pygame.mixer.music.stop()
    return resetear


def comenzar_juego():
    global resetear
    # Deshabilita el botón de "Jugar" después de presionarlo
    boton_jugar.config(state=tk.DISABLED)
    boton_reset.config(state=tk.NORMAL)
    resetear=0
    silabas = [
    # Sílabas de 2 letras
    "ab", "ac", "al", "an", "ar", "as", "az", "ba", "ca", "ce", "co", "da", "de", "di", "do", 
    "el", "en", "es", "ex", "fe", "fi", "fu", "ga", "ge", "go", "ha", "he", "ho", "id", "ig", 
    "im", "in", "ir", "ja", "je", "jo", "la", "le", "li", "lo", "lu", "ma", "me", "mi", "mo", 
    "mu", "na", "ne", "ni", "no", "nu", "pa", "pe", "pi", "po", "pu", "ra", "re", "ri", "ro", 
    "ru", "sa", "se", "si", "so", "su", "ta", "te", "ti", "to", "tu", "un", "ur", "us", "va", 
    "ve", "vi", "vo", "ya", "yo", "za", "ze", "zo",

    # Sílabas de 3 letras
    "aba", "abe", "abi", "abo", "abu", "ada", "ade", "adi", "ado", "adu", "ala", "ale", "ali", "alo", "alu",
    "ama", "ame", "ami", "amo", "amu", "ana", "ane", "ani", "ano", "anu", "ara", "are", "ari", "aro", "aru",
    "asa", "ase", "asi", "aso", "asu", "ata", "ate", "ati", "ato", "atu", "ava", "ave", "avi", "avo", "avu",
    "aza", "aze", "azi", "azo", "azu", "aba", "acu", "ado", "ajo", "ala", "amo", "apa", "ara", "asa", "ata", 
    "ave", "aza", "bal","bien", "bof", "bru", "cie", "cor", "cul", "dal", "ded", "dos", "dul", "eco", "ele",
    "esa", "eso", "eta", "fue", "gal", "gol", "hui", "ima", "ina", "ita", "jor", "kua", "lar", "lej", "lio",
    "lla", "mac", "mal", "mor", "nal", "ner", "nin", "nos", "nue", "oro", "oso", "ova", "pañ", "pez", "pla", 
    "que", "qui", "ras", "rec", "ris", "sas", "sel", "sol", "tal", "ten", "tia", "tio", "tor", "una", "uro",
    "usa", "uso", "uta", "uva", "vez", "vie", "voz", "vus", "xer","yac", "yed", "yel","zaf", "zap", "zen"
]

    # Muestra la cuenta regresiva
    for i in range(3, 0, -1):
        texto_cuenta_regresiva.set(f'Cuenta regresiva: {i}')
        ventana.update()
        time.sleep(1)
        if resetear==1:
            break
    texto_cuenta_regresiva.set('')

    modo=['Tic', 'Tac', 'Boom']
    

    # Muestra las palabras
    silaba=random.choice(silabas)
    texto_palabras.set(f'SILABA: {silaba} \n {random.choice(modo)}')
    #silabas.remove(silaba)

    # Reproduce un archivo de audio mientras esperas el tiempo aleatorio
    pygame.mixer.music.load('resources/TicTac.mp3')  # Empieza el tic tac
    pygame.mixer.music.play()
    
    # Espera un tiempo aleatorio entre 7 y 25 segundos
    tiempo_espera = random.randint(7, 25)
    for t in range(tiempo_espera, 0, -1):
        ventana.update()
        time.sleep(1)
        if resetear==1:
            break
    
    # Cambia a otro archivo de audio cuando se completa el tiempo
    if resetear == 0:
        pygame.mixer.music.load('resources/boom.mp3')  # Suena la bomba
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.stop()
    
    # Restaura la interfaz para jugar nuevamente
    texto_cuenta_regresiva.set('')
    texto_palabras.set('')
    texto_tiempo.set('')
    boton_jugar.config(state=tk.NORMAL)
    boton_reset.config(state=tk.DISABLED)

# Configuración de pygame
pygame.mixer.init()

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Tic Tac BOOM")
ventana.geometry("300x200")

# Variables de control para los textos
texto_cuenta_regresiva = tk.StringVar()
texto_palabras = tk.StringVar()
texto_tiempo = tk.StringVar()

# Etiquetas para mostrar los textos
ventana.iconbitmap('resources/bomb.ico')

etiqueta_cuenta_regresiva = tk.Label(ventana, textvariable=texto_cuenta_regresiva, font=("Arial", 20))
etiqueta_cuenta_regresiva.pack()

etiqueta_palabras = tk.Label(ventana, textvariable=texto_palabras, font=("Arial", 100))
etiqueta_palabras.pack()

etiqueta_tiempo = tk.Label(ventana, textvariable=texto_tiempo, font=("Arial", 50))
etiqueta_tiempo.pack()

# Botón "Jugar"
boton_jugar = tk.Button(ventana, text="JUGAR", command=comenzar_juego,font=("Arial", 20))
boton_jugar.pack()

boton_reset = tk.Button(ventana, text="RESET", command=reset,font=("Arial", 20))
boton_reset.pack()
boton_reset.config(state=tk.DISABLED)

ventana.mainloop()
