from odoo.http import request
from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale
from .utils import has_logged

class InheritWebsiteSale(WebsiteSale):
    
    @has_logged
    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True, sitemap=WebsiteSale.sitemap_shop)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        return super().shop(page, category, search, ppg, **post)
    
    @has_logged
    @http.route('/website_form/shop.sale.order', type='http', auth="public", methods=['POST'], website=True)
    def website_form_saleorder(self, **kwargs):
        return super().website_form_saleorder(**kwargs)
    
    @has_logged
    @http.route(['/shop/<model("product.template"):product>'], type='http', auth="public", website=True, sitemap=True)
    def product(self, product, category='', search='', **kwargs):
        return super().product(product, category, search, **kwargs)
    
    @has_logged
    @http.route(['/shop/product/<model("product.template"):product>'], type='http', auth="public", website=True, sitemap=False)
    def old_product(self, product, category='', search='', **kwargs):
        return super().old_product(product, category, search, **kwargs)
    
    @has_logged
    @http.route(['/shop/change_pricelist/<model("product.pricelist"):pl_id>'], type='http', auth="public", website=True, sitemap=False)
    def pricelist_change(self, pl_id, **post):
        return super().pricelist_change(pl_id, **post)
    
    @has_logged
    @http.route(['/shop/cart'], type='http', auth="public", website=True, sitemap=False)
    def cart(self, access_token=None, revive='', **post):
        return super().cart(access_token, revive, **post)
    
    @has_logged
    @http.route(['/shop/cart/update'], type='http', auth="public", methods=['POST'], website=True)
    def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
        return super().cart_update(product_id, add_qty, set_qty, **kw)
    
    @has_logged
    @http.route(['/shop/cart/update_json'], type='json', auth="public", methods=['POST'], website=True, csrf=False)
    def cart_update_json(self, product_id, line_id=None, add_qty=None, set_qty=None, display=True):
        return super().cart_update_json(product_id, line_id, add_qty, set_qty, display=True)
    
    @has_logged
    @http.route('/shop/save_shop_layout_mode', type='json', auth='public', website=True)
    def save_shop_layout_mode(self, layout_mode):
        return super().save_shop_layout_mode(layout_mode)
    
    @has_logged
    @http.route(['/shop/address'], type='http', methods=['GET', 'POST'], auth="public", website=True, sitemap=False)
    def address(self, **kw):
        return super().address(**kw)
    
    @has_logged
    @http.route(['/shop/checkout'], type='http', auth="public", website=True, sitemap=False)
    def checkout(self, **post):
        return super().checkout(**post)
    
    @has_logged
    @http.route(['/shop/confirm_order'], type='http', auth="public", website=True, sitemap=False)
    def confirm_order(self, **post):
        return super().confirm_order(**post)
    
    @has_logged
    @http.route(['/shop/extra_info'], type='http', auth="public", website=True, sitemap=False)
    def extra_info(self, **post):
        return super().extra_info(**post)
    
    @has_logged
    @http.route(['/shop/payment'], type='http', auth="public", website=True, sitemap=False)
    def payment(self, **post):
        return super().payment(**post)
    
    @has_logged
    @http.route(['/shop/payment/transaction/',
        '/shop/payment/transaction/<int:so_id>',
        '/shop/payment/transaction/<int:so_id>/<string:access_token>'], type='json', auth="public", website=True)
    def payment_transaction(self, acquirer_id, save_token=False, so_id=None, access_token=None, token=None, **kwargs):
        return super().payment_transaction(acquirer_id, save_token, so_id, access_token, token, **kwargs)
    
    @has_logged
    @http.route('/shop/payment/token', type='http', auth='public', website=True, sitemap=False)
    def payment_token(self, pm_id=None, **kwargs):
        return super().payment_token(pm_id, **kwargs)
    
    @has_logged
    @http.route('/shop/payment/get_status/<int:sale_order_id>', type='json', auth="public", website=True)
    def payment_get_status(self, sale_order_id, **post):
        return super().payment_get_status(sale_order_id, **post)
    
    @has_logged
    @http.route('/shop/payment/validate', type='http', auth="public", website=True, sitemap=False)
    def payment_validate(self, transaction_id=None, sale_order_id=None, **post):
        return super().payment_validate(transaction_id, sale_order_id, **post)
    
    
    @has_logged
    @http.route(['/shop/terms'], type='http', auth="public", website=True, sitemap=True)
    def terms(self):
        return super().terms()
    
    @has_logged
    @http.route(['/shop/confirmation'], type='http', auth="public", website=True, sitemap=False)
    def payment_confirmation(self, **post):
        
        # sale_order_id = request.session.get('sale_last_order_id')
        # if sale_order_id:
        #     order = request.env['sale.order'].sudo().browse(sale_order_id)
        #     return request.render("website_sale.confirmation", {'order': order})
        
        return super().payment_confirmation(**post)
    
    @has_logged
    @http.route(['/shop/print'], type='http', auth="public", website=True, sitemap=False)
    def print_saleorder(self, **kwargs):
        return super().print_saleorder(**kwargs)
    
    @has_logged
    @http.route(['/shop/tracking_last_order'], type='json', auth="public")
    def tracking_cart(self, **post):
        return super().tracking_cart(**post)
    
    # 
    # @has_loggedMatched 26 to Matched 30
    # @http.route(['/shop/add_product'], type='json', auth="user", methods=['POST'], website=True)
    # def add_product(self, name=None, category=None, **post):
    #     return super().add_product(name=None, category=None, **post)

    # 
    # @has_loggedMatched 30    
    # @http.route(['/shop/change_ppr'], type='json', auth='user')
    # def change_ppr(self, ppr):
    #     request.env['website'].get_current_website().shop_ppr = ppr
    
    @has_logged
    @http.route(['/shop/country_infos/<model("res.country"):country>'], type='json', auth="public", methods=['POST'], website=True)
    def country_infos(self, country, mode, **kw):
        return super().country_infos(country, mode, **kw)
    
    @has_logged
    @http.route('/shop/products/autocomplete', type='json', auth='public', website=True)
    def products_autocomplete(term, options={}, **kwargs):
        return super().products_autocomplete(term=term, options=options, **kwargs)
    
    @has_logged
    @http.route('/shop/products/recently_viewed', type='json', auth='public', website=True)
    def products_recently_viewed(self, **kwargs):
        return super().products_recently_viewed(**kwargs)
    
    @has_logged
    @http.route('/shop/products/recently_viewed_update', type='json', auth='public', website=True)
    def products_recently_viewed_update(self, product_id, **kwargs):
        return super().products_recently_viewed_update(product_id, **kwargs)
    
    @has_logged
    @http.route('/shop/products/recently_viewed_delete', type='json', auth='public', website=True)
    def products_recently_viewed_delete(self, product_id, **kwargs):
        return super().products_recently_viewed_delete(product_id, **kwargs)