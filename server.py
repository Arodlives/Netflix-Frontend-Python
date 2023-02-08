from flask_app import app
#  import your controllers here
from flask_app.controllers import routes

if __name__ == '__main__':
    app.run(debug=True)