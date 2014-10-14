
function pos_customer_discount(instance,module){
    var QWeb = instance.web.qweb;
	var _t = instance.web._t;

       module.Order = module.Order.extend({

           get_client_disc_id: function(){
            var client = this.get('client');
            return client ? client.POS_discount_id : "";
        },


    });



     module.OrderWidget.include({


        update_summary: function() {


            var order  = this.pos.get('selectedOrder');
            var orderlines = order.get('orderLines').models;

            var client_disc_id = this.pos.get_order().get_client_disc_id()[0];

            if (client_disc_id) {

                var client_disc_value = this.pos.get_customerdsc_value(client_disc_id);


                for (var i = 0, len = orderlines.length; i < len; i++) {

                    var orderline = orderlines[i];
                    var dscv = orderline.get_discount();

                    if (dscv == 0) {

                        orderline.set_discount(client_disc_value);

                    }
                    ;

                }

            }

            var self = this;
            this._super();
        },


    });



}
