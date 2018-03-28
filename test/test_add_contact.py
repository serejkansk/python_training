# -*- coding: utf-8 -*-
from model.contact import Contact
from sys import maxsize

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="svgasa", middlename="sagas", lastname="sbgasb", nickname="sah")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    def id_or_max(con):
        if con.id:
            return int(con.id)
        else:
            return maxsize
    assert sorted(old_contacts, key=id_or_max) == sorted(new_contacts, key=id_or_max)

#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname=""))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
