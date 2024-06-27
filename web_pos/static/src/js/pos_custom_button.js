/** @odoo-module **/
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { _t } from "@web/core/l10n/translation";
import { TextAreaPopup } from "@point_of_sale/app/utils/input_popups/textarea_popup";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { usePos } from "@point_of_sale/app/store/pos_hook";

export class CreateButton extends Component {
    static template = "point_of_sale.CreateButton";

    setup() {
        this.popup = useService("popup");
        this.pos = usePos();
    }

    async onClick() {
        const selectedLine = this.pos.get_order().get_selected_orderline();
        if (!selectedLine) {
            this.popup.add(ErrorPopup, {
                title: _t("OrderLine is not selected"),
                body: _t("Please select an order first!"),
            });
            return;
        }

        const { confirmed, payload: inputNote } = await this.popup.add(TextAreaPopup, {
            startingValue: selectedLine.getNote(),
            title: _t("Add Customer Note Here"),
        });

        if (confirmed) {
            selectedLine.setNote(inputNote);
        }
    }
}

// Add the CreateButton component before the OrderlineCustomerNoteButton
ProductScreen.addControlButton({
    component: CreateButton,
    position: ["before", "OrderlineCustomerNoteButton"], // Add the button before OrderlineCustomerNoteButton
});
