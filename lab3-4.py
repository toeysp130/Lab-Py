#watcharakorn#
import math

fnum = float( input("Enter float number : "))

print ()
print ("Ceil number : ", math.ceil(fnum))
print ("Floor number : ", math.floor(fnum))
print ("Sqrt number : ",math.sqrt(fnum))
print ("Trune number : ",math.trunc(fnum))

num = math.trunc(fnum)
print("Decimal Angle : ",num)
print("Radian Angle : ",math.radians(num))
print("Sin : " ,math.sin(math.radians(num)))
print("Cos : " ,math.cos(math.radians(num)))
print("Tan : " ,math.tan(math.radians(num)))

