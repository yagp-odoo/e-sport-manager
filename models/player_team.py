from odoo import models, fields


class PlayerTeam(models.Model):
    _name = "player.team"
    _description = "Here we have a team of registered players"
    _rec_name = "team_name"

    team_name = fields.Char(string="Team Name", required=True)
    player1_id = fields.Many2one(
        comodel_name="player.property", string="Add Player 1", required=True)
    player2_id = fields.Many2one(
        comodel_name="player.property", string="Add Player 2", required=True)
    player3_id = fields.Many2one(
        comodel_name="player.property", string="Add Player 3", required=True)
    player4_id = fields.Many2one(
        comodel_name="player.property", string="Add Player 4", required=True)
    player5_id = fields.Many2one(
        comodel_name="player.property", string="Add Player 5", required=True)
