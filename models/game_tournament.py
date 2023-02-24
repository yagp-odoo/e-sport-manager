from odoo import models, fields


class GameTournament(models.Model):
    _name = "game.tournament"
    _description = "Tournaments listed here..."

    name = fields.Char(string='Tournament Title')
    game = fields.Many2one(comodel_name="team.game", string='Game')
    teams_registered = fields.Many2one(
        comodel_name="player.team", string='Team Name')
    scheduled_date = fields.Datetime(default=fields.Date.today())

    state = fields.Selection(
        string='State of tournament',
        selection=[('C', 'Created'),
                   ('L', 'Live & Running!'), ('E', 'Ended'), ('P', 'Payments Done')],
        copy=False,
        default='C'
    )

    def btn_start(self):
        self.state = "L"

    def btn_end(self):
        self.state = "E"

    def btn_pay(self):
        self.state = "P"
