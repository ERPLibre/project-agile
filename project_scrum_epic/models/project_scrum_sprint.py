#!/usr/bin/env python3
# © 2024 TechnoLibre (http://www.technolibre.ca)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import fields, models


class ProjectScrumSprint(models.Model):
    _inherit = "project.scrum.sprint"

    epic_ids = fields.Many2many(
        comodel_name="project.scrum.epic",
        string="Epics",
    )

    def write(self, vals):
        res = super(ProjectScrumSprint, self).write(vals)
        if "us_ids" in vals:
            for rec in self:
                for us_id in rec.us_ids:
                    for task_id in us_id.task_ids:
                        if task_id.epic_id != rec.epic_id:
                            task_id.epic_id = (
                                rec.epic_id.id if rec.epic_id else False
                            )
        return res
