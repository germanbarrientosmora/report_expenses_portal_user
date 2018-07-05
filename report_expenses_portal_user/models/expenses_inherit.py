"""
* Created by gonzalezoscar on 5/07/18
* report_expenses_portal_user
"""

# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ExpensesInherit(models.Model):
    _inherit = 'hr.expense'

    x_project_id = fields.Many2one(
        'project.project',
        string="Project"
    )