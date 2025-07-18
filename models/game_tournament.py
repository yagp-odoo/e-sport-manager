from odoo import models, fields


class GameTournament(models.Model):
    _name = "game.tournament"
    _description = "Tournaments listed here..."

    name = fields.Char(string='Tournament Title')
    game = fields.Many2one("team.game", string='Game')
    teams_registered = fields.Many2one("player.team", string='Team Name')
    scheduled_date = fields.Datetime(default=fields.Date.today())
    state = fields.Selection(string='State of tournament',
        selection=[('created', 'Created'),
                   ('live', 'Live & Running!'),
                   ('ended', 'Ended'),
                   ('done', 'Payments Done')],
        copy=False,
        default='created'
    )

    def btn_start(self):
        self.state = "live"

    def btn_end(self):
        self.state = "ended"

    def btn_pay(self):
        self.state = "done"
