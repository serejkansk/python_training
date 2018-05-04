
import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_emails_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

#def test_phones_on_contact_view_page(app):
#    contact_from_view_page = app.contact.get_contact_from_view_page(0)
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
#    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

def test_all_info_on_home_page(app, db):
    contacts_from_hp = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(map(merge_mail_like_on_home_page, map(merge_phones_like_on_home_page, db.get_full_contact_list())), key=Contact.id_or_max)
    assert contacts_from_hp == contacts_from_db
    for item in range(len(contacts_from_db)):
        assert clear(contacts_from_hp[item].all_mails_from_home_page) == clear(contacts_from_db[item].all_mails_from_home_page)
        assert clear(contacts_from_hp[item].all_phones_from_home_page) == clear(contacts_from_db[item].all_phones_from_home_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",#если в результате очистки возникли пустые строки, то они тоже фильтруются и то что осталось склеивается с помощью перевода строки
                            map(lambda  x: clear(x),# к оставшимся применяется очистка лишних символов
                                filter(lambda x: x is not None,#из него выкидываются все пустые
                                    [contact.homephone, contact.workphone, contact.mobilephone, contact.secondaryphone]))))#исходный список из 4 элементов

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda  x: clear(x),
                                filter(lambda x: x is not None,
                                    [contact.email, contact.email2, contact.email3]))))