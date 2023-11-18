from flask import Flask, render_template, request, redirect, url_for

apphello = Flask(__name__)

@apphello.route("/")
def helloworld():
    return render_template("input_form.html")

@apphello.route("/contact")
@apphello.route("/contact/<name>")
def contact(name=None):
    return render_template("contact.html", name=name)

@apphello.route("/biodata")
def biodata():
    return render_template("biodata.html")

@apphello.route("/cv")
def cv():
    return render_template("cv.html")

@apphello.route("/porto")
def porto():
    return render_template("porto.html")

@apphello.route("/blog")
def blog():
    return render_template("blog.html")

@apphello.route("/article")
def article():
    return render_template("input_form.html")

@apphello.route("/fibonacci")
def fibonacci():
    return render_template("input_form.html")

@apphello.route("/blog_post/<int:post_id>")
def blog_post(post_id):
    return render_template("blog_post.html", post_id=post_id)

@apphello.route("/article_post/<int:post_id>")
def blog_post(post_id):
    return render_template("article_post.html", post_id=post_id)
