def load_results(file_path):
    results_file = open(file_path, 'r')
    results = results_file.readlines()
    results_file.close()
    return results


def load_score(line):
    scores = line[:-1].split(' - ')
    home_team, home_goals = scores[0].rsplit(' ', 1)
    away_goals, away_team = scores[1].split(' ', 1)
    return (home_team, int(home_goals),
            away_team, int(away_goals))


def get_teams(matches):
    return set([match[0] for match in matches])


def get_table(team_names):
    table = list()
    team_dictionary = {
        "team": "",
        "games": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "points": 0
    }

    for team in team_names:
        temp_dictionary = team_dictionary.copy()
        temp_dictionary["team"] = team
        table.append(temp_dictionary)

    return table


def get_row(table, team_name):
    for row in table:
        if row['team'] == team_name:
            return row
    return None


def process_match(table, match):
    h_team, h_goals, a_team, a_goals = match
    h_team_row = get_row(table, h_team)
    a_team_row = get_row(table, a_team)

    h_team_row['games'] += 1
    a_team_row['games'] += 1

    h_team_row['wins'] += h_goals > a_goals
    a_team_row['wins'] += a_goals > h_goals

    h_team_row['draws'] += h_goals == a_goals
    a_team_row['draws'] += a_goals == h_goals

    h_team_row['losses'] += h_goals < a_goals
    a_team_row['losses'] += a_goals < h_goals

    h_team_row['goals_for'] += h_goals
    h_team_row['goals_against'] += a_goals
    a_team_row['goals_for'] += a_goals
    a_team_row['goals_against'] += h_goals


if __name__ == '__main__':
    matches = list()

    lines = load_results("lab5_results.txt")
    for line in lines:
        matches.append(load_score(line))

    teams = get_teams(matches)
    table = get_table(teams)

    for match in matches:
        process_match(table, match)

    for team in table:
        team['points'] = team['wins'] * 3 + team['draws']

    table = sorted(table, key=lambda team: team['points'],
                   reverse=True)

    print(table)
