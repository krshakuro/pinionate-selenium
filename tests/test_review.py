import pytest
from fixture.application import Application

def test_review(app):
    app.widget.open_widget()
    app.widget.like_by_btn()
    app.widget.dislike_by_btn()
    app.widget.review_jumping()
    app.widget.open_negative_review()
    app.widget.open_positive_review()
    app.widget.review_jumping()