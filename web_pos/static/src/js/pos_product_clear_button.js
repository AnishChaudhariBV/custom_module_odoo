/** @odoo-module **/
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { _t } from "@web/core/l10n/translation";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { ConfirmPopup } from "@point_of_sale/app/utils/confirm_popup/confirm_popup";

export class CreateButton extends Component {
    static template = "point_of_sale.clearButton";

    setup() {
        this.popup = useService("popup");
        this.pos = useService("pos"); // Use the POS state hook to get the current order
    }

    onclear() {
            const selectedLine = this.pos.get_order().get_selected_orderline();
            this.pos.get_order().removeOrderline(selectedLine);
            console.log(selectedLine)
        };
    onclearAll() {
           const selectedLine = this.pos.get_order().get_orderlines();
           for(const line of selectedLine){
           if (line){
           this.pos.get_order().removeOrderline(line)
           }}

        };

    }


// Add the CreateButton component after the customer button
ProductScreen.addControlButton({
    component: CreateButton,
    position: ["after", "SetSaleOrderButton"], // Add the button before OrderlineCustomerNoteButton
});
