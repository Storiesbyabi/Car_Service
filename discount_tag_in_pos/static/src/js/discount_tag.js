import { usePos } from "@point_of_sale/app/hooks/pos_hook";
import { ProductCard } from "@point_of_sale/app/components/product_card/product_card";
import { patch } from "@web/core/utils/patch";


patch(ProductCard.prototype,{
    get DiscountTag(){
        this.props
    }


});