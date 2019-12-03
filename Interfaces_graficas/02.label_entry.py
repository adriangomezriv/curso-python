from tkinter import *

programa=Tk()
programa.title("Ventana principal")

miFrame=Frame(programa,width=900,height=900)
miFrame.pack()

labelNombre=Label(miFrame,text="Nombre: ")
labelNombre.grid(row=0, column=0, sticky="e", padx="12", pady="5")

cuadroNombre=Entry(miFrame)
#el metodo grid divide el filas y columnas
cuadroNombre.grid(row=0, column=1)
cuadroNombre.config(fg="black", justify="center")


labelApellido=Label(miFrame,text="Apellido: ")
labelApellido.grid(row=1, column=0, sticky="e", padx="12", pady="5")

cuadroApelido=Entry(miFrame)
#el metodo grid divide el filas y columnas
cuadroApelido.grid(row=1, column=1)
cuadroApelido.config(fg="black", justify="center")

labelContrasena=Label(miFrame,text="Contraseña: ")
labelContrasena.grid(row=2, column=0, sticky="e", padx="12", pady="5")

cuadroContrasena=Entry(miFrame)
#el metodo grid divide el filas y columnas
cuadroContrasena.grid(row=2, column=1)
cuadroContrasena.config(show="*", fg="black", justify="center")


labelDireccion=Label(miFrame,text="Direccion: ")
labelDireccion.grid(row=3, column=0, sticky="e", padx="12", pady="5")

cuadroDireccion=Entry(miFrame)
#el metodo grid divide el filas y columnas
cuadroDireccion.grid(row=3, column=1)
cuadroDireccion.config(fg="black", justify="center")

# miLabel=Label(miFrame,text="Hola estudiantes de python",
#               fg="red",font=("Times New Roman",26)).place(x=100,y=200)
programa.mainloop()