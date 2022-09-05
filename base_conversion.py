# Importar todas las librerías necesarias para el ejercicio:
from Definiciones import *


# Building the Python program GUI for base conversion
PyGui.theme ( "DarkAmber" )
layout = [ [ PyGui.Text ( "Elija la base que desea convertir: " ) ,
             PyGui.Combo ( [ "Decimal" , "Hexadecimal" , "Binario", "Octal" ] , key = "input" ) ] ,
           [ PyGui.Text ( "Elija la base de salida: " ) ,
             PyGui.Combo ( [ "Decimal" , "Hexadecimal" , "Binario", "Octal" ] , key = "output" ) ] ,
           [ PyGui.Text ( "Digite el número: " ) ,
             PyGui.InputText ( do_not_clear = False , key = "sc" ) ] ,
           [ PyGui.Text ( "Resultado de la conversión:" ) , PyGui.Text ( key = "result" ) ] ,
           [ PyGui.Text ( "El número ingresado fue: " ) , PyGui.Text ( key = "#inp" ) ] ,
           [ PyGui.Button ( "Convertir" ) , PyGui.Button ( "Limpiar" ) , PyGui.Button ( "Cerrar" ) ] ,
           [ PyGui.Output ( size = ( 50 , 10 ) ) ] ]

# sc = Sin convertir

window = PyGui.Window ( "Programa de conversión de datos" , layout )

# Program execution:
while True :
    event , values = window.read ( )
    print ( values )
    if event == PyGui.WIN_CLOSED or event == "Cerrar" :
        break
    elif event == "Convertir" :
        if values [ "input" ] == "Decimal" :
            if values [ "output" ] == "Binario" :
                window [ "result" ].update ( dec2bin ( values [ "sc" ] ) )
                window [ "#inp" ].update ( values [ "sc" ] )
            if values [ "output" ] == "Hexadecimal" :
                window [ "result" ].update ( dec2hex ( values [ "sc" ] ) )
                window [ "#inp" ].update ( values [ "sc" ] )
            if values [ "output" ] == "Decimal" :
                window [ "result" ].update ( values [ "sc" ] )
                window [ "#inp" ].update ( values [ "sc" ] )
            if values [ "output" ] == "Octal" :
                window [ "result" ].update ( dec2oct ( values [ "sc" ] ) )
                window [ "#inp" ].update ( values [ "sc" ] )
        if values [ "input" ] == "Binario" :
            if values [ "output" ] == "Decimal" :
                window [ "result" ].update ( bin2dec ( values [ "sc" ] ) )
                window [ "#inp" ].update ( values [ "sc" ] )
            if values [ "output" ] == "Hexadecimal" :
                window [ "result" ].update ( bin2hex ( values [ "sc" ] ) )
                window [ "#inp" ].update ( values [ "sc" ] )
            if values [ "output" ] == "Binario" :
                window [ "result" ].update ( values [ "sc" ] )
                window [ "#inp" ].update ( values [ "sc" ] )
            if values [ "output" ] == "Octal" :
                window [ "result" ].update ( bin2oct ( values [ "sc" ] ) )
                window [ "#inp" ].update ( values [ "sc" ] )
        if values [ "input" ] == "Hexadecimal" :
            if values [ "output" ] == "Decimal" :
                window [ "result" ].update ( hex2dec ( values [ "sc" ] ) )
                window [ "#inp" ].update ( values [ "sc" ] )
            if values [ "output" ] == "Binario" :
                window [ "result" ].update ( hex2bin ( values [ "sc" ] ) )
                window [ "#inp" ].update ( values [ "sc" ] )
            if values [ "output" ] == "Hexadecimal" :
                window [ "result" ].update ( values [ "sc" ] )
                window [ "#inp" ].update ( values [ "sc" ] )
            if values [ "output" ] == "Octal" :
                window [ "result" ].update ( hex2oct ( values [ "sc" ] ) )
                window [ "#inp" ].update ( values [ "sc" ] )
        if values [ "input" ] == "Octal" :
            if values [ "output" ] == "Decimal" :
                window [ "result" ].update ( oct2dec ( values [ "sc" ] ) )
                window [ "#inp" ].update ( values [ "sc" ] )
            if values [ "output" ] == "Binario" :
                window [ "result" ].update ( oct2bin ( values [ "sc" ] ) )
                window [ "#inp" ].update ( values [ "sc" ] )
            if values [ "output" ] == "Hexadecimal" :
                window [ "result" ].update ( oct2hex ( values [ "sc" ] ) )
                window [ "#inp" ].update ( values [ "sc" ] )
            if values [ "output" ] == "Octal" :
                window [ "result" ].update ( values [ "sc" ] )
                window [ "#inp" ].update ( values [ "sc" ] )
    elif event == "Limpiar" :
        window [ "result" ].update ( "" )
        window [ "#inp" ].update ( "" )

window.close ( )
