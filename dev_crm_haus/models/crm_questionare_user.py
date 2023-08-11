from email.policy import default
from odoo import api, fields, models, _
from datetime import datetime
import pytz
from odoo.exceptions import ValidationError
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


class CrmQuestionareUser(models.Model):
    _name = "crm.questionare.user"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = "CRM Questionare Form User"
    _rec_name = "questionare_name_fields"

    def get_current_user(self):
        data = self.env['employee.data'].search([('email_employee','=',self.env.user.login)], limit=1)
        return data
 
    def write(self, values):
        if (self.user_local_time < self.questionare_start_time_fields) and (self.curent_user_admin == False):
            raise ValidationError("You Are Not in Time to Fill The Questionare.")
        elif (self.user_local_time > self.questionare_end_time_fields) and (self.curent_user_admin == False):
            raise ValidationError("You Late to Fill The Questioner This Days.")
        return super(CrmQuestionareUser, self).write(values)

    user_fields = fields.Many2one('employee.data',string='Employee Data')
    email_employee = fields.Char(related="user_fields.email_employee")
    questionare_log = fields.Many2one('crm.log')
    questionare_name_fields = fields.Char(string="Questionare Name")
    temporary_location_selection_fields = fields.Selection(site_list,string="Sites Selection",default="Haus Office Meruya")
    list_questions_fields = fields.One2many('crm.questions.user','questionare_id')
    date_of_downloaded =  fields.Date(string="Date Of Downloaded")
    questionare_start_time_fields = fields.Float(string="Start Time")
    questionare_end_time_fields = fields.Float(string="End Time")
    user_local_time = fields.Float(compute='_compute_user_local_time', store=False)
    status = fields.Selection([('assigned','Assigned'),
    ('submitted','Submitted')],
    string="Status Of Your Questionare",default='assigned')
    curent_user_admin = fields.Boolean(string='is admin? ',compute='is_admin_login')
    
    @api.depends('questionare_start_time_fields')
    def _compute_user_local_time(self):
        user_timezone = self.env.user.tz or 'UTC'
        user_datetime = datetime.now(pytz.timezone(user_timezone)).time()
        print('start TIme',self.questionare_start_time_fields)
        print('end TIme',self.questionare_end_time_fields)
        times_final = user_datetime.hour * 3600 + user_datetime.minute * 60 + user_datetime.second
        print(times_final)
        self.user_local_time = times_final 

    @api.depends('curent_user_admin')
    def is_admin_login(self):
        if self.env.user.has_group('dev_crm_haus.group_crm_questioner_admin'):
            self.curent_user_admin = True
        else:
            self.curent_user_admin = False

    def list_data_user_questioner(self):
        return{
            'name': 'List Your Questioner',
            "type" : "ir.actions.act_window",
            "help":"No Questioner Yet !!!",
            "res_model" : self._name,
            "view_mode": "tree,form", 
            "domain": [('email_employee', '=', self.env.user.login)],
            "context":{'create': False, 'delete': False},
        }


    
 