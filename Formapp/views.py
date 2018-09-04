from flask import render_template, Blueprint, redirect, url_for, flash, session
from flask.json import jsonify

from Formapp.forms import *


blue = Blueprint("blue",__name__)


@blue.route("/",methods=['GET','POST'])
def product_view():
    name = None
    productForm = ProductForm()
    if productForm.validate_on_submit():
        name = productForm.proname.data
        productForm.proname.data = ""
    return render_template("product.html",**locals())

@blue.route("/login",methods=['GET','POST'])
def login_view():
    logform = LoginForm()
    if logform.validate_on_submit():
        username = logform.data.get("username")
        password = logform.data.get("password")
        session["username"] = username
        if username == "tom" and password =="123456":
            return redirect(url_for("blue.success_view"))
        else:
            flash("用户名或密码不正确")
    return render_template('login.html',logform=logform)

@blue.route('/success')
def success_view():
    return render_template('success.html')


@blue.route("/things")
def things_view():
    return render_template("things.html")

@blue.route('/fruit')
def fruit():
    return jsonify({'name':['草莓','仙桃','西瓜']})
@blue.route('/sport')
def sport():
    return jsonify({'name':['篮球','足球','排球']})