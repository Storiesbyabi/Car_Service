/** @odoo-module */
import { renderToElement } from "@web/core/utils/render";
import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";
publicWidget.registry.get_latest_event = publicWidget.Widget.extend({
   selector : '.events_section',
   async willStart() {
       const result = await rpc('/get_latest_event', {});
       if(result){
           console.log('result',result)
           this.$target.empty().html(renderToElement('school_management.event_data', {result: result}))
       }
   },
});

