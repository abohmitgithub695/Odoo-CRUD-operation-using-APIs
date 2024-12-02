# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request
class ReadApi(http.Controller):
    @http.route("/read/care_card_app.care_card_app/<int:card_no>", methods=["GET"], type="http", auth="public", csrf=False)
    def read_cardno(self, card_no):
        try:
            auth_header = request.httprequest.headers.get('Authorization')            
            if not auth_header:
                return "Missing Authorization."
            if not auth_header.startswith("Basic "):
                return "Invalid auth type."
            Authorization = auth_header.split(' ')[1]  
            if Authorization == "YWRtaW46YWRtaW4=":  
                card_record = request.env['care_card_app.care_card_app'].sudo().search([('card_no', '=', card_no)])   
                if not card_record:
                    return "Card number does not exist."
                response_data = {
                    "card_no": card_record.card_no,
                    "roll_number": card_record.roll_number,
                    "beneficiary": card_record.beneficiary,
                    "card_status": card_record.card_status,
                    "Card_Balance": card_record.Card_Balance,
                    "note": card_record.note
                }      
                return http.Response(json.dumps(response_data))
            else:
                return "Invalid Authorization."
        except Exception as error:
            return error