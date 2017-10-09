# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_voting(app):
    app.widget.open_widget()
    app.widget.init_widget()
    app.widget.close_channel_info()
    app.widget.like_by_btn()
    app.widget.dislike_by_btn()
    app.widget.like_by_swipe()
    app.widget.dislike_by_swipe()
    app.widget.close_widget()