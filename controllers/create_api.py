# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request
class CareCardApi(http.Controller):
    @http.route("/create/care_card_app.care_card_app", methods=["POST"], type="json", auth="public", csrf=False)
    def post_carecard(self):
        try:
            request_data = json.loads(request.httprequest.data)
            auth_header = request.httprequest.headers.get('Authorization')
            if not auth_header:
                return "Missing Authorization."        
            if not auth_header.startswith("Basic"):
                return "Invalid auth type."
            Authorization = auth_header.split(' ')[1]
            if Authorization == "YWRtaW46YWRtaW4=":  
                vals = {
                    'card_no': request_data.get('card_no'),
                    'beneficiary': request_data.get('beneficiary')
                }
                if not vals.get('card_no'):
                    return {
                        "error": "card_no is required"
                    }
                if not vals.get('beneficiary'):
                    return {
                        "error": "beneficiary name is required"
                    }
                res = request.env['care_card_app.care_card_app'].sudo().create(vals)                
                if res:
                    return {
                        "message": "The care card has been created successfully."
                    }
                return {
                    "error": "Failed to create the care card."
                }
            else:
                return {
                    "error": "Invalid Authorization."
                }
        except Exception as error:
            return {
                "error": str(error)
            }