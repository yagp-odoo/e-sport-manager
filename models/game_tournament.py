from odoo import models, fields


class GameTournament(models.Model):
    _name = "game.tournament"
    _description = "Tournaments listed here..."

    name = fields.Char(string='Tournament Title')
    game = fields.Many2one(comodel_name="team.game", string='Game')
    teams_registered = fields.Many2one(
        comodel_name="player.team", string='Team Name')
    scheduled_date = fields.Datetime()

    state = fields.Selection(
        string='State of tournament',
        selection=[('D', 'Draft'), ('C', 'Created'),
                   ('L', 'Live & Running!'), ('E', 'Ended'), ('P', 'Payments Done')],
        copy=False,
        default='D'
    )
