from tkinter import *
from tkinter import filedialog as Fichero

ruta = ""

def nuevo():
    texto.delete(1.0, "end")
    root.title("Mi editor")
    mensaje.set("Nuevo Archivo")

def abrir():
    global ruta
    ruta = Fichero.askopenfilename(
        initialdir='.',
        filetypes=(("Ficheros de texto", "*.txt"),  
        ), 
        title="Abrir un fichero."
    )
    if ruta:
        with open(ruta, "r") as archivo:
            contenido = archivo.read()
            texto.delete("1.0", END)
            texto.insert(END, contenido)
            archivo.close()
            mensaje.set("Archivo abierto con exito!")

def guardar():
    global ruta
    if ruta != "":
        contenido = texto.get(1.0, 'end')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set('Archivo guardado con exito!')
    else:
        guardar_como()
            
def guardar_como():
    global ruta
    ruta = Fichero.asksaveasfilename(title = 'Guardar un archivo',
                                        defaultextension = '.txt')
    if ruta is not None:
        contenido = texto.get("1.0", END)
        with open(ruta, 'w') as archivo:
            archivo.write(contenido)
            archivo.close()
        mensaje.set("Archivo guardado con exito!")

root = Tk()
root.title("El bloc de Paola")

menubar = Menu(root)
root.config(menu = menubar, background="pink")
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label='Nuevo', command=nuevo)
filemenu.add_command(label='Abrir', command = abrir)
filemenu.add_command(label='Guardar', command=guardar)
filemenu.add_command(label='Guardar como', command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label='Salir', command = root.destroy)
menubar.add_cascade(label = 'Archivo', menu = filemenu)

texto = Text(root)
texto.pack(fill = 'both', expand = 1)
texto.config(font=('Arial', 18),
            padx=15,
            pady=15,
            selectbackground='#ff0080')

mensaje = StringVar()
mensaje.set("Bienvenido a tu bloc de notas")
monitor = Label(root, textvar = mensaje, justify= "center", background="pink")
monitor.pack(side = "left")

root.mainloop()
