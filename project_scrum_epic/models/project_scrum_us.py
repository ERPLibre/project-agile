#!/usr/bin/env python3
# © 2024 TechnoLibre (http://www.technolibre.ca)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo import api, fields, models


class ProjectScrumUs(models.Model):
    _inherit = "project.scrum.us"

    epic_id = fields.Many2one(comodel_name="project.scrum.epic", string="Epic")

    def write(self, vals):
        res = super(ProjectScrumUs, self).write(vals)
        if "epic_id" in vals:
            for rec in self:
                for task_id in rec.task_ids:
                    if task_id.epic_id != rec.epic_id:
                        task_id.epic_id = (
                            rec.epic_id.id if rec.epic_id else False
                        )
        return res
