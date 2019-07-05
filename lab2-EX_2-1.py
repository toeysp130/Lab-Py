'''******************************************
6206021612059 Watcharakorn  Choptum
section C  IT
******************************************'''
Cash = float( input("Enter number money withdraw : ") )

c1p = Cash//1000
c2p = Cash//500 - c1p*2
c3p = Cash//100 - c1p*10 - c2p*5

print ("Cash B1000 : ", c1p)
print ("Cash B500  : ", c2p)
print ("Cash B100  : ", c3p)

