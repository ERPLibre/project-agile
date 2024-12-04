#!/usr/bin/env python3
# © 2024 TechnoLibre (http://www.technolibre.ca)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    epic_id = fields.Many2one(
        "project.scrum.epic",
        string="Epic",
        compute="_compute_epic_id",
        readonly=False,
        store=True,
    )

    @api.depends("us_id")
    def _compute_epic_id(self):
        for rec in self:
            # Ignore when unassign User stories
            if rec.us_id:
                rec.epic_id = (
                    rec.us_id.epic_id.id if rec.us_id.epic_id else False
                )
