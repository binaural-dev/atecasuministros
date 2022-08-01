odoo.define("ateca_barcode.LinesWidgetExtend", function(require) {
	"use strict";
	let LinesWidget = require("stock_barcode.LinesWidget");
	let core = require("web.core");

	let QWeb = core.qweb;

	let LinesWidgetExtend = LinesWidget.include({
		template: "stock_barcode_lines_widget",
		events: _.extend({}, LinesWidget.prototype.events, {}),
		_renderLines: function() {
			let $next = this.$(".o_next_page");
			let $previous = this.$(".o_previous_page");
			let $addLine = this.$(".o_add_line");

			$previous.toggleClass("o_hidden");
			$next.toggleClass("o_hidden");
			$addLine.toggleClass("o_hidden");

			this._super.apply(this, arguments);
		},
	});
});
