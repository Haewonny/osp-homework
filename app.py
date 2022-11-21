from flask import Flask, render_template, request
from database import DBhandler
import sys

app = Flask(__name__)

DB = DBhandler()

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/register_review")
def reg_review():
    nickname = request.args.get("nickname")
    menu = request.args.get("menu")
    star = request.args.get("star")
    content = request.args.get("content")

    print(nickname, menu, star, content)
    return render_template("register_review.html")


@app.route("/register_reviewpost", methods=['POST'])
def reg_review_post():
    global idx
    data = request.form

    DB.insert_review(data['nickname'], data)

    print(data)
    return render_template("result_review.html", data=data)



@app.route("/register_reviewpost")
def reg_reviewpost():
    return render_template("result_review.html")


@app.route("/register_restaurant")
def reg_restaurant():
    name = request.args.get("name")
    cate = request.args.get("cate")
    park = request.args.get("park")
    addr = request.args.get("addr")
    tel = request.args.get("tel")
    price1 = request.args.get("price1")
    price2 = request.args.get("price2")
    time = request.args.get("time")
    site = request.args.get("site")
    print(name, cate, park, addr, tel, price1, price2, time, site)
    return render_template("register_restaurant.html")


@app.route("/register_menu", methods=['POST'])
def reg_menu():
    data = request.form
    print(data)
    return render_template("register_menu.html", data=data)



@app.route("/register_bestmenu", methods=['POST'])
def reg_best_menu():
    data = request.form
    print(data)
    return render_template("register_bestmenu.html", data=data)


@app.route("/submit_restaurant_post", methods=['POST'])
def reg_restaurant_submit_post():
    global idx
    image_file = request.files["file"]
    image_file.save("static/img/{}".format(image_file.filename))
    data=request.form
    return render_template("result.html", data=data)

@app.route("/submit_bestmenu_post", methods=['POST'])
def submit_bestmenu_post():
    data = request.form
    print(data)
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
