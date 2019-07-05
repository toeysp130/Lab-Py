'''******************************************
6206021612059 Watcharakorn  Choptum
section C  IT
******************************************'''
Num = int( input( "Enter integer number : ") )
M1=Num%10       #Num คือ 5271 >> ค่า ที่Mod(หารเอาแต่เศษ) >> เก็บค่าที่ M1 มีค่าเท่ากับ 1
Num //= 10      #Num = 527
M2=Num%10       #Num = 527 Mod 10 จะได้ 52 และเก็บ 7 >> M2
Num //= 10      #Num = 52
M3=Num%10       #Num = 52 Mod 10 จะได้ 5  และเก็บ 2 >> M3
Num //= 10      #Num = 5
M4=Num%10       #Num = 5 Mod 10 จะได้ .5 และเก็บ 5 M4

print (int(M4))
print (int(M3))
print (int(M2))
print (int(M1))
