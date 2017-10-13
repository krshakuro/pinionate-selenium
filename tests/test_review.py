import pytest
from fixture.application import Application

def test_review(app):
    app.widget.open_widget()
    app.widget.init_widget()
    app.widget.like_by_btn()
    app.widget.dislike_by_btn()
    app.widget.review_jumping()
    assert app.widget.negative_votes_count() == 1
    assert app.widget.positive_votes_count() == 1
    app.widget.open_negative_review()
    assert app.widget.negative_votes_count() == 1
    app.widget.open_positive_review()
    assert app.widget.positive_votes_count() == 1
    app.widget.review_jumping()
    assert app.widget.thumbnails_count() == 3