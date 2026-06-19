
import { patch } from "@web/core/utils/patch";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { rpc } from "@web/core/network/rpc";
import { useState} from "@odoo/owl";

import { _t } from "@web/core/l10n/translation";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

patch(PaymentScreen.prototype,{


    get CustomerAccLimit(){
        const partner = this.currentOrder.partner_id
        const customer_acc = this.payment_methods_from_config
        const order =this.currentOrder._prices.original.taxDetails.base_amount
        const payment_lines= this.paymentLines
        // console.log('partner',partner.customer_limit)
        // console.log('Order',order)
        let len = payment_lines.length
            for(let i=0;i<len;i++) {
                console.log('id',payment_lines[i].payment_method_id.id)
                if(payment_lines[i].payment_method_id.id == 3){
                    console.log('2345678',partner.customer_limit)
                    if(payment_lines[i].amount > partner.customer_limit){
                         this.dialog.add(AlertDialog, {
                    title: _t("Partner Not Selected"),
                    body: _t("The partner should be selected"),
                });

                    }
                }
            }


        // console.log('acc',this.currentOrder.payment_ids)
        if(partner.customer_limit>0){
            return partner.customer_limit
        }
    },

    async validateOrder(){
        const partner = this.currentOrder.partner_id
        const customer_acc = this.payment_methods_from_config
        const order =this.currentOrder._prices

        await super.validateOrder()

    }

});