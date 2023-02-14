from odoo import models, fields


class TeamGames(models.Model):
    _name = "team.game"
    _description = "This is the list of games available on the platfrom..."

    name = fields.Char(string='Game Name')
    players_required = fields.Integer(
        string='Players Required', default=5)

    platform = fields.Selection([("M", "Mobile/Tablet"), ("PC", "Laptop/PC")])
