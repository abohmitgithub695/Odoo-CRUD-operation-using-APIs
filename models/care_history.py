from odoo import models, fields, api


class Care_History(models.Model):
        _name = 'care.history'
        user_id = fields.Many2one('res.users')
        care_id = fields.Many2one('models')
        old_card_status = fields.Char()
        new_card_status = fields.Char()



