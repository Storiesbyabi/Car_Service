import { usePos } from "@point_of_sale/app/hooks/pos_hook";
import { ProductCard } from "@point_of_sale/app/components/product_card/product_card";
import { patch } from "@web/core/utils/patch";
import { Orderline } from "@point_of_sale/app/components/orderline/orderline";


patch(ProductCard.prototype,{
    get DiscountTag(){

        console.log('dis',this.props.product.discount_tag)
        if(this.props.product.discount_tag) {
            return this.props.product.discount_tag
        }
    }
});

// patch(OrderDisplay.prototype,{
//         get order() {
//             console.log('order_line', this.getOrderLines())
//         }
// })