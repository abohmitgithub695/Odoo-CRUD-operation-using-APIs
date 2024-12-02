# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request
class UpdateApi(http.Controller):
        @http.route("/update/care_card_app.care_card_app/<int:card_no>", methods=["PUT"], type="json", auth="public", csrf=False)
        def update_cardno(self,card_no):
            try:
                auth_header = request.httprequest.headers.get('Authorization')                
                if not auth_header:
                    return "Missing Authorization."
                if not auth_header.startswith("Basic "):
                    return "Invalid auth type."
                credentials = auth_header.split(' ')[1]  
                if credentials == "YWRtaW46YWRtaW4=": 
                    card_record = request.env['care_card_app.care_card_app'].sudo().search([('card_no','=',card_no)])
                    if not card_record:
                        return {
                        "error":"Crad number does not exist"
                        }                 
                    print(card_record)
                    args = request.httprequest.data.decode()
                    vals = json.loads(args)
                    print(vals)
                    res = card_record.write(vals)
                    if res:
                        return {
                            "The care card has been updated successfully"
                        }
                    print(card_record.beneficiary)
                else:
                    return "Invalid Authorization."
            except Exception as error:
                return {
                     "message":error
                     }