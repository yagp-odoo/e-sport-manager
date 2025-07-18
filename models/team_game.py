from odoo import models, fields

PLATFORM_SELECTION = [
    ('mobile', 'Mobile/Tablet'),
    ('pc', 'Laptop/PC'),
    ('console', 'Console(PlayStation, Xbox, Nintendo Switch)'),
]

class TeamGames(models.Model):
    _name = "team.game"
    _description = "This is the list of games available on the platfrom..."


    name = fields.Char(string='Game Name')
    players_required = fields.Integer(string='Players Required', default=5)
    platform = fields.Selection(PLATFORM_SELECTION)
