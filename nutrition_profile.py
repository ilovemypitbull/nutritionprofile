def percentage(part, whole):
  return round(100 * float(part)/float(whole), 2)

print ("What item are you measuring?")
item = input()

print("How many grams of protein are in your item?")
protein = float(input())

print("How many grams of carbs are in your item?")
carb = float(input())

print("How many grams of fat are in your item?")
fat = float(input())

protein_cals = protein * 4
carb_cals = carb * 4
fat_cals = fat * 9
total_cals = protein_cals + fat_cals + carb_cals

protein_cals_percentage = percentage(protein_cals, total_cals)
carb_cals_percentage = percentage(carb_cals, total_cals)
fat_cals_percentage = percentage(fat_cals, total_cals)


print("***Nutrition Profile for", item,"***")
print(protein_cals, "calories from protein")
print(carb_cals, "calories from carbs")
print(fat_cals, "calories from fat")
print(str(protein_cals_percentage) + "% protein",  str(carb_cals_percentage) + "% carbs", str(fat_cals_percentage) + "% fat")

