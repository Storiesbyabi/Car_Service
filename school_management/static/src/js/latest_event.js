/** @odoo-module */
import { renderToElement } from "@web/core/utils/render";
import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";
import {  WillStart} from "@odoo/owl";

console.log(132213213)
publicWidget.registry.get_latest_event = publicWidget.Widget.extend({
   selector : '.events_section',

   async willStart(){
       const result = await rpc('/get_latest_event', {});
       let heroCarousel = Math.floor(Math.random() * 10) + 1;
       console.log('carousel',heroCarousel)
       if(result){
           const sliceAt = 4;
const dataArr = Object.entries(result);
const obA = Object.fromEntries(dataArr.slice(0, sliceAt));
const obB = Object.fromEntries(dataArr.slice(sliceAt,8));
const obC = Object.fromEntries(dataArr.slice(8))
           let list = [obA,obB,obC]
           console.log('oba',obA)
           console.log('obb',obB)
           console.log('obc',obC)
           console.log('list',list)
           console.log('result',result)
           this.$target.empty().html(renderToElement('school_management.event_data', {result_list: list,heroCarousel:heroCarousel}))
       }
   },
});

