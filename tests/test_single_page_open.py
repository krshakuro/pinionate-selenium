import pytest
from fixture.application import Application

def test_single_page_open_by_refresh(app):
    app.widget.open_widget()
    app.refresh()
    app.widget.is_single_page_presented()

def test_single_page_open_by_avatar(app):
    app.open_home_page()
    app.first_avatar_opening()
    app.widget.is_single_page_presented()
