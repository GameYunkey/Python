#------------------------------------------------#
#LEVEL 1 = 10 - LEVEL 25 = 100
## Werte einstellung für den Levelaufstieg
# Startwerte
L1 = 10  # Anzahl Liegestütze am ersten Tag
r = 0.10  # Wachstumsrate von 20%w
tage = 25  # Anzahl Tage
liegestuetzen = L1 * (1 + r) ** (tage - 1)
print(liegestuetzen)
#------------------------------------------------#

#------------------------------------------------#
#LEVEL 25 = 100 - LEVEL 50 = 325
## Werte einstellung für den Levelaufstieg
# Startwerte
L1 = 100  # Anzahl Liegestütze am ersten Tag
r = 0.05  # Wachstumsrate von 20%w
tage = 25  # Anzahl Tage

liegestuetzen = L1 * (1 + r) ** (tage - 1)
print(liegestuetzen)
#------------------------------------------------#
