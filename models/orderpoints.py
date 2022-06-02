from odoo import api, fields, models, tools, _
import datetime
class Orderpoint(models.Model):
    _inherit = 'stock.warehouse.orderpoint'

    def _get_project(self):
        att_model = self.env['stock.move']
        for obj in self:
            query = [("reference","ilike","WH/MO"),("state","!=","done"),("state","!=","cancel"),("state","!=","draft")]
            dd=[]
            ee=[]
            ff=[]
            ss=[]
            for i in att_model.search(query):
                if obj.product_id ==i.product_id:
                    if i.product_uom_qty==i.forecast_availability:
                       continue
                    else: 
                        dd.append(i.raw_material_production_id.product_id.name)
                        ee.append(i.x_remark)
                        ff.append(i.create_uid.name)
                        if i.date_move_list==False:
                                ss.append(datetime.datetime.strftime(i.date, "%Y-%m-%d"))
                        else:
                            ss.append( datetime.datetime.strftime(i.date_move_list, "%Y-%m-%d"))
            obj.x_project=dd
            obj.x_remark=ee
            obj.x_name=ff
            obj.x_date=ss
