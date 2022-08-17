from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.static import players
import json

def get_curry():
	response = shotchartdetail.ShotChartDetail(
	    team_id=0,
	    player_id=201939,
	    season_nullable='2021-22',
	    context_measure_simple = 'FGA', #<-- Default is 'PTS' and will only return made shots, but we want all shot attempts
	    season_type_all_star='Regular Season'
	)
	json_text = response.get_json()
	content = json.loads(json_text)
	return content


def get_ShotData(team_id=0,	player_id=201939, season_nullable='2021-22', context_measure_simple = 'FGA', season_type_all_star='Regular Season'):
	response = shotchartdetail.ShotChartDetail(
	    team_id=0,
	    player_id=player_id,
	    season_nullable='2021-22',
	    context_measure_simple = 'FGA', #<-- Default is 'PTS' and will only return made shots, but we want all shot attempts
	    season_type_all_star='Regular Season'
	)

	json_text = response.get_json()
	content = json.loads(json_text)
	return content

def get_playersdata():
	nba_players = players.get_players()

	return nba_players