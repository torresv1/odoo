openerp.pos_line = function(instance){

    var module = instance.point_of_sale;

    pos_categories_at(instance, module);
    openerp_posline_showline(instance,module);


};
