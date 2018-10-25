from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import current_user
from app import db
from app.email import send_email
from app.models import User, Club, Review
from app.club.forms import MakeClub, ReviewClub

club = Blueprint('club', __name__)

@club.route('/new-club', methods=['GET', 'POST'])
def new_club():
    # ill get  to this
    form = MakeClub()
    if form.validate_on_submit():
        c = Club(name=form.name.data)
        db.session.add(c)
        db.session.commit()
        flash('new club added', 'form-success')
    return render_template('club/new-club.html', form=form)

@club.route('/clubs', methods=['GET', 'POST'])
def clubs():
    clubs = Club.query.all()
    return render_template('club/clubs.html', clubs=clubs)

@club.route('/club/<int:id>', methods=['GET', 'POST'])
def get_club_info(id):
    club = Club.query.filter_by(id=id).first()
    return render_template('club/club_info.html', club=club)

@club.route('/club/<int:id>/add-review', methods=['GET', 'POST'])
def add_review(id):
    club = Club.query.filter_by(id=id).first()
    form = ReviewClub()
    if form.validate_on_submit():
        r = Review(good=form.good.data)
        r.author = current_user
        c = Club.query.filter_by(id=id).first()
        c.club_reviews.append(r)
        db.session.add(r)
        db.session.add(c)
        db.session.commit()
    return render_template('club/add_review.html', club=club, form=form)
