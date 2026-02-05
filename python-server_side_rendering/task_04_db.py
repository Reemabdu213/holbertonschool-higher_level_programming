#!/usr/bin/env python3
"""Flask application to display data from JSON, CSV, or SQLite."""

import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render the items page with data from JSON file."""
    with open('items.json', 'r') as f:
        data = json.load(f)
    items_list = data.get('items', [])
    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    """Render products from JSON, CSV, or SQLite based on query parameter."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        with open('products.json', 'r') as f:
            products_list = json.load(f)
    elif source == 'csv':
        products_list = []
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products_list.append(row)
    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Products')
            rows = cursor.fetchall()
            products_list = [dict(row) for row in rows]
            conn.close()
        except sqlite3.Error as e:
            return render_template('product_display.html',
                                   error=str(e))
    else:
        return render_template('product_display.html',
                               error="Wrong source")

    if product_id:
        product_id = int(product_id)
        products_list = [p for p in products_list if p['id'] == product_id]
        if not products_list:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
