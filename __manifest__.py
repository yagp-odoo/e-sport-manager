{
    'name': "Tournaments",
    'sequence': -99,  # Always #1
    'depends': ['base'],
    'author': 'Yagnik ツ',
    'application': True,
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/player_detail_views.xml',
        'views/player_team_views.xml',
        'views/team_game_views.xml',
        'views/game_tournament_views.xml',
        'views/player_menus.xml'
    ]
}


# TODOs
"""
[IMP] `game.tournament` -> add prize_pool, sponsor_ids, currency_id, stream_url
[ADD] `match.participation` or `player.stats` -> Track Kills, deaths, assists, MVPs, games played...
[ADD] `tournament.type` -> Ex: Solo, Duo, Squad, 5v5, Deathmatch, etc
[IMP] `player.detail` -> Social LINKS!!! + Player Remarks(Like Useful for Banned Player, hmm?)
[IMP] `game.tournament` -> Free or Paid Tournament

Extras in Future(maybe): Total tournaments played/won per player, Team win rates, Game popularity by platform
Match Result Reporting with Proof -> Screenshot, MVP Name, Score breakdown
"""
