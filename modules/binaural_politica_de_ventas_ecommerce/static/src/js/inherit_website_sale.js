odoo.define("binaural_politica_de_ventas_ecommerce.inherit_website_sale", function(require) {
    'use strict';

    var core = require("web.core");
    var publicWidget = require("web.public.widget");
    var WebsiteSaleInherited = publicWidget.registry.WebsiteSale;

    var _t = core._t;

    WebsiteSaleInherited.include({
        _onClickAddCartJSON: function (ev){
            return this.onBinClickAddCartJSON(ev);
        },
        onBinClickAddCartJSON: function (ev) {
            ev.preventDefault();
            console.log("thissssssssss");
            var $link = $(ev.currentTarget);
            var $inputQuantity = $link.closest('.input-group').find("input.quantity");
            var $salesPolicyInput = $link.closest('.input-group').find('input.sales_policy');
            console.log($salesPolicyInput);
            // var min = parseFloat($inputQuantity.data("min") || 0);
            var salesPolicy = parseFloat($salesPolicyInput.val());
            var max = parseFloat($inputQuantity.data("max") || Infinity);
            var previousQty = parseFloat($inputQuantity.val() || 0, 10);
            var quantity = ($link.has(".fa-minus").length ? ((salesPolicy)*-1) : salesPolicy) + previousQty;
            var newQty = quantity > salesPolicy ? (quantity < max ? quantity : max) : salesPolicy;
    
            if (newQty !== previousQty) {
                $inputQuantity.val(newQty).trigger('change');
            }
            return false;
        }
    });
});