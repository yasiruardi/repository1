from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import db, ProjectActivity

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://sql6688615:sBWKBTHveq@sql6.freesqldatabase.com:3306/sql6688615'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/activities', methods=['POST', 'GET'])
def handle_activities():
    if request.method == 'POST':
        activity_data = request.json
        new_activity = ProjectActivity(name=activity_data['name'])
        db.session.add(new_activity)
        db.session.commit()
        return jsonify({'message': 'Activity added successfully'}), 200
    elif request.method == 'GET':
        activities = ProjectActivity.query.all()
        return jsonify([{'id': activity.id, 'name': activity.name} for activity in activities]), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
