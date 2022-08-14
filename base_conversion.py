#Importing all needed modules and libraries
import PySimpleGUI as pg

#Program definition of functions for conversion: 


def dec2bin(val):
    return "{0:b}".format(int(val)) #Funciona correctamente

def dec2hex(val):
    n=int(val, 10);
    hex = format(n,'x');
    return(hex.upper())

def bin2dec(val):
    return int(val, 2);

def hex2dec(val):
    return int(val, 16);

def bin2hex(val):
    n = int(val, 2)
    hex = format(n, 'x')
    return(hex.upper())

def hex2bin(val):
    conversion = bin(int(val, 16)).zfill(8)
    return(conversion)



#Building the Python program GUI for base_conversion
pg.theme("DarkAmber")
layout = [[pg.Text("Elija la base que desea convertir: "),
         pg.Combo(["Decimal", "Hexadecimal", "Binario"], key="input")],
         [pg.Text("Elija la base de salida: "),
         pg.Combo(["Decimal", "Hexadecimal", "Binario"], key="output")], 
         [pg.Text("Digite el número: "),
         pg.InputText(do_not_clear=False, key="sc")],
         [pg.Text("Resultado de la conversión:"), pg.Text(key="result")],
         [pg.Text("El número ingresado fue: "), pg.Text(key="#inp")],
         [pg.Button("Convertir"), pg.Button("Limpiar"), pg.Button("Cerrar")]]
#sc = Sin convertir
window = pg.Window("Demo", layout)

#Program execution:
while True: 
    event, values = window.read()
    print(values)
    if event == pg.WIN_CLOSED or event=="Cerrar":
        break
    elif event == "Convertir":
        if values["input"] == "Decimal":
            if values["output"] == "Binario":
                window["result"].update(dec2bin(values["sc"]));
                window["#inp"].update(values["sc"]);
            if values["output"] == "Hexadecimal":
                window["result"].update(dec2hex(values["sc"]));
                window["#inp"].update(values["sc"]);
            if values["output"] == "Decimal":
                window["result"].update(values["sc"]);
                window["#inp"].update(values["sc"]);
        if values["input"] == "Binario":
             if values["output"] == "Decimal":
                window["result"].update(bin2dec(values["sc"]));
                window["#inp"].update(values["sc"]);
             if values["output"] == "Hexadecimal":
                window["result"].update(bin2hex(values["sc"]));
                window["#inp"].update(values["sc"]);
             if values["output"] == "Binario":
                window["result"].update(values["sc"]);
                window["#inp"].update(values["sc"]);
        if values["input"] == "Hexadecimal":
             if values["output"] == "Decimal":
                window["result"].update(hex2dec(values["sc"]));
                window["#inp"].update(values["sc"]);
             if values["output"] == "Binario":
                window["result"].update(hex2bin(values["sc"]));
                window["#inp"].update(values["sc"]);
             if values["output"] == "Hexadecimal":
                window["result"].update(values["sc"]);
                window["#inp"].update(values["sc"]);
    elif event == "Limpiar":
        window["result"].update("")
        window["#inp"].update("")

window.close()

