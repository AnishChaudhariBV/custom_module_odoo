/* @odoo-module */

import { PartnerListScreen } from "@point_of_sale/app/screens/partner_list/partner_list";
import { patch } from "@web/core/utils/patch";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { _t } from "@web/core/l10n/translation";


patch(PartnerListScreen.prototype, {
     setup(_defaultObj, options) {
        super.setup(...arguments);
         this.customer_sundry = this.customer_sundry.bind(this);
    },
     async customer_sundry() {
        const customer_name = this.pos.db.get_partner_by_id(67);

        if (customer_name) {


            this.state.selectedPartner = customer_name;
            this.confirm();
        } else {
              this.popup.add(ErrorPopup, {
                    title: _t("Not Found"),
                    body: _t("This Sundry Customer Is Not found please Add this."),
                });
        }
    }
});