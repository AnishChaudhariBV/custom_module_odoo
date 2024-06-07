/* @odoo-module */
import publicWidget from "@web/legacy/js/public/public_widget";
import PortalSidebar from '@portal/js/portal_sidebar';

PortalSidebar.include({
    selector: ".o_portal_purchase_sidebar",
    init: function (parent) {
        this._super(parent);
    },
    start: function() {
        this._super.apply(this, arguments);

        // Apply CSS styles
        this.$el.css({
            'background-color': '#E8E8E8',   // existing background color
            'padding': '20px',                // add padding
            'border-radius': '5px',           // add border radius
            'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.1)', // add box shadow
            'font-size': '14px',              // set font size
            'color': '#333'                   // set text color
        });

        const $button = $('<button>', {
            text: 'Click Me',
            css: {
                'margin-top': '10px',
                'padding': '10px 20px',
                'border': 'none',
                'border-radius': '5px',
                'background-color': '#007bff',
                'color': '#fff',
                'cursor': 'pointer'
            }
        });

        this.$el.append($button);

        $button.on('click', () => {
            alert('Thank you !');
        });
    }
});
