# Importar modulos

import PySimpleGUI as PyGui
import logging as log
import subprocess
import sys

# Configuración del logger

log.basicConfig(level = log.DEBUG,
                format = '%(asctime)s - %(levelname)s - %(message)s')


# Definición de funciones para la conversión de bases:
# Decimales a otras bases


def dec2bin ( val ) :
    return "{0:b}".format ( int ( val ) )


def dec2hex ( val ) :
    n = int ( val , 10 )
    hexadecimal = format ( n , 'x' )
    return hexadecimal.upper ( )


def dec2oct ( val ) :
    return "{0:o}".format ( int ( val ) )


# Binario a otras bases


def bin2dec ( val ) :
    return int ( val , 2 )


def bin2hex ( val ) :
    n = int ( val , 2 )
    hexadecimal = format ( n , 'x' )
    return hexadecimal.upper ( )


def bin2oct ( val ) :
    return "{0:o}".format ( int ( val , 2 ) )


# Hexadecimal a otras bases


def hex2dec ( val ) :
    return int ( val , 16 )


def hex2bin ( val ) :
    conversion = bin ( int ( val , 16 ) ).zfill ( 8 )
    return conversion


def hex2oct ( val ) :
    return "{0:o}".format ( int ( val , 16 ) )


# Octal a otras bases


def oct2dec ( val ) :
    return int ( val , 8 )


def oct2bin ( val ) :
    conversion: bin = bin ( int ( val , 8 ) ).zfill ( 8 )
    return conversion


def oct2hex ( val ) :
    n: int = int ( val , 8 )
    hexadecimal = format ( n , 'x' )
    return hexadecimal.upper ( )


# Salidas de la consola


def runCommand(cmd, timeout=None, window=None):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
        output += line
        print(line)
        window.Refresh() if window else None        # yes, a 1-line if, so shoot me
    retval = p.wait(timeout)
    return (retval, output)