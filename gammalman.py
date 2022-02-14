# Om mannen hittar dig (inte färdig)
import random
import time
spelare = 3

man = random.randint(1,9)
 
print (man)
def hittad():
    if man==spelare:
        while True:
            svar=int(input("mannen har hittat dig, vill du 1. gömma dig eller 2.springa till ett annat rum?"))
            if svar==1:
                print("du gömmer dig...")
                time.sleep(5)
                val=random.randint(1,2)
                if val==1:
                    print ("mannen hittar dig och tar hand om dig...")
                    quit #(?)
                    break
                elif val==2:
                    print("mannen hittar dig inte och går vidare till ett annat rum")
                    break
            if svar==2:
                print("du springer iväg...")
                time.sleep(5)
                val=random.randint(1,2)
                if val==1:
                    print ("mannen tar fast dig ändå...")
                    quit #(?)
                    break
                elif val==2:
                    print("mannen blir förvirrad och du lyckas springa iväg")
                    break

