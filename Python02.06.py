import argparse

def args_ok(wert):
    if not wert:
        print("Keine Angabe")
    for w in wert:
        if w=="lala":
            print("Choice 1 von ok")
        elif w=="hi":
            print("Choice 2 von ok")
        elif w=="lol":
            print("Choice 3 von ok")
        else:
            print("Keine Angabe")

def args_gut(wert):
    if not wert:
        print("Keine Angabe")
    for w in wert:
        if w=="böse":
            print("Choice 1 von gut")
        elif w=="nervös":
            print("Choice 2 von gut")
        elif w=="lustig":
            print("Choice 3 von gut")
        else:
            print("Keine Angabe")

def args_a(wert):
    if len(wert)==0:
        print("Keine Angabe")
    for w in wert:
        if int(w)==2:
            print("Choice 1 von a")
        elif int(w)==5:
            print("Choice 2 von a")
        elif int(w)==7:
            print("Choice 3 von a")
        else:
            print("Keine Angabe")

def quadrat(zahl):
    if zahl.isdigit():
        print(int(zahl)*int(zahl))

def quadrat2(zahl):
    print(zahl*zahl)

quadrat("12")

quadrat2(16)

""" ('ok',['lala'],['hi'],['lol']), ('gut',['böse'],['nervös'],['lustig']), ('1',['2'],['5'],['7'])"""
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-ok', required=True, nargs='*', default=[], choices=['lala', 'hi', 'lol'])
parser.add_argument('-gut', required=False, nargs='*', default=[], choices=['böse', 'nervös', 'lustig'])
parser.add_argument('-a', required=False, nargs='*', default="0", choices=['2', '5', '7'])
args = parser.parse_args()
args_ok(args.ok)
args_gut(args.gut)
args_a(args.a)
