Total = 0.0
Score = ""
Count = 1
while Score != "-1":
    Score = input(f"Enter score value #{Count} : ")
    if Score != "-1":
        Count += 1
        Total += float(Score)
Count -= 1
Avr = Total/Count
print()
print(f"Number of Score : {Count}")
print(f"Total Score Value : {Total}")
print(f"Average Score : {Avr}")
