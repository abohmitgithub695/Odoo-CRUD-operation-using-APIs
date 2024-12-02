# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
class ReadApi(http.Controller):
    @http.route("/api/test", methods=["GET"], type="http", auth="user", csrf=False)
    def test_api(self):
        try:
            auth_header = request.httprequest.headers.get('Authorization')            
            if not auth_header:
                return "Missing Authorization ."
            if not auth_header.startswith("Basic"):
                return "Invalid auth type must be (basic auth)."
            Authorization = auth_header.split(' ')
            if Authorization == "YWRtaW46YWRtaW4=":  
                return "valid Authorization"
            else:
                return "Invalid Authorization check username or password."
        except Exception as error:
            return error