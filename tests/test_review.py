import pytest
from fixture.application import Application

def test_stats(app):
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

def test_jumping_after_positive_vote(app):
    app.widget.open_widget()
    app.widget.init_widget()
    app.widget.like_by_btn()
    app.widget.review_jumping()
    app.widget.is_counter_presented()
    app.widget.is_back_button_presented()
    app.widget.review_jumping()
    app.widget.is_review_button_presented()
    assert app.widget.positive_votes_count() == 1

def test_jumping_after_negative_vote(app):
    app.widget.open_widget()
    app.widget.init_widget()
    app.widget.dislike_by_btn()
    app.widget.review_jumping()
    app.widget.is_counter_presented()
    app.widget.is_back_button_presented()
    app.widget.review_jumping()
    app.widget.is_review_button_presented()
    assert app.widget.negative_votes_count() == 1

def test_jumping_after_skipped_vote(app):
    app.widget.open_widget()
    app.widget.init_widget()
    app.widget.skip_by_btn()
    app.widget.review_jumping()
    app.widget.is_counter_presented()
    app.widget.is_back_button_presented()
    app.widget.review_jumping()
    app.widget.is_review_button_presented()
    assert app.widget.skipped_votes_count() == 1
