from flask import Flask, request, render_template

from engine import Engine


app = Flask(__name__)

engine = Engine()

@app.route('/', methods=['GET'])
def index():
    if 'search' in request.args.keys():
        search = request.args['search']
        print(f"Você buscou por {search=}")
        results = engine.search(search)
        print(results)
        return render_template('index.html', results=results, termos=search)
    else:
        return render_template('index.html')

