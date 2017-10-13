# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application

def test_open_close_widget_by_btn(app):
    app.widget.open_widget()
    app.widget.init_widget()
    app.widget.close_channel_info()
    app.widget.close_widget_by_btn()
    app.widget.is_widget_closed()

def test_open_close_widget_by_clk(app):
    app.widget.open_widget()
    app.widget.close_widget_by_clk()
    app.widget.is_widget_closed()


