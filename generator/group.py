# -*- coding: utf-8 -*-
from model.group import Group
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 1
f = "data/groups.json"

for o, a in opts:
    if o =="-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):#генератор случайных строк
    symbols = string.ascii_letters + string.digits + " "*10#символы, которые собираемся использовать в случайно сгенерированной строке
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])#выбираем символ из заданной стркои случайным образом (многократно), будет сгенерированна случайная длина не превышающая максимальную

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(n)#сгенерировали случайный обьект 5 раз и по итогу список
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)#определили путь к файлу

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))