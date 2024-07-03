/** @odoo-module */
import { registry } from "@web/core/registry";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { Component, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class LocationScreen extends Component {
    static template = "pos_config.LocationScreen";

    setup() {
        super.setup(...arguments);
        this.pos = usePos();
        this.orm = useService('orm');
        this.state = useState({
            locations: [], // Initialize empty array for locations
        });
        this.loadLocations();
    }

async loadLocations() {
        try {
            const locations = await this.orm.call(
                "res.location",
                "search_read",
                [[['id', 'in', this.pos.config.location_ids]], ['id', 'location_area']]
            );
            console.log(locations)
            this.state.locations = locations;
        } catch (error) {
            console.error('Error fetching locations:', error);
        }
    }
    async click(loc){
        const current_order=this.pos.get_order()
        current_order.location=loc.location_area
        console.log(current_order.location)
        this.pos.showScreen('ProductScreen');

    }
}

registry.category("pos_screens").add("LocationScreen", LocationScreen);
