from odoo import models, fields


class PlayerTeam(models.Model):
    _name = "player.team"
    _description = "Here we have a team of registered players......"
    _rec_name = "team_name"

    team_name = fields.Char(string="Team Name", required=True)
    team_logo = fields.Image(string="Team Logo")
    players_id = fields.One2many("player.team.member", "team_id", string="Player(s)")
