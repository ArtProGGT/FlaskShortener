from flask.templating import render_template
from flask.helpers import url_for, redirect

from . import app, db
from .forms import URLForm
from .models import URLModel, get_short


@app.route("/", methods=["GET", "POST"])
def index():
    form = URLForm()

    if form.validate_on_submit():
        url = URLModel()
        url.original_url = form.original_url.data
        url.short_url = get_short()
        db.session.add(url)
        db.session.commit()

        return redirect(url_for("urls"))

    return render_template("index.html", form=form)


@app.route("/urls", methods=["GET"])
def urls():
    urls = URLModel.query.all()

    return render_template("urls.html", urls=urls[::-1])


@app.route("/<string:short_url>", methods=["GET"])
def url_redirect(short_url):
    all_urls = URLModel.query.all()
    url_id = None
    for short in all_urls:
        if short.short_url == short_url:
            url_id = short.url_id
    url = URLModel.query.get(url_id)

    if url:
        url.visits += 1
        db.session.add(url)
        db.session.commit()

        return redirect(url.original_url)
