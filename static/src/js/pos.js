odoo.define('pos_receipt.pos_model_extend', function (require) {
    "use strict";

	var models = require('point_of_sale.models');

    models.PosModel = models.PosModel.extend({
        after_load_server_data: function() {
            this.load_orders();
            this.set_start_order();
            if(this.config.use_proxy){
                if (this.config.iface_customer_facing_display) {
                    this.on('change:selectedOrder', this.send_current_order_to_customer_facing_display, this);
                }

                return this.connect_to_proxy();
            }
            //INI.MOD.MONTAG 22.04.11
            //MANDA MENSAJE A CAJEROS CADA N MILISEGUNDOS
            setInterval(function () {
            alert("¡RECUERD SACAR EL EFECTIVO DE LA CAJA CADA 4 HORAS!")
            }, 14400000);
            //FIN.MOD.MONTAG 22.04.11
            return Promise.resolve();
        }
    });
});