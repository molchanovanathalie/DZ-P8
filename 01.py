def choose_coffee(preference_1, preference_2, preference_3):
    None_list = []
    if preference_1 == 'Эспрессо':
        if ingredients[0] >0:
            ingredients[0] = ingredients[0] - 1
            print (preference_1)
        else: None_list.append(preference_1)
    elif preference_1 == 'Капучино':
        if ingredients[0] > 0 and ingredients[1] > 2:
            ingredients[0] = ingredients[0] - 1
            ingredients[1] = ingredients[1] - 3
            print (preference_1)
        else: None_list.append(preference_1)
    elif preference_1 == 'Латте Маккиато':
        if ingredients[0] > 0 and ingredients[1] > 1 and ingredients[2] > 0:
            ingredients[0] = ingredients[0] - 1
            ingredients[1] = ingredients[1] - 2
            ingredients[2] = ingredients[2] - 1
            print (preference_1)
        else: None_list.append(preference_1)

    if preference_2 == 'Эспрессо':
        if ingredients[0] >0:
            ingredients[0] = ingredients[0] - 1
            print (preference_2)
        else: None_list.append(preference_2)
    elif preference_2 == 'Капучино':
        if ingredients[0] > 0 and ingredients[1] > 2:
            ingredients[0] = ingredients[0] - 1
            ingredients[1] = ingredients[1] - 3
            print (preference_2)
        else: None_list.append(preference_2)
    elif preference_2 == 'Латте Маккиато':
        if ingredients[0] > 0 and ingredients[1] > 1 and ingredients[2] > 0:
            ingredients[0] = ingredients[0] - 1
            ingredients[1] = ingredients[1] - 2
            ingredients[2] = ingredients[2] - 1
            print (preference_2)
    else: None_list.append(preference_2)


    if preference_3 == 'Эспрессо':
        if ingredients[0] >0:
            ingredients[0] = ingredients[0] - 1
            print (preference_3)
        else: None_list.append(preference_3)
    elif preference_3 == 'Капучино':
        if ingredients[0] > 0 and ingredients[1] > 2:
            ingredients[0] = ingredients[0] - 1
            ingredients[1] = ingredients[1] - 3
            print (preference_3)
        else: None_list.append(preference_3)
    elif preference_3 == 'Латте Маккиато':
        if ingredients[0] > 0 and ingredients[1] > 1 and ingredients[2] > 0:
            ingredients[0] = ingredients[0] - 1
            ingredients[1] = ingredients[1] - 2
            ingredients[2] = ingredients[2] - 1
            print (preference_3)
        else: None_list.append(preference_3)


    if None_list == []:
        return 'хорощего дня'
    else:
        return f'нет возможности предложить Вам {None_list}'


ingredients = [4, 2, 2]
print(choose_coffee('Латте Маккиато', 'Эспрессо', 'Капучино'  ))

# Эспрессо 1 кофе
# Капучино 1 кофе, 3 молока
# Маккиато 1 кофе, 2 молока, 1 зс