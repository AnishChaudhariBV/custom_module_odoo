/* @odoo-module */

import { Order } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";

patch(Order.prototype, {
    setup(_defaultObj, options) {
        super.setup(...arguments);
        this.add_note = this.add_note || "";
        this.location = this.location || "";
        this.discount_applied = false
    },

    //@override
    export_as_JSON() {
        const json = super.export_as_JSON(...arguments);
        if (json) {
            json.add_note = this.add_note;
            json.location = this.location;
            json.discount_applied = this.discount_applied;
        }
        return json;
    },

    //@override
    init_from_JSON(json) {
        super.init_from_JSON(...arguments);
        this.add_note = json.add_note;
        this.location = json.location;
        this.discount_applied = json.discount_applied;
    },

    //@override
    export_for_printing() {
        const result = super.export_for_printing(...arguments);
        result.custom_note = this.custom_note;
        result.location = this.location;
        return result;
    },

    getCustomNote() {
        return this.add_note;
    },

    setCustomNote(note) {
        this.add_note = note || "";
    },
});

