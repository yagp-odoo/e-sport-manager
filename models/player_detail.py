from odoo import models, fields, api
from odoo.exceptions import ValidationError


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
    age = fields.Integer(string="Age", compute="_compute_age")
    like_game_ids = fields.Many2many("team.game", string="Games of Interest", store=True)
    available = fields.Boolean(string='Available to Play', default=True)
    nation_id = fields.Many2one('res.country', string="Nationality", copy=False)

    # In-Game Name
    bgmi_ign = fields.Char(string="BGMI")
    valo_ign = fields.Char(string="Valorant")
    csgo_ign = fields.Char(string="CS:GO")

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
