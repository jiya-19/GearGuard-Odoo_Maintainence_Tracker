from odoo import models, fields

class GearEquipment(models.Model):
    _name = 'gear.equipment'
    _description = 'Equipment'

    name = fields.Char(string="Equipment Name", required=True)
    serial_number = fields.Char(string="Serial Number")
    purchase_date = fields.Date(string="Purchase Date")
    warranty = fields.Char(string="Warranty Info")
    location = fields.Char(string="Location")
    team_id = fields.Many2one('gear.maintenance.team', string="Maintenance Team")

    maintenance_count = fields.Integer(
        compute='_compute_maintenance_count'
    )

    def _compute_maintenance_count(self):
        for rec in self:
            rec.maintenance_count = self.env[
                'gear.maintenance.request'
            ].search_count([('equipment_id', '=', rec.id)])
    def open_maintenance_requests(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Maintenance Requests',
            'res_model': 'maintenance.request',
            'view_mode': 'tree,form',
            'domain': [('equipment_id', '=', self.id)],
            'context': {'default_equipment_id': self.id},
        }