# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application

def test_open_close_widget(app):
    app.widget.open_widget()
    app.widget.init_widget()
    app.widget.close_channel_info()
    app.widget.close_widget()

