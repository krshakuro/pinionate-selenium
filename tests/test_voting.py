# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application

def test_voting(app):
    app.widget.open_widget()
    app.widget.init_widget()
    app.widget.close_channel_info()
    app.widget.like_by_btn()
    app.widget.dislike_by_btn()
    # assert app.widget.negative_votes_count() == 1
    # app.widget.skip_by_btn()
    # app.widget.like_by_swipe()
    # app.widget.dislike_by_swipe()
    # app.widget.skip_by_swipe()
