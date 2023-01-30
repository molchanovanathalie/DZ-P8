# Код Цезаря

ABC = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й',
       'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
       'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

def encrypt_ceasar(msg, shift):
    text = ''
    for i in msg:
        for j in ABC:
            if i == j:
                ind = ABC.index(j)
                if (ind + shift) < len(ABC) - 1:
                    text = text + ABC[ind+shift]
                else:
                    raz_indx = (ind+shift) - len(ABC)
                    text = text + ABC[raz_indx]

    return text

print (encrypt_ceasar('БАКТЕРИЯ',2))