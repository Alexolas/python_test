import os

print("Hallo, ich habe 5 Fragen an Sie. Sie können zwischen den Fragen wählen.")
punkte=0
while True:
    print("Geben Sie die Nummer der gewünschten Frage ein.")
    print("Geben Sie STOP ein, wenn Sie das Programm verlassen möchten.")
    nummer=input()
    if nummer.upper()=="STOP":
        print("Sie haben "+str(punkte)+" Punkt(e) erreicht.")
        os.system("pause")
        break
    elif nummer.isalpha() or int(nummer)>5 or int(nummer)<1:
        print("Es muss eine Nummer von 1 bis 5 sein!")
    elif nummer.lower=="ok":
        print("Sie haben noch einen Versuch! (Glaube ich...")
    else:
        if int(nummer)==1:
            print("Was ist 1+1?")
            print("A: 4\nB: 2\nC: 9")
            print("Gebe nun A, B oder C als Antwort ein.")
            buchstabe1=input()
            if buchstabe1=="A" or buchstabe1=="C":
                print("Falsch!")
            elif buchstabe1=="B":
                print("Richtig!")
                punkte+=1
            else:
                print("Benutzen Sie einen gültigen Buchstaben! Zur Strafe müssen Sie von vorne anfangen.")
                
        if int(nummer)==2:
            print("Wo steht der Eifelturm von Pisa?")
            print("A: in Pisa\nB: in Paris\nC: Hahahahahaha!!!")
            print("Gebe nun A, B oder C als Antwort ein.")
            buchstabe2=input()
            if buchstabe2=="A" or buchstabe2=="B":
                print("Falsch!")
            elif buchstabe2=="C":
                print("Richtig!")
                punkte+=1
            else:
                print("Benutzen Sie einen gültigen Buchstaben! Zur Strafe müssen Sie von vorne anfangen.")
                
        if int(nummer)==3:
            print("lst in diesem Satz etwas falsch geschrieben?")
            print("J: Ja"+"\n"+"N: Nein")
            print("Gebe nun J oder N als Antwort ein.")
            buchstabe3=input()
            if buchstabe3=="N":
                print("Falsch!")
            elif buchstabe3=="J":
                print("Richtig!")
                punkte+=1
            else:
                print("Benutzen Sie einen gültigen Buchstaben! Zur Strafe müssen Sie von vorne anfangen.")
                
        if int(nummer)==4:
            print("Welche Aussage ist falsch?")
            print("A:Keine"+"\n"+"B:Ich kann lesen"+"\n"+"C:Es gibt eine")
            print("Gebe nun A, B oder C als Antwort ein.")
            buchstabe4=input()
            if buchstabe4=="B" or buchstabe4=="C":
                print("Falsch!")
            elif buchstabe4=="A":
                print("Richtig!")
                punkte+=1
            else:
                print("Benutzen Sie einen gültigen Buchstaben! Zur Strafe müssen Sie von vorne anfangen.")
                
        if int(nummer)==5:
            print("Ein Würfel ist rund.")
            print("J: Ja"+"\n"+"N: Nein")
            print("Gebe nun J oder N als Antwort ein.")
            buchstabe5=input()
            if buchstabe5=="J":
                print("Falsch!")
            elif buchstabe5=="N":
                print("Richtig!")
                punkte+=1
            else:
                print("Benutzen Sie einen gültigen Buchstaben! Zur Strafe müssen Sie von vorne anfangen.")
                
                