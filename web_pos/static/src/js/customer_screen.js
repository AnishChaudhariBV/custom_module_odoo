/** @odoo-module */
import { registry } from "@web/core/registry";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { Component, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

// Define the CustomerScreen component
export class CustomerScreen extends Component {
    static template = "pos_config.Contact_screen";

    setup() {
        super.setup(...arguments);
        this.pos = usePos();
        this.state = useState({ contacts: [] });
        this.orm = useService('orm');

        this.loadContacts();
    }

    async loadContacts() {
        try {
            const contacts = await this.orm.call(
                "custom.contact",
                "search_read",
                [[['id', 'in', this.pos.config.contact_ids]], ['id', 'name']]
            );
            this.state.contacts = contacts;
            console.log(contacts);
        } catch (error) {
            console.error('Error fetching contacts:', error);
        }
    }
    async click(con){
    const custom_contact = this.pos.get_order()
    custom_contact.contact=con.name
    console.log(custom_contact.contact)
    this.pos.showScreen('ProductScreen')}
}

// Register the CustomerScreen component in the pos_screens category
registry.category("pos_screens").add("CustomerScreen", CustomerScreen);
console.log("CustomerScreen registered");
