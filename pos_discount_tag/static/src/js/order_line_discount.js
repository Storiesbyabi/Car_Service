import { usePos } from "@point_of_sale/app/hooks/pos_hook";
import { patch } from "@web/core/utils/patch";
import { Orderline } from "@point_of_sale/app/components/orderline/orderline";



patch(Orderline.prototype,{
        setup() {


            // this.line.setDiscount(this.props.line.product_id.discount_tag)
            super.setup();
            const product = this.props.line.product_id;
            console.log("ghb", product.discount_tag)

            if(product && product.discount_tag){
                this.line.setDiscount(product.discount_tag)
            }
        }
        // get line() {
        //     console.log('order_line')
        //     super.line();
        //
        // }
})