def get_count_char(str_):
    
    str_ = str_.lower()
    letters_dict = {}
    count_ = 0

    for sign in str_:
        if sign.isalpha():
            letters_dict[sign] = letters_dict.get(sign, count_) + 1

    return letters_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
