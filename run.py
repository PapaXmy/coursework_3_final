from flask import Flask
from app.posts_comment.views import pc_blueprint
from app.api.views import api_blueprint



app = Flask(__name__)

app.register_blueprint(pc_blueprint)
app.register_blueprint(api_blueprint)
if __name__ == '__main__':
    app.run(debug=True, port=4775)


