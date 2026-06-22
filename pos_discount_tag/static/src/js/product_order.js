import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";
import { PosStore } from "@point_of_sale/app/services/pos_store";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { Orderline } from "@point_of_sale/app/components/orderline/orderline";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";


patch(PosStore.prototype,{
    async selectOrderLine(order,line){



        console.log('qty',line.qty)
        console.log('line',line.product_id.prd_quantity)


           if(line.product_id.prd_quantity){
               if(line.qty > line.product_id.prd_quantity){

                this.dialog.add(AlertDialog, {
                    title: _t("Product Qty limit"),
                    body: _t("Product Qty limit has exceed"),
                });

        }

           }
           await super.selectOrderLine(order,line)
    }
})


patch(ProductScreen.prototype,{
     onNumpadClick(buttonValue){
         super.onNumpadClick(buttonValue)

         const order_line=this.pos.getOrder().getSelectedOrderline()
         const prd_qty = order_line.product_id.product_tmpl_id.prd_quantity

         console.log('ol',order_line.qty)
         const unitpart =order_line.getQuantityStr().unitPart
         console.log('unuit',unitpart)

        console.log('getnum',prd_qty)
         if(prd_qty > 0) {
             if (order_line.qty > prd_qty) {





                   this.dialog.add(AlertDialog, {
                       title: _t("Product Qty limit"),
                       body: _t("Product Qty limit has exceed"),
                   });

             }
         }

    }
})