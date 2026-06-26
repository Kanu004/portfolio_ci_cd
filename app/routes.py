from flask import Blueprint, render_template

bp = Blueprint("main", __name__)

PORTFOLIO = {
    "name": "Kanika",
    "title": "Python Developer and AI/ML Analst",
    "email": "kanika@gmail.com",
    "github": "https://github.com/example",
    "linkedin": "https://linkedin.com/in/example",
    "bio": (
        "I build reliable web applications and automate delivery pipelines. "
        "Passionate about clean code, testing, and CI/CD best practices."
    ),
    "skills": [
        "Python",
        "Flask",
        "Docker",
        "GitHub Actions",
        "pytest",
        "HTML/CSS",
        "Linux",
        "AWS",
    ],
    "projects": [
        {
            "name": "Task Manager API",
            "description": (
                "RESTful API with Flask, SQLAlchemy, and JWT authentication."
            ),
            "tech": ["Python", "Flask", "PostgreSQL"],
            "url": "#",
        },
        {
            "name": "CI/CD Pipeline Demo",
            "description": (
                "Automated test, build, and deploy workflow using GitHub Actions."
            ),
            "tech": ["GitHub Actions", "Docker", "pytest"],
            "url": "#",
        },
        {
            "name": "Data Dashboard",
            "description": (
                "Interactive dashboard for visualizing metrics with Plotly and Flask."
            ),
            "tech": ["Python", "Plotly", "Flask"],
            "url": "#",
        },
    ],
}


@bp.route("/")
def index():
    return render_template("index.html", portfolio=PORTFOLIO)


@bp.route("/about")
def about():
    return render_template("about.html", portfolio=PORTFOLIO)


@bp.route("/projects")
def projects():
    return render_template("projects.html", portfolio=PORTFOLIO)


@bp.route("/health")
def health():
    return {"status": "ok"}, 200
