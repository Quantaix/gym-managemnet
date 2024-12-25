from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def my_Func():
    return render_template('hi.html')

@app.route('/home')
def my_Function():
    return render_template('hi.html')

@app.route('/about')
def about():
    return render_template('aboutus.html')

@app.route('/member')
def contact():
    return render_template('membership.html')
if __name__ == '__main__':
    app.run(debug=True)