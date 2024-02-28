from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "MY_FL@sk_App_Here"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
    app.config['UPLOAD_FOLDER'] = 'uploads'

    @app.route("/hello")
    def hello():
        return "hellow world"
    
    return app