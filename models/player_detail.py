from odoo import models, fields


class PlayerProperty(models.Model):
    _name = "player.detail"
    _description = "This is a Player Property Model"

    name = fields.Char(required=True)
    e_mail = fields.Char(string="E-Mail ID")
    discord = fields.Char(string="Discord ID", required=True)
    contact = fields.Char(string="Phone Number...", required=True)

    like_game_ids = fields.Many2many(
        comodel_name="team.game", string="Games of Interest")
