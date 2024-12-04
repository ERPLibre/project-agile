#!/usr/bin/env python3
# © 2024 TechnoLibre (http://www.technolibre.ca)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo import api, fields, models


class HelpdeskTicket(models.Model):

    _inherit = "helpdesk.ticket"

    epic_id = fields.Many2one(
        string="Epic",
        comodel_name="project.scrum.epic",
        compute="_compute_epic_id",
        readonly=False,
        store=True,
    )

    @api.depends("project_id")
    def _compute_epic_id(self):
        for record in self:
            record.epic_id = False

    def write(self, vals):
        res = super(HelpdeskTicket, self).write(vals)
        for rec in self:
            if "task_id" in vals:
                if rec.epic_id != rec.task_id.epic_id:
                    rec.epic_id = rec.task_id.epic_id.id
            if "us_id" in vals:
                if rec.epic_id != rec.us_id.epic_id:
                    rec.epic_id = rec.us_id.epic_id.id
        return res
