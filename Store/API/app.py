from flask import Flask, jsonify


app = Flask(__name__)



products = [
    {
        "id": 1,
        "name": "G2 2024 World Jersey",
        "price": 109.95,
        "description": "LoL World Champion jersey",
        "image": "https://pbs.twimg.com/media/GYPTnnAXoAAqEnY.png"
    },
    {
        "id": 2,
        "name": "Gallery Dapt Hoodie",
        "price": 22.3,
        "description": "A powerful representation between athletic and elevated style, "
                       "this garment features an unorthodox take of our classic sweater. "
                       "Each hoodie has been appliquéd with our 'art on display' patch by the cuff.",
        "image": "https://gallerydept.com/cdn/shop/files/size-logo-hoodie---black---SLH-50011---size-L_Front_540x.jpg?v=1721149839"
    },
{
        "id": 3,
        "name": "Mens Casual Premium Slim Fit T-Shirts",
        "price": 22.3,
        "description": "Comfortable and stylish.",
        "image": "https://picsum.photos/id/201/300/300"
    },
{
        "id": 4,
        "name": "Mens Casual Premium Slim Fit T-Shirts",
        "price": 22.3,
        "description": "Comfortable and stylish.",
        "image": "https://picsum.photos/id/201/300/300"
    },
{
        "id": 5,
        "name": "Mens Casual Premium Slim Fit T-Shirts",
        "price": 22.3,
        "description": "Comfortable and stylish.",
        "image": "https://picsum.photos/id/201/300/300"
    },

]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    return jsonify(product) if product else ("Not Found", 404)

if __name__ == '__main__':
    app.run(debug=True)