import base64
from odoo import http
from odoo.http import request, content_disposition
from odoo.exceptions import ValidationError

class MyModelController(http.Controller):

    @http.route('/web/binary/download_csv_file_completed_report', type='http', auth='public')
    def download_csv_file(self, **kw):
        Model = request.env['download.report.questionare']
        record_id = int(kw.get('id'))
        record = Model.browse(record_id)

        if record.report_files:
            csv_data = base64.b64decode(record.report_files).decode('utf-8')
            filename = kw.get('filename', 'completed_report.csv')
            return request.make_response(
                csv_data,
                headers=[
                    ('Content-Type', 'text/csv'),
                    ('Content-Disposition', content_disposition(filename)),
                ]
            )
        else:
            raise ValidationError('no data is found')


    @http.route('/web/binary/download_csv_file_missed_report', type='http', auth='public')
    def download_csv_file_missed(self, **kw):
        Model = request.env['download.report.questionare.missed']
        record_id = int(kw.get('id'))
        record = Model.browse(record_id)

        if record.report_files:
            csv_data = base64.b64decode(record.report_files).decode('utf-8')
            filename = kw.get('filename', 'missed_report.csv')
            return request.make_response(
                csv_data,
                headers=[
                    ('Content-Type', 'text/csv'),
                    ('Content-Disposition', content_disposition(filename)),
                ]
            )
        else:
            raise ValidationError('no data is found')
