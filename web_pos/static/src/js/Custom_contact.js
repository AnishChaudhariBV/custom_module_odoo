/** @odoo-module **/

import { useService } from "@web/core/utils/hooks";
import { Component,useState } from "@odoo/owl";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";

class CustomerButton extends Component {
    static template = 'point_of_sale.custom_contact';

    setup() {
        this.popup = useService("popup");
        this.pos = useService("pos");
        this.state=useState({selectedcontacts:"Contacts"})
        this.contact_custom()

    }
async contact_custom(){
    const custom=this.pos.get_order()
    if (custom){
           this.state.selectedcontacts= custom.contact
            }
    }


    async custom_contact() {
        this.pos.showScreen('CustomerScreen');
    }
}

ProductScreen.addControlButton({
    component: CustomerButton,
    position: ["after", "SetSaleOrderButton"]
});

export default CustomerButton;
