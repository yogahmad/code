START_GAMEWEEK_MUST_BE_LESS_THAN_OR_EQUAL_TO_END_GAMEWEEK = (
    "Start Gameweek must be less then or equal to End Gameweek"
)

_FPL_BASE_URL = "https://fantasy.premierleague.com/api"
FPL_MATCH_API_URL = "{}/fixtures/".format(_FPL_BASE_URL)
FPL_BOOTSTRAP_STATIC_API_URL = "{}/bootstrap-static/".format(_FPL_BASE_URL)


def FPL_PLAYERS_POINT_API_URL(player_id):
    return "{}/element-summary/{}/".format(_FPL_BASE_URL, player_id)


def FPL_PLAYERS_POINT_BY_GAMEWEEK_API_URL(gameweek):
    return "{}/event/{}/live/".format(_FPL_BASE_URL, gameweek)


def UNDERSTAT_MATCH_API(match_id):
    return "https://understat.com/match/{}".format(match_id)


def UNDERSTAT_TEAM_API(team_id):
    return "https://understat.com/team/{}/2021".format(team_id)
