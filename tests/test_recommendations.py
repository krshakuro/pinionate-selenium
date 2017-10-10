# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application

def test_recommendations(app):
    app.widget.open_widget()
    app.refresh()
