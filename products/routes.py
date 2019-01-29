from flask_intro import app
from flask import render_template, request, redirect
from flask_intro.db import query

@app.route('/products', methods=['GET'])
def list_products():
    query_string = f"""
        select * from products;
    """
    result = query(query_string)
    return render_template('product_list.html', products=result)

@app.route('/products/new')
def new_product():
    return render_template('new_product.html')

@app.route('/products', methods=['POST'])
def create_product():
    name = request.form['name']
    price = request.form['price']
    query_string = f"""
        INSERT INTO products (
            name,
            price
        ) VALUES (
            "{name}", {price}
        );
    """ # Please don't do this irl... poor bobby tables
    print(query_string)
    insert_result = query(query_string)
    print(insert_result)
    return redirect('/products')
