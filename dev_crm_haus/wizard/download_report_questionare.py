import math
import requests
from requests import get
from odoo import api, fields, models, http, _
from datetime import datetime
from odoo.exceptions import ValidationError, UserError
import csv
import base64
from pytz import timezone
from lxml import etree
from email.policy import default


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
             ('HAUS TNG - VILLA TANGERANG INDAH',
              'HAUS TNG - VILLA TANGERANG INDAH'),
             ('HAUS! TNG - TALAGA BASTARI', 'HAUS! TNG - TALAGA BASTARI'),
             ('HAUS! JKT - SUMUR BOR', 'HAUS! JKT - SUMUR BOR'),
             ('HAUS! TNG - BUKIT SERUA INDAH', 'HAUS! TNG - BUKIT SERUA INDAH'),
             ('HAUS! TNG - CURUG', 'HAUS! TNG - CURUG'),
             ('HAUS! BGR - CITRA INDAH CITY', 'HAUS! BGR - CITRA INDAH CITY'),
             ('HAUS! DPK - MEKARSARI CIMANGGIS',
              'HAUS! DPK - MEKARSARI CIMANGGIS'),
             ('HAUS! BGR - CIAPUS', 'HAUS! BGR - CIAPUS'),
             ('HAUS! DPK - PENGASINAN SAWANGAN',
              'HAUS! DPK - PENGASINAN SAWANGAN'),
             ('HAUS! TNG - VILLA DAGO PAMULANG',
              'HAUS! TNG - VILLA DAGO PAMULANG'),
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
             ('HAUS! CKR - TARUM BARAT CIKARANG',
              'HAUS! CKR - TARUM BARAT CIKARANG'),
             ('HAUS! BKS - MUTIARA GADING', 'HAUS! BKS - MUTIARA GADING'),
             ('HAUS! BKS - SUMBER ARTHA BINTARA',
              'HAUS! BKS - SUMBER ARTHA BINTARA'),
             ('HAUS! JKT - TAMAN KOTA KEMBANGAN',
              'HAUS! JKT - TAMAN KOTA KEMBANGAN'),
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
             ('HAUS! BKS - KEMANG RAYA JATICEMPAKA',
              'HAUS! BKS - KEMANG RAYA JATICEMPAKA'),
             ('HAUS! BKS - PLASA CIBUBUR', 'HAUS! BKS - PLASA CIBUBUR'),
             ('Haus Office Meruya', 'Haus Office Meruya'),
             ('Haus Office Sastra Graha', 'Haus Office Sastra Graha'),
             ]


