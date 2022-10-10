import tkinter as tk

window = tk.Tk()


def convert():
    tempVal = v.get()
    tempUnit = t.get()
    tConvUnit = vc.get()

    if tempUnit == "cel" and tConvUnit == "kel":
        newTemp = int(tempVal) + 273
        result.set(tempVal + " degree celsius = " + str(newTemp) + " degree Fahrenheit")


    print("Convert Successfully")
    
greeting = tk.Label(text="Convert your temperature")
greeting.pack()

t = tk.StringVar()
tEntry = tk.Entry(textvariable=t)
tEntry.pack()

v = tk.StringVar()
vEntry = tk.Entry(textvariable=v)
vEntry.pack()

vc = tk.StringVar()
vcEntry = tk.Entry(textvariable=vc)
vcEntry.pack()

result = tk.StringVar()
res = tk.Label(textvariable=result)
res.pack()

button = tk.Button(text="Convert", command=convert)
button.pack()

window.mainloop()
