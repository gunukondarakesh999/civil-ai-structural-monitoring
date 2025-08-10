import csv 


import matplotlib.pyplot as plt
# crack_widths = [0.03,0.15,0.20,0.45,0.10]
limit = 0.3 


# for i ,crack in enumerate(crack_widths,1):
#     if crack > limit:
#         print("Crack "+str(i)+" : "+str(crack)+" - Exceed limit")
#     else:
#         print("Crack"+str(i)+" : "+str(crack)+" - Safe ")


crack_width =[0.15,0.22,0.20,0.35,0.4,0.60,0.11,0.65]

def classify_crack(width):
    if width <= 0.2:
        return " ✅ Safe"
    elif width <=0.3:
        return "⚠ Monitor"
    elif width <=0.5:
        return "🔧 Repair Needed" 
    else:
        return "🚨 Critical" 
    
results = []

for i , crack in enumerate(crack_width, 1):
    severity = classify_crack(crack)
    print(f"Crack {i}: {crack} mm- {severity}")
    results.append([i,crack,severity])

with open("crack_report.csv",mode="w",newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Crack ID", "Width (mm)", "Severity"])
    writer.writerows(results)

print("Report saved as crack_report.csv")


crack_ids = [r[0] for r in results]
widths = [r[1] for r in results]
colors = ["red" if w > limit else "green" for w in widths]

plt.bar(crack_ids, widths, color=colors)
plt.axhline(y=limit, color="orange", linestyle="--", label=f"Limit {limit} mm")
plt.xlabel("Crack ID")
plt.ylabel("Width (mm)")
plt.title("Crack Width Analysis")
plt.legend()
plt.show()