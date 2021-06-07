print("Bitte gebe eine Zahl ein.")
x=input()

if x.isdigit():
    f=int(x)
    print("Deine Zahl war:"+x+".")
    print("Das Quadrat von "+x+" ist "+str(f*f)+".")
else:
    print("Error!")

