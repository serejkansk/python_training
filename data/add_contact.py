# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string

constant = [
    Contact(firstname="firstname1", lastname="lastname1"),
    Contact(firstname="firstname2", lastname="lastname2")
]


def random_string(prefix, maxlen):#генератор случайных строк
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10#символы, которые собираемся использовать в случайно сгенерированной строке
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])#выбираем символ из заданной стркои случайным образом (многократно), будет сгенерированна случайная длина не превышающая максимальную

testdata = [Contact(firstname="", middlename="", lastname="", nickname="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 15), lastname=random_string("lastname", 20),
            nickname=random_string("nickname", 10))
    for i in range(1)
    ]