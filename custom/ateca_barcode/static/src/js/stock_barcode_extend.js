odoo.define("ateca_barcode.ClientAction", function(require) {
	"use strict";
	let core = require("web.core");
	let ClientAction = require("stock_barcode.ClientAction");

	let _t = core._t;

	let ClientActionExtend = ClientAction.include({
		_step_product: async function(barcode, linesActions) {
			console.log("Escaneando");
			let self = this;
			this.currentStep = 'product';
			this.stepState = $.extend(true, {}, this.currentState);
			let errorMessage;

			let product = await this._isProduct(barcode);
			if (product) {
				if (product.tracking !== 'none' && self.requireLotNumber) {
					this.currentStep = 'lot';
				}
				let res = this._incrementLines({ 'product': product, 'barcode': barcode });
				if (res.externalLine) {
					return Promise.reject(_t("El producto no puede ser agregado a la linea."));
				} else {
					if (product.tracking === 'none' || !self.requireLotNumber) {
						linesActions.push([this.linesWidget.incrementProduct, [res.id || res.virtualId, product.qty || 1, this.actionParams.model]]);
					} else {
						linesActions.push([this.linesWidget.incrementProduct, [res.id || res.virtualId, 0, this.actionParams.model]]);
					}
				}
				this.scannedLines.push(res.id || res.virtualId);
				return Promise.resolve({ linesActions: linesActions });
			} else {
				let success = function(res) {
					return Promise.resolve({ linesActions: res.linesActions });
				};
				let fail = function(specializedErrorMessage) {
					self.currentStep = 'product';
					if (specializedErrorMessage) {
						return Promise.reject(specializedErrorMessage);
					}
					if (!self.scannedLines.length) {
						if (self.groups.group_tracking_lot) {
							errorMessage = _t("You are expected to scan one or more products or a package available at the picking's location");
						} else {
							errorMessage = _t('You are expected to scan one or more products.');
						}
						return Promise.reject(errorMessage);
					}

					let destinationLocation = self.locationsByBarcode[barcode];
					if (destinationLocation) {
						return self._step_destination(barcode, linesActions);
					} else {
						errorMessage = _t('You are expected to scan more products or a destination location.');
						return Promise.reject(errorMessage);
					}
				};
				return self._step_lot(barcode, linesActions).then(success, function() {
					return self._step_package(barcode, linesActions).then(success, fail);
				});
			}
		},

		_incrementLines: function(params) {
			let line = this._findCandidateLineToIncrement(params);
			const incrementQty = 1;
			let isExternalLine = true;

			// De aqui para abajo son las modificaciones con respecto a la vista para incrementar
			// lineas con el codigo de barras.


			if (line) {
				isExternalLine = false;
				// Update the line with the processed quantity.
				if (
					params.product.tracking === "none" ||
					params.lot_id ||
					params.lot_name ||
					!this.requireLotNumber
				) {
					if (this._isPickingRelated()) {
						line.qty_done += incrementQty;
						if (params.package_id) {
							line.package_id = params.package_id;
						}
						if (params.result_package_id) {
							line.result_package_id = params.result_package_id;
						}
					} else if (this.actionParams.model === "stock.inventory") {
						line.product_qty += params.product.qty || 1;
					}
				}
			}
			if (this._isPickingRelated()) {
				if (params.lot_id) {
					line.lot_id = [params.lot_id];
				}
				if (params.lot_name) {
					line.lot_name = params.lot_name;
				}
			} else if (this.actionParams.model === "stock.inventory") {
				if (params.lot_id) {
					line.prod_lot_id = [params.lot_id, params.lot_name];
				}
			}
			return {
				id: line.id,
				virtualId: line.virtual_id,
				lineDescription: line,
				externalLine: isExternalLine,
			};
		},
	});

	core.action_registry.add(
		"ateca_barcode_client_action_extend",
		ClientActionExtend
	);

	return ClientActionExtend;
});
