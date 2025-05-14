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

# In the case where there's missing data in the teams dataframe, we'd can fix both datasets using the sample code blocks below:

# For team data
if epl_teams_df.isnull().sum().sum() > 0:
    # For numerical columns, fill with median
    num_cols = epl_teams_df.select_dtypes(include=['int64', 'float64']).columns
    for col in num_cols:
        if epl_teams_df[col].isnull().sum() > 0:
            epl_teams_df[col] = epl_teams_df[col].fillna(epl_teams_df[col].median())
    
    # For categorical columns, fill with mode
    # The mode of a range of values represents the most frequently occurring value
    cat_cols = epl_teams_df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        if epl_teams_df[col].isnull().sum() > 0:
            epl_teams_df[col] = epl_teams_df[col].fillna(epl_teams_df[col].mode()[0])

# For player data
if epl_players_df.isnull().sum().sum() > 0:
    # For numerical columns, fill with median
    num_cols = epl_players_df.select_dtypes(include=['int64', 'float64']).columns
    for col in num_cols:
        if epl_players_df[col].isnull().sum() > 0:
            epl_players_df[col] = epl_players_df[col].fillna(epl_players_df[col].median())
    
    # For categorical columns, fill with mode
    cat_cols = epl_players_df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        if epl_players_df[col].isnull().sum() > 0:
            epl_players_df[col] = epl_players_df[col].fillna(epl_players_df[col].mode()[0])

print('\n\n')

# 1.4: Perform basic data cleaning (rename columns, fix data types, etc.)

# Example code on how you'd rename a column, if you needed to
# In the code below, we are changing the name of the 'goals' column in the players dataframe to 'goals_scored'
# epl_players_df = epl_players_df.rename(columns = { 'goals': 'Goals Scored' })

# Check for duplicates
print('Duplicate entries in teams data:')
print(epl_teams_df.duplicated().sum())

print('\n')

print('Duplicate entries in players data:')
print(epl_players_df.duplicated().sum())

print('\n')

# Remove duplicates if any exist
if epl_teams_df.duplicated().sum() > 0:
    epl_teams_df = epl_teams_df.drop_duplicates()
    print("\nDuplicates removed from team data.")

if epl_players_df.duplicated().sum() > 0:
    epl_players_df = epl_players_df.drop_duplicates()
    print("\nDuplicates removed from player data.")


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

# Disciplinary metrics for teams
print('\Team Disciplinary Statistics')
team_disciplinary = epl_teams_df[['team_name', 'fouls_committed', 'yellow_cards', 'red_cards', 'manager_bans', 'players_suspended', 'games_missed_suspensions']]
print(team_disciplinary.describe())

print('\n')

# Disciplinary metrics for players
print('\nPlayer Disciplinary Statistics')
player_disciplinary = epl_players_df[['player_name', 'team_name', 'fouls_committed', 'yellow_cards', 'red_cards', 'games_suspended']]
print(player_disciplinary.describe())

print('\n\n')


## Part 2: Team Performance Analysis

### 2.1 Calculate performance metrics for each team

# Add per-match metrics
epl_teams_df['avg_goals_scored'] = epl_teams_df['goals_scored'] / epl_teams_df['matches_played']
epl_teams_df['avg_goals_conceded'] = epl_teams_df['goals_conceded'] / epl_teams_df['matches_played']

# Calculate home vs away performance
epl_teams_df['home_points'] = epl_teams_df['home_wins'] * 3 + epl_teams_df['home_draws'] * 1
epl_teams_df['away_points'] = epl_teams_df['away_wins'] * 3 + epl_teams_df['away_draws'] * 1
epl_teams_df['home_win_pct'] = epl_teams_df['home_wins'] / (epl_teams_df['home_wins'] + epl_teams_df['home_draws'] + epl_teams_df['home_losses'])
epl_teams_df['away_win_pct'] = epl_teams_df['away_wins'] / (epl_teams_df['away_wins'] + epl_teams_df['away_draws'] + epl_teams_df['away_losses'])

# Goal efficiency metrics
epl_teams_df['shot_conversion_rate'] = epl_teams_df['goals_scored'] / epl_teams_df['shots']
epl_teams_df['shot_on_target_conversion'] = epl_teams_df['goals_scored'] / epl_teams_df['shots_on_target']
epl_teams_df['shot_accuracy'] = epl_teams_df['shots_on_target'] / epl_teams_df['shots']

