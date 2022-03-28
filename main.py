from flask import (render_template, redirect, 
                    url_for, request)
from models import db, Project, app
from datetime import date, datetime 
import random



@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/about')
def about():
    projects = Project.query.all()
    return render_template('about.html', projects=projects)


@app.route('/project/new', methods=['GET', 'POST'])
def add_project():
    projects = Project.query.all()
    if request.form:
        capture = request.form['date']
        sql_happy = datetime.strptime(capture, '%Y-%m')
        new_project = Project(title=request.form['title'], date=sql_happy,
        description=request.form['description'], skills = request.form['skills'],               
        url = request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html', projects=projects)


@app.route('/project/<id>')
def projects_detail(id):
    projects = Project.query.all()
    project = Project.query.get(id)
    return render_template('detail.html', project=project, projects=projects)


@app.route('/project/edit/<id>', methods=['GET', 'POST'])
def edit_project(id):
    projects = Project.query.all()
    project = Project.query.get(id)
    if request.form:
        project.title = request.form['title']
        project.date = request.form['date']
        project.date = datetime.strptime(project.date, '%Y-%m')
        project.description = request.form['description']
        project.skills = request.form['skills']              
        url = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', project=project, projects=projects)


@app.route('/project/<id>/delete')
def delete_project(id):
    projects = Project.query.all()
    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404
    

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='0.0.0.0')