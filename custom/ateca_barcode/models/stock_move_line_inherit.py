from odoo import api, models, _
from odoo.exceptions import UserError


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    @api.constrains("qty_done")
    def _check_qty_done(self):
        for move_line in self:
            if move_line.qty_done > move_line.product_uom_qty:
                raise UserError(_("No puedes registrar más de la cantidad reservada."))
