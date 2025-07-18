from odoo import models, fields


class PlayerTeamMember(models.Model):
    _name = "player.team.member"
    _description = "Team Members"

    team_id = fields.Many2one("player.team", required=True)
    player_id = fields.Many2one("player.detail", required=True)
    player_name = fields.Char(related="player_id.name")
    role = fields.Char(string="Role in Team")
