function pos_customer_at(instance, module){

    var PosModelSuper = module.PosModel
    module.PosModel = module.PosModel.extend({
        load_server_data: function(){
            var self = this;
            var loaded = PosModelSuper.prototype.load_server_data.call(this);

            loaded = loaded.then(function(){
                return self.fetch(
                    'res.partner',
                    ['POS_discount_id'],
                    {}
                );

            }).then(function(partnersd){
                $.each(partnersd, function()
                {
                    $.extend(self.db.get_partner_by_id(this.id) || {}, this)
                })
                return $.when()
            })
            return loaded;
        },

    })
}

function pos_customer_disc_at(instance, module){


    module.PosModel.prototype.models.push({


            model:  'pos.customer.dsc.c',
            fields: ['id','name','value'],
            domain: null,
            loaded: function(self,customerdsc){ self.customerdsc = customerdsc; },



    });

    module.PosModel = module.PosModel.extend({

        get_customerdsc: function () {
            return this.customerdsc;
        },

        get_customerdsc_value: function (id) {

            var customerdsc = this.customerdsc;
            var dfg = _.where(customerdsc, {id: id,})
            return dfg[0].value;
        },

    });




}

