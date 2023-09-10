from flaskr import app
from flask import render_template

#ホームページトップ
@app.route('/')
def blog_creation1():
    check = 1  # 変数を作成
    return render_template(
        'blog_creation1.html',
        check = 1
    )

#blog_creation2への移動
@app.route('/blog_creation2')
def blog_creation2():
    return render_template(
        'blog_creation2.html'
    )

#blog_creation3への移動
@app.route('/blog_creation3')
def blog_creation3():
    return render_template(
        'blog_creation3.html'
    )

#blog_creation4への移動
@app.route('/blog_creation4')
def blog_creation4():
    return render_template(
        'blog_creation4.html'
    )

#blog_creation5への移動
@app.route('/blog_creation5')
def blog_creation5():
    return render_template(
        'blog_creation5.html'
    )

#blog_creation6への移動
@app.route('/blog_creation6')
def blog_creation6():
    return render_template(
        'blog_creation6.html'
    )

#blog_creation7への移動
@app.route('/blog_creation7')
def blog_creation7():
    return render_template(
        'blog_creation7.html'
    )

#blog_creation8への移動
@app.route('/blog_creation8')
def blog_creation8():
    return render_template(
        'blog_creation8.html'
    )

#blog_creation9への移動
@app.route('/blog_creation9')
def blog_creation9():
    return render_template(
        'blog_creation9.html'
    )