from tkinter import *



def button_action():

    entry_text = int(eingabefeld.get())

    if variable.get() == "von Celsius nach Kelvin":
        entry_text = entry_text + 273.15
        Label(fenster, text=entry_text).place(x=200, y=210)
    elif variable.get() == "von Kelvin nach Celsius":
        entry_text = entry_text - 273.15
        Label(fenster, text=entry_text).place(x=200, y=210)
    else:
        print("Fehler")




fenster = Tk()

u = 100
v = 30
abstand = 30

fenster.geometry("450x300")
fenster.title("Temperatur Umwandler")

Label0 = Label(fenster, text = "******* TEMPERATUR UMWANDLER *******").place(x = u, y = v)
v = v + abstand
Label1 = Label(fenster, text = "1.) Gewünschte Umrechnung Auswählen").place(x = u, y = v)
v = v + abstand
Label2 = Label(fenster, text = "2.) Temperatur Eingeben").place(x = u, y = v)
v = v + abstand
Label3 = Label(fenster, text = "3.)Taste ''Umrechnen'' Drücken").place(x = u, y = v)
v = v + abstand


variable = StringVar(fenster)
variable.set("von Celsius nach Kelvin") # default value

dropDown = OptionMenu(fenster, variable, "von Celsius nach Kelvin", "von Kelvin nach Celsius")


dropDown.place(x = u, y = v)
v = v + abstand

eingabefeld = Entry(fenster)
eingabefeld.place(x = u, y = v)
Umrechnen_Button = Button(fenster, text = "Umrechnen", command = button_action).place(x = u * 3, y = v + 3)
v = v + abstand

Label_ausgabe = Label(fenster, text = "Ausgabe : ").place(x = u, y = v)
v = v + abstand

fenster.mainloop()
