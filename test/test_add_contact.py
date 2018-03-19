# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
        app.session.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="svgasa", middlename="sagas", lastname="sbgasb", nickname="sah"))
        app.session.logout()


def test_add_empty_contact(app):
        app.session.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="", middlename="", lastname="", nickname=""))
        app.session.logout()
