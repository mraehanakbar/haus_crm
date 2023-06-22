from email.policy import default
import math
import requests
from requests import get
from odoo import api, fields, models, http, _
from datetime import datetime
from odoo.exceptions import ValidationError

site_list = {
    'name': [
        ('HAUS! JKT - BINUS 1', 'HAUS! BINUS 1'),
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
    ],
    'location': [
        (-6.2007562, 106.7825184),
        (-6.3548109, 106.8314291),
        (-6.2213356, 106.7010479),
        (-6.8633967, 107.5867264),
        (-6.9121355, 107.6998974),
        (-6.1693577, 106.7889386),
        (-6.2624373, 106.7286241),
        (-6.2336871, 106.7466062),
        (-6.9236617, 107.559724),
        (-6.1233645, 106.7151742),
        (-6.1534001, 106.4278513),
        (-6.2049496, 106.9326346),
        (-6.1626537, 106.8631665),
        (-6.345643, 106.8625284),
        (-7.0645883, 110.4428938),
        (-6.3943489, 106.9349595),
        (-6.35338, 106.7151316),
        (-6.1710319, 106.6770079),
        (-6.3086683, 106.7532975),
        # Dummy Value
        (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1,
                                                                                                                         1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
        (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1,
                                                                                                                         1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
        (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1,
                                                                                                                         1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
        (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1,
                                                                                                                         1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
        (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1,
                                                                                                                         1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
        (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1,
                                                                                                                         1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
        (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1,
                                                                                                                         1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
        (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1,
                                                                                                                         1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
    ]
}


class download_questionare(models.TransientModel):
    _name = "download.questionare"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "download questionare"

    temporary_location_selection_fields = fields.Selection(site_list['name'],
                                                           string="Sites Selection", default="Haus Office Meruya")

    downloaded_date = fields.Date(
        string='Start Date', default=datetime.today(), readonly=True)

    latitude = fields.Float(string='Latitude')
    longitude = fields.Float(string='Longitude')
    is_nearby = fields.Boolean('Is nearby?', default=False)

    def my_filtering_function_quiz(pair):
        key, value = pair
        if value[2]['content_id'] == self.course_title:
            return True
        else:
            return False

    def download_the_questionare(self):
        full_data = self.env['crm.questionare.admin'].search([])
        search_questions = self.env['crm.questions.admin'].search([])

        dict_data = {}

        for i in range(len(full_data.mapped('questionare_name_fields'))):
            current_data = full_data.mapped(
                'temporary_location_selection_fields')[i]

            if current_data == self.temporary_location_selection_fields:
                search_data_2_count = self.env['crm.questionare.user'].search_count([('questionare_name_fields', '=', full_data.mapped('questionare_name_fields')[i]),
                                                                                     ('temporary_location_selection_fields', '=', full_data.mapped('temporary_location_selection_fields')[
                                                                                      i]), ('temporary_location_selection_fields', '=', full_data.mapped('temporary_location_selection_fields')[i]),
                                                                                     ('email_employee', '=', self.env.user.login)])

                search_data_2 = self.env['crm.questionare.user'].search([('questionare_name_fields', '=', full_data.mapped('questionare_name_fields')[i]),
                                                                         ('temporary_location_selection_fields', '=', full_data.mapped('temporary_location_selection_fields')[
                                                                          i]), ('temporary_location_selection_fields', '=', full_data.mapped('temporary_location_selection_fields')[i]),
                                                                         ('email_employee', '=', self.env.user.login)])

                if search_data_2_count == 0:
                    self.env['crm.questionare.user'].sudo().create({
                        'questionare_name_fields': full_data.mapped('questionare_name_fields')[i],
                        'temporary_location_selection_fields': full_data.mapped('temporary_location_selection_fields')[i],
                        'date_of_downloaded': self.downloaded_date
                    })

                    # Make record in model log
                    self.env['crm.log'].sudo().create({
                        'name': self.env.user.name,
                        'location': self.temporary_location_selection_fields,
                    })

                    def my_filtering_function_content(pair):
                        key, value = pair
                        if value[2]['questionare_name'] == full_data.mapped('questionare_name_fields')[i]:
                            return True
                        else:
                            return False

                    for x in range(len(search_questions.mapped('question_audit_fields'))):
                        dict_data[search_questions.mapped('question_audit_fields')[x]] = (0, 0, {
                            'questionare_id': int(search_data_2),
                            'questionare_name': str(search_questions.mapped('questionare_name')[x]),
                            'question_audit_fields': str(search_questions.mapped('question_audit_fields')[x]),
                        })

                    filtered_grades = dict(
                        filter(my_filtering_function_content, dict_data.items()))
                    print(filtered_grades)
                    search_data_3 = self.env['crm.questionare.user'].search(
                        [('questionare_name_fields', '=', full_data.mapped('questionare_name_fields')[i])])
                    search_data_3.sudo().write({
                        'list_questions_fields': list(filtered_grades.values())
                    })

                elif search_data_2_count > 0:
                    pass
