from flask import Flask
from flask.templating import render_template
from flask_restful import Api
from resources.led import LED

app = Flask(__name__)
api = Api(app)


@app.get('/')
def index():
    return render_template("index")


if __name__ == '__main__':
    api.add_resource(LED, '/')
    app.run(debug=True)
