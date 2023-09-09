from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
@app.route('/<formula>')
def render_formula(formula=''):
    return render_template('equation_renderer.html', formula=formula)
