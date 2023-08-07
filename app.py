# create Server in Flask
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_behind_proxy import FlaskBehindProxy

from api import new_results, get_activity, get_key
from flask_sqlalchemy import SQLAlchemy


# create Flask app
app = Flask(__name__)
proxied = FlaskBehindProxy(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    
    if request.method == 'POST':
        activity_number = int(request.form.get('activity_number'))
        review_text = request.form.get('review_text')

        data_lst = session.get('data_lst', [])
        key = get_key(data_lst[activity_number - 1])
        review = Review(activity_id=key,review_text=review_text)

        #add info to database
        db.session.add(review)
        db.session.commit()

        flash(f'Review Submitted!', 'success')

        # redirect to the same page after form submission to prevent form resubmission on refresh
        return redirect(url_for('home'))


    elif request.method == 'GET':
        if 'data_lst' not in session or 'get_new_activities' in request.args:
            session['data_lst'] = new_results()

        data_lst = session.get('data_lst', [])
        activities = list()

        for i in range(len(data_lst)):
            activity = get_activity(data_lst[i])
            activities.append(activity)

        return render_template('index.html', activities=activities)


class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer)
    review_text = db.Column(db.String(255), nullable=False)


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.config['SECRET_KEY'] = '609612690866607ff931bb2c445e56e977d46b702a16a8dcd063f9ab699ed670'
    app.run(debug=True, host="0.0.0.0")
