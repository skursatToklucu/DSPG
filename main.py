from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

app = Flask(__name__)
app.json_encoder = LazyJSONEncoder

# SWAGGER BEGIN
swagger_template = dict(
    info={
        'title': LazyString(lambda: 'Drum Playground API document'),
        'version': LazyString(lambda: '0.1'),
        'description': LazyString(
            lambda: ''),
    },
    host=LazyString(lambda: request.host)
)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'DSPG',
            "route": '/dspg.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

swagger = Swagger(app, template=swagger_template,
                  config=swagger_config)


@swag_from("dspg.yml", methods=['GET'])
@app.route("/")
def hello_world():
    return "Hello World!!!"


# SWAGGER END

if __name__ == "__main__":
    app.run()
