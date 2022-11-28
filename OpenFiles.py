from pprint import pprint
cook_book = {}
def ingredient_dish(ingredient):
    igredient_book = {}
    igredient_data = ingredient.split(" | ")
    igredient_book["ingredient_name"] = igredient_data[0]
    igredient_book["quantity"] = igredient_data[1]
    igredient_book["measure"] = igredient_data[2]
    return igredient_book


with open('recipes.txt',"r",encoding="utf-8") as recipes_file:
    recipe_dish = recipes_file.read().split("\n\n")
    for dish in recipe_dish:
        structure_dish = dish.split("\n")
        cook_book[structure_dish[0]] = []
        for ingredient in structure_dish[2:]:
            cook_book[structure_dish[0]].append(ingredient_dish(ingredient))
pprint(cook_book)

print("-"*150)

dishes = ['Омлет', 'Утка по-пекински', 'Запеченный картофель', 'Фахитос']
person_count = 3
def get_shop_list_by_dishes(dishes, person_count):
    total_ingredient = {}
    for dishes_name in dishes:
        dishes_list = cook_book[dishes_name]
        for dishes_item in dishes_list:
            if dishes_item["ingredient_name"] in total_ingredient:
                total_ingredient[dishes_item["ingredient_name"]]["quantity"] += int(dishes_item["quantity"]) * person_count
            else:
                total_ingredient[dishes_item["ingredient_name"]] = {"measure": dishes_item["measure"],"quantity": int(dishes_item["quantity"]) * person_count}
    pprint(total_ingredient)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

print("-"*150)

# file = {}
# file_data = []
# with open('1.txt',"r",encoding="utf-8") as file_1:
#     file_1_line = file_1.read().split("\n")
#     file_1_spisok = []
#     file_1_spisok.append("1.txt")
#     file_1_spisok.append(len(file_1_line))
#     for strange_1 in file_1_line:
#         file_1_spisok.append(strange_1+'\n')
#     file_data.append(file_1_spisok)
# with open('2.txt',"r",encoding="utf-8") as file_2:
#     file_2_line = file_2.read().split("\n")
#     file_2_spisok = []
#     file_2_spisok.append("2.txt")
#     file_2_spisok.append(len(file_2_line))
#     for strange_2 in file_2_line:
#         file_2_spisok.append(strange_2 + '\n')
#     file_data.append(file_2_spisok)
# with open('3.txt',"r",encoding="utf-8") as file_3:
#     file_3_line = file_3.read().split("\n")
#     file_3_spisok = []
#     file_3_spisok.append("3.txt")
#     file_3_spisok.append(len(file_3_line))
#     for strange_3 in file_3_line:
#         file_3_spisok.append(strange_3 + '\n')
#     file_data.append(file_3_spisok)
# file_data.sort(key=len)
# file_list = open('file_3.txt',"w",encoding="utf-8")
# for line_date in file_data:
#     for i in line_date:
#         file_list.write(str(i)+'\n')
# file_list.closed
# print("Объединенный файл file_3.txt создан")
file = ['1.txt','2.txt','3.txt']
list_file = {}
for file_name in file:
    text_file = open(file_name,"r",encoding="utf-8")
    lines = text_file.readlines()
    lines_dict = {}
    lines_dict[file_name] = lines
    list_file[len(lines)] = lines_dict
list_file = sorted(list_file.items(), key=lambda item: item[0])
file_list = open('file_3.txt',"w",encoding="utf-8")
for lens,name in list_file:
    for name_list, text in name.items():
        file_list.write(f'{name_list}\n{lens}\n{"".join(text)}\n\n')
file_list.closed
print("Объединенный файл file_3.txt создан")

