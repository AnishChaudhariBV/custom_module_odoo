/* @odoo-module */
import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.CustomFormWidget = publicWidget.Widget.extend({
    selector: '.custom-button',

    events: {
        'click': '_onLinkClick',
    },

    start() {
        this._super.apply(this, arguments);
        console.log('CustomFormWidget has been initialized');
        return this._super(...arguments);
    },

    _onLinkClick(event) {
        event.preventDefault();

        const userConfirmed = confirm('Are you sure you want to go to the home page?');

        if (userConfirmed) {

            window.location.href = '/';
        }


    },
});
