import pandas as pd

# 1.1: Load CSV files
epl_teams_df = pd.read_csv('../../data/epl_team_data.csv')
epl_players_df = pd.read_csv('../../data/epl_player_data.csv')

print('\n\n')

# 1.2: Examine data structure
print('EPL Teams Data Information')
epl_teams_df.info()

print('\n')

# Display the first few rows of team data
print(epl_teams_df.head())

print('\n========================================================================================\n')

print('EPL Players Data Information')
epl_players_df.info()

print('\n')

# Display the first few rows of players data
print(epl_players_df.head())

# 1.3: Handle missing values in both datasets
print('\nMissing values in teams data:')
print(epl_teams_df.isnull().sum())

print('\n')

print('\nMissing values in players data:')
print(epl_players_df.isnull().sum())

# In the case where there's missing data in the teams dataframe, we'd do this:
# TODO: Add code block

# In the case where there's missing data in the players dataframe, we'd do this:
# TODO: Add code block


print('\n\n')

# 1.4: Perform basic data cleaning (rename columns, fix data types, etc.)

# TODO: Add sample code to rename columns | students_df = students_df.rename(columns = { 'math_score': 'Mathematics Score' })

# Check for duplicates
print('Duplicate entries in teams data:')
print(epl_teams_df.duplicated().sum())

print('\n')

print('Duplicate entries in players data:')
print(epl_players_df.duplicated().sum())

# TODO: Add a code block to show how to remove duplicates


# Ensure data types are appropriate
epl_teams_df['team_name'] = epl_teams_df['team_name'].astype('string')

epl_players_df['team_name'] = epl_players_df['team_name'].astype('string')
epl_players_df['player_name'] = epl_players_df['player_name'].astype('string')
epl_players_df['nationality'] = epl_players_df['nationality'].astype('string')
epl_players_df['position'] = epl_players_df['position'].astype('string')

print('\n\n')

# 1.5 Create appropriate relationships between the two datasets

# Get unique team names fro players data
player_teams = epl_players_df['team_name'].unique()

team_names = epl_teams_df['team_name'].unique()

# Check if all players' teams exists in team data (using list comprehension)
missing_teams = [team for team in player_teams if team not in team_names]

# Alternative: Using for loop
# _missing_teams = []
# for team in player_teams:
#     if team not in team_names:
#         _missing_teams.append(team)

if missing_teams:
    print('The following teams in player data don\'t match team data:')
    print(missing_teams)
else:
    print('All player teams match teams data. Relationship is established!')


print('\n\n')

# 1.6: Calculate summary statistics for the key numerical columns in both datasets, including disciplinary metrics
print('EPL 2023/2024 Team Data Summary')
print(epl_teams_df.describe())

print('EPL 2023/2024 Player Data Summary')
print(epl_players_df.describe())

print('\n\n')

# Discplinary metrics for teams
print('\Team Disciplinary Statistics')
team_disciplinary = epl_teams_df[['team_name', 'fouls_committed', 'yellow_cards', 'red_cards', 'manager_bans', 'players_suspended', 'games_missed_suspensions']]
print(team_disciplinary.describe())

print('\n')

# Discplinary metrics for players
print('\nPlayer Disciplinary Statistics')
player_discipinary = epl_players_df[['player_name', 'team_name', 'fouls_committed', 'yellow_cards', 'red_cards', 'games_suspended']]
print(player_discipinary.describe())

print('\n\n')

# TODO: Complete the tasks