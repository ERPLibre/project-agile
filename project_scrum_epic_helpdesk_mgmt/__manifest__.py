# © 2024 TechnoLibre (http://www.technolibre.ca)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Project Scrum Epic Helpdesk Mgmt",
    "summary": "Extend project scrum Epic to helpdesk mgmt",
    "version": "14.0.1.0.0",
    "category": "Project Management",
    "author": "TechnoLibre, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/project-agile",
    "depends": [
        "project_scrum_epic",
        "project_scrum_helpdesk_mgmt",
    ],
    "data": [
        "views/helpdesk_ticket_view.xml",
        "views/project_scrum_epic.xml",
    ],
    "installable": True,
    "auto_install": True,
    "license": "AGPL-3",
    "application": False,
}
