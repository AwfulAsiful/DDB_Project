from flask import Flask,render_template,url_for
app=Flask(__name__)

@app.template_filter('static_url')
def static_url(filename):
    return url_for('static', filename=filename)

@app.route('/')
def test():
    return render_template('base.html')

@app.route('/products')
def product():
    return '<h2>WTF!!!</h2>'

@app.route('/login')
def login():
    return '<h2>Login!!!</h2>'



if(__name__)=='__main__':
    app.run(debug=True)
