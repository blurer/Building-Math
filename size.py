#!/usr/bin/env python3

print('Building Size Calculator')
type = input('shell (s) or dimensions (d): ')

if type == "d":
    L = input('Length: ')
    W = input('Width: ')
    F = input('Floors: ')
    Length = int(L)
    Width = int(W)
    Floor = int(L)
    print(Length * Width * Floor)
elif type == "s":
    S = input('Size: ')
    f = input('Floors: ')
    Size = int(S)
    Floor = int(f)
    print(Size * Floor)
else:
    print('Error.')

