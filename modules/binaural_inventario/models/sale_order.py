import logging

from odoo import _, api
from odoo.exceptions import ValidationError
from odoo.models import Model

_logger = logging.getLogger()


class SaleOrderInherited(Model):
    _inherit = "sale.order"

    @api.constrains("order_line")
    def _constrains_order_line_sales_policy(self):
        for sale_order in self:
            if len(sale_order.order_line):
                product = self._check_order_lines(sale_order.order_line)
                if product:
                    raise ValidationError(_(f"El producto {product.name} tiene una política de ventas, la cantidad a vender" 
                                            f"debe ser un múltiplo de sí mismo o {product.sales_policy}"))

    # @api.constrains("website_order_line")
    # def _constrains_website_order_line_sales_policy(self):
    #     for sale_order in self:
    #         if len(sale_order.website_order_line):
    #             product = self._check_order_lines(sale_order.website_order_line)
    #             if product:
    #                 raise ValidationError(_(f"El producto {product.name} tiene una política de ventas, la cantidad a vender" 
    #                                         f"debe ser un múltiplo de sí mismo o {product.sales_policy}"))

    def _check_order_lines(self, sale_order_line):
        for line in sale_order_line:
            product = line.product_id
            if product.sales_policy > 1 and product.available_qty >= product.sales_policy and (line.product_uom_qty % product.sales_policy) != 0:
                return product
        
        return False