# Filling Out the Team


while True:
    speed, weight, strength = map(float, input().split())

    if speed==weight==strength==0:
        break

    can_do = []
    if speed<=4.5 and weight>=150 and strength>=200:
        can_do.append("Wide Receiver")
    if speed<=6.0 and weight>=300 and strength>=500:
        can_do.append("Lineman")
    if speed<=5.0 and weight>=200 and strength>=300:
        can_do.append("Quarterback")
    
    if can_do:
        print(*can_do)
    else:
        print("No positions")
    
