from email.policy import default
from odoo import api, fields, models, _
from datetime import datetime
from odoo.exceptions import ValidationError
import csv
import base64

site_list = [('HAUS! JKT - BINUS 1', 'HAUS! BINUS 1'),
    ('HAUS! DPK - GUNADARMA', 'HAUS! DEPOK'),
    ('HAUS! TNG - KARANG TENGAH', 'HAUS! KARANG TENGAH'),
    ('HAUS! BDG - GEGER KALONG', 'HAUS! GEGER KALONG'),
    ('HAUS! BDG - UJUNG BERUNG', 'HAUS! UJUNG BERUNG'),
    ('HAUS! JKT - TANJUNG GEDONG', 'HAUS! TANJUNG GEDONG'),
    ('HAUS! TNG - CEGER', 'HAUS! CEGER'),
    ('HAUS! JKT - PETUKANGAN', 'HAUS! PETUKANGAN'),
    ('HAUS! BDG - CIJERAH', 'HAUS! CIJERAH'),
    ('HAUS! JKT - MENCENG', 'HAUS! MENCENG'),
    ('HAUS! TNG - KUTABUMI', 'HAUS! KUTABUMI'),
    ('HAUS! JKT - PENGGILINGAN', 'HAUS! PENGGILINGAN'),
    ('HAUS! JKT - SUMUR BATU', 'HAUS! SUMUR BATU'),
    ('HAUS! JKT - CIBUBUR', 'HAUS! CIBUBUR'),
    ('HAUS! BKS - TAMBUN', 'HAUS! TAMBUN'),
    ('HAUS! BGR - CIKEAS', 'HAUS! CIKEAS'),
    ('HAUS! TNG - PAMULANG 1', 'HAUS! PAMULANG 1'),
    ('HAUS! TNG - PORIS', 'HAUS! PORIS'),
    ('HAUS! TNG - CIPUTAT', 'HAUS! CIPUTAT'),
    ('HAUS! JKT - JAGAKARSA 1', 'HAUS! JAGAKARSA 1'),
    ('HAUS! JKT - TEBET', 'HAUS! TEBET'),
    ('HAUS! JKT - PONDOK KELAPA', 'HAUS! PONDOK KELAPA'),
    ('HAUS! TNG - BINONG', 'HAUS! BINONG'),
    ('HAUS! JKT - BINUS 2', 'HAUS! BINUS 2'),
    ('HAUS! JKT - KOTA BAMBU', 'HAUS! KOTA BAMBU'),
    ('HAUS! BDG - KIARA CONDONG', 'HAUS! KIARA CONDONG'),
    ('HAUS! JKT - BUARAN', 'HAUS! BUARAN'),
    ('HAUS! JKT - PADEMANGAN', 'HAUS! PADEMANGAN'),
    ('HAUS! BKS - CAMAN', 'HAUS! CAMAN'),
    ('HAUS! TNG - KARAWACI', 'HAUS! KARAWACI'),
    ('HAUS! BKS - KARTINI', 'HAUS! KARTINI'),
    ('HAUS! JKT - KAYU MANIS', 'HAUS! KAYU MANIS'),
    ('HAUS! JKT - HALIM', 'HAUS! HALIM'),
    ('HAUS! JKT - PASAR RUMPUT', 'HAUS! PASAR RUMPUT'),
    ('HAUS! JKT - KOJA', 'HAUS! KOJA'),
    ('HAUS! TNG - PAMULANG 2', 'HAUS! PAMULANG 2'),
    ('HAUS! JKT - PONDOK LABU', 'HAUS! PONDOK LABU'),
    ('HAUS! JKT - KALISARI', 'HAUS! KALISARI'),
    ('HAUS! JKT - RAYA TENGAH', 'HAUS! RAYA TENGAH'),
    ('HAUS! JKT - KRESEK KOSAMBI', 'HAUS! KRESEK KOSAMBI'),
    ('HAUS! BDG - CIKUTRA', 'HAUS! CIKUTRA'),
    ('HAUS! DPK - PEKAPURAN', 'HAUS! PEKAPURAN'),
    ('HAUS! BDG - CIMAHI', 'HAUS! CIMAHI'),
    ('HAUS! DPK - SAWANGAN', 'HAUS! SAWANGAN'),
    ('HAUS! BKS - HANKAM', 'HAUS! HANKAM'),
    ('HAUS! JKT - CILANGKAP', 'HAUS! CILANGKAP'),
    ('HAUS! BKS - RAWALUMBU', 'HAUS! RAWALUMBU'),
    ('HAUS! BKS - CIBITUNG', 'HAUS! CIBITUNG'),
    ('HAUS! BDG - METRO', 'HAUS! METRO'),
    ('HAUS! BKS - KARANG SATRIA', 'HAUS! KARANG SATRIA'),
    ('HAUS! TNG - SEPATAN', 'HAUS! SEPATAN'),
    ('HAUS! DPK - SENTOSA', 'HAUS! SENTOSA'),
    ('HAUS! JKT - CIRACAS', 'HAUS! CIRACAS'),
    ('HAUS! JKT - CIPINANG', 'HAUS! CIPINANG'),
    ('HAUS! JKT - KAHFI CIGANJUR', 'HAUS! KAHFI CIGANJUR'),
    ('HAUS! JKT - JAGAKARSA 2', 'HAUS! JAGAKARSA 2'),
    ('HAUS! DPK - KEADILAN', 'HAUS! KEADILAN'),
    ('HAUS! BKS - NUSANTARA', 'HAUS! NUSANTARA'),
    ('HAUS! JKT - PEJATEN', 'HAUS! PEJATEN'),
    ('HAUS! BGR - KEBON PEDES', 'HAUS! KEBON PEDES'),
    ('HAUS! BGR - AIR MANCUR', 'HAUS! AIR MANCUR'),
    ('HAUS! BGR - MAWAR', 'HAUS! MAWAR'),
    ('HAUS! TNG - REMPOA 2', 'HAUS! REMPOA 2'),
    ('HAUS! JKT - PANCORAN 2', 'HAUS! PANCORAN 2'),
    ('HAUS! TNG - PARUNG SERAB', 'HAUS! PARUNG SERAB'),
    ('HAUS! DPK - PITARA', 'HAUS! PITARA'),
    ('HAUS! JKT - POLTANGAN', 'HAUS! POLTANGAN'),
    ('HAUS! JKT - MERUYA', 'HAUS! MERUYA'),
    ('HAUS! JKT - TANAH ABANG', 'HAUS! TANAH ABANG'),
    ('HAUS! BGR - CIBINONG', 'HAUS! CIBINONG'),
    ('HAUS! BKS - PONDOK UNGU 2', 'HAUS! PONDOK UNGU 2'),
    ('HAUS! JKT - MERCU BUANA', 'HAUS! MERCUBUANA'),
    ('HAUS! TNG - CIRENDEU', 'HAUS! CIRENDEU'),
    ('HAUS! BGR - TAJUR', 'HAUS! TAJUR'),
    ('HAUS! BKS - GALAXY', 'HAUS! GALAXY'),
    ('HAUS! TNG - CITRA RAYA', 'HAUS! CITRA RAYA'),
    ('HAUS! JKT - KARBELA', 'HAUS! KARBELA'),
    ('HAUS! BGR - DRAMAGA', 'HAUS! DRAMAGA'),
    ('HAUS! JKT - BANGKA', 'HAUS! BANGKA'),
    ('HAUS! BDG - CIBIRU', 'HAUS! CIBIRU'),
    ('HAUS! TNG - PASAR LAMA', 'HAUS! PASAR LAMA'),
    ('HAUS! TNG - JOMBANG', 'HAUS! JOMBANG'),
    ('HAUS! BKS - JATIWARINGIN', 'HAUS! JATIWARINGIN'),
    ('HAUS! BDG - BALEENDAH', 'HAUS! BALEENDAH'),
    ('HAUS! JKT - CEMPAKA PUTIH', 'HAUS! CEMPAKA PUTIH'),
    ('HAUS! JKT - CIPETE', 'HAUS! CIPETE'),
    ('HAUS! JKT - GREEN VILLE', 'HAUS! GREEN VILLE'),
    ('HAUS! JKT - SEMANAN', 'HAUS! SEMANAN'),
    ('HAUS! JKT - PLUIT', 'HAUS! PLUIT'),
    ('HAUS! JKT - RAWAMANGUN', 'HAUS! RAWAMANGUN'),
    ('HAUS! BDG - STT TELKOM', 'HAUS! STT TELKOM BANDUNG'),
    ('HAUS! JKT - CITRA GARDEN', 'HAUS! CITRA GARDEN'),
    ('HAUS! JKT - PGC', 'HAUS! PGC'),
    ('HAUS! JKT - WARAKAS', 'HAUS! WARAKAS'),
    ('HAUS! JKT - SUNTER', 'HAUS! SUNTER'),
    ('HAUS! TNG - ANGGREK LOKA BSD', 'HAUS! ANGGREK LOKA BSD'),
    ('HAUS! BDG - BUAH BATU', 'HAUS! BUAH BATU'),
    ('HAUS! TNG - KELAPA DUA', 'HAUS! KELAPA DUA TANGERANG'),
    ('HAUS! JKT - PLAZA KALIBATA', 'HAUS! JKT - PLAZA KALIBATA'),
    ('HAUS! BKS - PONDOK UNGU', 'HAUS! PONDOK UNGU'),
    ('HAUS! BKS - BINTARA', 'HAUS! BINTARA'),
    ('HAUS! BKS - HARAPAN INDAH', 'HAUS! HARAPAN INDAH'),
    ('HAUS! JKT - SEASON CITY', 'HAUS! SEASON CITY'),
    ('HAUS! KWG - GALUH MAS', 'HAUS! KARAWANG'),
    ('HAUS! BGR - CIBINONG CITY MALL', 'HAUS! CIBINONG CITY MALL'),
    ('HAUS! SBY - SEMOLOWARU', 'HAUS! SEMOLOWARU'),
    ('HAUS! SBY - SIWALANKERTO', 'HAUS! SIWALANKERTO'),
    ('HAUS! SBY - MULYOSARI', 'HAUS! MULYOSARI'),
    ('HAUS! SBY - WIYUNG', 'HAUS! WIYUNG'),
    ('HAUS! SBY - RUNGKUT MADYA', 'HAUS! RUNGKUT MADYA'),
    ('HAUS! SBY - GWALK CIPUTRA', 'HAUS! GWALK CIPUTRA'),
    ('HAUS! SBY - MANUKAN', 'HAUS! MANUKAN'),
    ('HAUS! SBY - NGAGELREJO', 'HAUS! NGAGELREJO'),
    ('HAUS! SBY - ROYAL PLAZA', 'HAUS! ROYAL PLAZA'),
    ('HAUS! TNG - BINTARO', 'HAUS! BINTARO'),
    ('HAUS! GRT - CIMANUK', 'HAUS! GARUT CIMANUK'),
    ('HAUS! SRG - CICERI', 'HAUS! SERANG CICERI'),
    ('HAUS! YYK - TAMAN SISWA', 'HAUS! YOGYA TAMAN SISWA'),
    ('HAUS! YYK - GODEAN', 'HAUS! YOGYA GODEAN'),
    ('HAUS! YYK - PALAGAN', 'HAUS! YOGYA PALAGAN'),
    ('HAUS! YYK - GEJAYAN', 'HAUS! YOGYA GEJAYAN'),
    ('HAUS! YYK - KALIURANG', 'HAUS! YOGYA KALIURANG'),
    ('HAUS! YYK - KAPTEN TENDEAN', 'HAUS! YOGYA KAPTEN TENDEAN'),
    ('HAUS! TNG - PANARUB', 'HAUS! PANARUB'),
    ('HAUS! BDG - ANTAPANI', 'HAUS! ANTAPANI'),
    ('HAUS! DPK - BEJI', 'HAUS! BEJI'),
    ('HAUS! CRB - CIREMAI', 'HAUS! CIREBON CIREMAI'),
    ('HAUS! CRB - PERJUANGAN', 'HAUS! CIREBON PERJUANGAN'),
    ('HAUS! YYK - GLAGAHSARI', 'HAUS! YOGYA GLAGAHSARI'),
    ('HAUS! YYK - SETURAN', 'HAUS! YOGYA SETURAN'),
    ('HAUS! YYK - JAKAL UII', 'HAUS! YOGYA JAKAL UII'),
    ('HAUS! SKB - BENTENG', 'HAUS! SUKABUMI BENTENG '),
    ('HAUS! SKB - CIKOLE', 'HAUS! SUKABUMI CIKOLE'),
    ('HAUS! SRG - CIKANDE', 'HAUS! SERANG CIKANDE'),
    ('HAUS! CRB - CIREBON SUPER BLOCK', 'HAUS! CIREBON SUPERBLOCK'),
    ('HAUS! BDG - TAMAN KOPO INDAH', 'HAUS! TAMAN KOPO INDAH '),
    ('HAUS! JKT - SARINAH', 'HAUS! SARINAH'),
    ('HAUS! CLG - TEMU PUTIH', 'HAUS! CILEGON TEMU PUTIH'),
    ('HAUS! SKT - SUPOMO', 'HAUS! SOLO SUPOMO'),
    ('HAUS! SKT - JAYA WIJAYA', 'HAUS! SOLO JAYA WIJAYA'),
    ('HAUS! SKT - SUTOYO', 'HAUS! SOLO SUTOYO'),
    ('HAUS! SKT - GARUDA MAS', 'HAUS! SOLO GARUDA MAS'),
    ('HAUS! SKT - UNS', 'HAUS! SOLO UNS'),
    ('HAUS! SDA - DELTA SARI', 'HAUS! DELTA SARI'),
    ('HAUS! GSK - KOTA BARU', 'HAUS! GRESIK KOTA BARU'),
    ('HAUS! SDA - TAMAN PINANG', 'HAUS! TAMAN PINANG'),
    ('HAUS! SBY - KETINTANG', 'HAUS! KETINTANG'),
    ('HAUS! SBY - DUKUH KUPANG', 'HAUS! DUKUH KUPANG'),
    ('HAUS! SDA - SURAPATI', 'HAUS! SIDOARJO SURAPATI'),
    ('HAUS! SDA - PONDOK JATI', 'HAUS! SIDOARJO PONDOK JATI'),
    ('HAUS! SMG - ANJASMORO', 'HAUS! SEMARANG ANJASMORO'),
    ('HAUS! BDG - CIBADUYUT', 'HAUS! CIBADUYUT'),
    ('HAUS! JKT - SRENGSENG', 'HAUS! SRENGSENG'),
    ('HAUS! SMG - GAJAH', 'HAUS! SEMARANG GAJAH'),
    ('HAUS! YYK - MALIOBORO', 'HAUS! YOGYA MALIOBORO'),
    ('HAUS! TNG - GRAHA RAYA', 'HAUS! TNG - GRAHA RAYA'),
    ('HAUS! SMG - SARINAH', 'HAUS! SMG - SARINAH'),
    ('HAUS! BDG - PADALARANG', 'HAUS! BDG - PADALARANG'),
    ('HAUS! BGR - INDRAPRASTA', 'HAUS! BGR - INDRAPRASTA'),
    ('HAUS! TNG - PURI BETA', 'HAUS! TNG - PURI BETA'),
    ('HAUS! CKR - GRAHA ASRI', 'HAUS! CKR - GRAHA ASRI'),
    ('HAUS! KWG - SARIMULYA', 'HAUS! KWG - CIKAMPEK'),
    ('HAUS! JKT - PONDOK PINANG', 'HAUS! JKT - PONDOK PINANG'),
    ('HAUS! JKT - RADIO DALAM', 'HAUS! JKT - RADIO DALAM'),
    ('HAUS! TNG - BOJONG NANGKA', 'HAUS! TNG - DASANA INDAH'),
    ('HAUS! KWG -TANJUNG MEKAR', 'HAUS! KWG -TANJUNGMEKAR'),
    ('HAUS! JKT-CEGER', 'HAUS! JKT - GEMPOL RAYA '),
    ('HAUS! JKT - SUMAGUNG', 'HAUS! JKT - SUMAGUNG'),
    ('HAUS! BGR - TAMAN YASMIN', 'HAUS! BGR - TAMAN YASMIN'),
    ('HAUS! BGR - KOTA WISATA', 'HAUS! BGR - KOTA WISATA'),
    ('HAUS! SKB - CIBADAK', 'HAUS! SKB - CIBADAK'),
    ('HAUS! TNG - TAMAN CIBODAS', 'HAUS! TNG - TAMAN CIBODAS'),
    ('HAUS! TNG - BANJAR WIJAYA', 'HAUS! TNG - BANJAR WIJAYA'),
    ('HAUS! DPK - GRAND DEPOK CITY', 'HAUS! DPK - GRAND DEPOK CITY'),
    ('HAUS! TNG - NUSA LOKA BSD', 'HAUS! TNG - NUSA LOKA BSD'),
    ('HAUS! JKT - GANDARIA', 'HAUS! JKT - GANDARIA'),
    ('HAUS! DPK - CITAYAM', 'HAUS! DPK - CITAYAM'),
    ('HAUS! TNG - GONDRONG CIPONDOH', 'HAUS! TNG - GONDRONG CIPONDOH'),
    ('HAUS! TNG - DUTA GARDEN', 'HAUS! TNG - DUTA GARDEN'),
    ('HAUS! TNG - BERINGIN RAYA', 'HAUS! TNG - BERINGIN RAYA'),
    ('HAUS! BGR - CIOMAS', 'HAUS! BGR - CIOMAS'),
    ('HAUS TNG - VILLA TANGERANG INDAH', 'HAUS TNG - VILLA TANGERANG INDAH'),
    ('HAUS! TNG - TALAGA BASTARI', 'HAUS! TNG - TALAGA BASTARI'),
    ('HAUS! JKT - SUMUR BOR', 'HAUS! JKT - SUMUR BOR'),
    ('HAUS! TNG - BUKIT SERUA INDAH', 'HAUS! TNG - BUKIT SERUA INDAH'),
    ('HAUS! TNG - CURUG', 'HAUS! TNG - CURUG'),
    ('HAUS! BGR - CITRA INDAH CITY', 'HAUS! BGR - CITRA INDAH CITY'),
    ('HAUS! DPK - MEKARSARI CIMANGGIS', 'HAUS! DPK - MEKARSARI CIMANGGIS'),
    ('HAUS! BGR - CIAPUS', 'HAUS! BGR - CIAPUS'),
    ('HAUS! DPK - PENGASINAN SAWANGAN', 'HAUS! DPK - PENGASINAN SAWANGAN'),
    ('HAUS! TNG - VILLA DAGO PAMULANG', 'HAUS! TNG - VILLA DAGO PAMULANG'),
    ('HAUS! TNG - HASYIM ASHARI', 'HAUS! TNG - HASYIM ASHARI'),
    ('HAUS! BGR - DURIAN RAYA', 'HAUS! BGR - DURIAN RAYA'),
    ('HAUS! DPK - JATIMULYA CILODONG', 'HAUS! DPK - JATIMULYA CILODONG'),
    ('HAUS! BKS - KRANGGAN PERMAI', 'HAUS! BKS - KRANGGAN PERMAI'),
    ('HAUS! BKS - NANGKA RAYA', 'HAUS! BKS - NANGKA RAYA'),
    ('HAUS! SRG - LOPANG RAYA', 'HAUS! SRG - LOPANG RAYA'),
    ('HAUS! JKT - JELAMBAR UTAMA', 'HAUS! JKT - JELAMBAR UTAMA'),
    ('HAUS! BKS - PURI GADING', 'HAUS! BKS - PURI GADING'),
    ('HAUS! CKR - INDUSTRI CIKARANG', 'HAUS! CKR - INDUSTRI CIKARANG'),
    ('HAUS! BKS - JATI KRAMAT RAYA', 'HAUS! BKS - JATI KRAMAT RAYA'),
    ('HAUS! JKT - PISANGAN LAMA', 'HAUS! JKT - PISANGAN LAMA'),
    ('HAUS! BGR - SUKAHATI', 'HAUS! BGR - SUKAHATI'),
    ('HAUS! CRB - KUTAGARA', 'HAUS! CRB - KUTAGARA'),
    ('HAUS! CRB - SHELL KESAMBI', 'HAUS! CRB - SHELL KESAMBI'),
    ('HAUS! DPK - RADEN SANIM', 'HAUS! DPK - RADEN SANIM'),
    ('HAUS! BKS - PATRIOT', 'HAUS! BKS - PATRIOT'),
    ('HAUS! JKT - PENGUMBEN', 'HAUS! PENGUMBEN'),
    ('HAUS! BKS - PRAMUKA RAWALUMBU', 'HAUS! BKS - PRAMUKA RAWALUMBU'),
    ('HAUS! BDG - DIPATIUKUR', 'HAUS! DIPATIUKUR'),
    ('HAUS! BDG - CIMAHI 2', 'HAUS! BDG - AMIR MACHMUD'),
    ('HAUS! BGR - POMAD BOGOR', 'HAUS! BGR - POMAD BOGOR'),
    ('HAUS! SKB - CISAAT', 'HAUS! SKB - CISAAT'),
    ('HAUS! BGR - SURYA KENCANA', 'HAUS! BGR - SURYA KENCANA'),
    ('HAUS! BKS - DUKUH ZAMBRUD', 'HAUS! BKS - DUKUH ZAMBRUD'),
    ('HAUS! JKT - CITRA GARDEN 7', 'HAUS! JKT - CITRA GARDEN 7'),
    ('HAUS! BDG - CIUMBULEUIT', 'HAUS! BDG - CIUMBULEUIT'),
    ('HAUS! CKR - TARUM BARAT CIKARANG', 'HAUS! CKR - TARUM BARAT CIKARANG'),
    ('HAUS! BKS - MUTIARA GADING', 'HAUS! BKS - MUTIARA GADING'),
    ('HAUS! BKS - SUMBER ARTHA BINTARA', 'HAUS! BKS - SUMBER ARTHA BINTARA'),
    ('HAUS! JKT - TAMAN KOTA KEMBANGAN', 'HAUS! JKT - TAMAN KOTA KEMBANGAN'),
    ('HAUS! BKS - MUCHTAR TABRANI', 'HAUS! BKS - MUCHTAR TABRANI'),
    ('HAUS! SBG - OTISTA', 'HAUS! SBG - OTISTA'),
    ('HAUS! JKT - STASIUN GAMBIR', 'HAUS! JKT - STASIUN GAMBIR'),
    ('HAUS! BKS - KALIABANG', 'HAUS! BKS - KALIABANG'),
    ('HAUS! JKT - CITY PARK', 'HAUS! JKT - CITY PARK'),
    ('HAUS! DPK - ITC DEPOK', 'HAUS! DPK - ITC DEPOK'),
    ('HAUS! PWK - UPI PURWAKARTA', 'HAUS! PWK - UPI PURWAKARTA'),
    ('HAUS! BGR - CIKARET CIBINONG', 'HAUS! BGR - CIKARET CIBINONG'),
    ('HAUS! BDG - RANCAEKEK', 'HAUS! BDG - RANCAEKEK'),
    ('HAUS! BKS - GRAND WISATA', 'HAUS! BKS - GRAND WISATA'),
    ('HAUS! BKS - KEMANG RAYA JATICEMPAKA', 'HAUS! BKS - KEMANG RAYA JATICEMPAKA'),
    ('HAUS! BKS - PLASA CIBUBUR', 'HAUS! BKS - PLASA CIBUBUR'),
    ('Haus Office Meruya', 'Haus Office Meruya'),
    ('Haus Office Sastra Graha', 'Haus Office Sastra Graha'),]


