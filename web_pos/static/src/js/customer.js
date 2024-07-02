/* @odoo-module */

import { PartnerListScreen } from "@point_of_sale/app/screens/partner_list/partner_list";
import { patch } from "@web/core/utils/patch";

patch(PartnerListScreen.prototype, {
     setup(_defaultObj, options) {
        super.setup(...arguments);
         this.customer_sundry = this.customer_sundry.bind(this);
    },
     async customer_sundry() {
        const customer_name = this.pos.db.get_partner_by_id(65);

        if (customer_name) {


            this.state.selectedPartner = customer_name;
            this.confirm();
        } else {
            this.notification.add("Sundry customer not found.", { type: "danger" });
        }
    }
});