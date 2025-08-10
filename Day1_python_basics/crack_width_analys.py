crack_widths = [0.03,0.15,0.20,0.45,0.10]
limit = 0.3 


for i ,crack in enumerate(crack_widths,1):
    if crack > limit:
        print("Crack "+str(i)+" : "+str(crack)+" - Exceed limit")
    else:
        print("Crack"+str(i)+" : "+str(crack)+" - Safe ")