class CrmQuestionareAdmin(models.Model):
    _name = "crm.questionare.admin"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = "CRM Questionare Form"
    _rec_name = "questionare_name_fields"

    @api.model
    def create(self,vals):
        if not vals.get('list_questions_fields'):
            raise ValidationError("Tidak Ada Pertanyaan Yang Ditulis")

        if len(vals['questionare_assigned_user'][0][2]) < 1:
            raise ValidationError("Harus Setidaknya ada User Yang di assign")

        vals['status'] = 'submitted'
        results = vals['questionare_assigned_user'][0][2]
        dict_data = {}

        for i in range(len(results)):
            search_data = self.env['employee.data'].search([('id','=',results[i])])
            email_data = search_data.mapped('email_employee')[0]
            name_data = search_data.mapped('first_name_employee')[0]
            template_data = {
            'subject': 'Haus Questioner CRM',
            'body_html': 'Hai {}, Kamu Telah Mendapat Task Untuk Mengisi Questioner {} harap Dikerjakan Tepat Waktu Yah'.format(name_data,vals['questionare_name_fields']),
            'email_from': 'erphaus@gmail.com',
            'auto_delete': True,
            'email_to': email_data,
            }
            mail_id = self.env['mail.mail'].sudo().create(template_data)
            mail_id.sudo().send()
            
            full_data = self.env['crm.questionare.admin'].search([])
            search_questions = self.env['crm.questions.admin'].search([])
            
                
            search_data_2_count = self.env['crm.questionare.user'].search_count([('questionare_name_fields', '=', vals['questionare_name_fields']),
                                                                                ('temporary_location_selection_fields', '=', vals['temporary_location_selection_fields']), ('date_of_downloaded', '=', datetime.today()),
                                                                                ('email_employee', '=', search_data.mapped('email_employee')[0])])

            search_data_2 = self.env['crm.questionare.user'].search([('questionare_name_fields', '=', vals['questionare_name_fields']),
                                                                    ('temporary_location_selection_fields', '=', vals['temporary_location_selection_fields']),('date_of_downloaded', '=', datetime.today()),
                                                                    ('email_employee', '=', search_data.mapped('email_employee')[0])])

            if search_data_2_count == 0:
                def my_filtering_function_content(pair):
                    key, value = pair
                    if value[2]['questionare_name'] == vals['questionare_name_fields']:
                        return True
                    else:
                        return False

                
                
                for x in range(len(vals['list_questions_fields'])):                        
                    dict_data[vals['list_questions_fields'][x][2]['question_audit_fields']] = (0, 0, {
                        'questionare_id': int(search_data_2),
                        'questionare_name': str(vals['questionare_name_fields']),
                        'question_audit_fields': str(vals['list_questions_fields'][x][2]['question_audit_fields']),
                        'questions_type_fields': vals['list_questions_fields'][x][2]['questions_type_fields']
                    })
               
                filtered_grades = dict(filter(my_filtering_function_content, dict_data.items()))
                """
                search_data_3 = self.env['crm.questionare.user'].search(
                    [('questionare_name_fields', '=', vals['questionare_name_fields']),('email_employee', '=', search_data.mapped('email_employee')[0])])
                search_data_3.sudo().write({

                })
                """
                self.env['crm.questionare.user'].sudo().create({
                    'user_fields':int(results[i]),
                    'email_employee':search_data.mapped('email_employee')[0],
                    'questionare_name_fields': vals['questionare_name_fields'],
                    'questionare_start_time_fields':vals['questionare_start_time_fields'],
                    'questionare_end_time_fields':vals['questionare_end_time_fields'],
                    'temporary_location_selection_fields': vals['temporary_location_selection_fields'],
                    'date_of_downloaded':datetime.today(),
                    'list_questions_fields': list(filtered_grades.values()),
                    'status':'assigned',
                })

        model_ref = 'dev_crm_haus.model_crm_questionare_admin'
        model = self.env.ref(model_ref, raise_if_not_found=False)
        scheduled_action = {'list_user':results,
        'questionare_name': vals['questionare_name_fields'],
        'list_question':list(filtered_grades.values()),
        'date_downloaded':datetime.today(),
        'temporary_location_selection_fields':vals['temporary_location_selection_fields'],
        }

        if (model) and (vals['timestamp_fields'] == '1_day') :
            # Create the scheduled action record
            ScheduledAction = self.env['ir.cron']
            action = ScheduledAction.create({
                'name': 'My Scheduled Action {}'.format(vals['questionare_name_fields']),
                'model_id': model.id,
                'state': 'code',
                'code': 'model.my_scheduled_function(dict_var={})'.format(scheduled_action),
                'interval_number': 1,  # Set the interval number (e.g., 1 for daily)
                'interval_type': 'days',  # Set the interval type (e.g., days, weeks, months, etc.)
                'numbercall': -1,  # Set to -1 to run indefinitely or set a specific number for limited runs
                'active': True,  # Set to True to activate the scheduled action
            })

            print("Scheduled action created successfully!")
        else:
            print("Model not found or not installed.")

        if (model) and (vals['timestamp_fields'] == '1_weeks') :
            # Create the scheduled action record
            ScheduledAction = self.env['ir.cron']
            action = ScheduledAction.create({
                'name': 'My Scheduled Action {}'.format(vals['questionare_name_fields']),
                'model_id': model.id,
                'state': 'code',
                'code': 'model.my_scheduled_function(dict_var={})'.format(scheduled_action),
                'interval_number': 1,  # Set the interval number (e.g., 1 for daily)
                'interval_type': 'weeks',  # Set the interval type (e.g., days, weeks, months, etc.)
                'numbercall': -1,  # Set to -1 to run indefinitely or set a specific number for limited runs
                'active': True,  # Set to True to activate the scheduled action
            })

            print("Scheduled action created successfully!")
        else:
            print("Model not found or not installed.")

        if (model) and (vals['timestamp_fields'] == '1_month') :
            # Create the scheduled action record
            ScheduledAction = self.env['ir.cron']
            action = ScheduledAction.create({
                'name': 'My Scheduled Action {}'.format(vals['questionare_name_fields']),
                'model_id': model.id,
                'state': 'code',
                'code': 'model.my_scheduled_function(dict_var={})'.format(scheduled_action),
                'interval_number': 1,  # Set the interval number (e.g., 1 for daily)
                'interval_type': 'months',  # Set the interval type (e.g., days, weeks, months, etc.)
                'numbercall': -1,  # Set to -1 to run indefinitely or set a specific number for limited runs
                'active': True,  # Set to True to activate the scheduled action
            })

            print("Scheduled action created successfully!")
        else:
            print("Model not found or not installed.")

        if (model) and (vals['timestamp_fields'] == '1_year') :
            # Create the scheduled action record
            ScheduledAction = self.env['ir.cron']
            action = ScheduledAction.create({
                'name': 'My Scheduled Action {}'.format(vals['questionare_name_fields']),
                'model_id': model.id,
                'state': 'code',
                'code': 'model.my_scheduled_function(dict_var={})'.format(scheduled_action),
                'interval_number': 12,  # Set the interval number (e.g., 1 for daily)
                'interval_type': 'months',  # Set the interval type (e.g., days, weeks, months, etc.)
                'numbercall': -1,  # Set to -1 to run indefinitely or set a specific number for limited runs
                'active': True,  # Set to True to activate the scheduled action
            })

            print("Scheduled action created successfully!")
        else:
            print("Model not found or not installed.")

        rec = super(CrmQuestionareAdmin, self).create(vals)
        return rec

    def unlink(self):
        for rec in self:
            self.env['crm.questionare.user'].search([('questionare_name_fields', '=', rec.questionare_name_fields)]).sudo().unlink()
            self.env['ir.cron'].search([('name','=','My Scheduled Action {}'.format(rec.questionare_name_fields))]).sudo().unlink()

        return super(CrmQuestionareAdmin, self).unlink()

    def write(self,vals):
        old_list = self.questionare_assigned_user.mapped('email_employee')
        updated_list = []

        try:
            if vals['questionare_assigned_user']:
                results = vals['questionare_assigned_user'][0][2]
                for i in range(len(results)):
                    search_data = self.env['employee.data'].search([('id','=',results[i])])
                    updated_list.append(search_data.mapped('email_employee')[0])
                    full_data = self.env['crm.questionare.admin'].search([])
                    search_questions = self.env['crm.questions.admin'].search([])
                    dict_data = {}
                        
                    search_data_2_count = self.env['crm.questionare.user'].search_count([('questionare_name_fields', '=', self.questionare_name_fields),
                                                                                        ('temporary_location_selection_fields', '=', self.temporary_location_selection_fields), ('temporary_location_selection_fields', '=', self.temporary_location_selection_fields),
                                                                                        ('email_employee', '=', search_data.mapped('email_employee')[0])])

                    search_data_2 = self.env['crm.questionare.user'].search([('questionare_name_fields', '=', self.questionare_name_fields),
                                                                            ('temporary_location_selection_fields', '=', self.temporary_location_selection_fields),
                                                                            ('email_employee', '=', search_data.mapped('email_employee')[0])])

                    if (search_data_2_count == 0):
                        self.env['crm.questionare.user'].sudo().create({
                            'user_fields':int(results[i]),
                            'email_employee':search_data.mapped('email_employee')[0],
                            'questionare_start_time_fields':self.questionare_start_time_fields,
                            'questionare_end_time_fields':self.questionare_end_time_fields,
                            'questionare_name_fields': self.questionare_name_fields,
                            'temporary_location_selection_fields': self.temporary_location_selection_fields,
                        })

                        def my_filtering_function_content(pair):
                            key, value = pair
                            if value[2]['questionare_name'] == self.questionare_name_fields:
                                return True
                            else:
                                return False


                        for x in range(len(self.list_questions_fields.mapped('questionare_name'))):
                            dict_data[self.list_questions_fields.mapped('question_audit_fields')[x]] = (0, 0, {
                                'questionare_id': int(search_data_2),
                                'questionare_name': str(self.list_questions_fields.mapped('questionare_name')[x]),
                                'question_audit_fields': str(self.list_questions_fields.mapped('question_audit_fields')[x]),
                                'questions_type_fields': str(self.list_questions_fields.mapped('questions_type_fields')[x])
                            })

                        
                        filtered_grades = dict(filter(my_filtering_function_content, dict_data.items()))
                        search_data_3 = self.env['crm.questionare.user'].search(
                            [('questionare_name_fields', '=', self.questionare_name_fields),('email_employee', '=', search_data.mapped('email_employee')[0])])
                        search_data_3.sudo().write({
                            'list_questions_fields': list(filtered_grades.values()),
                            'status':'assigned',
                        })
                
                    else:
                        def my_filtering_function_content(pair):
                            key, value = pair
                            if value[2]['questionare_name'] == self.questionare_name_fields:
                                return True
                            else:
                                return False

                        for x in range(len(self.list_questions_fields.mapped('questionare_name'))):
                            dict_data[self.list_questions_fields.mapped('question_audit_fields')[x]] = (0, 0, {
                                'questionare_id': int(search_data_2),
                                'questionare_name': str(self.list_questions_fields.mapped('questionare_name')[x]),
                                'question_audit_fields': str(self.list_questions_fields.mapped('question_audit_fields')[x]),
                                'questions_type_fields': str(self.list_questions_fields.mapped('questions_type_fields')[x])
                            })
                        
                        filtered_grades = dict(filter(my_filtering_function_content, dict_data.items()))
                
                reversed_list = []
                print('this is old list:',old_list)
                print('this is updated list:',updated_list)
                for data in old_list:
                    if data not in updated_list:
                        search_data = self.env['crm.questionare.user'].search([('email_employee','=',data),('questionare_name_fields','=',self.questionare_name_fields)]).sudo().unlink()
                
                for notified_person in updated_list:
                    search_data = self.env['employee.data'].search([('email_employee','=',notified_person)])
                    name_person = search_data.mapped('first_name_employee')[0]
                    template_data = {
                    'subject': 'Haus Questioner CRM',
                    'body_html': 'Hai {}, Kamu Telah Mendapat Task Untuk Mengisi Questioner {} harap Dikerjakan Tepat Waktu Yah'.format(name_person,self.questionare_name_fields),
                    'email_from': 'erphaus@gmail.com',
                    'auto_delete': True,
                    'email_to': notified_person,
                    }
                    mail_id = self.env['mail.mail'].sudo().create(template_data)
                    mail_id.sudo().send()
                
                for data in updated_list:
                    search_data = self.env['employee.data'].search([('email_employee','=',data)])
                    reversed_list.append(search_data.mapped('id')[0])
                scheduled_action = {'list_user':reversed_list,
                'questionare_name': self.questionare_name_fields,
                'list_question':list(filtered_grades.values()),
                'date_downloaded':datetime.today(),
                'temporary_location_selection_fields':self.temporary_location_selection_fields,
                }
                cron_search = self.env['ir.cron'].search([('name','=','My Scheduled Action {}'.format(self.questionare_name_fields))])
                cron_search.sudo().write({
                    'code': 'model.my_scheduled_function(dict_var={})'.format(scheduled_action),
                })


        except:
            print("Not Satisfied")
            updated_list = old_list
            pass


        

        try:
            if vals['list_questions_fields']:
                for name in updated_list:
                    search_data = self.env['employee.data'].search([('email_employee','=',name)])
                
                    search_data_2 = self.env['crm.questionare.user'].search([('questionare_name_fields', '=', self.questionare_name_fields),
                                                            ('temporary_location_selection_fields', '=', self.temporary_location_selection_fields),
                                                            ('email_employee', '=', name)])
                    dict_data = {}

                    def my_filtering_function_content(pair):
                        key, value = pair
                        if value[2]['questionare_name'] == self.questionare_name_fields:
                            return True
                        else:
                            return False

                    post_val = len(vals['list_questions_fields'])-1
                    post_data = []
                    for data in vals['list_questions_fields']:
                        if data[0] == 0 :
                            post_data.append(data)
                    for x in range(len(post_data)):
                        print(post_data[x])            
                        dict_data[post_data[x][2]['question_audit_fields']] = (0, 0, {
                            'questionare_id': int(search_data_2),
                            'questionare_name': str(self.questionare_name_fields),
                            'question_audit_fields': str(post_data[x][2]['question_audit_fields']),
                            'questions_type_fields': post_data[x][2]['questions_type_fields']
                        })
                    print('pass')
                    filtered_grades = dict(filter(my_filtering_function_content, dict_data.items()))
                    search_data_3 = self.env['crm.questionare.user'].search(
                        [('questionare_name_fields', '=', self.questionare_name_fields),('email_employee', '=', name)])
                    search_data_3.sudo().write({
                        'list_questions_fields': list(filtered_grades.values()),
                        'status':'assigned',
                    })
            for data in old_list:
                if data not in updated_list:
                    search_data = self.env['employee.data'].search([('first_name_employee','=',data)])
                    self.env['crm.questionare.user'].search([('questionare_name_fields', '=', self.questionare_name_fields),('email_employee', '=', data)]).sudo().unlink()

        except:
            pass

        res = super(CrmQuestionareAdmin, self).write(vals)
        return res

    questionare_name_fields = fields.Char(string="Questionare Name",required=True)
    logging_fields = fields.One2many('crm.log','id_questioner',compute='_compute_logging_fields')
    temporary_location_selection_fields = fields.Selection(site_list,string="Sites Selection",default="Haus Office Meruya",required=True)
    list_questions_fields = fields.One2many('crm.questions.admin','questionare_id')
    status = fields.Selection([('drafted','Drafted'),
    ('submitted','Submitted')
    ],string='status',default='drafted')
    questionare_assigned_user = fields.Many2many('employee.data',string="List Of Participant",domain = "[('current_status_employee','=','Active')]",required=True)
    questionare_start_time_fields = fields.Float(string="Start Time",required=True)
    questionare_end_time_fields = fields.Float(string="End Time",required=True)
    timestamp_fields = fields.Selection([
        ('1_day','Every Day'),
        ('1_weeks','Every Week'),
        ('1_month','Every Month'),
        ('1_year','Every Year'),
        ],string="Timestamp",required=True)
    _sql_constraints = [('questionare_name_fields', 'unique (questionare_name_fields)', 'Questionare Dengan Nama Serupa Sudah Ada'),]
    report_files = fields.Binary(string='Report Data',compute='compute_report_data')
    
    @api.depends('questionare_name_fields')
    def _compute_logging_fields(self):
        for record in self:
            record.logging_fields = self.env['crm.log'].search([('questioner', '=', record.questionare_name_fields)])

    def my_scheduled_function(self,dict_var):
        for i in range(len(dict_var['list_user'])):
            search_data = self.env['employee.data'].search([('id','=',dict_var['list_user'][i])])


            search_data_2_count = self.env['crm.questionare.user'].search_count([('questionare_name_fields', '=', dict_var['questionare_name']),
                                                                                ('temporary_location_selection_fields', '=', dict_var['temporary_location_selection_fields']), ('date_of_downloaded', '=', datetime.today()),
                                                                                ('email_employee', '=', search_data.mapped('email_employee')[0])])

            search_data_2 = self.env['crm.questionare.user'].search([('questionare_name_fields', '=', dict_var['questionare_name']),
                                                                                ('temporary_location_selection_fields', '=', dict_var['temporary_location_selection_fields']), ('date_of_downloaded', '=', datetime.today()),
                                                                                ('email_employee', '=', search_data.mapped('email_employee')[0])])

            if search_data_2_count == 0:
                self.env['crm.questionare.user'].sudo().create({
                    'user_fields':int(dict_var['list_user'][i]),
                    'email_employee':search_data.mapped('email_employee')[0],
                    'questionare_name_fields': dict_var['questionare_name'],
                    'temporary_location_selection_fields': dict_var['temporary_location_selection_fields'],
                    'date_of_downloaded':datetime.today(),
                    'list_questions_fields': dict_var['list_question']
                })
            print('questioner for {} have been Made'.format(search_data.mapped('email_employee')[0]))


    @api.depends('report_files')
    def compute_report_data(self):
        data_to_export = []

        search_data_questionare = self.env['crm.questionare.user'].search([])

        for record in search_data_questionare.filtered(lambda questionare:questionare.questionare_name_fields == self.questionare_name_fields ):
            questioner_name = record.questionare_name_fields
            search_user = self.env['employee.data'].search([('email_employee','=',record.email_employee)])
            questioner_user = search_user.mapped('first_name_employee')[0]
            questioner_date = record.date_of_downloaded

            
            for questions in record.list_questions_fields.filtered(lambda questionare:questionare.questionare_name == self.questionare_name_fields ):
                questioner_type_questions = questions.questions_type_fields
                questioner_questions = questions.question_audit_fields

                if questioner_type_questions == 'pilihan_ganda': 
                    try:
                        answers = questions.mapped('questions_selection_choice').mapped('answers_selections')[0]
                        print(answers)
                    except:
                        answers = "Not Answered"
                        print(answers)
                elif questioner_type_questions == "text":
                    answers = questions.answer_audit_fields
                elif questioner_type_questions == "true_false":
                    answers = questions.questions_yes_no_choice_fields

                data_to_export.append({'Questioner':questioner_name,
                                        'User':questioner_user, 
                                        'Date':questioner_date,
                                        'Questions':questioner_questions,
                                        'Type Questions':questioner_type_questions,
                                        'Answers':answers,
                })

        csv_data = ''
        if data_to_export:
            fields = data_to_export[0].keys()
            csv_data += ','.join(fields) + '\n'
            for record in data_to_export:
                values = [str(record[field]) for field in fields]
                csv_data += ','.join(values) + '\n'

        # Save the CSV data as a binary field
        self.write({'report_files': base64.b64encode(csv_data.encode('utf-8'))})

    @api.constrains('questionare_start_time_fields','questionare_end_time_fields')
    def _check_start_end_time(self):
        for record in self:
            if record.questionare_start_time_fields > record.questionare_end_time_fields:
                raise ValidationError("Start time cannot be greater than end time.")

    @api.constrains('questionare_assigned_user')
    def _check_questionare_assigned_user(self):
        for record in self:
            if not record.questionare_assigned_user:
                raise ValidationError("Data Partisipan Tidak Boleh Kosong")



    def download_csv_file(self):
        filename = 'my_file.csv'
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/binary/download_csv_file?id=%s&filename=%s' % (self.id, filename),
            'target': 'new',
        }