class DownloadReportQuestionare(models.TransientModel):
    _name = "download.report.questionare"
    _inherit = []
    _description = "download report of questionare"

    temporary_location_selection_fields = fields.Selection(
        site_list, string="Sites Selection", default="Haus Office Meruya")
    start_date_created_date_fields = fields.Date(string='Start Date Created')
    end_date_created_date_fields = fields.Date(string='End Date Created')
    start_date_submited_date_fields = fields.Date(
        string='Start Date Submitted')
    end_date_submited_date_fields = fields.Date(string='End Date Submitted')
    list_questionare_fields = fields.Many2one(
        'crm.questionare.admin', string="Questionare")
    questionare_name_fields = fields.Char(
        related='list_questionare_fields.questionare_name_fields')
    organization_employee = fields.Selection([
        ('OPERATION', 'Operation'),
        ('HUMAN RESOURCES', 'Human Resources'),
        ('PROCUREMENT & SUPPLY CHAIN', 'Procurement & Supply Chain'),
        ('FINANCE & ACCOUNTING', 'Finance & Accounting'),
        ('MARKETING', 'Marketing'),
        ('INTERNAL AUDIT', 'Internal Audit'),
        ('GENERAL MANAGEMENT', 'General Management'),
        ('BUSINESS DEVELOPMENT', 'Bussiness Development'),
        ('TECHNOLOGY', 'Technology'),
    ], string="User Departement", track_visibility='onchange')
    name_assigned_user_fields = fields.Many2one(
        'employee.data', string="Assined Users", domain="[('current_status_employee','=','Active')]")
    report_files = fields.Binary(
        string='Report Data', compute='download_report_completed')
    report_files_missed = fields.Binary(string='Report Data Missed')
    data_available = fields.Boolean(compute='download_report_completed')

    @api.depends('report_files', 'data_available')
    def download_report_completed(self):
        data_to_export = []

        def float_to_formatted_time(float_hours):
            hours = int(float_hours // 3600)
            minutes = int((float_hours % 3600) // 60)
            seconds = int(float_hours % 60)
            formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            return formatted_time

        if self.name_assigned_user_fields:
            for data in self.name_assigned_user_fields:
                email_employee = data.email_employee
        else:
            email_employee = ""

        key_of_search = {'start_date_created': ('date_of_downloaded', '>=', self.start_date_created_date_fields),
                         'end_date_created': ('date_of_downloaded', '<=', self.end_date_created_date_fields),
                         'sites_questioner': ('temporary_location_selection_fields', '=', self.temporary_location_selection_fields),
                         'start_date_submitted': ('submitted_date', '>=', self.start_date_submited_date_fields),
                         'end_date_submitted': ('submitted_date', '<=', self.end_date_submited_date_fields),
                         'questionare_name': ('questionare_name_fields', '=', self.questionare_name_fields),
                         'departement_user_asssigned': ('user_departement', '=', self.organization_employee),
                         'status_fields': ('status', '=', 'completed_reports'),
                         'name_of_users': ('email_employee', '=', email_employee)
                         }

        list_query = []
        if self.start_date_created_date_fields:
            print("Test Case Pass 1")
            list_query.append(key_of_search['start_date_created'])

        if self.start_date_submited_date_fields:
            print("Test Case Pass 2")
            list_query.append(key_of_search['start_date_submitted'])

        if self.end_date_created_date_fields:
            print("Test Case Pass 3")
            list_query.append(key_of_search['end_date_created'])

        if self.start_date_submited_date_fields:
            print("Test Case Pass 4")
            list_query.append(key_of_search['end_date_submitted'])

        if self.list_questionare_fields:
            print("Test Case Pass 5")
            list_query.append(key_of_search['questionare_name'])

        if self.temporary_location_selection_fields:
            print("Test Case Pass 6")
            list_query.append(key_of_search['sites_questioner'])

        if self.organization_employee:
            list_query.append(key_of_search['departement_user_asssigned'])

        if self.name_assigned_user_fields:
            list_query.append(key_of_search['name_of_users'])

        list_query.append(key_of_search['status_fields'])

        search_data = self.env['crm.questionare.user'].search(list_query)

        if search_data:
            self.data_available = True
            print("success")
            for data in search_data:
                questioner_name = data.questionare_name_fields
                search_user = self.env['employee.data'].search(
                    [('email_employee', '=', data.email_employee)])
                questioner_user = search_user.mapped('first_name_employee')[0]
                questioner_date_assigned = data.date_of_downloaded
                questioner_check_in_time = data.check_in_time_fields
                questioner_check_out_time = data.check_out_time_fields
                questioner_status = data.status
                questioner_category = data.questionare_category_fields
                questioner_sites = data.temporary_location_selection_fields
                questioner_user_departement = data.user_departement

                for questions in data.list_questions_fields:
                    questioner_type_questions = questions.questions_type_fields
                    question_audit = questions.question_audit_fields

                    if questioner_type_questions == 'pilihan_ganda':
                        try:
                            answers = questions.mapped('questions_selection_choice').mapped(
                                'answers_selections')[0]
                            print(answers)
                        except:
                            answers = "Not Answered"
                            print(answers)
                    elif questioner_type_questions == "text":
                        answers = questions.answer_audit_fields
                    elif questioner_type_questions == "true_false":
                        answers = questions.questions_yes_no_choice_fields

                    data_to_export.append({'Questioner': questioner_name,
                                           'User': questioner_user,
                                           'Date': questioner_date_assigned,
                                           'Check-in-Time': float_to_formatted_time(questioner_check_in_time),
                                           'Check-Out-Time': float_to_formatted_time(questioner_check_out_time),
                                           'Status': questioner_status,
                                           'Category': questioner_category,
                                           'Sites': questioner_sites,
                                           'Departement': questioner_user_departement,
                                           'Question': question_audit,
                                           'Question-Type': questioner_type_questions,
                                           'Answers': answers
                                           })

            csv_data = ''
            if data_to_export:
                fields = data_to_export[0].keys()
                csv_data += ','.join(fields) + '\n'
                for record in data_to_export:
                    values = [str(record[field]) for field in fields]
                    csv_data += ','.join(values) + '\n'

            self.write(
                {'report_files': base64.b64encode(csv_data.encode('utf-8'))})

        else:
            self.data_available = False
            self.write({'report_files': False})

    def download_csv_file_completed_report(self):
        if self.data_available:
            filename = 'completed_report.csv'
            return {
                'type': 'ir.actions.act_url',
                'url': '/web/binary/download_csv_file_completed_report?id=%s&filename=%s' % (self.id, filename),
                'target': 'new',
            }
        else:
            raise ValidationError("No Data")


class DownloadReportQuestionareMissed(models.TransientModel):
    _name = "download.report.questionare.missed"
    _inherit = []
    _description = "download report of questionare that Missed"

    temporary_location_selection_fields = fields.Selection(
        site_list, string="Sites Selection", default="Haus Office Meruya")
    start_date_created_date_fields = fields.Date(string='Start Date Created')
    end_date_created_date_fields = fields.Date(string='End Date Created')
    organization_employee = fields.Selection([
        ('OPERATION', 'Operation'),
        ('HUMAN RESOURCES', 'Human Resources'),
        ('PROCUREMENT & SUPPLY CHAIN', 'Procurement & Supply Chain'),
        ('FINANCE & ACCOUNTING', 'Finance & Accounting'),
        ('MARKETING', 'Marketing'),
        ('INTERNAL AUDIT', 'Internal Audit'),
        ('GENERAL MANAGEMENT', 'General Management'),
        ('BUSINESS DEVELOPMENT', 'Bussiness Development'),
        ('TECHNOLOGY', 'Technology'),
    ], string="User Departement", track_visibility='onchange')
    list_questionare_fields = fields.Many2one(
        'crm.questionare.admin', string="Questionare")
    questionare_name_fields = fields.Char(
        related='list_questionare_fields.questionare_name_fields')
    name_assigned_user_fields = fields.Many2one(
        'employee.data', string="Assigned User", domain="[('current_status_employee','=','Active')]")
    report_files = fields.Binary(
        string='Report Data', compute='download_report_missed')
    data_available = fields.Boolean(compute='download_report_missed')

    @api.depends('report_files', 'data_available')
    def download_report_missed(self):
        data_to_export = []

        def float_to_formatted_time(float_hours):
            hours = int(float_hours // 3600)
            minutes = int((float_hours % 3600) // 60)
            seconds = int(float_hours % 60)
            formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            return formatted_time

        if self.name_assigned_user_fields:
            for data in self.name_assigned_user_fields:
                email_employee = data.email_employee

        else:
            email_employee = ''

        key_of_search = {
            'start_date_created': ('date_of_downloaded', '>=', self.start_date_created_date_fields),
            'end_date_created': ('date_of_downloaded', '<=', self.end_date_created_date_fields),
            'sites_questioner': ('temporary_location_selection_fields', '=', self.temporary_location_selection_fields),
            'questionare_name': ('questionare_name_fields', '=', self.questionare_name_fields),
            'departement_user_asssigned': ('user_departement', '=', self.organization_employee),
            'status_fields': ('status', '=', 'missed_reports'),
            'name_of_users': ('email_employee', '=', email_employee)
        }

        list_query = []
        if self.start_date_created_date_fields:
            print("Test Case Pass 1")
            list_query.append(key_of_search['start_date_created'])

        if self.end_date_created_date_fields:
            print("Test Case Pass 3")
            list_query.append(key_of_search['end_date_created'])

        if self.list_questionare_fields:
            print("Test Case Pass 5")
            list_query.append(key_of_search['questionare_name'])

        if self.temporary_location_selection_fields:
            print("Test Case Pass 6")
            list_query.append(key_of_search['sites_questioner'])

        if self.organization_employee:
            list_query.append(key_of_search['departement_user_asssigned'])

        if self.name_assigned_user_fields:
            list_query.append(key_of_search['name_of_users'])

        list_query.append(key_of_search['status_fields'])

        search_data = self.env['crm.questionare.user'].search(list_query)

        if search_data:
            self.data_available = True
            print("success")
            for data in search_data:
                questioner_name = data.questionare_name_fields
                search_user = self.env['employee.data'].search(
                    [('email_employee', '=', data.email_employee)])
                questioner_user = search_user.mapped('first_name_employee')[0]
                questioner_date_assigned = data.date_of_downloaded
                questioner_status = data.status
                questioner_category = data.questionare_category_fields
                questioner_sites = data.temporary_location_selection_fields
                questioner_user_departement = data.user_departement

                for questions in data.list_questions_fields:
                    questioner_type_questions = questions.questions_type_fields
                    question_audit = questions.question_audit_fields

                    if questioner_type_questions == 'pilihan_ganda':
                        try:
                            answers = questions.mapped('questions_selection_choice').mapped(
                                'answers_selections')[0]
                            print(answers)
                        except:
                            answers = "Not Answered"
                            print(answers)
                    elif questioner_type_questions == "text":
                        answers = questions.answer_audit_fields
                    elif questioner_type_questions == "true_false":
                        answers = questions.questions_yes_no_choice_fields

                    data_to_export.append({'Questioner': questioner_name,
                                           'User': questioner_user,
                                           'Date': questioner_date_assigned,
                                           'Sites': questioner_sites,
                                           'Departement': questioner_user_departement,
                                           'Status': questioner_status,
                                           })

            csv_data = ''
            if data_to_export:
                fields = data_to_export[0].keys()
                csv_data += ','.join(fields) + '\n'
                for record in data_to_export:
                    values = [str(record[field]) for field in fields]
                    csv_data += ','.join(values) + '\n'

            self.write(
                {'report_files': base64.b64encode(csv_data.encode('utf-8'))})

        else:
            self.data_available = False
            self.write({'report_files': False})

    def download_csv_file_missed_report(self):
        if self.data_available:
            filename = 'missed_report.csv'
            return {
                'type': 'ir.actions.act_url',
                'url': '/web/binary/download_csv_file_missed_report?id=%s&filename=%s' % (self.id, filename),
                'target': 'new',
            }
        else:
            raise ValidationError("No Data")


class DownloadReportIssue(models.TransientModel):
    _name = "download.report.issue"
    _inherit = []
    _description = "download report of issue"

    temporary_location_selection = fields.Selection(
        site_list, string="Sites Selection", default="Haus Office Meruya")
    start_date_created_date_issue_fields = fields.Date(
        string='Start Date Created Issue')
    end_date_created_date_issue_fields = fields.Date(
        string='End Date Created Issue')

    start_date_solved_date_issue_fields = fields.Date(
        string='Start Date Solved Issue')
    end_date_solved_date_issue_fields = fields.Date(
        string='End Date Solved Issue')
    organization_employee_reporter = fields.Selection([
        ('OPERATION', 'Operation'),
        ('HUMAN RESOURCES', 'Human Resources'),
        ('PROCUREMENT & SUPPLY CHAIN', 'Procurement & Supply Chain'),
        ('FINANCE & ACCOUNTING', 'Finance & Accounting'),
        ('MARKETING', 'Marketing'),
        ('INTERNAL AUDIT', 'Internal Audit'),
        ('GENERAL MANAGEMENT', 'General Management'),
        ('BUSINESS DEVELOPMENT', 'Bussiness Development'),
        ('TECHNOLOGY', 'Technology'),
    ], string="Reporter Departement", track_visibility='onchange')

    organization_employee_assigned_user = fields.Selection([
        ('OPERATION', 'Operation'),
        ('HUMAN RESOURCES', 'Human Resources'),
        ('PROCUREMENT & SUPPLY CHAIN', 'Procurement & Supply Chain'),
        ('FINANCE & ACCOUNTING', 'Finance & Accounting'),
        ('MARKETING', 'Marketing'),
        ('INTERNAL AUDIT', 'Internal Audit'),
        ('GENERAL MANAGEMENT', 'General Management'),
        ('BUSINESS DEVELOPMENT', 'Bussiness Development'),
        ('TECHNOLOGY', 'Technology'),
    ], string="Assigned User Departement", track_visibility='onchange')

    state = fields.Selection(
        [('open', 'Open'), ('not_solved', 'Not Solved'), ('solved', 'Solved'), ('overdue', 'Overdue')], default='open', string="State", required=True)

    reporter_employee = fields.Many2one(
        'employee.data', string="Reporter", domain="[('current_status_employee','=','Active')]")
    assigned_employee = fields.Many2one(
        'employee.data', string="Assigned Users", domain="[('current_status_employee','=','Active')]")
    issue_problem = fields.Many2one('crm.issue')
    issue_problem_name = fields.Char(related='issue_problem.issue_problem')
    report_files = fields.Binary(
        string='Report Data', compute='download_report')
    data_available = fields.Boolean(compute='download_report')

    @api.depends('report_files', 'data_available')
    def download_report(self):
        data_to_export = []

        if self.reporter_employee:
            for data in self.reporter_employee:
                reporter_email = data.email_employee

        if self.assigned_employee:
            for data in self.assigned_employee:
                assigned_email = data.email_employee

        key_of_search = {
            'start_date_created': ('issue_created_date', '>=', self.start_date_created_date_issue_fields),
            'end_date_created': ('issue_created_date', '<=', self.end_date_created_date_issue_fields),
            'start_date_solved': ('issue_solved_date', '>=', self.start_date_solved_date_issue_fields),
            'end_date_solved': ('issue_solved_date', '<=', self.end_date_solved_date_issue_fields),
            'sites_questioner': ('temporary_location_selection', '=', self.temporary_location_selection),
            'issue_name': ('issue_problem', '=', self.issue_problem_name),
            'departement_user_reporter': ('department_reporter', '=', self.organization_employee_reporter),
            'status_fields': ('state', '=', self.state),
            'name_of_users_reporter': ('reporter_email', '=', reporter_email),
        }

        list_query = []
        if self.start_date_created_date_issue_fields:
            print("Test Case Pass 1")
            list_query.append(key_of_search['start_date_created'])

        if self.end_date_created_date_issue_fields:
            print("Test Case Pass 3")
            list_query.append(key_of_search['end_date_created'])

        if self.start_date_solved_date_issue_fields:
            print("Test Case Pass 5")
            list_query.append(key_of_search['start_date_solved'])

        if self.end_date_solved_date_issue_fields:
            print("Test Case Pass 6")
            list_query.append(key_of_search['end_date_solved'])

        if self.temporary_location_selection:
            list_query.append(key_of_search['sites_questioner'])

        if self.issue_problem:
            list_query.append(key_of_search['issue_name'])

        if self.state:
            list_query.append(key_of_search['status_fields'])

        if self.organization_employee_reporter:
            list_query.append(key_of_search['departement_user_reporter'])

        if self.reporter_employee:
            list_query.append(key_of_search['name_of_users_reporter'])

        search_data = self.env['crm.issue'].search(list_query)

        def float_to_formatted_time(float_hours):
            hours = int(float_hours // 3600)
            minutes = int((float_hours % 3600) // 60)
            seconds = int(float_hours % 60)
            formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            return formatted_time

        if search_data:
            self.data_available = True
            for data in search_data:
                reporter_employee = data.reporter_name
                search_user = self.env['employee.data'].search(
                    [('email_employee', '=', data.reporter_email)])
                temporary_location_selection = data.temporary_location_selection
                questioner_state = data.state

                data_to_export.append({'Issue': data.issue_problem,
                                       'User': reporter_employee,
                                       'Sites': temporary_location_selection,
                                       'Status': data.state,
                                       })

            csv_data = ''
            if data_to_export:
                fields = data_to_export[0].keys()
                csv_data += ','.join(fields) + '\n'
                for record in data_to_export:
                    values = [str(record[field]) for field in fields]
                    csv_data += ','.join(values) + '\n'

            self.write(
                {'report_files': base64.b64encode(csv_data.encode('utf-8'))})

        else:
            self.data_available = False
            self.write({'report_files': False})

    def download_csv_file_issue(self):
        if self.data_available:
            filename = 'issue_report.csv'
            return {
                'type': 'ir.actions.act_url',
                'url': '/web/binary/download_csv_file_issue_report?id=%s&filename=%s' % (self.id, filename),
                'target': 'new',
            }
        else:
            raise ValidationError("No Data")
