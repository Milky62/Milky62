
def prosjek (a,b,c,d): 

    return (a+b+c+d)/4 
    

prvi=int(input("Unesite prvu ocjenu: ")) 

drugi=int(input("Unesite drugu ocjenu: ")) 

treci=int(input("Unesite trecu ocjenu: ")) 

cetvrti=int(input("Unesite cetvrtu ocjenu: ")) 


p=prosjek(prvi,drugi,treci,cetvrti) 

print("\nTvoj prosjek ocjene je ",p)
prosjek = [ "petica" , "5", "cetvorka", "4" , "trojka", "3"]
upit =input ( "\nUpiši prosjek: ")

if upit in prosjek:
    print ("\nMožeš živjeti pod mojim krovom")

else:
     print ("\nLetiš van iz moje kuće")
