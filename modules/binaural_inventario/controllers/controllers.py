# # -*- coding: utf-8 -*-
# import logging
# import json
# from werkzeug.exceptions import Forbidden, NotFound

# from odoo import _, http
# from odoo.http import request
# from odoo.addons.website_sale.controllers.main import WebsiteSale

# _logger = logging.getLogger()


# class WebsiteSaleInherited(WebsiteSale):
#     @http.route(['/shop/<model("product.template"):product>'], type='http', auth="public", website=True, sitemap=True)
#     def product(self, product, category='', search='', **kwargs):
#         if not product.can_access_from_current_website():
#             raise NotFound()

#         return request.render("website_sale.product", self._prepare_product_values(product, category, search, **kwargs))

#     @http.route(['/shop/cart/update'], type='http', auth="public", methods=['POST'], website=True)
#     def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
#         product = request.env["product.template"].search([('id', '=', int(product_id))])
#         if product.sales_policy > 1 and product.available_qty >= product.sales_policy and (int(add_qty) % product.sales_policy) != 0:
#             product.policy_error = True
#             return request.redirect(f"/shop/{product.id}")

        # res = super(WebsiteSale, self).cart_update(product_id, add_qty, set_qty, **kw)
        

# class BinauralInventario(http.Controller):
#     @http.route('/binaural_inventario/binaural_inventario/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/binaural_inventario/binaural_inventario/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('binaural_inventario.listing', {
#             'root': '/binaural_inventario/binaural_inventario',
#             'objects': http.request.env['binaural_inventario.binaural_inventario'].search([]),
#         })

#     @http.route('/binaural_inventario/binaural_inventario/objects/<model("binaural_inventario.binaural_inventario"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('binaural_inventario.object', {
#             'object': obj
#         })
