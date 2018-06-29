from flask import Flask, render_template
from extract_relations import do_search
from get_articles import ext_articles

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/c_search", methods=['POST', 'GET'])
def custom_search():
    result = do_search()
    return render_template("relations.html", result=result)


@app.route("/a_search", methods=['POST'])
def article_search():
    result = ext_articles()
    return render_template("relations.html", result=result)


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug='True')