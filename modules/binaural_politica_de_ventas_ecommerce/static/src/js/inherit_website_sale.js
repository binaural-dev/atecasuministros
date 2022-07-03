odoo.define("binaural_politica_de_ventas_ecommerce.inherit_website_sale", function(require) {
    'use strict';

    var core = require("web.core");
    var ajax = require('web.ajax');

    var VariantMixin = require('sale.VariantMixin');
    var publicWidget = require("web.public.widget");

    var WebsiteSaleInherited = publicWidget.registry.WebsiteSale;
    var QWeb = core.qweb;
    var xml_load = ajax.loadXML(
        '/binaural_politica_de_ventas_ecommerce/static/src/xml/website_sale_stock_product_availability.xml',
        QWeb
    );
    var _t = core._t;

    WebsiteSaleInherited.include({
        events: _.extend({}, WebsiteSaleInherited.prototype.events, {
            'change input.quantity': '_onChangeSalesPolicy',
        }),
        _onClickAddCartJSON: function (ev){
            return this.onBinClickAddCartJSON(ev);
        },
        onBinClickAddCartJSON: function (ev) {
            ev.preventDefault();
            let $link = $(ev.currentTarget);
            let $inputQuantity = $link.closest('.input-group').find("input.quantity");
            let $salesPolicyInput = $link.closest('.input-group').find('input.sales_policy');
            // var min = parseFloat($inputQuantity.data("min") || 0);
            const salesPolicy = parseFloat($salesPolicyInput.val());
            const max = parseFloat($inputQuantity.data("max") || Infinity);
            const previousQty = parseFloat($inputQuantity.val() || 0, 10);
            const quantity = ($link.has(".fa-minus").length ? ((salesPolicy)*-1) : salesPolicy) + previousQty;
            const newQty = quantity > salesPolicy ? (quantity < max ? quantity : max) : salesPolicy;
            
            if (newQty !== previousQty) {
                console.log(max);
                console.log(newQty);
                $inputQuantity.val(newQty).trigger('change');
            }

            return false;
        },
        _onChangeSalesPolicy: function (ev) {
            let $input = $(ev.currentTarget);
             
            const currentQty = $input.val();
            const salesPolicy = $input.closest('.input-group').find('input.sales_policy').val();

            if ((currentQty % salesPolicy) !== 0) {
                const newQty = Math.round(currentQty / salesPolicy) * salesPolicy;
                $input.val(newQty);
            }
        }
    });

    VariantMixin._onChangeCombinationStock = function (ev, $parent, combination) {
        var product_id = 0;
        // needed for list view of variants
        if ($parent.find('input.product_id:checked').length) {
            product_id = $parent.find('input.product_id:checked').val();
        } else {
            product_id = $parent.find('.product_id').val();
        }
        var isMainProduct = combination.product_id &&
            ($parent.is('.js_main_product') || $parent.is('.main_product')) &&
            combination.product_id === parseInt(product_id);

        if (!this.isWebsite || !isMainProduct){
            return;
        }

        var qty = $parent.find('input[name="add_qty"]').val();
        var salesPolicy = $parent.find('input[name="sales_policy"]').val();

        $parent.find('#add_to_cart').removeClass('out_of_stock');
        $parent.find('#buy_now').removeClass('out_of_stock');
        if (combination.product_type === 'product' && _.contains(['always', 'threshold'], combination.inventory_availability)) {
            combination.virtual_available -= parseInt(combination.cart_qty);
            if (combination.virtual_available < 0) {
                combination.virtual_available = 0;
            }
            // Handle case when manually write in input
            if (qty > combination.virtual_available) {
                var $input_add_qty = $parent.find('input[name="add_qty"]');
                if ((combination.virtual_available % salesPolicy) !== 0) {
                    const newQty = Math.round(combination.virtual_available / salesPolicy) * salesPolicy;
                    combination.va_not_multiple = true;
                    $input_add_qty.val(newQty);
                    $parent.find('#add_to_cart').addClass('disabled out_of_stock');
                    $parent.find('#buy_now').addClass('disabled out_of_stock');
                } else {
                    qty = combination.virtual_available || 1;
                    $input_add_qty.val(qty);     
                }
            }
            if (qty > combination.virtual_available
                || combination.virtual_available < 1 || qty < 1) {
                $parent.find('#add_to_cart').addClass('disabled out_of_stock');
                $parent.find('#buy_now').addClass('disabled out_of_stock');
            }
        }

        xml_load.then(function () {
            $('.oe_website_sale')
                .find('.availability_message_' + combination.product_template)
                .remove();

            var $message = $(QWeb.render(
                'website_sale_stock.product_availability',
                combination
            ));
            $('div.availability_messages').html($message);
        });
    };
});