# Display new metrics
print("\nTeam Performance Metrics:")
performance_columns = [
    'team_name', 'avg_goals_scored', 'avg_goals_conceded', 'shot_conversion_rate',
    'shot_accuracy', 'home_win_pct', 'away_win_pct'
]
print(epl_teams_df[performance_columns].head())

print('\n\n')

### 2.2 Create performance rating and Fair Play Index

# Create performance rating
epl_teams_df['performance_rating'] = (
    (epl_teams_df['points'] * 2) + (epl_teams_df['goals_scored'] * 0.5) - (epl_teams_df['goals_conceded'] * 0.3) + 
    (epl_teams_df['clean_sheets'] * 3) - (epl_teams_df['red_cards'] * 2) - (epl_teams_df['yellow_cards'] * 0.5)
)

# Create Fair Play Index
epl_teams_df['fair_play_index'] = 100 - (
    (epl_teams_df['fouls_committed'] * 0.1) + (epl_teams_df['yellow_cards'] * 1) + 
    (epl_teams_df['red_cards'] * 3) + (epl_teams_df['manager_bans'] * 2)
)

# Display the ratings
print("\nTeam Ratings and Fair Play Index:")
rating_cols = ['team_name', 'performance_rating', 'fair_play_index']
print(epl_teams_df[rating_cols].sort_values('performance_rating', ascending=False))

print('\n\n')


### 2.3 Identify top teams in different categories

# Top 5 attacking teams (most goals scored)
print("\nTop 5 Attacking Teams:")
print(epl_teams_df[['team_name', 'goals_scored', 'avg_goals_scored']].sort_values('goals_scored', ascending=False).head(5))

# Top 5 defensive teams (fewest goals conceded)
print("\nTop 5 Defensive Teams:")
print(epl_teams_df[['team_name', 'goals_conceded', 'avg_goals_conceded', 'clean_sheets']].sort_values('goals_conceded').head(5))

# Most efficient teams (highest goal-to-shot ratio)
print("\nTop 5 Most Efficient Teams:")
print(epl_teams_df[['team_name', 'shot_conversion_rate', 'goals_scored', 'shots']].sort_values('shot_conversion_rate', ascending=False).head(5))

# Most disciplined teams (best Fair Play Index)
print("\nTop 5 Most Disciplined Teams:")
print(epl_teams_df[['team_name', 'fair_play_index', 'fouls_committed', 'yellow_cards', 'red_cards']].sort_values('fair_play_index', ascending=False).head(5))

# Most aggressive teams (most fouls committed)
print("\nTop 5 Most Aggressive Teams:")
print(epl_teams_df[['team_name', 'fouls_committed', 'yellow_cards', 'red_cards']].sort_values('fouls_committed', ascending=False).head(5))

# Over/under-performing teams (comparing actual points vs. expected points)
epl_teams_df['points_difference'] = epl_teams_df['points'] - epl_teams_df['expected_points']

print("\nTop 5 Over-performing Teams:")
print(epl_teams_df[['team_name', 'points', 'expected_points', 'points_difference']].sort_values('points_difference', ascending=False).head(5))

print("\nTop 5 Under-performing Teams:")
print(epl_teams_df[['team_name', 'points', 'expected_points', 'points_difference']].sort_values('points_difference').head(5))

print('\n\n')

### 2.4 Calculate correlations between key metrics


# Calculate correlations
correlation_metrics = [
    'position', 'points', 'wage_budget', 'possession_pct', 'shots', 'goals_scored', 'goals_conceded',
    'yellow_cards', 'red_cards', 'fouls_committed', 'points_difference'
]
                      
correlation_matrix = epl_teams_df[correlation_metrics].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

# Specific correlations of interest
print("\nSpecific Correlations of Interest:")
print(f"Team wage budget and final position: {epl_teams_df['wage_budget'].corr(epl_teams_df['position']):.4f}")
print(f"Possession percentage and points earned: {epl_teams_df['possession_pct'].corr(epl_teams_df['points']):.4f}")
print(f"Number of shots and goals scored: {epl_teams_df['shots'].corr(epl_teams_df['goals_scored']):.4f}")
print(f"Disciplinary record (yellow cards) and league position: {epl_teams_df['yellow_cards'].corr(epl_teams_df['position']):.4f}")
print(f"Fouls committed and goals conceded: {epl_teams_df['fouls_committed'].corr(epl_teams_df['goals_conceded']):.4f}")
print(f"Possession percentage and pass accuracy: {epl_teams_df['possession_pct'].corr(epl_teams_df['pass_accuracy']):.4f}")

