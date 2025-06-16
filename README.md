🍕 Pizza Restaurant API
A RESTful API for managing restaurants, pizzas, and their associations using Flask, SQLAlchemy, and Flask-Migrate. This project follows the MVC architecture.

📁 Project Structure
markdown
Copy
Edit
pizza-api-challenge/
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── pizza.py
│   │   ├── restaurant.py
│   │   └── restaurant_pizza.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── pizza_controller.py
│   │   ├── restaurant_controller.py
│   │   └── restaurant_pizza_controller.py
├── migrations/
├── challenge-1-pizzas.postman_collection.json
└── README.md
🚀 Setup Instructions
1. Clone and Install Dependencies
bash
Copy
Edit
git clone https://github.com/your-username/pizza-api-challenge.git
cd pizza-api-challenge
python3 -m venv venv
source venv/bin/activate
pip install flask flask_sqlalchemy flask_migrate
2. Set Environment Variable
bash
Copy
Edit
export FLASK_APP=server/app.py
3. Database Setup
bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
4. Seed the Database
bash
Copy
Edit
python -m server.seed
📬 Routes Summary
🏪 Restaurants
GET /restaurants
Returns a list of all restaurants.

Response:

json
Copy
Edit
[
  {
    "id": 1,
    "name": "Mama's Pizza",
    "address": "123 Main St"
  }
]
GET /restaurants/<int:id>
Returns details of a single restaurant and its pizzas.

Response:

json
Copy
Edit
{
  "id": 1,
  "name": "Mama's Pizza",
  "address": "123 Main St",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Tomato, Mozzarella, Basil"
    }
  ]
}
If not found:

json
Copy
Edit
{
  "error": "Restaurant not found"
}
Status: 404 Not Found

DELETE /restaurants/<int:id>
Deletes a restaurant and all related restaurant_pizzas.

Response:
Status: 204 No Content

If not found:

json
Copy
Edit
{
  "error": "Restaurant not found"
}
Status: 404 Not Found

🍕 Pizzas
GET /pizzas
Returns a list of all pizzas.

Response:

json
Copy
Edit
[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Tomato, Mozzarella, Basil"
  }
]
🔗 RestaurantPizzas
POST /restaurant_pizzas
Creates a new restaurant-pizza association.

Request:

json
Copy
Edit
{
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 1
}
Success Response:

json
Copy
Edit
{
  "id": 4,
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 1,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Tomato, Mozzarella, Basil"
  },
  "restaurant": {
    "id": 1,
    "name": "Mama's Pizza",
    "address": "123 Main St"
  }
}
Validation Error:

json
Copy
Edit
{
  "errors": ["Price must be between 1 and 30"]
}
Status: 400 Bad Request

✅ Validation Rules
RestaurantPizza price must be an integer between 1 and 30.

If validation fails, return a 400 Bad Request with error messages.

🧪 Postman Usage
Open Postman

Click Import

Upload the file challenge-1-pizzas.postman_collection.json

Test all routes interactively.



