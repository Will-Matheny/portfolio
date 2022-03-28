from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime 



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)



class Project(db.Model):
    id = db.Column("Id", db.Integer, primary_key=True)
    title = db.Column("Title", db.String())
    date = db.Column("Date", db.Date)
    description = db.Column("Description", db.Text)
    skills = db.Column("Skills", db.Text)
    url = db.Column('GitHub Repo Link', db.Text)

    
    
    def __repr__(self):
        return f'''Title: {self.title},
        Date: {self.date},
        Description: {self.description},
        Skills: {self.skills},
        Github Repo Link: {self.url}'''
    
    