print('\n\n')

## Part 3: Player Performance Analysis

### 3.1 Identify and analyze Nigerian players

# Identify Nigerian players
nigerian_players = epl_players_df[epl_players_df['nationality'] == 'Nigeria']

print(f"\nFound {len(nigerian_players)} Nigerian players in the dataset:")
print(nigerian_players[['player_name', 'team_name', 'position', 'age']])

# If Nigerian players exist, analyze their performance
if len(nigerian_players) > 0:
    # Calculate performance metrics
    print("\nPerformance metrics of Nigerian players:")
    performance_cols = ['player_name', 'team_name', 'position', 'matches_played', 'goals', 'assists', 'minutes_played']
    print(nigerian_players[performance_cols])
    
    # Calculate per-90-minutes metrics for fair comparison
    nigerian_players['goals_per_90'] = 90 * nigerian_players['goals'] / nigerian_players['minutes_played']
    nigerian_players['assists_per_90'] = 90 * nigerian_players['assists'] / nigerian_players['minutes_played']
    nigerian_players['shots_per_90'] = 90 * nigerian_players['shots'] / nigerian_players['minutes_played']
    
    # Group by position to compare with positional averages
    player_position_groups = epl_players_df.groupby('position')
    
    # Calculate averages by position
    position_avgs = player_position_groups.agg({
        'goals': 'mean',
        'assists': 'mean',
        'tackles': 'mean',
        'interceptions': 'mean',
        'fouls_committed': 'mean',
        'yellow_cards': 'mean',
        'red_cards': 'mean'
    }).reset_index()
    
    # Rename columns to indicate these are averages
    position_avgs = position_avgs.rename(columns={
        'goals': 'avg_goals',
        'assists': 'avg_assists',
        'tackles': 'avg_tackles',
        'interceptions': 'avg_interceptions',
        'fouls_committed': 'avg_fouls',
        'yellow_cards': 'avg_yellows',
        'red_cards': 'avg_reds'
    })
    
    # Merge Nigerian players with position averages
    nigerian_analysis = pd.merge(nigerian_players, position_avgs, on='position')
    
    # Calculate comparison metrics
    nigerian_analysis['goals_vs_avg'] = nigerian_analysis['goals'] - nigerian_analysis['avg_goals']
    nigerian_analysis['assists_vs_avg'] = nigerian_analysis['assists'] - nigerian_analysis['avg_assists']
    nigerian_analysis['fouls_vs_avg'] = nigerian_analysis['fouls_committed'] - nigerian_analysis['avg_fouls']
    nigerian_analysis['yellows_vs_avg'] = nigerian_analysis['yellow_cards'] - nigerian_analysis['avg_yellows']
    
    # Show comparison metrics
    print("\nNigerian players compared to position averages:")
    comparison_cols = [
        'player_name', 'position', 'goals', 'avg_goals', 'goals_vs_avg', 'assists', 'avg_assists', 'assists_vs_avg',
        'fouls_committed', 'avg_fouls', 'fouls_vs_avg', 'yellow_cards', 'avg_yellows', 'yellows_vs_avg'
    ]
    print(nigerian_analysis[comparison_cols])
    
    # Disciplinary comparison
    print("\nDisciplinary record comparison:")
    disc_cols = ['player_name', 'position', 'fouls_committed', 'fouls_suffered', 'yellow_cards', 'red_cards', 'games_suspended']
    print(nigerian_analysis[disc_cols])
else:
    print("No Nigerian players found in the dataset.")

print('\n')

### 3.2 Identify top performers in different categories

# Filter players with significant minutes played (e.g., at least 450 minutes, or 5 full matches)
significant_minutes = 450
active_players = epl_players_df[epl_players_df['minutes_played'] >= significant_minutes].copy()

# Calculate per-90-minutes metrics for fair comparison
active_players['goals_per_90'] = 90 * active_players['goals'] / active_players['minutes_played']
active_players['assists_per_90'] = 90 * active_players['assists'] / active_players['minutes_played']
active_players['shots_per_90'] = 90 * active_players['shots'] / active_players['minutes_played']
active_players['tackles_per_90'] = 90 * active_players['tackles'] / active_players['minutes_played']
active_players['interceptions_per_90'] = 90 * active_players['interceptions'] / active_players['minutes_played']
active_players['fouls_per_90'] = 90 * active_players['fouls_committed'] / active_players['minutes_played']

