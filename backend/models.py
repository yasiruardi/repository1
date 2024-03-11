from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ProjectActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f'<ProjectActivity {self.name}>'
