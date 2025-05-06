## English Premier League Data Analysis

### Instructions & Deliverables 

#### Instructions [READ THROUGH]

1. Create a GitHub account and then a project for submitting take-home exercises for this bootcamp. Ensure the project is public.
2. After you creating the project, follow the instructions (on GitHub) to map the project to a folder on your laptop.
3. Within the project folder on your laptop, create weekly folders for submission of tasks. For example, for the week 7 tasks, you'll create a `Week 7` folder and have your solution for Week 7 tasks in the folder.
4. Once done with the tasks, push your changes to GitHub and share the URL for the Notebook file. Remember, not the GitHub project URL, but the URL for the Jupyter Notebook file.
5. Use the Google Forms link to send in your submission: https://forms.gle/UQ9PNddiUCgT7dwy5


#### Deliverables for this task

1. Put your final work in a Jupyter Notebook (`.ipynb`) containing your code and analysis (markdown explanations)
2. Two processed CSV files:
- `epl_team_analysis_results.csv` containing the team data plus calculated metrics
- `epl_player_analysis_results.csv` containing the player data plus calculated metrics
3. A brief report (using Markdown) summarizing your key findings that would be useful for Nigerian sports broadcasters

><i>You're not expected to complete all the tasks, however you're expected to give it your best attempt. If you do complete all the tasks, even better.</i>

> **REMEMBER:** Do not willingly hurt your chances to learn by outsourcing to an LLM like GPT, Claude, etc.

### Context

As a Data Analyst for a sports analytics company, you've been tasked with analyzing the 2023/2024 English Premier League (EPL) season data to provide insights for a Nigerian sports television network. This data analysis will help their commentators prepare for upcoming broadcasts and understand performance trends of various clubs, particularly those with Nigerian players.

### Dataset Description

You will be working with two related data files (located in the `data` directory):

1. `epl_team_data.csv` - Contains team-level statistics including:
- Match results and standings
- Goals scored/conceded
- Team performance metrics (possession, shots, etc.)
- Fan engagement metrics
- Disciplinary records (team totals)
- Team Financial data


2. `epl_player_data.csv` - Contains player-level statistics including:
- Personal information (name, nationality, position, age)
- Performance stats (goals, assists, etc.)
- Playing time (matches, minutes)
- Disciplinary records (fouls, cards, suspensions)

### Tasks

**Part 1: Basic Data Exploration and Preparation**
1. Load the provided CSV file into Pandas DataFrames
2. Examine the data structure of both datasets (shape, columns, data types)
3. Check for and handle any missing values appropriately in both datasets
4. Perform basic data cleaning (rename columns, fix data types, etc.)
5. Create appropriate relationships between the two datasets
6. Calculate summary statistics for the key numerical columns in both datasets, including disciplinary metrics

**Part 2: Team Performance Analysis with NumPy and Pandas**

1. Calculate the following for each team:
   - Total points accumulated
   - Average goals scored and conceded per match
   - Goal difference
   - Home vs. away performance comparison
   - Total fouls committed and suffered
   - Disciplinary record (yellow cards, red cards, match bans)
   
2. Create a new column for performance rating using the formula:
   ```
   Rating = (Points × 2) + (Goals_Scored × 0.5) - (Goals_Conceded × 0.3) + (Clean_Sheets × 3) - (Red_Cards × 2) - (Yellow_Cards × 0.5)
   ```

3. Create a "Fair Play Index" using:
   ```
   Fair_Play_Index = 100 - ((Fouls × 0.1) + (Yellow_Cards × 1) + (Red_Cards × 3) + (Manager_Bans × 2))
   ```

4. Identify:
   - Top 5 attacking teams (most goals scored)
   - Top 5 defensive teams (fewest goals conceded)
   - Most efficient teams (highest goal-to-shot ratio)
   - Most disciplined teams (best Fair Play Index)
   - Most aggressive teams (most fouls committed)
   - Over/underperforming teams (comparing actual points vs. expected points)

5. Calculate the correlation between:
   - Team wage budget and final league position
   - Possession percentage and points earned
   - Number of shots and goals scored
   - Disciplinary record and league position
   - Fouls committed and goals conceded
   - Yellow/red cards and points deduction


**Part 3: Player Performance Analysis**

1. Using the player dataset, identify all Nigerian players and:
   - Calculate their performance metrics
   - Analyze their disciplinary records compared to positional averages
   - Compare their statistics to the league average for their position

2. Using the player dataset, identify the top performers in different categories:
   - Top goalscorers
   - Most assists
   - Best defensive record
   - Most valuable players (based on goals/assists and defensive contributions)
   - Most disciplined players (fewest cards relative to minutes played)
   - Most aggressive players (most fouls committed)

### Tips

- Remember to use NumPy functions for numerical operations to ensure efficiency
- Use Pandas' groupby, join, merge, and aggregation functions for more complex analyses
- Apply proper error handling for missing values
- Use descriptive variable names and include comments in your code
- Consider both absolute and relative metrics when assessing disciplinary records
- Account for positions when analyzing disciplinary records (defenders naturally commit more fouls)
- Consider the difference between "tactical" fouls (which may be beneficial) and unnecessary cards
