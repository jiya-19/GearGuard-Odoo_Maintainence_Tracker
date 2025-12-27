from odoo import models, fields, api
from datetime import date

class GearMaintenanceRequest(models.Model):
    _name = 'gear.maintenance.request'
    _description = 'Maintenance Request'

    name = fields.Char(string="Subject", required=True)
    equipment_id = fields.Many2one('gear.equipment', string="Equipment")
    team_id = fields.Many2one('gear.maintenance.team', string="Team")
    assigned_to = fields.Many2one('res.users', string="Technician")
    scheduled_date = fields.Date(string="Scheduled Date")
    duration = fields.Float(string="Hours Spent")
    type = fields.Selection([
        ('corrective', 'Corrective'),
        ('preventive', 'Preventive')
    ], required=True, default='corrective')
    state = fields.Selection([
        ('new','New'),
        ('assigned','Assigned'),
        ('in_progress','In Progress'),
        ('done','Repaired'),
        ('scrap','Scrap')
    ], default='new', tracking=True)

    is_overdue = fields.Boolean(compute='_compute_overdue', store=True)

    @api.depends('scheduled_date','state')
    def _compute_overdue(self):
        today = date.today()
        for rec in self:
            rec.is_overdue = rec.scheduled_date and rec.scheduled_date < today and rec.state not in ['done','scrap']

    def action_assign(self):
        self.state = 'assigned'

    def action_start(self):
        self.state = 'in_progress'

    def action_done(self):
        self.state = 'done'

    def action_scrap(self):
        self.state = 'scrap'
