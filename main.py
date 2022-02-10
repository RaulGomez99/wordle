# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 21:08:24 2022

@author: Raul
"""
import palabras;

def crearPlantilla():
    objeto = [palabras.gerRandomWord() ,None, 0];
    tablero = [
            [[None, 0],[None, 0],[None, 0],[None, 0],[None, 0]],
            [[None, 0],[None, 0],[None, 0],[None, 0],[None, 0]],
            [[None, 0],[None, 0],[None, 0],[None, 0],[None, 0]],
            [[None, 0],[None, 0],[None, 0],[None, 0],[None, 0]],
            [[None, 0],[None, 0],[None, 0],[None, 0],[None, 0]],
            [[None, 0],[None, 0],[None, 0],[None, 0],[None, 0]]
        
        ];
    objeto[1] = tablero;
    return(objeto);

def suma(obj):
    acum = 0;
    for i in obj:
        acum += i[1];
    return acum;

def compruebaPartida(objeto):
    for i in objeto[1]:
        if(suma(i) == 10):
            print('GANASTE !!!!!!');
            return 1;
        if i[0][1] == 0:
            return 0;
    print('PERDISTE!!!!', objeto[0]);
    return -1;

def devuelveMarca(num):
    if num == -1:
        return ('|', '|');
    if num ==  1:
        return ('(', ')');
    if num ==  2:
        return ('*', '*');
    return('[',']')

def muestraMapa(tablero):
    for i in tablero:
        for j in i:
            marca = devuelveMarca(j[1]);
            if j[0] == None:
                letra = ' ';
            else:
                letra = j[0];
            print(marca[0] + ' ' + letra + ' ' + marca[1], end = '');
        print('');

def jugarJugada(palabra, objeto):
    if len(palabra) != 5:
        return -1;
    
    if not palabras.compruebaPalabra(palabra):
        return -1;
    
    for i in range(5):
        objeto[1][objeto[2]][i][0] = palabra[i];
        if palabra[i] == objeto[0][i]:
            objeto[1][objeto[2]][i][1] = 2;
        elif palabra[i] in objeto[0]:
            objeto[1][objeto[2]][i][1] = 1;
        else:
            objeto[1][objeto[2]][i][1] = -1;
    objeto[2] += 1;
    return 1;
    
    
    
    
def main():
    plantilla = crearPlantilla();
    while compruebaPartida(plantilla) == 0:
        jugada = -1;
        while jugada < 0:
            palabra = input('Escriba palabra:');
            jugada = jugarJugada(palabra, plantilla);
        muestraMapa(plantilla[1]);
    
main();