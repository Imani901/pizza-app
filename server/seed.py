from server.app import app
from server.config import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    print("🌱 Seeding database...")

    # Optional: clear tables
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    # Create pizzas
    pizza1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    pizza2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
    db.session.add_all([pizza1, pizza2])
    db.session.commit()

    # Create restaurants
    r1 = Restaurant(name="Mama's Pizza", address="123 Main St")
    r2 = Restaurant(name="Papa's Pizza", address="456 Elm St")
    db.session.add_all([r1, r2])
    db.session.commit()

    # Create join table entries
    rp1 = RestaurantPizza(price=10, pizza_id=pizza1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=12, pizza_id=pizza2.id, restaurant_id=r1.id)
    rp3 = RestaurantPizza(price=8, pizza_id=pizza2.id, restaurant_id=r2.id)
    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("✅ Done seeding!")
