# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):#генератор случайных строк
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10#символы, которые собираемся использовать в случайно сгенерированной строке
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])#выбираем символ из заданной стркои случайным образом (многократно), будет сгенерированна случайная длина не превышающая максимальную

testdata = [Contact(firstname="", middlename="", lastname="", nickname="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 15), lastname=random_string("lastname", 20),
            nickname=random_string("nickname", 10))
    for i in range(1)
    ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)