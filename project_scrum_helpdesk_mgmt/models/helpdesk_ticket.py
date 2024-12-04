#!/usr/bin/env python3
# © 2024 TechnoLibre (http://www.technolibre.ca)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo import api, fields, models


class HelpdeskTicket(models.Model):

    _inherit = "helpdesk.ticket"

    us_id = fields.Many2one(
        string="User Stories",
        comodel_name="project.scrum.us",
        compute="_compute_us_id",
        readonly=False,
        store=True,
    )

    sprint_ids = fields.Many2many(
        comodel_name="project.scrum.sprint",
        string="Sprint",
        related="us_id.sprint_ids",
    )

    project_use_scrum = fields.Boolean(
        related="project_id.use_scrum", readonly=1
    )

    @api.depends("project_id")
    def _compute_us_id(self):
        for record in self:
            record.us_id = False

    def write(self, vals):
        res = super(HelpdeskTicket, self).write(vals)
        for rec in self:
            if "task_id" in vals:
                if rec.us_id != rec.task_id.us_id:
                    rec.us_id = rec.task_id.us_id.id
        return res
