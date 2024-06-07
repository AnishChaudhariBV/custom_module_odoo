/* @odoo-module */

import { ExpenseListController } from '@hr_expense/views/list';
import { patch } from "@web/core/utils/patch";
import { jsonrpc } from "@web/core/network/rpc_service";

patch(ExpenseListController.prototype, {
  async sendEmail() {
    const selectedRecords = this.model.root.selection.map((record) => record.resId);

    if (!selectedRecords.length) {
      this.notification.add('Please select at least one expense report.', {
        title: 'No Reports Selected',
        type: 'warning',
      });
      return;
    }

    try {
      const emailPromises = selectedRecords.map((recordId) =>
        jsonrpc('/web/dataset/call_kw/hr.expense/action_send_email', {
          model: 'hr.expense',
          method: 'action_send_email',
          args: [recordId],
          kwargs: {},
        })
      );

      this.notification.add('Expense report emails sent successfully!', {
        title: 'Success',
        type: 'success',
      });
    } catch (error) {
      console.error('Error sending expense report emails:', error);
      this.notification.add('Failed to send some or all expense report emails.', {
        title: 'Error',
        type: 'danger',
      });
    }
  },
});
