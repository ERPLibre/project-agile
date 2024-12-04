#!/usr/bin/env python3
# © 2024 TechnoLibre (http://www.technolibre.ca)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo import api, fields, models


class ProjectScrumEpic(models.Model):
    _inherit = "project.scrum.epic"

    ticket_ids = fields.One2many(
        comodel_name="helpdesk.ticket", inverse_name="epic_id", string="Tickets"
    )
    ticket_count = fields.Integer(compute="_compute_ticket_count", string="# Tickets", store=True)

    def _compute_ticket_count(self):
        for location in self:
            location.ticket_count = self.env["helpdesk.ticket"].search_count(
                [("epic_id", "=", location.id)]
            )
