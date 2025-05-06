from flask import Flask, render_template,request,redirect, url_for


app = Flask(__name__)

posts = [
    {
        'title': ' Post 1. We Help You Create Perfect Modern Design',
        'content': 'Post 1. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
        'date_created': '20.05.2025'
    },

    {
        'title': ' Post 2. We Help You Create Perfect Modern Design',
        'content': 'Post 2. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
        'date_created': '20.05.2025'
    },

]

@app.route('/')
def home():
    return render_template('index.html',posts=posts)

@app.route('/post')
def post_single():
    return render_template('post_single.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post_create')
def post_create():
    return render_template('post_create.html')

if __name__ == '__main__':
    app.run(debug=True)