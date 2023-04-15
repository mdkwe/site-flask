from flask import Flask, render_template

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']
# print(app.config['SQLALCHEMY_DATABASE_URI'])

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/result/')
def result():
        return render_template('result.html')

if __name__ == "__main__":
        app.run()


## Il est temps d'utiliser l'héritage. A noter qu'il y a des problèmes de couleurs