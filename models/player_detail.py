from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class PlayerProperty(models.Model):
    _name = "player.detail"
    _description = "This is a Player Property Model"

    _sql_constraints = [
        ('bgmi_uniq', 'UNIQUE (bgmi_ign)',
         'This IGN is already in use.'),
        ('valo_uniq', 'UNIQUE (valo_ign)',
         'This IGN is already in use.'),
    ]

    name = fields.Char(required=True)
    e_mail = fields.Char(string="E-Mail ID")
    discord = fields.Char(string="Discord ID", required=True)
    contact = fields.Char(string="Phone Number", required=True)
    dob = fields.Date(string="Date of Birth")
    age = fields.Integer(
        string="Age", compute="_compute_age")

    like_game_ids = fields.Many2many(
        comodel_name="team.game", string="Games of Interest", store=True)

    active = fields.Boolean(string='Available to Play', default=True)

    # A player can have one nationality, but same nation can be assigned to many players,
    nation_id = fields.Many2one(
        comodel_name='res.country', string="Nationality", copy=False)

    bgmi_ign = fields.Char(string="BGMI In Game Name")
    valo_ign = fields.Char(string="Valorant In Game Name")
    csgo_ign = fields.Char(string="CSGO In Game Name")

    @api.depends("dob")
    def _compute_age(self):
        for rec in self:
            if (rec.dob):
                temp = int((fields.Date.today() - rec.dob).days / 365)
                if (temp < 18):
                    rec.age = 0
                    raise ValidationError(
                        "Please enter a valid date of birth. Only players older than 18 are allowed to play.")
                rec.age = temp
                return True
            else:
                rec.age = 0
