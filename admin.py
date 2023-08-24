# from flask import Flask,render_template
# app=Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('index.html')
# @app.route('/profile/<username>')
# def profile(username):
#     return render_template('profile.html',username=username,isActive=True)
#
# @app.route('/books')
# def book():
#     books=[
#            {'name':'HARRY POTTER','author':'J.K.ROWLING','cover':'https://i.pinimg.com/originals/55/80/cc/5580cc860bb34f93859136695f2c46fd.jpg'},
#            {'name':'CHARLOTTES WEB','author':'E.B.WHITE','cover':'https://interactive.wttw.com/sites/default/files/charlottes-web@2x.jpg'},
#            {'name':'PETER PAN','author':'J.M.BARRIE','cover':'https://cdn-2.cinemaparadiso.co.uk/070801043816_l.jpg'}
#         ]
#     return render_template('book.html',books=books)
# app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Your list of books (move it outside the route for global access)
books = [
    {'name': 'HARRY POTTER', 'author': 'J.K.ROWLING', 'cover': 'https://i.pinimg.com/originals/55/80/cc/5580cc860bb34f93859136695f2c46fd.jpg'},
    {'name': 'CHARLOTTES WEB', 'author': 'E.B.WHITE', 'cover': 'https://interactive.wttw.com/sites/default/files/charlottes-web@2x.jpg'},
    {'name': 'PETER PAN', 'author': 'J.M.BARRIE', 'cover': 'https://cdn-2.cinemaparadiso.co.uk/070801043816_l.jpg'}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username, isActive=True)

@app.route('/books')
def book():
    return render_template('book.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = {
            'name': request.form['name'],
            'author': request.form['author'],
            'cover': request.form['cover']
        }
        books.append(new_book)
        return redirect(url_for('book'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
