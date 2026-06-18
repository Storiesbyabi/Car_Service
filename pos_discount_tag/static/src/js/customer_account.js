
import { patch } from "@web/core/utils/patch";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";

patch(PaymentScreen.prototype,{
    get CustomerAcc(){
        console.log('pay',this.currentOrder.payment_ids)
    }
});