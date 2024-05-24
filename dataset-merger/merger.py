import json

def merge_datasets():

    with open('Users-Dataset.json', 'r') as f:
        users = json.load(f)

    with open('VideoGames-Dataset.json', 'r') as f:
        games = json.load(f)

    merged_data = []
    for user in users:
        user_data = {
            "Username": user["Name"],
            "UserID": user["UserID"],
            "Friends": user["Friends"],
            "Specifications": user["Specifications"],
            "Games": []
        }
        for preference in user["Preferences"]:
            for game in games:
                if "Genre" in game and preference.lower() == game["Genre"].lower():
                    user_data["Games"].append({"Name": game["Name"], "Genre": game["Genre"]})
                    break

        merged_data.append(user_data)

    with open('../datasets/User-Videogame-Dataset.json', 'w') as f:
        json.dump(merged_data, f, indent=4)

if __name__ == "__main__":
    merge_datasets()
