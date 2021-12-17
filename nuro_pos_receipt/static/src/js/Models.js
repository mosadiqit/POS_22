odoo.define('nuro_pos_receipt.models', function (require) {
    "use strict";

    var models = require('point_of_sale.models');

    var _super_Orderline = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
    export_for_printing: function () {
            var receipt_line = _super_Orderline.export_for_printing.apply(this, arguments);
            if (this.product.barcode) {
                receipt_line['product_barcode'] = this.product.barcode;
            }


            return receipt_line;
        }
    });
});