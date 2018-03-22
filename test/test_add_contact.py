# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
        app.contact.create(Contact(firstname="svgasa", middlename="sagas", lastname="sbgasb", nickname="sah"))


def test_add_empty_contact(app):
        app.contact.create(Contact(firstname="", middlename="", lastname="", nickname=""))
