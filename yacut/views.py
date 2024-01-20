from flask import flash, redirect, render_template, url_for

from . import app, db
from .constants import LEN_CUSTOM_ID
from .forms import URLMapForm
from .models import URLMap
from random import choices as random_choices
from string import ascii_letters, digits

ALPHABET = ascii_letters + digits


def get_from_db(short_id: str):
    return URLMap.query.filter_by(short=short_id)


def get_unique_short_id(LEN_CUSROM_ID):
    return ''.join(random_choices(ALPHABET, k=LEN_CUSTOM_ID))


@app.route('/', methods=['GET', 'POST'])
def add_url_view():
    form = URLMapForm()
    if form.validate_on_submit():
        short_id = form.custom_id.data
        if not short_id:
            short_id = get_unique_short_id()
        if get_from_db(short_id).first():
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('index.html', form=form)
        url = URLMap(original=form.original_link.data, short=short_id)
        db.session.add(url)
        db.session.commit()
        return render_template(
            'index.html',
            form=form,
            short_link=url_for('url_view', short_id=url.short, _external=True),
        )
    return render_template('index.html', form=form)


@app.route('/<short_id>', methods=['GET'])
def url_view(short_id: str) -> str:
    url = get_from_db(short_id).first_or_404()
    return redirect(url.original)
