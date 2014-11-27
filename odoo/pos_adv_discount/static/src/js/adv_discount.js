function sum(numbers) {
           return _.reduce(numbers, function(result, current) {
        return result + parseFloat(current);
        }, 0);
}


function supersum(amounts,id ){

                var simplelist = _.pluck(amounts, 'id');

                if (_.include(simplelist, id) == true) {

                    var prod_disc =  _.where(amounts, {id: id});
                    var TotalDiscount = _.chain(prod_disc)
                                .groupBy("id")
                                .map(function(value, key)
                                    {
                                     return {
                                                Item: key,
                                                Total: sum(_.pluck(value, "disc"))
                                     }
                                })
                                .value();
                    }

                if (_.size(TotalDiscount)>0)
                    {
                        return TotalDiscount[0].Total ;
                    }

    return 0;

}


function convert_amount_to_pertent(amount, discount) {

     var percent = 100*discount/amount;
                if (percent>0) {
                    //return percent.toFixed(2);
                    return percent;
                }
  return 0;

}





function pos_adv_discount(instance,module){
    var QWeb = instance.web.qweb;
	var _t = instance.web._t;


    var round_pr = instance.web.round_precision;
    var round_dec = instance.web.round_decimals;

       module.Order = module.Order.extend({

           get_client_disc_id: function(){
            var client = this.get('client');
            return client ? client.POS_discount_id : "";
        },

       });



     module.OrderWidget.include({


        recurse_tree: function(item, items){

            var db = this.pos.db;
            var cat_childs = db.get_category_childs_ids(item);

                for(var c in cat_childs) {

                    if (cat_childs[c]) {

                        items.push(cat_childs[c]);
                        this.recurse_tree(cat_childs[c],items);

                    }

                }

        return items;

        },






        update_summary: function() {


            var order  = this.pos.get('selectedOrder');
            var orderlines = order.get('orderLines').models;

           // var client_disc_id = this.pos.get_order().get_client_disc_id()[0];

            var self = this;

            var customer_id = this.pos.get('selectedOrder').get_client();

            var exc_spec_rule = [];
            var amounts_all = [];
            var amounts_product = [];
            var amounts_customer = [];

            var amounts_cp_product= [];
            var amounts_cp_customer= [];

            var amounts_allcustomer_category= [];
            var amounts_cc_category= [];
            var amounts_cc_customer= [];


            var advdiscounts =  self.pos.advdiscounts;

            for(var i = 0, len = advdiscounts.length; i < len; i++){

                var advdiscount = advdiscounts[i];


//For All products and ALL customers
                if ( advdiscount.pfilter == "all" &&  advdiscount.cfilter == "all" ){

                    //amounts_all.push(advdiscount.amount);

                    amounts_all.push({id:0, disc:advdiscount.amount, val_met:advdiscount.value_method});

                }

//For All customer and Select products

                if ( advdiscount.cfilter == "all" &&    advdiscount.pfilter == "product" ){

                    for(var j = 0, lenj = advdiscount.product.length; j < lenj; j++) {

                        amounts_product.push({id:advdiscount.product[j], disc:advdiscount.amount, val_met:advdiscount.value_method});
                    }
                }

//For Select Customers and all products

                if ( advdiscount.cfilter == "customer"  &&  advdiscount.pfilter == "all" ){

                    for(var c = 0, lenc = advdiscount.partner.length; c < lenc; c++) {

                        amounts_customer.push({id:advdiscount.partner[c], disc:advdiscount.amount, val_met:advdiscount.value_method});
                    }
                }



//For All Customers and category
               if ( advdiscount.cfilter == "all" &&    advdiscount.pfilter == "category" ){


                   for(var pc = 0, lenpc = advdiscount.pcategory.length; pc < lenpc; pc++) { //selected categories for all customers.

                        //add in array category id and discount amount
                        amounts_allcustomer_category.push({id:advdiscount.pcategory[pc], disc:advdiscount.amount, val_met:advdiscount.value_method});

                        //get all subcategory (make tree to flat list with all children)
                        var items = [];
                        var cat_child = self.recurse_tree(advdiscount.pcategory[pc], items);
                        //add each record to array
                        _.each(cat_child, function(num){ amounts_allcustomer_category.push({id:num, disc:advdiscount.amount, val_met:advdiscount.value_method}); });


                   }

                }

//For Select Customers and category
                if ( advdiscount.cfilter == "customer"  &&   advdiscount.pfilter == "category"){

                    for(var cc_p = 0, lencc_p = advdiscount.pcategory.length; cc_p < lencc_p; cc_p++) {

                        amounts_cc_category.push({id:advdiscount.pcategory[cc_p], disc:advdiscount.amount, val_met:advdiscount.value_method});

                        //get all subcategory (make tree to flat list with all children)
                        var cc_items = [];
                        var cc_cat_child = self.recurse_tree(advdiscount.pcategory[cc_p], cc_items);
                        //add each record to array
                        _.each(cc_cat_child, function(num){ amounts_cc_category.push({id:num, disc:advdiscount.amount, val_met:advdiscount.value_method}); });


                  }

                    for(var cc_c = 0, lencc_c = advdiscount.partner.length; cc_c < lencc_c; cc_c++) {


                        amounts_cc_customer.push({id:advdiscount.partner[cc_c], disc:advdiscount.amount, val_met:advdiscount.value_method});
                  }

                }


//For Select Customers and Product


                if ( advdiscount.cfilter == "customer"  &&   advdiscount.pfilter == "product"){

                    for(var cp_p = 0, lencp_p = advdiscount.product.length; cp_p < lencp_p; cp_p++) {


                       amounts_cp_product.push({id:advdiscount.product[cp_p], disc:advdiscount.amount, val_met:advdiscount.value_method});
                  }

                    for(var cp_c = 0, lencp_c = advdiscount.partner.length; cp_c < lencp_c; cp_c++) {


                       amounts_cp_customer.push({id:advdiscount.partner[cp_c], disc:advdiscount.amount, val_met:advdiscount.value_method});
                  }

                }



 //For Special Rule
                if ( advdiscount.pfilter == "special" ){

                    exc_spec_rule.push(advdiscount.product_1[0]);
                }
//end
            }

var currency_rounding = this.pos.currency.rounding;

            for (var i = 0, len = orderlines.length; i < len; i++) {

                var orderline = orderlines[i];
                var dscv = orderline.get_discount();
                var product_id = orderline.get_product().id;
                var category_id = orderline.get_product().pos_categ_id[0];





                var customer_detect_for_customer = 0;
                var customer_detect_for_cp_customer = 0 ;
                var customer_detect_for_cc_customer = 0;



                var all_all_percent = [];

                var all_all_amount = [];


                if (_.include(exc_spec_rule, product_id) == true) {  //if product in special rule

                 //   dsc_for_all = 0;
                 //   dsc_for_product = 0;
                 //   dsc_for_customer = 0;
                 //   dsc_for_cp_product = 0;

                }
                else {



                    all_all_percent.push(supersum(_.where(amounts_all, {val_met: 'percent'}),0));
                    all_all_amount.push(supersum(_.where(amounts_all, {val_met: 'amount'}),0));


//get discount summ buy Product id. for example if product exist in diferent rules by product

                    all_all_percent.push(supersum(_.where(amounts_product, {val_met: 'percent'}),product_id));
                    all_all_amount.push(supersum(_.where(amounts_product, {val_met: 'amount'}),product_id));


//for all customer and select category

                    all_all_percent.push(supersum(_.where(amounts_allcustomer_category, {val_met: 'percent'}),category_id));
                    all_all_amount.push(supersum(_.where(amounts_allcustomer_category, {val_met: 'amount'}),category_id));


//If Customer Selected
                    if (customer_id != null) {

                        //all customer
                        customer_detect_for_customer = supersum(amounts_customer, customer_id.id);
                        //Select customer and select product
                        customer_detect_for_cp_customer = supersum(amounts_cp_customer, customer_id.id);
                        //Select customer and select catagory
                        customer_detect_for_cc_customer = supersum(amounts_cc_customer, customer_id.id);

                    }

//select customer

                    if (customer_detect_for_customer > 0) {

                        all_all_percent.push(supersum(_.where(amounts_customer, {val_met: 'percent'}),customer_id.id));
                        all_all_amount.push(supersum(_.where(amounts_customer, {val_met: 'amount'}),customer_id.id));

                    }



//select customer to category
                    if (customer_detect_for_cc_customer > 0) {

                        all_all_percent.push(supersum(_.where(amounts_cc_category, {val_met: 'percent'}),category_id));
                        all_all_amount.push(supersum(_.where(amounts_cc_category, {val_met: 'amount'}),category_id));

                    }


// select customer to product
                    if (customer_detect_for_cp_customer > 0) {


                        all_all_percent.push(supersum(_.where(amounts_cp_product, {val_met: 'percent'}),product_id));
                        all_all_amount.push(supersum(_.where(amounts_cp_product, {val_met: 'amount'}),product_id));

                    }

                    //////

                }


// Get base amout , after add amount off , new_amount , convert to discount.

              var sum_all_all_amount = sum(all_all_amount);

                if (sum_all_all_amount != 0) {

                    var base_amount = round_pr(orderline.get_quantity() * orderline.get_unit_price(), currency_rounding);

                    var new_amount = round_pr(orderline.get_quantity() * (orderline.get_unit_price() - sum_all_all_amount), currency_rounding);

                    var catp = convert_amount_to_pertent(base_amount,base_amount-new_amount );

                    all_all_percent.push(round_dec(catp,2));
                }




              var sum_all_all_percent = sum(all_all_percent);


                if (sum_all_all_percent > 100 ) {
                   this.pos_widget.screen_selector.show_popup('error',{
                    message: _t('Warning: '+orderline.get_product().display_name+' - Product has discount above 100%.'),
                });
                }

               if (dscv != sum_all_all_percent &&  sum_all_all_percent < 100 ) {

                    orderline.set_discount(sum_all_all_percent);

                }


            }


            this._super();
        },


    });



}
