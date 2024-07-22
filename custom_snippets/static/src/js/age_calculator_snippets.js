/** @odoo-module **/

import publicWidget from '@web/legacy/js/public/public_widget';

publicWidget.registry.AgeCounterWidget = publicWidget.Widget.extend({
    selector: '.age_counter_widget',

    events: {
        'submit #ageCounterForm': '_onFormSubmit',
    },

    start() {
        console.log("AgeCounterWidget started");
        this._super(...arguments);
    },

    _onFormSubmit(event) {
        event.preventDefault();
        console.log("Form submitted");

        const form = this.$('#ageCounterForm');
        const birthdate = form.find('#birthdate').val();
        if (birthdate) {
            const age = this._calculateAge(birthdate);
            const ageField = $(`
                <div class="form-group mt-3">
                    <label>Your age is:</label>
                    <p class="form-control-static">${age} years</p>
                </div>
            `);
            this.$('#ageDisplay').empty().append(ageField);
        } else {
            form.addClass('was-validated');
        }
    },

    _calculateAge(birthdate) {
        const birthDate = new Date(birthdate);
        const today = new Date();
        let age = today.getFullYear() - birthDate.getFullYear();
        const monthDiff = today.getMonth() - birthDate.getMonth();
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }
        return age;
    },
});
