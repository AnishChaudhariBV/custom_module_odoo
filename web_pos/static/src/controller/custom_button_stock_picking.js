/** @odoo-module **/

import { registry } from "@web/core/registry";
import { FormController } from "@web/views/form/form_controller";
import { formView } from "@web/views/form/form_view";

// Extend FormController to add custom behavior
class CustomButtonFormController extends FormController {
    setup() {
        super.setup();
        console.log("Custom controller is working now");
    }

    custom_button_action() {
        alert("Hello Buddy, Controller IS Working Now");
    }
}

// Define a custom form view with the new controller
export const customButtonFormView = {
    ...formView,
    Controller: CustomButtonFormController,
    buttonTemplate: "web_pos.stock_picking_button",
};

// Register the custom form view
registry.category("views").add("custom_button_form_view", customButtonFormView);
