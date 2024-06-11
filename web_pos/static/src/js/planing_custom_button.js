/* @odoo-module */

import { PlanningGanttController } from "@planning/views/planning_gantt/planning_gantt_controller";
import { patch } from "@web/core/utils/patch";
import { jsonrpc } from "@web/core/network/rpc_service";
patch(PlanningGanttController.prototype, {
    copyPreviousWeekDummy() {
        const today = new Date();
        const formattedDate = today.string(); // Format date as YYYY-MM-DD
        alert(`Hello! Today's date is ${formattedDate}`);
    },
  })
