# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application

def test_recommendations(app):
    app.widget.open_widget()
    app.refresh()
    app.widget.is_recommended_channels_block_presented()