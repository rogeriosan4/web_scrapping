#[PARTE 1]
from flask import Flask, render_template
from web import get_filmes


#[PARTE 2]
app = Flask(__name__)

#[PARTE 3]
@app.route('/', methods=['GET'])
def filmes():
    filmes = get_filmes()
    return render_template('cards.html', filmes=filmes)

#[PARTE 4]
if __name__ == "__main__":
    app.run(debug=True)
