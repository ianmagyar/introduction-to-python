def load_matches(file_path):
    results_file = open(file_path, 'r')
    results = results_file.readlines()
    results_file.close()
    return results


def get_match(line):
    teams = line[:-1].split(' - ')
    h_team, h_goals = teams[0].rsplit(' ', 1)
    a_goals, a_team = teams[1].split(' ', 1)
    return (h_team, int(h_goals),
            a_team, int(a_goals))


def get_table(results):
    temp_dictionary = {
        "team": "",
        "matches": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "points": 0
    }

    table = []
    teams = set([result[0] for result in results])

    for team_name in teams:
        team_dictionary = temp_dictionary.copy()
        team_dictionary['team'] = team_name
        table.append(team_dictionary)

    return table


def get_team_row(table, team_name):
    for row in table:
        if row['team'] == team_name:
            return row
    return None


def process_match(table, result):
    h_team, h_goals, a_team, a_goals = result
    h_team_row = get_team_row(table, h_team)
    a_team_row = get_team_row(table, a_team)

    h_team_row['matches'] += 1
    a_team_row['matches'] += 1

    h_team_row['wins'] += h_goals > a_goals
    a_team_row['wins'] += a_goals > h_goals

    h_team_row['draws'] += h_goals == a_goals
    a_team_row['draws'] += h_goals == a_goals

    h_team_row['losses'] += h_goals < a_goals
    a_team_row['losses'] += a_goals < h_goals

    h_team_row['goals_for'] += h_goals
    h_team_row['goals_against'] += a_goals
    a_team_row['goals_for'] += a_goals
    a_team_row['goals_against'] += h_goals


if __name__ == '__main__':
    matches = load_matches("lab5_results.txt")
    results = []

    for match in matches:
        results.append(get_match(match))

    table = get_table(results)

    for result in results:
        process_match(table, result)

    for team in table:
        team['points'] = 3 * team['wins'] + team['draws']

    table = sorted(table, key=lambda row: row['points'],
                   reverse=True)
    print(table)
