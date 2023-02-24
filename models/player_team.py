from odoo import models, fields


class PlayerTeam(models.Model):
    _name = "player.team"
    _description = "Here we have a team of registered players......"
    _rec_name = "team_name"

    team_name = fields.Char(string="Team Name", required=True)
    team_logo = fields.Image(string="Team Logo")

    player1_id = fields.Many2one(
        comodel_name="player.detail", string="Add Player 1")
    player2_id = fields.Many2one(
        comodel_name="player.detail", string="Add Player 2")
    player3_id = fields.Many2one(
        comodel_name="player.detail", string="Add Player 3")
    player4_id = fields.Many2one(
        comodel_name="player.detail", string="Add Player 4")
    player5_id = fields.Many2one(
        comodel_name="player.detail", string="Add Player 5")
