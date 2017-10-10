# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application

def test_expand(app):
    app.widget.open_widget()
    app.widget.expand_by_btn()

def test_link_button(app):
    app.widget.open_widget()
    app.open_link_page()
    app.widget.click_link_button()

def test_buy_button(app):
    app.widget.open_widget()
    app.open_buy_page()
    app.widget.click_buy_button()

def test_info(app):
    app.widget.open_widget()
    app.open_info_page()
    app.widget.click_info_button()
    app.widget.click_info_button()
