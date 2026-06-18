import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";
import { PosStore } from "@point_of_sale/app/services/pos_store";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";


patch(PosStore.prototype,{
    pay(){
        const order = this.getOrder()
        const partner = order.getPartner()
        if(!partner) {
            console.log('not partner',this.dialog)
        this.dialog.add(AlertDialog, {
                    title: _t("Partner Not Selected"),
                    body: _t("The partner should be selected"),
                });
        }
        else{
             console.log('order',order.amount_total)
        console.log('partner',partner.name)
        if(partner.limit_amount <= order.amount_total){
            this.dialog.add(AlertDialog, {
                    title: _t("Partner Order Limit"),
                    body: _t("Partner Order Limit has exceeded"),
                });
        }else{
            console.log('lesser')
            super.pay()
        }

        }


    }
})