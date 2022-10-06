from tkinter import *
from tkinter import Label,messagebox
from random import choice
import os
#--------------------------------------------------------------
#_Este programa sirve para crear contraseñas aleatorias para tus dispositivos
#_se puede modificar con las (letras) y (numeros) en la funcion de (ContraseñaAle)
#_tambien tiene la funcion para crear TXT, tambien le agregue una opcion para poder elegirle el nombre y donde guardarlo
#_aunque por default se guarda en la carpeta donde esta el .py 
#_si quieres comprobar si tu contraseña es segura, puedes comprobarlo aqui https://password.kaspersky.com/es/
#_tiene buenos resultados y es sencillo.
#--------------------------------------------------------------
root=Tk()
root.title("Contraseñas aleatorias by Jeff McWill")
root.geometry("325x90")
root.resizable(0,0)
root.iconbitmap("ico.ico")
lista=[]
#--------------------------------------------------------------
def ContraseñaAle():
	entry1 = entrada_programa.get()
	label_resultado.grid(row=3,column=2)

	if entry1 == "":
		label_resultado["text"]="Agrega valores."
	elif int(entry1) > 30:
		label_resultado["text"]="La longitud de la contraseña \n no puede ser mayor a 30."
	else:
		#diccionarios de letras, se pueden modificar.
		valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
		p=""
		contraseña_final=p.join([choice(valores)for i in range(int(entry1))])
		lista.append(contraseña_final)

		label_resultado["text"]="Contraseña:",contraseña_final

def CrearTXT():
	try:
		label_resultado2.grid(row=4,column=2)
		file=open("contraseñasegura.txt","w")
		file.write(f"{lista}")
		label_resultado2["text"]="archivo creado con exito."
		file.close()
	except:
		messagebox.showwarning("Error","No has creado ninguna contraseña.")

def salirAplicacion():
	valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicacion?")
	if valor=="yes":
		root.destroy()

#--------------------------------------------------------------
#Labels
label_titulo=Label(root,text="/// Contraseñas aleatorias ///")
label_titulo.grid(row=1,column=2)
label_longitud=Label(root,text="* Longitud:")
label_longitud.grid(row=2,column=1)
#--------------------------------------------------------------
label_resultado=Label(root)
label_resultado.grid(row=3,column=2)
label_resultado2=Label(root)
label_resultado2.grid(row=4,column=2)
#--------------------------------------------------------------
#Boton
boton_resultado=Button(root,text="Crear",command=ContraseñaAle)
boton_resultado.grid(row=2,column=3)
boton_creartxt=Button(root,text="TXT",command=CrearTXT)
boton_creartxt.grid(row=2,column=4)
boton_Cerrar=Button(root,text="Exit",command=salirAplicacion)
boton_Cerrar.grid(row=2,column=5)
#--------------------------------------------------------------
#Entry
entrada_programa=Entry(root)
entrada_programa.grid(row=2,column=2)
#--------------------------------------------------------------
root.mainloop()
#--------------------------------------------------------------