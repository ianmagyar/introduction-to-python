def load_results(file_path):
    # open file and read results from it
    # returns a list of rows as strings
    my_file = open(file_path, 'r', encoding='utf-8')
    result_rows = my_file.readlines()
    my_file.close()
    return result_rows


def load_score(line):
    # loads score from a row as string
    # returns a tuple of four values: home team name, home team goals
    # away team name, away team goals
    home_score, away_score = line[:-1].split(' - ')
    home_team, home_goals = home_score.rsplit(' ', 1)
    away_goals, away_team = away_score.split(' ', 1)
    return (home_team, int(home_goals), away_team, int(away_goals))


def get_team_list(scores):
    # returns a set of unique team names
    return set([score[0] for score in scores])


def create_table(team_names):
    # creates an empty table with team names
    # there is one dictionary for every team with the following info:
    # team name, number of games played, number of wins, number of draws
    # number of losses, number of goals scored, number of goals conceeded
    # number of points
    table = list()
    dictionary_template = {
        "team": "",
        "games_played": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "points": 0
    }

    for team in team_names:
        team_dictionary = dictionary_template.copy()
        team_dictionary['team'] = team
        table.append(team_dictionary)

    return table


def get_team_row(table, team_name):
    # finds the dictionary corresponding to the team in a table
    for row in table:
        if row['team'] == team_name:
            return row
    return None


def update_points(table):
    # calculates the team's points based on number of wins, draws, losses
    for row in table:
        row['points'] = 3 * row['wins'] + row['draws']


def add_match_to_table(table, match_info):
    # updates table based on a match result
    # input is a list representing the table and
    # a tuple representing the match result
    # updates table directly, returns nothing
    home_team, home_goals, away_team, away_goals = match_info
    home_team_row = get_team_row(table, home_team)
    away_team_row = get_team_row(table, away_team)

    home_team_row['games_played'] += 1
    away_team_row['games_played'] += 1

    home_team_row['wins'] += home_goals > away_goals
    away_team_row['wins'] += away_goals > home_goals
    home_team_row['draws'] += home_goals == away_goals
    away_team_row['draws'] += away_goals == home_goals
    home_team_row['losses'] += home_goals < away_goals
    away_team_row['losses'] += away_goals < home_goals

    home_team_row['goals_for'] += home_goals
    home_team_row['goals_against'] += away_goals
    away_team_row['goals_for'] += away_goals
    away_team_row['goals_against'] += home_goals

    update_points(table)


def generate_table(results_file_path):
    # gets path to file with results
    # generates table and fills it with values based on match results
    # returns the table as a list of dictionaries
    lines = load_results(results_file_path)

    match_infos = list()
    for line in lines:
        match_infos.append(load_score(line))

    list_of_teams = get_team_list(match_infos)
    table = create_table(list_of_teams)

    for match_info in match_infos:
        add_match_to_table(table, match_info)

    return table


def print_table(table):
    # prints table in a user-friendly way
    # columns:
    # rank, team, games, wins, draws, losses, goals for, goals against, points
    # does not return anything
    team_name_length = max([(len(row['team'])) for row in table])
    header = "|Rank|Team{}|G |W |D |L |GF |GA |P |".format(
        ' ' * (team_name_length - len("Team")))
    print(header)
    print('-' * len(header))
    row_template = "|{:>4}|{:<{team_name_length}}|{:>2}|{:>2}|{:>2}|{:>2}|{:>3}|{:>3}|{:>2}|"
    for rank, team_data in enumerate(table, start=1):
        print(row_template.format(
            rank, team_data['team'], team_data['games_played'],
            team_data['wins'], team_data['draws'], team_data['losses'],
            team_data['goals_for'], team_data['goals_against'],
            team_data['points'], team_name_length=team_name_length)
        )


def sort_table(table, sort_by, ascending=True):
    # sorts table based on a key, returns a copy of the table
    return sorted(table, key=lambda team: team[sort_by], reverse=not ascending)


if __name__ == '__main__':
    table = generate_table("buli_results.txt")

    table = sort_table(table, 'points', ascending=False)

    print_table(table)
