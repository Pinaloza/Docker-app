
from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)
app.secret_key = "bakery-secret"

PRODUCTS = [
    {"id":1,"name":"Tiramisu","price":8.99},
    {"id":2,"name":"Lotus Biscoff","price":7.99},
    {"id":3,"name":"Belgian Waffle","price":5.99},
    {"id":4,"name":"Chocolate Waffle","price":6.49},
    {"id":5,"name":"Bread","price":2.99},
    {"id":6,"name":"Croissant","price":3.49},
    {"id":7,"name":"Baguette","price":2.49},
    {"id":8,"name":"Muffin","price":2.99},
    {"id":9,"name":"Donut","price":1.99},
    {"id":10,"name":"Cake","price":12.99},
]

@app.route("/")
def home():
    return render_template("index.html", products=PRODUCTS)

@app.route("/add/<int:pid>")
def add(pid):
    cart = session.get("cart", {})
    cart[str(pid)] = cart.get(str(pid), 0) + 1
    session["cart"] = cart
    return redirect(url_for("home"))

@app.route("/cart")
def cart():
    cart = session.get("cart", {})
    items = []
    total = 0
    for p in PRODUCTS:
        qty = cart.get(str(p["id"]), 0)
        if qty:
            subtotal = qty * p["price"]
            total += subtotal
            items.append((p, qty, subtotal))
    return render_template("cart.html", items=items, total=total)

@app.route("/checkout", methods=["GET","POST"])
def checkout():
    if request.method == "POST":
        session["cart"] = {}
        return render_template("success.html", name=request.form["name"])
    return render_template("checkout.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
