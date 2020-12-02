""" cute cat """


def cute_cat(num):
    """ cute cat """
    dict_cat = {}  # .setdefault("Garfield","Cat01")
    dict_fox = {}  # .setdefault("Fubuki","Fox01")
    for _ in range(num):
        name = input()[1:-1].split(" : ")
        # print(name)
        if "Cat" in name[1]:
            dict_cat.update({name[0][1:-1]: name[1][1:-1]})
        if "Fox" in name[1]:
            dict_fox.update({name[0][1:-1]: name[1][1:-1]})
    if "Cat01" not in dict_cat.values() and "Garfield" \
        not in dict_cat.keys() and "Garfield" not in dict_fox.keys():
        dict_cat.update({"Garfield": "Cat01"})
    if "Fox01" not in dict_fox.values() and "Fubuki" \
        not in dict_cat.keys() and "Fubuki" not in dict_fox.keys():
        dict_fox.update({"Fubuki": "Fox01"})
    lst_cat, lst_fox = list(dict_cat.items()), list(dict_fox.items())
    lst_cat.sort(key=lambda x: int((x[1])[3:]))
    lst_fox.sort(key=lambda x: int((x[1])[3:]))
    print("Cat :", len(lst_cat))
    print("Fox :", len(lst_fox))
    _ = [print(i[0], i[1], sep=" : ") for i in lst_cat]
    _ = [print(i[0], i[1], sep=" : ") for i in lst_fox]


    #print(lst_cat, lst_fox)
cute_cat(int(input()))
