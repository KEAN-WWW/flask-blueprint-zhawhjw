from flask import Flask

# initialize Flask service
app = Flask(__name__)
# register blueprint


if __name__ == "__main__":
    app.run(debug=True)

