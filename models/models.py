# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
class care_card_app(models.Model):
    _name = 'care_card_app.care_card_app'
    _description = 'care_card_app.care_card_app'
    _rec_name='beneficiary'

    ref = fields.Char(default='new' , readonly=True)
    card_no = fields.Integer(string="Card number", required=True )
    roll_number = fields.Char(string="roll number" )    
    beneficiary = fields.Text(string="beneficiary name" ,required=True,size=15)
    validity_date = fields.Date(string='Validity Date', help='The date until which the care card is valid.')    
    card_status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
        ('expired', 'Expired'),
        ('closed','Closed'),
    ], string='Card Status', default='active')
    
    Card_Balance = fields.Float(string="Card Balance" , default=0.0 ,digits=(2,4))
    card_issue_date = fields.Date(string='Card Issue Date', help='The date when the care card was issued.')
    note = fields.Text(string='Notes', help='Additional information related to the care card.')
    active = fields.Boolean(default=True)
    _sql_constraints = [
        ('card_No_unique', 'unique(card_No)', 'The card_No must be unique!'),   
        ('beneficiary_unique', 'unique(beneficiary)', 'The beneficiary name must be unique!')
    ]
    @api.constrains('card_No')
    def _check_unique_card_number(self):
        for record in self:
            if self.search_count([('card_No', '=', record.card_No)]) > 1:
                raise ValidationError('The card number must be unique!')      
    @api.constrains('card_issue_date')
    def _check_issue_date(self):
        for record in self:
            if record.card_issue_date > fields.Date.today():
                raise ValidationError("The card issue date cannot be in the future!")         
    @api.constrains('card_No')
    def _check_Card_No(self):
        for record in self:
            if record.card_No < 0:
                raise ValidationError("The Card No  must be integer")
    @api.constrains('Card_Balance')
    def _check_Card_Balance(self):
        for record in self:
            if record.Card_Balance < 0:
                raise ValidationError("The Card Balance  must be integer")        
    @api.constrains('validity_date')
    def _validity_date(self):
        for record in self:
            if record.validity_date < fields.Date.today():
                raise ValidationError("The validity date must be in the future!")
    @api.model
    def _create_roll_number(self):
        for care in self.search([('roll_number','=',False)]):
            care.roll_number= "care" + str(care.id)
    def action_card_status_active(self):
        for rec in self:
            rec.create_history_record(rec.card_status,'active')
            rec.card_status="active"
            # rec.write({
            #     'card_status':'active'
            # })
    def action_card_status_inactive(self):
        for rec in self:
            rec.create_history_record(rec.card_status,'inactive')

            rec.card_status="inactive"
            # rec.write({
            #     'card_status':'inactive'
            # })
    def action_card_status_suspended(self):
        for rec in self:
            rec.create_history_record(rec.card_status,'suspended')
            rec.card_status="suspended"
            # rec.write({
            #     'card_status':'suspended'
            # })
    def action_card_status_expired(self):
        for rec in self:
            rec.create_history_record(rec.card_status,'expired')
            rec.card_status="expired"
            # rec.write({
            #     'card_status':'expired'
            # })
    def action_card_status_closed(self):
        for rec in self:
            rec.card_status="closed"
            # rec.write({
            #     'card_status':'closed'
            # })
    def action(self):
          print(self.env['care_card_app.care_card_app'].search([('beneficiary','=','salem')]))
          print(self.env['care_card_app.care_card_app'].search([('beneficiary','!=','salem')]))
          print(self.env['care_card_app.care_card_app'].search([('beneficiary','!=','abdulrahmannjn'),('card_no','=','99')]))
          print(self.env['care_card_app.care_card_app'].search(['|',('beneficiary','!=','abdulrahmannjn'),('card_no','=','99')]))      
      
      
      
            # rec.write({
            #     'card_status':'closed'
            # })
    def action_env(self):
        print(self.env)
        print(self.env.user)
        print(self.env.user.name)
        print(self.env.user.login)        
        print(self.env.user.id)
        print(self.env.company.name)
        print(self.env.company.street)
        print(self.env.context)
        print(self.env.cr )
        print(self.env['models'].create({
            'card_no':44,
            'beneficiary':'salomey'

        }))
        print(self.env['models'].serach([]))
        print(self.env.user.id)

    @api.model
    def create(self,vals):
        res = super(care_card_app,self).create(vals)
        if res.ref=='new':
           res.ref = self.env['ir.sequence'].next_by_code('sequence_care')
        return res
    def create_history_record(self,old_card_status,new_card_status):
        for rec in self:
            rec.env['care.history'].create({
                'user_id':rec.env.uid,
                'care_id':rec.env.uid,
                'old_card_status':old_card_status,
                'new_card_status':new_card_status

            })
    def action_button(self):
        print("hellow abdoooooooooo")
