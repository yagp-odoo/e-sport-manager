from odoo import models, fields


class PlayerProperty(models.Model):
    _name = "player.property"
    _description = "This is a Player Property Model"
    _rec_name = "in_game_name"

    in_game_name = fields.Char(string="In Game Name", required=True)

    e_mail = fields.Char(string="E-Mail ID", required=True)
    discord = fields.Char(string="Discord ID", required=True)
