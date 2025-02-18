from flask import Flask
from application.bp.homepage import bp_homepage

# initialize Flask service
app = Flask(__name__)
# register blueprint
app.register_blueprint(bp_homepage)

if __name__ == "__main__":
    app.run(debug=True)

