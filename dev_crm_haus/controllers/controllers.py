import base64
from odoo import http
from odoo.http import request, content_disposition


class MyModelController(http.Controller):

    @http.route('/web/binary/download_csv_file', type='http', auth='public')
    def download_csv_file(self, **kw):
        Model = request.env['crm.questionare.admin']
        record_id = int(kw.get('id'))
        record = Model.browse(record_id)

        if record.report_files:
            csv_data = base64.b64decode(record.report_files).decode('utf-8')
            filename = kw.get('filename', 'my_file.csv')
            return request.make_response(
                csv_data,
                headers=[
                    ('Content-Type', 'text/csv'),
                    ('Content-Disposition', content_disposition(filename)),
                ]
            )
        else:
            return request.not_found()
