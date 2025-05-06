import pandas as pd
import numpy as np
import random
from datetime import datetime

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Create lists of player nationalities, positions, and team names
nationalities = [
    "England", "France", "Spain", "Portugal", "Brazil", "Argentina", "Germany", 
    "Italy", "Netherlands", "Belgium", "Nigeria", "Ghana", "Senegal", "Ivory Coast", 
    "South Korea", "Japan", "United States", "Mexico", "Colombia", "Uruguay", 
    "Scotland", "Wales", "Denmark", "Sweden", "Norway", "Finland", "Austria", 
    "Switzerland", "Croatia", "Serbia", "Poland", "Ukraine", "Turkey", "Algeria", 
    "Morocco", "Egypt", "Cameroon", "Mali", "DR Congo", "South Africa", "Australia", 
    "New Zealand", "Canada", "Jamaica", "Republic of Ireland", "Northern Ireland"
]

positions = ["Goalkeeper", "Defender", "Midfielder", "Forward"]
position_weights = [0.1, 0.35, 0.35, 0.2]  # Approximate distribution in a team

team_names = [
    "Manchester City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham Hotspur",
    "Chelsea", "Newcastle United", "Manchester United", "West Ham United", "Crystal Palace",
    "Brighton & Hove Albion", "AFC Bournemouth", "Fulham", "Wolverhampton Wanderers", 
    "Everton", "Brentford", "Nottingham Forest", "Luton Town", "Burnley", "Sheffield United"
]

# Player name generation
first_names = [
    "James", "Jack", "Harry", "Oliver", "George", "Noah", "Charlie", "Thomas", "Oscar", "William",
    "Leo", "Alfie", "Henry", "Archie", "Joshua", "Freddie", "Ethan", "Isaac", "Lucas", "Jacob",
    "Mohammed", "Adam", "Daniel", "Samuel", "Joseph", "David", "Alexander", "Edward", "John", "Ryan",
    "Mason", "Dylan", "Sean", "Christian", "Cameron", "Kyle", "Aaron", "Jamie", "Matthew", "Benjamin",
    "Nathan", "Jake", "Luke", "Callum", "Jordan", "Lewis", "Alex", "Max", "Patrick", "Tyler",
    "Ibrahim", "Abdul", "Ali", "Mohammed", "Ahmed", "Omar", "Hassan", "Yusuf", "Karim", "Bilal",
    "Juan", "Carlos", "José", "Miguel", "Antonio", "Francisco", "Manuel", "Javier", "Alejandro", "David",
    "Pierre", "Jean", "Louis", "Nicolas", "Julien", "Paul", "Antoine", "Thomas", "Mathieu", "Alexandre",
    "Hans", "Klaus", "Lukas", "Felix", "Jonas", "Niklas", "Jan", "Tim", "Florian", "Maximilian",
    "Giovanni", "Marco", "Alessandro", "Francesco", "Lorenzo", "Andrea", "Luca", "Matteo", "Simone", "Roberto"
]

last_names = [
    "Smith", "Jones", "Williams", "Taylor", "Brown", "Davies", "Evans", "Wilson", "Thomas", "Johnson",
    "Roberts", "Robinson", "Thompson", "Wright", "Walker", "White", "Edwards", "Hughes", "Green", "Hall",
    "Lewis", "Harris", "Clarke", "Patel", "Jackson", "Wood", "Turner", "Martin", "Cooper", "Hill",
    "Moore", "Ward", "Watson", "Anderson", "Harrison", "King", "Campbell", "Young", "Mitchell", "Baker",
    "James", "Kelly", "Allen", "Bell", "Phillips", "Lee", "Adams", "Morris", "Scott", "Cook",
    "Silva", "Santos", "Oliveira", "Pereira", "Costa", "Fernandes", "Rodrigues", "Martins", "Sousa", "Alves",
    "Garcia", "Rodriguez", "Hernandez", "Martinez", "Lopez", "Gonzalez", "Perez", "Sanchez", "Gomez", "Diaz",
    "Muller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Hoffmann", "Schulz",
    "Rossi", "Ferrari", "Esposito", "Bianchi", "Romano", "Colombo", "Ricci", "Marino", "Greco", "Bruno",
    "Dubois", "Bernard", "Thomas", "Robert", "Richard", "Petit", "Durand", "Leroy", "Moreau", "Simon"
]

