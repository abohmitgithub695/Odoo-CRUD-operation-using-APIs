# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
class DeleteApi(http.Controller):
    @http.route("/delete/care_card_app.care_card_app/<int:card_no>", methods=["DELETE"], type="http", auth="public", csrf=False)
    def delete_cardno(self, card_no):
        try:
            auth_header = request.httprequest.headers.get('Authorization')            
            if not auth_header:
                return "Missing Authorization."
            if not auth_header.startswith("Basic"):
                return "Invalid auth type."
            Authorization = auth_header.split(' ')[1]  
            if Authorization == "YWRtaW46YWRtaW4=":
                card_record = request.env['care_card_app.care_card_app'].sudo().search([('card_no', '=', card_no)])   
                if not card_record:
                    return "Card number does not exist."
                card_record.unlink()
                return"The care card has been deleted successfully"      
            else:
                return "Invalid Authorization."
        except Exception as error:
            return error