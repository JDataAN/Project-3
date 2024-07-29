from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///state_data.db'
db = SQLAlchemy(app)

class StateData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(50))
    activity_level = db.Column(db.String(50))
    activity_level_label = db.Column(db.String(50))
    weekend = db.Column(db.String(50))
    week = db.Column(db.Integer)
    season = db.Column(db.String(50))

# Create the database tables within the application context
with app.app_context():
    db.create_all()

@app.route('/api/state-data', methods=['GET'])
def get_flu_data():
    all_data = StateData.query.all()
    results = [
        {
            "state": data.state,
            "activity_level": data.activity_level,
            "activity_level_label": data.activity_level_label,
            "weekend": data.weekend,
            "week": data.week,
            "season": data.season
        } for data in all_data]

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
