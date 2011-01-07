#!/usr/bin/python

number = "7316717653133062491922511967442657474235534919493496983520312774506\
32623957831801698480186947885184385861560789112949495459501737958331952853208\
80551112540698747158523863050715693290963295227443043557668966489504452445231\
61731856403098711121722383113622298934233803081353362766142828064444866452387\
49303589072962904915604407723907138105158593079608667017242712188399879790879\
22749219016997208880937766572733300105336788122023542180975125454059475224352\
58490771167055601360483958644670632441572215539753697817977846174064955149290\
86256932197846862248283972241375657056057490261407972968652414535100474821663\
70484403199890008895243450658541227588666881164271714799244429282308634656748\
13919123162824586178664583591245665294765456828489128831426076900422421902267\
10556263211111093705442175069416589604080719840385096245544436298123098787992\
72442849091888458015616609791913387549920052406368991256071760605886116467109\
40507754100225698315520005593572972571636269561882670428252483600823257530420\
752963450"

mul_max = int(number[0]) * int(number[1]) * int(number[2]) * \
          int(number[3]) * int(number[4])
tmp = mul_max

for i in range(5, len(number)):
    # Watch out, 0 leads to black hole and world destruction
    if(int(number[i - 5])):
        tmp /= int(number[i - 5])
    if(int(number[i])):
        tmp *= int(number[i])
    if(tmp > mul_max):
        mul_max = tmp

print(int(mul_max))
