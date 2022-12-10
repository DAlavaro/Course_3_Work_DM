from flask import Flask

#Импортируем блупринты
from main.views import main_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

#Регистрируем блупринты
app.register_blueprint(main_blueprint)

if __name__ == "__main__":
    app.run(host="localhost", port=10001, debug=True)