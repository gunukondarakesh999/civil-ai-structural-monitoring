

materials ={
    "Cement": 500,
    "Sand":50 ,
    "Steel" :60
}

def estimation(cement_bags,sand_bags,steel_kg):
    return (cement_bags*materials["Cement"])+(sand_bags*materials["Sand"])+(cement_bags*materials["Steel"])

total =estimation(50,200,500)
print(f"Total Material Cost :{total}")