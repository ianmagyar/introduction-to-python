def load_results(file_path):
    # open file and read results from it
    # returns a list of rows as strings
    pass


def load_score(line):
    # loads score from a row as string
    # returns a tuple of four values: home team name, home team goals
    # away team name, away team goals
    pass


def get_team_list(scores):
    # returns a set of unique team names
    pass


def create_table(team_names):
    # creates an empty table with team names
    # there is one dictionary for every team with the following info:
    # team name, number of games played, number of wins, number of draws
    # number of losses, number of goals scored, number of goals conceeded
    # number of points
    pass


def get_team_row(table, team_name):
    # finds the dictionary corresponding to the team in a table
    pass


def update_points(table):
    # calculates the team's points based on number of wins, draws, losses
    pass


def add_match_to_table(table, match_info):
    # updates table based on a match result
    # input is a list representing the table and
    # a tuple representing the match result
    # updates table directly, returns nothing
    pass


def generate_table(results_file_path):
    # gets path to file with results
    # generates table and fills it with values based on match results
    # returns the table as a list of dictionaries
    pass


def print_table(table):
    # prints table in a user-friendly way
    # columns:
    # rank, team, games, wins, draws, losses, goals for, goals against, points
    # does not return anything
    pass


def sort_table(table):
    # sorts table based on a key, returns a copy of the table
    pass


if __name__ == '__main__':
    table = generate_table("buli_results.txt")

    table = sort_table(table)

    print_table(table)
