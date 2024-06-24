/** @odoo-module **/
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { _t } from "@web/core/l10n/translation";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { ConfirmPopup } from "@point_of_sale/app/utils/confirm_popup/confirm_popup";

export class CreateButton extends Component {
    static template = "point_of_sale.CreateButton";

    setup() {
        this.popup = useService("popup");
    }


   onClick() {
//        this.popup.add(ErrorPopup, {
//                    title: _t("Error Message"),
//                    body: _t("This A Simple Message For Pop UP testing Purpose."),
//                });
                this.popup.add(ConfirmPopup, {
                    title: _t("Confirm Message"),
                    body: _t("This A Simple Message For Confirm Pop UP testing Purpose."),
                });

    }
}

// Add the CreateButton component after the customer button
ProductScreen.addControlButton({
    component: CreateButton,
    position: ["before", "OrderlineCustomerNoteButton"], // Add the button before OrderlineCustomerNoteButton
});
