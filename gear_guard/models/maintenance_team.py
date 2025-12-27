from odoo import models, fields

class GearMaintenanceTeam(models.Model):
    _name = 'gear.maintenance.team'
    _description = 'Maintenance Team'

    name = fields.Char(string="Team Name", required=True)
    leader_id = fields.Many2one('res.users', string="Team Leader")
    member_ids = fields.Many2many('res.users', string="Team Members")
