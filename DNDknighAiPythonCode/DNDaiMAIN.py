import random
print("########################################")
print("#                 DND                  #")
print("#                Knight                #")
print("#                  AI                  #")
print("########################################")
print("")
print("###############################################")
dicegit = int(input("Insert Dice Num (1,20): "))
MNSTERHP = int(input("Insert Enemy health: "))
MNSTERAC = int(input("Insert Enemy AC: "))
MNSTERATK = int(input("Insert Enemy Attack score: "))
print("###############################################")
knighthp = 20
knightAC = 15
knightATK = 34
print("##################")
Knightdiceroll = int(input("Insert Knight dice Num: "))
print("##################")
########################################################
################### AI #################################
finalisedknighthp = Knightdiceroll + knighthp
finalisedknightAC = Knightdiceroll + knightAC
finalisedknightATK = Knightdiceroll + knightATK
########################################################
################# ENEMY ################################
finalisedEhp = dicegit + MNSTERHP
finalisedEAC = dicegit + MNSTERAC
finalisedEATK = dicegit + MNSTERATK
########################################################

