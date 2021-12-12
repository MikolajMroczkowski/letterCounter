def countLetters(text):
    litery = []
    wyniki = ""
    for obj in text:
        indexOfLitera = -1
        for obj2 in range(0,len(litery)):
            if(litery[obj2].letter==obj):
                indexOfLitera = obj2
        if indexOfLitera != -1:
            litery[indexOfLitera].number += 1
        else:
            litery.append(Litera(1,obj))
    print(litery)
    for x in litery:
        wyniki += x.letter+" "+str(x.number)+" \n"
    return wyniki

class Litera(object):
    def __init__(self, number,letter):
        self.number = number
        self.letter = letter