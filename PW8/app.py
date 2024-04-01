from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/project1')
def project1():
    project_name = "Tower Defense"
    image = "images/project1"
    technologies = "Unity, C#"
    repository_link = "https://github.com/ShepelM1/Tower-Defense"
    return render_template('project.html', project_name=project_name, image=image, technologies=technologies, repository_link=repository_link)

@app.route('/project2')
def project2():
    project_name = "GitHub Portfolio"
    image = "images/project2"
    technologies = "SCSS, HTML, Ruby, Shell, JavaScript, GitHub"
    repository_link = "https://github.com/ShepelM1/ShepelM1.github.io"
    return render_template('project.html', project_name=project_name, image=image, technologies=technologies, repository_link=repository_link)

if __name__ == '__main__':
    app.run(debug=True)
