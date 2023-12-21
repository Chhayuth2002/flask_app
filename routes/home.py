from app import app, render_template, request, text


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')
