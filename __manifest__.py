{
    'name': "Tournaments",
    'sequence': -99,
    'depends': ['base'],
    'application': True,
    'license': 'LGPL-3',
    'data': ['security/ir.model.access.csv',
             'views/player_detail_views.xml',
             'views/player_team_views.xml',
             'views/team_game_views.xml',
             'views/game_tournament_views.xml',
             'views/player_menus.xml']
}
