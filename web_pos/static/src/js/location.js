/** @odoo-module **/

import { useService } from "@web/core/utils/hooks";
import { Component ,useState} from "@odoo/owl";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";

class LocationButton extends Component {
    static template = 'point_of_sale.location';

    setup() {
        this.popup = useService("popup");
        this.pos = useService("pos");
        this.state=useState({selectedlocation:"Locations"})
        this.get_location()
    }
async get_location(){
const current_order=this.pos.get_order()
if (current_order){
       this.state.selectedlocation= current_order.location
        }
}
    async add_location() {
        this.pos.showScreen('LocationScreen');
    }
}

ProductScreen.addControlButton({
    component: LocationButton,
    position: ["after", "SetSaleOrderButton"],
});

export default LocationButton;
