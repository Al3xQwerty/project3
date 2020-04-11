from flask import Flask
from posts.blueprint import posts

app = Flask(__name__)

app.register_blueprint(posts, uri_prefix='/blog')