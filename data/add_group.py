# -*- coding: utf-8 -*-
from model.group import Group
import random
import string

constant = [
    Group(name="name1", header="header1", footer="fotter1"),
    Group(name="name2", header="header2", footer="fotter2")
]


def random_string(prefix, maxlen):#генератор случайных строк
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10#символы, которые собираемся использовать в случайно сгенерированной строке
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])#выбираем символ из заданной стркои случайным образом (многократно), будет сгенерированна случайная длина не превышающая максимальную

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(1)#сгенерировали случайный обьект 5 раз и по итогу список
]
