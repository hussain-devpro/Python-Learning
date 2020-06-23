# Flask applications follows Model Template View (MTV) architecture
# Model: Responsible for data processing, hidden from user
# Templates: Responsible for displaying data to the user (Through HTML). Jinja 2 templates are used for this component
# render_template will search the html files in templates directory. Jinja variables are used for dynamic html contents
# View: Responsible for controlling the flow of the program. Its determine the mapping from python function to URLs


from flask import Flask, render_template, abort, jsonify, request, redirect, url_for
from model import db, save_db
count = 0
app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        cards=db
    )


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index=len(db)-1)
    except IndexError:
        abort(404)


@app.route("/api/card/")  # API which return json objects instead of HTML, we can refer them as REST APIs
def api_card_list():
    return jsonify(db) # return db  # it is not allowed to serialize the list, So it doesn't work


@app.route("/api/card/<int:index>")
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)


# By default post method is not allowed
@app.route("/add_card", methods=["GET", "POST"])
def add_card():
    if request.method == "POST":
        # User has submitted the form
        card={'question': request.form['question'], 'answer': request.form['answer']}
        db.append(card)
        save_db()
        return redirect(url_for("card_view", index=len(db)-1))
    else:
        # User has not submitted the form instead requested the form by loading the URL (GET request)
        return render_template("add_card.html")


@app.route("/remove_card/<int:index>", methods=["GET", "POST"])
def remove_card(index):
    try:
        if request.method == "POST":
            # User has submitted the form
            del db[index]
            save_db()
            return redirect(url_for("welcome"))
        else:
            # User has not submitted the form instead requested the form by loading the URL (GET request)
            return render_template("remove_card.html", card=db[index])
    except IndexError:
        abort(404)
