import json
import random
import string

preferences_list = ["sports","platform","Racing","role-playing","puzzle","misc","shooter","simulation"
    ,"action","fighting","adventure","strategy"]
specifications_list = [
    ["Intel Core i5-12400F", "500GB SSD NVMe", "Monitor Full HD (1920x1080) 27'", "16GB RAM"],
    ["AMD Ryzen 5 5600X", "1TB SSD NVMe", "Monitor Full HD (1920x1080) 24'", "16GB RAM"],
    ["Intel Core i7-13700K", "2TB SSD NVMe", "Monitor QHD (2560x1440) 32'", "32GB RAM"],
    ["AMD Ryzen 7 7800X", "500GB SSD NVMe + 2TB HDD", "Monitor 4K (3840x2160) 27'", "32GB RAM"],
    ["Intel Core i5-12500H", "512GB SSD NVMe", "Pantalla Full HD (1920x1080) 15'", "16GB RAM"],
    ["AMD Ryzen 5 6600H", "512GB SSD NVMe", "Pantalla Full HD (1920x1080) 17'", "16GB RAM"],
    ["Intel Core i7-13800H", "1TB SSD NVMe", "Pantalla QHD (2560x1440) 16'", "32GB RAM"],
    ["AMD Ryzen 7 7800H", "1TB SSD NVMe", "Pantalla 4K (3840x2160) 15'", "32GB RAM"],
    ["Intel Core i5-12400F", "256GB SSD NVMe", "Nvidia GeForce GTX 1650", "8GB RAM"],
    ["AMD Ryzen 5 5600X", "512GB SSD NVMe", "AMD Radeon RX 6500 XT", "16GB RAM"],
    ["Intel Core i7-13700K", "1TB SSD NVMe", "Nvidia GeForce RTX 3060 Ti", "16GB RAM"],
    ["AMD Ryzen 7 7800X", "2TB SSD NVMe", "Nvidia GeForce RTX 3070", "32GB RAM"],
    ["Intel Core i5-12500H", "512GB SSD NVMe", "Nvidia GeForce GTX 1650", "8GB RAM"],
    ["AMD Ryzen 5 6600H", "512GB SSD NVMe", "AMD Radeon RX 6600M", "16GB RAM"],
    ["Intel Core i7-13800H", "1TB SSD NVMe", "Nvidia GeForce RTX 3080", "32GB RAM"],
    ["AMD Ryzen 7 7800H", "2TB SSD NVMe", "AMD Radeon RX 6800M", "32GB RAM"],
    ["Intel Core i5-12400F", "256GB SSD NVMe", "Sin tarjeta grafica dedicada (uso de graficos integrados)", "4GB RAM"],
    ["AMD Ryzen 5 5600X", "512GB SSD NVMe", "Sin tarjeta grafica dedicada (uso de graficos integrados)", "8GB RAM"],
    ["Intel Core i7-13700K", "1TB SSD NVMe", "Sin tarjeta grafica dedicada (uso de graficos integrados)", "16GB RAM"],
    ["AMD Ryzen 7 7800X", "2TB SSD NVMe", "Sin tarjeta grafica dedicada (uso de graficos integrados)", "32GB RAM"]
]
names_list = ["Juan", "Yasser", "Adrian", "Fernando", "Frank", "Diego", "Camila",
              "Miguel", "Jose", "Alejandro", "Carlos", "David", "Eduardo", "Francisco", "Guillermo", "Hector",
              "Jesus", "Jorge", "Andrea", "Ariel", "Bruno", "Jaime", "Kevin", "Noah", "Sofia",
              "Valentina", "Valeria", "Zoe", "Ana", "Carmen", "Claudia", "Daniela", "Elena",
              "Isabel", "Laura", "Maria", "Mariana", "Sandra"]
surnames_list = ["Pescoran", "Renteria", "Valerio", "Gamio", "Sanchez", "Garcia", "Lopez",
                 "Martinez", "Fernandez", "Gonzalez", "Perez", "Rodriguez", "Sanchez", "Alonso",
                 "Ramirez", "Silva", "Diaz", "Flores", "Gomez", "Mendoza", "Ortiz", "Reyes",
                 "Vargas", "Vasquez", "Vera"]

def generate_user_id():
    characters = string.ascii_lowercase + string.digits
    user_id = ''.join(random.choice(characters) for i in range(12))
    return user_id

def generate_full_name(used_names):
    while True:
        name = random.choice(names_list) + " " + random.choice(surnames_list)
        full_name = name.strip()
        if full_name not in used_names:
            return full_name

def generate_users_json():
    data = []
    used_names = []
    used_ids = []
    used_friends = {}  # Initialize an empty dictionary to store user friend lists

    for _ in range(500):
        user_id = generate_user_id()
        while user_id in used_ids:
            user_id = generate_user_id()

        used_ids.append(user_id)

        full_name = generate_full_name(used_names)
        preferences = random.sample(preferences_list, k=random.randint(3, 5))
        specifications = random.choice(specifications_list)

        # Ensure at least one friend, even if there aren't enough potential friends
        possible_friends = [user for user in used_ids if user != user_id]
        num_possible_friends = len(possible_friends)
        friends = random.sample(possible_friends, k=min(num_possible_friends, 1))  # Guaranteed 1 friend

        # Optionally, add more friends up to a maximum of 2 (adjust max_additional_friends as needed)
        max_additional_friends = 2
        if num_possible_friends > 1:
            additional_friends = random.sample(possible_friends, k=min(num_possible_friends, max_additional_friends))
            friends.extend(additional_friends)

        # Update friends lists for bidirectional friendships (modified logic)
        for friend_id in friends:
            used_friends.setdefault(user_id, []).append(friend_id)
            used_friends.setdefault(friend_id, []).append(user_id)  # Add user_id as a friend to friend_id

        user_data = {
            "UserID": user_id,
            "Name": full_name,
            "Preferences": preferences,
            "Specifications": specifications,
            "Friends": friends
        }

        data.append(user_data)

    with open('../datasets/Users-Dataset.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)

if __name__ == "__main__":
    generate_users_json()