# Top goalscorers
print("\nTop 10 Goalscorers:")
top_goals = active_players[['player_name', 'team_name', 'position', 'goals', 'goals_per_90', 'matches_played']]
print(top_goals.sort_values('goals', ascending=False).head(10))

# Top assist providers
print("\nTop 10 Assist Providers:")
top_assists = active_players[['player_name', 'team_name', 'position', 'assists', 'assists_per_90', 'matches_played']]
print(top_assists.sort_values('assists', ascending=False).head(10))

# Goal contributions (goals + assists)
active_players['goal_contributions'] = active_players['goals'] + active_players['assists']
active_players['goal_contributions_per_90'] = active_players['goals_per_90'] + active_players['assists_per_90']

print("\nTop 10 Goal Contributors:")
top_contributors = active_players[['player_name', 'team_name', 'position', 'goal_contributions', 'goal_contributions_per_90', 'matches_played']]
print(top_contributors.sort_values('goal_contributions', ascending=False).head(10))

# Best defensive record - split by position
defenders = active_players[active_players['position'].isin(['Defender', 'Center-back', 'Full-back'])]
midfielders = active_players[active_players['position'].isin(['Midfielder', 'Central midfielder', 'Defensive midfielder'])]

# Top defenders (by tackles + interceptions)
defenders['defensive_actions'] = defenders['tackles'] + defenders['interceptions']
defenders['defensive_actions_per_90'] = defenders['tackles_per_90'] + defenders['interceptions_per_90']

print("\nTop 10 Defenders (by defensive actions):")
top_defenders = defenders[['player_name', 'team_name', 'position', 'defensive_actions', 'defensive_actions_per_90', 'matches_played']]
print(top_defenders.sort_values('defensive_actions', ascending=False).head(10))

# Discipline metrics - cards per 90 minutes
active_players['cards_per_90'] = 90 * (active_players['yellow_cards'] + 3*active_players['red_cards']) / active_players['minutes_played']
active_players['discipline_index'] = 100 - (active_players['yellow_cards'] * 3 + active_players['red_cards'] * 10)

# Most disciplined players (lowest cards per minute)
print("\nTop 10 Most Disciplined Players (with at least 10 matches):")

# Filter the dataframe to retrieve players that have played over 10 games
playersWithOver10Games = active_players[active_players['matches_played'] >= 10]

disciplined = playersWithOver10Games[
    ['player_name', 'team_name', 'position', 'yellow_cards', 'red_cards', 'cards_per_90', 'discipline_index', 'matches_played']
]
print(disciplined.sort_values('cards_per_90').head(10))

# Most aggressive players (most fouls)
print("\nTop 10 Most Aggressive Players (most fouls committed):")
aggressive = active_players[['player_name', 'team_name', 'position', 'fouls_committed', 'fouls_per_90', 'matches_played']]
print(aggressive.sort_values('fouls_committed', ascending=False).head(10))

# Create player value metric for overall contribution
# For attackers and midfielders
attacking_value = (active_players['goals'] * 3) + (active_players['assists'] * 2) + (active_players['shots_on_target'] * 0.5)

# For defenders and goalkeepers
defensive_value = (active_players['tackles'] * 1) + (active_players['interceptions'] * 1.5)

# Combined player value metric
active_players['player_value'] = attacking_value + defensive_value - (active_players['yellow_cards'] * 1) - (active_players['red_cards'] * 3)

# Most valuable players overall
print("\nTop 10 Most Valuable Players (Overall Contribution):")
valuable = active_players[['player_name', 'team_name', 'position', 'player_value', 'goals', 'assists', 'tackles', 'interceptions', 'matches_played']]
print(valuable.sort_values('player_value', ascending=False).head(10))


## Saving Results to CSV Files

# Save team analysis results
team_analysis_results = epl_teams_df.copy()

# Export to CSV
try:
    team_analysis_results.to_csv('epl_team_analysis_results.csv', index=False)
    print("\nTeam analysis results successfully exported to 'epl_team_analysis_results.csv'")
except Exception as e:
    print(f"Error exporting team analysis results: {e}")

# Save player analysis results
player_analysis_results = active_players.copy()

# Export to CSV
try:
    player_analysis_results.to_csv('epl_player_analysis_results.csv', index=False)
    print("Player analysis results successfully exported to 'epl_player_analysis_results.csv'")
except Exception as e:
    print(f"Error exporting player analysis results: {e}")
