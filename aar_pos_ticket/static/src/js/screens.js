"use strict";
/*
    License: OPL-1
    author: farooq@aarsol.com   
*/
odoo.define('aar_pos_ticket.screens', function (require) {

    var models = require('point_of_sale.models');
    var screens = require('point_of_sale.screens');
    var core = require('web.core');
    var utils = require('web.utils');
    var round_pr = utils.round_precision;
    var _t = core._t;
    var gui = require('point_of_sale.gui');
    var qweb = core.qweb;

   
    screens.ReceiptScreenWidget.include({

        print: function() {
        var self = this;

        if (!this.pos.config.iface_print_via_proxy) { // browser (html) printing

            // The problem is that in chrome the print() is asynchronous and doesn't
            // execute until all rpc are finished. So it conflicts with the rpc used
            // to send the orders to the backend, and the user is able to go to the next
            // screen before the printing dialog is opened. The problem is that what's
            // printed is whatever is in the page when the dialog is opened and not when it's called,
            // and so you end up printing the product list instead of the receipt...
            //
            // Fixing this would need a re-architecturing
            // of the code to postpone sending of orders after printing.
            //
            // But since the print dialog also blocks the other asynchronous calls, the
            // button enabling in the setTimeout() is blocked until the printing dialog is
            // closed. But the timeout has to be big enough or else it doesn't work
            // 1 seconds is the same as the default timeout for sending orders and so the dialog
            // should have appeared before the timeout... so yeah that's not ultra reliable.

            this.lock_screen(true);

            setTimeout(function(){
                self.lock_screen(false);
            }, 1000);

            this.print_web();
        } else {    // proxy (xml) printing
            this.print_xml();
            this.lock_screen(false);
        }
//        this.$('.button.print').unbind("click").bind("click", function(){
//        alert("this is Overridden click event!");
//        });
        },
        renderElement: function () {
            var self = this;
            var is_printed = false ;
            var current_order = null ;
            var prev_oder = self.pos.get_order();

            this._super();
            this.$('.back_order').click(function () {
                var order = self.pos.get_order();
                if (order) {
                    self.pos.gui.show_screen('products');
                }

            });
            //  allow printing only once
            if (this.pos.config.print_once){
                this.$('.button.print').unbind("click").bind("click", function(){
                    var current_order = self.pos.get_order();
                    if (current_order != prev_oder){
                        is_printed = false ;
                        prev_oder = current_order;
                    }
                    if (!is_printed){
                        if (!self._locked) {
                            self.print();
                            is_printed = true ;
                        }
                    }
                    else{
                        self.pos.gui.show_popup('error',{
                            title: _t('طباعة متكررة '),
                            body:  _t("لا يمكنك الطباعة اكثر من مره "),

                        });
                    }
            });
            }
        },
        show: function () {
            this._super();
            try {
                JsBarcode("#barcode", this.pos.get('selectedOrder').ean13, {
                    format: "EAN13",
                    displayValue: true,
                    fontSize: 20
                });
            } catch (error) {
            }
        },

        
    });

    

});