# Function to create a realistic player dataset
def generate_player_data(num_players=542):
    # Known players from the 2023/2024 EPL season
    existing_players = [
        # Top Goalscorers and Key Players
        {"player_id": 1, "team_name": "Manchester City", "player_name": "Erling Haaland", "nationality": "Norway", "position": "Forward", "age": 23, "matches_played": 31, "matches_started": 30, "minutes_played": 2595, "goals": 27, "assists": 5, "shots": 125, "shots_on_target": 55, "passes_completed": 550, "pass_accuracy": 78.6, "tackles": 15, "interceptions": 5, "fouls_committed": 18, "fouls_suffered": 35, "yellow_cards": 2, "red_cards": 0, "games_suspended": 0},
        {"player_id": 2, "team_name": "Arsenal", "player_name": "Bukayo Saka", "nationality": "England", "position": "Forward", "age": 22, "matches_played": 38, "matches_started": 38, "minutes_played": 3178, "goals": 16, "assists": 11, "shots": 98, "shots_on_target": 40, "passes_completed": 1250, "pass_accuracy": 81.2, "tackles": 35, "interceptions": 18, "fouls_committed": 25, "fouls_suffered": 50, "yellow_cards": 4, "red_cards": 0, "games_suspended": 0},
        {"player_id": 3, "team_name": "Liverpool", "player_name": "Mohamed Salah", "nationality": "Egypt", "position": "Forward", "age": 31, "matches_played": 32, "matches_started": 30, "minutes_played": 2601, "goals": 18, "assists": 9, "shots": 105, "shots_on_target": 45, "passes_completed": 950, "pass_accuracy": 80.5, "tackles": 18, "interceptions": 10, "fouls_committed": 15, "fouls_suffered": 28, "yellow_cards": 1, "red_cards": 0, "games_suspended": 0},
        {"player_id": 4, "team_name": "Aston Villa", "player_name": "Ollie Watkins", "nationality": "England", "position": "Forward", "age": 28, "matches_played": 37, "matches_started": 37, "minutes_played": 3153, "goals": 19, "assists": 13, "shots": 90, "shots_on_target": 40, "passes_completed": 800, "pass_accuracy": 75.0, "tackles": 20, "interceptions": 12, "fouls_committed": 30, "fouls_suffered": 45, "yellow_cards": 6, "red_cards": 0, "games_suspended": 0},
        {"player_id": 5, "team_name": "Manchester City", "player_name": "Phil Foden", "nationality": "England", "position": "Midfielder", "age": 23, "matches_played": 35, "matches_started": 32, "minutes_played": 2730, "goals": 19, "assists": 8, "shots": 90, "shots_on_target": 40, "passes_completed": 1100, "pass_accuracy": 85.0, "tackles": 30, "interceptions": 18, "fouls_committed": 18, "fouls_suffered": 45, "yellow_cards": 2, "red_cards": 0, "games_suspended": 0},
        {"player_id": 6, "team_name": "Chelsea", "player_name": "Cole Palmer", "nationality": "England", "position": "Midfielder", "age": 21, "matches_played": 34, "matches_started": 31, "minutes_played": 2733, "goals": 16, "assists": 9, "shots": 78, "shots_on_target": 38, "passes_completed": 1100, "pass_accuracy": 84.5, "tackles": 22, "interceptions": 15, "fouls_committed": 18, "fouls_suffered": 40, "yellow_cards": 3, "red_cards": 0, "games_suspended": 0},
        {"player_id": 7, "team_name": "Newcastle United", "player_name": "Alexander Isak", "nationality": "Sweden", "position": "Forward", "age": 30, "matches_played": 30, "matches_started": 27, "minutes_played": 2357, "goals": 21, "assists": 2, "shots": 80, "shots_on_target": 38, "passes_completed": 650, "pass_accuracy": 79.2, "tackles": 10, "interceptions": 6, "fouls_committed": 12, "fouls_suffered": 25, "yellow_cards": 1, "red_cards": 0, "games_suspended": 0},
        {"player_id": 8, "team_name": "Manchester United", "player_name": "Bruno Fernandes", "nationality": "Portugal", "position": "Midfielder", "age": 29, "matches_played": 35, "matches_started": 34, "minutes_played": 2970, "goals": 10, "assists": 8, "shots": 95, "shots_on_target": 30, "passes_completed": 1050, "pass_accuracy": 81.9, "tackles": 40, "interceptions": 20, "fouls_committed": 55, "fouls_suffered": 48, "yellow_cards": 11, "red_cards": 0, "games_suspended": 1},
        
        # Players with disciplinary records (most cards, fouls)
        {"player_id": 9, "team_name": "Chelsea", "player_name": "Conor Gallagher", "nationality": "England", "position": "Midfielder", "age": 24, "matches_played": 37, "matches_started": 34, "minutes_played": 3020, "goals": 5, "assists": 5, "shots": 55, "shots_on_target": 18, "passes_completed": 1500, "pass_accuracy": 85.0, "tackles": 85, "interceptions": 55, "fouls_committed": 83, "fouls_suffered": 70, "yellow_cards": 12, "red_cards": 1, "games_suspended": 1},
        {"player_id": 10, "team_name": "Fulham", "player_name": "João Palhinha", "nationality": "Portugal", "position": "Midfielder", "age": 28, "matches_played": 35, "matches_started": 33, "minutes_played": 2879, "goals": 4, "assists": 1, "shots": 50, "shots_on_target": 15, "passes_completed": 900, "pass_accuracy": 80.1, "tackles": 95, "interceptions": 70, "fouls_committed": 65, "fouls_suffered": 30, "yellow_cards": 13, "red_cards": 1, "games_suspended": 2},
        {"player_id": 11, "team_name": "AFC Bournemouth", "player_name": "Marcos Senesi", "nationality": "Argentina", "position": "Defender", "age": 26, "matches_played": 37, "matches_started": 37, "minutes_played": 3330, "goals": 1, "assists": 1, "shots": 20, "shots_on_target": 5, "passes_completed": 1200, "pass_accuracy": 84.0, "tackles": 85, "interceptions": 60, "fouls_committed": 52, "fouls_suffered": 30, "yellow_cards": 13, "red_cards": 0, "games_suspended": 1},
        {"player_id": 12, "team_name": "Tottenham Hotspur", "player_name": "Yves Bissouma", "nationality": "Mali", "position": "Midfielder", "age": 27, "matches_played": 33, "matches_started": 30, "minutes_played": 2580, "goals": 2, "assists": 3, "shots": 35, "shots_on_target": 10, "passes_completed": 1500, "pass_accuracy": 86.0, "tackles": 95, "interceptions": 70, "fouls_committed": 65, "fouls_suffered": 50, "yellow_cards": 11, "red_cards": 2, "games_suspended": 4},
        {"player_id": 13, "team_name": "Sheffield United", "player_name": "Oliver McBurnie", "nationality": "Scotland", "position": "Forward", "age": 27, "matches_played": 34, "matches_started": 31, "minutes_played": 2600, "goals": 6, "assists": 3, "shots": 70, "shots_on_target": 25, "passes_completed": 550, "pass_accuracy": 72.0, "tackles": 40, "interceptions": 25, "fouls_committed": 55, "fouls_suffered": 40, "yellow_cards": 9, "red_cards": 2, "games_suspended": 3},
        {"player_id": 14, "team_name": "Chelsea", "player_name": "Reece James", "nationality": "England", "position": "Defender", "age": 24, "matches_played": 15, "matches_started": 12, "minutes_played": 1080, "goals": 0, "assists": 2, "shots": 15, "shots_on_target": 4, "passes_completed": 650, "pass_accuracy": 82.0, "tackles": 45, "interceptions": 25, "fouls_committed": 18, "fouls_suffered": 20, "yellow_cards": 3, "red_cards": 2, "games_suspended": 4},
        
        # Nigerian Players
        {"player_id": 15, "team_name": "Nottingham Forest", "player_name": "Taiwo Awoniyi", "nationality": "Nigeria", "position": "Forward", "age": 26, "matches_played": 20, "matches_started": 12, "minutes_played": 1150, "goals": 6, "assists": 3, "shots": 22, "shots_on_target": 11, "passes_completed": 172, "pass_accuracy": 74.0, "tackles": 9, "interceptions": 1, "fouls_committed": 9, "fouls_suffered": 13, "yellow_cards": 2, "red_cards": 0, "games_suspended": 0},
        {"player_id": 16, "team_name": "Nottingham Forest", "player_name": "Ola Aina", "nationality": "Nigeria", "position": "Defender", "age": 27, "matches_played": 22, "matches_started": 20, "minutes_played": 1820, "goals": 1, "assists": 1, "shots": 8, "shots_on_target": 3, "passes_completed": 634, "pass_accuracy": 81.0, "tackles": 47, "interceptions": 18, "fouls_committed": 18, "fouls_suffered": 2, "yellow_cards": 3, "red_cards": 0, "games_suspended": 0},
        {"player_id": 17, "team_name": "Fulham", "player_name": "Calvin Bassey", "nationality": "Nigeria", "position": "Defender", "age": 24, "matches_played": 29, "matches_started": 25, "minutes_played": 2250, "goals": 1, "assists": 0, "shots": 5, "shots_on_target": 2, "passes_completed": 1667, "pass_accuracy": 85.0, "tackles": 49, "interceptions": 28, "fouls_committed": 15, "fouls_suffered": 2, "yellow_cards": 4, "red_cards": 1, "games_suspended": 1},
        {"player_id": 18, "team_name": "Brentford", "player_name": "Frank Onyeka", "nationality": "Nigeria", "position": "Midfielder", "age": 26, "matches_played": 26, "matches_started": 11, "minutes_played": 1050, "goals": 1, "assists": 2, "shots": 22, "shots_on_target": 9, "passes_completed": 375, "pass_accuracy": 78.0, "tackles": 37, "interceptions": 23, "fouls_committed": 24, "fouls_suffered": 4, "yellow_cards": 8, "red_cards": 0, "games_suspended": 1},
        {"player_id": 19, "team_name": "Fulham", "player_name": "Alex Iwobi", "nationality": "Nigeria", "position": "Midfielder", "age": 28, "matches_played": 32, "matches_started": 27, "minutes_played": 2420, "goals": 5, "assists": 2, "shots": 55, "shots_on_target": 20, "passes_completed": 1012, "pass_accuracy": 82.0, "tackles": 31, "interceptions": 15, "fouls_committed": 12, "fouls_suffered": 8, "yellow_cards": 2, "red_cards": 0, "games_suspended": 0},
    ]
    
    # Generate data for remaining players to reach the desired number
    data = []
    
    # Add existing players
    for i, player in enumerate(existing_players, 1):
        player["player_id"] = i
        data.append(player)
    
    # Generate remaining players
    for i in range(len(existing_players) + 1, num_players + 1):
        # 80% English for lower-profile players, 20% international
        nationality_choice = random.choices(
            [random.choice(nationalities), "England"], 
            weights=[0.6, 0.4], 
            k=1
        )[0]
        
        position = random.choices(positions, weights=position_weights, k=1)[0]
        team_name = random.choice(team_names)
        
        # Generate player name
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        player_name = f"{first_name} {last_name}"
        
        # Basic player info
        age = random.randint(18, 38)
        
        # Generate sensible match stats
        matches_played = random.randint(1, 38)
        matches_started = random.randint(0, matches_played)
        minutes_played = int(matches_started * 90 * random.uniform(0.7, 1.0) + 
                          (matches_played - matches_started) * random.uniform(5, 30))
        
        # Performance metrics based on position and minutes played
        if position == "Forward":
            goals = int(np.random.negative_binomial(3, 0.3, 1)[0] * minutes_played / 2000)
            assists = int(np.random.negative_binomial(2, 0.3, 1)[0] * minutes_played / 2000)
            shots = int(np.random.normal(minutes_played / 35, minutes_played / 100, 1)[0])
            shots_on_target = int(shots * random.uniform(0.3, 0.5))
            passes_completed = int(np.random.normal(minutes_played / 4, minutes_played / 15, 1)[0])
            pass_accuracy = round(random.uniform(68, 82), 1)
            tackles = int(np.random.normal(minutes_played / 120, minutes_played / 300, 1)[0])
            interceptions = int(tackles * random.uniform(0.4, 0.7))
            
        elif position == "Midfielder":
            goals = int(np.random.negative_binomial(2, 0.25, 1)[0] * minutes_played / 3000)
            assists = int(np.random.negative_binomial(3, 0.25, 1)[0] * minutes_played / 2500)
            shots = int(np.random.normal(minutes_played / 60, minutes_played / 150, 1)[0])
            shots_on_target = int(shots * random.uniform(0.25, 0.45))
            passes_completed = int(np.random.normal(minutes_played / 2.5, minutes_played / 10, 1)[0])
            pass_accuracy = round(random.uniform(76, 88), 1)
            tackles = int(np.random.normal(minutes_played / 70, minutes_played / 200, 1)[0])
            interceptions = int(tackles * random.uniform(0.5, 0.8))
            
        elif position == "Defender":
            goals = int(np.random.negative_binomial(1, 0.15, 1)[0] * minutes_played / 5000)
            assists = int(np.random.negative_binomial(1, 0.2, 1)[0] * minutes_played / 4000)
            shots = int(np.random.normal(minutes_played / 180, minutes_played / 400, 1)[0])
            shots_on_target = int(shots * random.uniform(0.2, 0.4))
            passes_completed = int(np.random.normal(minutes_played / 3, minutes_played / 12, 1)[0])
            pass_accuracy = round(random.uniform(78, 90), 1)
            tackles = int(np.random.normal(minutes_played / 50, minutes_played / 150, 1)[0])
            interceptions = int(tackles * random.uniform(0.6, 0.9))
            
        else:  # Goalkeeper
            goals = 0
            assists = 0
            shots = 0
            shots_on_target = 0
            passes_completed = int(np.random.normal(minutes_played / 4, minutes_played / 15, 1)[0])
            pass_accuracy = round(random.uniform(65, 80), 1)
            tackles = 0
            interceptions = 0
        
        # Cap values to realistic ranges
        goals = max(0, min(goals, 25))
        assists = max(0, min(assists, 15))
        shots = max(0, min(shots, 120))
        shots_on_target = max(0, min(shots_on_target, 60))
        passes_completed = max(0, min(passes_completed, 2500))
        tackles = max(0, min(tackles, 100))
        interceptions = max(0, min(interceptions, 80))
        
        # Discipline stats
        fouls_committed = int(np.random.negative_binomial(3, 0.15, 1)[0] * minutes_played / 2000)
        fouls_suffered = int(np.random.negative_binomial(3, 0.15, 1)[0] * minutes_played / 2000)
        
        # More fouls for defenders and defensive midfielders
        if position == "Defender":
            fouls_committed = int(fouls_committed * random.uniform(1.2, 1.5))
        
        # More fouls suffered for attackers and attacking midfielders
        if position == "Forward":
            fouls_suffered = int(fouls_suffered * random.uniform(1.2, 1.5))
        
        # Cap fouls to realistic ranges
        fouls_committed = max(0, min(fouls_committed, 85))
        fouls_suffered = max(0, min(fouls_suffered, 75))
        
        # Cards based on fouls committed
        yellow_card_prob = fouls_committed / 100
        yellow_cards = int(np.random.binomial(min(15, fouls_committed), yellow_card_prob, 1)[0])
        
        # Red cards are rare
        red_card_prob = 0.01 + (yellow_cards / 100)
        red_cards = int(np.random.binomial(1, red_card_prob, 1)[0])
        
        # Suspensions based on cards
        games_suspended = 0
        if red_cards > 0:
            games_suspended += red_cards
        if yellow_cards >= 5:
            games_suspended += yellow_cards // 5
        
        # Create player record
        player = {
            "player_id": i,
            "team_name": team_name,
            "player_name": player_name,
            "nationality": nationality_choice,
            "position": position,
            "age": age,
            "matches_played": matches_played,
            "matches_started": matches_started,
            "minutes_played": minutes_played,
            "goals": goals,
            "assists": assists,
            "shots": shots,
            "shots_on_target": shots_on_target,
            "passes_completed": passes_completed,
            "pass_accuracy": pass_accuracy,
            "tackles": tackles,
            "interceptions": interceptions,
            "fouls_committed": fouls_committed,
            "fouls_suffered": fouls_suffered,
            "yellow_cards": yellow_cards,
            "red_cards": red_cards,
            "games_suspended": games_suspended
        }
        
        data.append(player)
    
    return pd.DataFrame(data)

# Generate full player dataset
players_df = generate_player_data(542)

# Output to CSV
players_df.to_csv("epl_player_data.csv", index=False)

print(f"Generated {len(players_df)} player records")
print("Sample records:")
print(players_df.head())

# Basic statistics
print("\nBasic Statistics:")
print(f"Total players: {len(players_df)}")
print(f"Players by position: {players_df['position'].value_counts().to_dict()}")
print(f"Total goals: {players_df['goals'].sum()}")
print(f"Players with red cards: {(players_df['red_cards'] > 0).sum()}")
print(f"Nigerian players: {(players_df['nationality'] == 'Nigeria').sum()}")

# Statistics for Nigerian players
nigerian_players = players_df[players_df['nationality'] == 'Nigeria']
print("\nNigerian Players Statistics:")
print(nigerian_players[['player_name', 'team_name', 'position', 'goals', 'assists', 'yellow_cards', 'red_cards']])