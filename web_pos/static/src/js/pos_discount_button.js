/** @odoo-module **/

import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { _t } from "@web/core/l10n/translation";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { NumberPopup } from "@point_of_sale/app/utils/input_popups/number_popup";

class CustomDiscount extends Component {
    static template = "point_of_sale.DiscountButton";

    setup() {
        this.popup = useService("popup");
        this.pos = useService("pos");
        this.orm = useService("orm");
    }

    async onCustomDiscount() {
        try {
            // Fetch the discount value from ir.config_parameter
            const result = await this.orm.call("ir.config_parameter", "get_param", ["web_pos.discount_value"]);
            const customDiscount = parseFloat(result);
            console.log(customDiscount)

            // Validate the discount value
            if (customDiscount >= 100 || customDiscount <= 0 || isNaN(customDiscount)) {
                throw new Error("Invalid discount value");
            }

            // Apply the discount to selected order lines
            const selectedLines = this.pos.get_order().get_orderlines();
            const ordered = this.pos.get_order()

            ordered.discount_applied = true
               console.log(ordered.discount_applied)
            if (!selectedLines || selectedLines.length === 0) {
                this.popup.add(ErrorPopup, {
                    title: _t("No Order Lines"),
                    body: _t("Please add products to the order first!"),
                });
                return;
            }

            for (let selectedLine of selectedLines) {
                selectedLine.set_discount(customDiscount);

            }

        } catch (error) {
            console.error("Error applying discount:", error);
            this.popup.add(ErrorPopup, {
                title: _t("Error Applying Discount"),
                body: _t("There was an error applying the discount. Please try again later."),
            });
        }
    }
}

ProductScreen.addControlButton({
    component: CustomDiscount,
    position: ["after", "clearButton"],
});
