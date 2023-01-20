import time, os
elephant = ("                        ____",
"                   .---'-   \\",
"      .-----------/          \\",
"     /           (         ^  |   __",
"&   (             \        O  /  / .'",
"._/(              '-'  (.   (_.' /",
"     \                    \     ./",
"      |    |       |    |/ '._.'",
"       )   @).____\|  @ |",
"   .  /    /       (    | ",
"  \|, '_:::\  . ..  '_:::\ ..\)."

)
os.system('cls')
for j in range(1,15):
    os.system('cls')
    for i in elephant:
        print(" "*j*5 + i)
    time.sleep(0.5)

os.system('cls')
print(
"""
                                                                               /eeeeeeeeeee\ 
                                                                 /RRRRRRRRRR\ /eeeeeeeeeeeee\ /RRRRRRRRRR\ 
                                                                /RRRRRRRRRRRR\|eeeeeeeeeeeee|/RRRRRRRRRRRR\ 
                                                               /RRRRRRRRRRRRRR +++++++++++++ RRRRRRRRRRRRRR\ 
                                                              |RRRRRRRRRRRRRR ############### RRRRRRRRRRRRRR| 
                                                              |RRRRRRRRRRRRR ######### ####### RRRRRRRRRRRRR| 
                                                               \RRRRRRRRRRR ######### ######### RRRRRRRRRR/ 
                                                                 |RRRRRRRRR ########## ######## RRRRRRRR| 
                                                                |RRRRRRRRRR ################### RRRRRRRRR| 
                                                                             ######     ###### 
                                                                             #####       ##### 
                                                                             #nnn#       #nnn#


Art by Morfina and Susie Oviatt on asciiart.eu                                                                             
"""
)

input("Press any ENTER to exit.")
