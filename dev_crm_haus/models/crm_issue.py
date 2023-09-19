from email.policy import default
from math import radians, sin, cos, acos
import requests
from requests import get
from odoo import api, fields, models, http, _
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError

site_list = {
    'name':[
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
    'location':[
    (-6.2007562,106.7825184),
    (-6.3548109,106.8314291),
    (-6.2213356,106.7010479),
    (-6.8633967,107.5867264),
    (-6.9121355,107.6998974),
    (-6.1693577,106.7889386),
    (-6.2624373,106.7286241),
    (-6.2336871,106.7466062),
    (-6.9236617,107.559724),
    (-6.1233645,106.7151742),
    (-6.1534001,106.4278513),
    (-6.2049496,106.9326346),
    (-6.1626537,106.8631665),
    (-6.345643,106.8625284),
    (-7.0645883,110.4428938),
    (-6.3943489,106.9349595),
    (-6.35338,106.7151316),
    (-6.1710319,106.6770079),
    (-6.3086683,106.7532975),
    (-7.0611259,110.4262594),
    (-6.2279219,106.8536194),
    (-6.2307846,106.9324388),
    (-6.2363236,106.5816351),
    (-6.2007176,106.7828242),
    (-6.194567,106.8000964),
    (-6.9222817,107.6430881),
    (-6.220733,106.9168877),
    (-6.1358162,106.8235596),
    (-6.264949,106.9394229),
    (-6.2150184,106.6019186),
    (-6.2471408,106.9994353),
    (-6.1977074,106.8593855),
    (-6.2755608,106.8463213),
    (-6.2114359,106.8416363),
    (-6.1270133,106.8546103),
    
    #Dummy Value
    (1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),
    (1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),
    (1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),
    (1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),
    (1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),
    (1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),
    (1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),
    (1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),
   ]
}


class CrmIssue(models.Model):
    _name = "crm.issue"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "CRM Issue Form"
    _rec_name = "issue_problem"

    @api.model
    def create(self, vals):
        assigned_user = []
        vals['issue_status'] = 'submitted'
        vals['state'] = 'open'
        vals['issue_created_date'] = datetime.today()
        """
        if len(vals['assigned_employee'][0][2]) < 1:
            raise ValidationError("Harus Setidaknya ada User Yang di assign")
        """
        try:
            results = vals['assigned_employee'][0][2]
            for i in range(len(results)):
                search_data = self.env['employee.data'].search([('id','=',results[i])])
                email_data = search_data.mapped('email_employee')[0]
                name_data = search_data.mapped('first_name_employee')[0]
                template_data = {
                'subject': 'Haus Questioner CRM',
                'body_html': 'Hai {}, Kamu Telah Mendapat Issue {} oleh {}'.format(name_data,vals['issue_problem'],vals['reporter_name']),
                'email_from': 'erphaus@gmail.com',
                'auto_delete': True,
                'email_to': email_data,
                }
                mail_id = self.env['mail.mail'].sudo().create(template_data)
                mail_id.sudo().send()
                assigned_user.append([email_data,name_data])
            
            scheduled_list = {
                'list_involved_user': assigned_user,
                'reporter_name': vals['reporter_name'],
                'reporter_email': vals['reporter_email'],
                'issues': vals['issue_problem'],
                'due_date':vals['issue_due_date'],
                'category':self.env['crm.category'].search([('id','=',vals['issue_category'])]).name,
                'sites_selection':vals['temporary_location_selection'],
            }

            model_ref = 'dev_crm_haus.model_crm_issue'
            model = self.env.ref(model_ref, raise_if_not_found=False)
            ScheduledAction = self.env['ir.cron']
            due_date_str = scheduled_list['due_date']
            due_date_format = '%Y-%m-%d %H:%M:%S'
            due_date = datetime.strptime(due_date_str, due_date_format)
            next_call = due_date - timedelta(1)

            action = ScheduledAction.create({
                        'name': 'auto overdue issue {} by {} category {} sites {}'.format(scheduled_list['issues'],scheduled_list['reporter_name'],scheduled_list['category'],scheduled_list['sites_selection']),
                        'model_id': model.id,
                        'state': 'code',
                        'code': 'model.sending_auto_overdue(dict_var={})'.format(scheduled_list),
                        'interval_number': 1,  # Set the interval number (e.g., 1 for daily)
                        'nextcall': scheduled_list['due_date'],
                        'interval_type': 'minutes',  # Set the interval type (e.g., days, weeks, months, etc.)
                        'numbercall': 1,  # Set to -1 to run indefinitely or set a specific number for limited runs
                        'active': True,  # Set to True to activate the scheduled action
                        })
            second_action = ScheduledAction.create({
                        'name': 'overdue reminder issue {} by {} category {} sites {}'.format(scheduled_list['issues'],scheduled_list['reporter_name'],scheduled_list['category'],scheduled_list['sites_selection']),
                        'model_id': model.id,
                        'state': 'code',
                        'code': 'model.sending_reminder_due_date(dict_var={})'.format(scheduled_list),
                        'interval_number': 1,  # Set the interval number (e.g., 1 for daily)
                        'nextcall': next_call ,
                        'interval_type': 'minutes',  # Set the interval type (e.g., days, weeks, months, etc.)
                        'numbercall': 1,  # Set to -1 to run indefinitely or set a specific number for limited runs
                        'active': True,  # Set to True to activate the scheduled action
                        })
        
        except:
            pass
        res = super(CrmIssue, self).create(vals)
        return res

    def write(self,vals):
        old_user = self.assigned_employee.mapped('email_employee')
        assigned_user = []
        try:
            if vals['assigned_employee']:
                results = vals['assigned_employee'][0][2]
                for i in range(len(results)):
                    search_data = self.env['employee.data'].search([('id','=',results[i])])
                    email_data = search_data.mapped('email_employee')[0]
                    name_data = search_data.mapped('first_name_employee')[0]
                    if email_data not in old_user:
                        template_data = {
                        'subject': 'Haus Questioner CRM',
                        'body_html': 'Hai {}, Kamu Telah Mendapat Issue {} oleh {}'.format(name_data,self.issue_problem,self.reporter_name),
                        'email_from': 'erphaus@gmail.com',
                        'auto_delete': True,
                        'email_to': email_data,
                        }
                        mail_id = self.env['mail.mail'].sudo().create(template_data)
                        mail_id.sudo().send()
                    assigned_user.append([email_data,name_data])

                    scheduled_list = {
                        'list_involved_user': assigned_user,
                        'reporter_name': self.reporter_name,
                        'reporter_email': self.reporter_email,
                        'issues': self.issue_problem,
                        'due_date':self.issue_due_date,
                        'category':self.issue_category.name,
                        'sites_selection':self.temporary_location_selection,
                    }
                    cron_search_overdue = self.env['ir.cron'].search([('name','=','auto overdue issue {} by {} category {} sites {}'.format(self.issue_problem,self.reporter_name,self.issue_category.name,self.temporary_location_selection))])
                    if cron_search_overdue:
                        cron_search_overdue.write({
                            'code':'model.sending_auto_overdue(dict_var={})'.format(scheduled_list),
                        })
                    cron_search_overdue_reminder = self.env['ir.cron'].search([('name','=','overdue reminder issue {} by {} category {} sites {}'.format(self.issue_problem,self.reporter_name,self.issue_category.name,self.temporary_location_selection))])

        except:
            pass
        
        try:
            if vals['state'] == 'solved':
                vals['issue_solved_date'] = datetime.today()
                if self.env.user.login == self.reporter_email:
                    template_data = {
                    'subject': 'Haus Questioner CRM',
                    'body_html': 'Hai {}, Issue anda yang Bernama {} Telah Solved oleh {}'.format(user.first_name_employee,self.issue_problem,self.env.user.name),
                    'email_from': 'erphaus@gmail.com',
                    'auto_delete': True,
                    'email_to': self.reporter_email,
                    }
                    mail_id = self.env['mail.mail'].sudo().create(template_data)
                    mail_id.sudo().send()
                    assigned_user.append([email_data,name_data])

                for user in assigned_employee:
                    template_data = {
                    'subject': 'Haus Questioner CRM',
                    'body_html': 'Hai {}, Issue {} Telah Solved oleh {}'.format(user.first_name_employee,self.issue_problem,self.env.user.name),
                    'email_from': 'erphaus@gmail.com',
                    'auto_delete': True,
                    'email_to': user.email_employee,
                    }
                    mail_id = self.env['mail.mail'].sudo().create(template_data)
                    mail_id.sudo().send()
                    assigned_user.append([email_data,name_data])
        except:
            pass

        print(self.assigned_employee)
        res = super(CrmIssue, self).write(vals)
        return res

    # Define Some Fields Or Function Here
    issue_problem = fields.Char(required=True)
    issue_category = fields.Many2one("crm.category", String="Category", required=True)
    issue_due_date = fields.Datetime(string="Due Date")
    issue_created_date = fields.Date(string="Created Date",readonly=True)
    issue_solved_date = fields.Date(string="Solved Date",readonly=True)
    issue_comment = fields.Text(String="Comment")
    issue_attachment = fields.Binary("Attachment", attachment=True)
    assigned_employee = fields.Many2many('employee.data',string="Assigned Users",domain = "[('current_status_employee','=','Active')]",required=True)
    issue_checkin = fields.One2many('crm.activity.checkin','id_issue',string="Issue Checkin")
    issue_status = fields.Selection([('drafted','Drafted'),('submitted','Submitted')],default='drafted') 
    #Tambahin fungsi get_name_user
    def get_name_user(self):
        try:
            search_data = self.env['employee.data'].search([('email_employee', '=', self.env.user.login),('current_status_employee', '=', 'Active')])
            name = search_data.mapped('first_name_employee')[0]
           # last_name = search_data.mapped('last_name_employee')[0]
            return name
        except:
            return ''
            
    def get_department_user(self):
        try:
            search_data = self.env['employee.data'].search([('email_employee', '=', self.env.user.login)])
            position = search_data.mapped('organization_employee')[0]
            return position
        except:
            return ''
    
    def get_email(self):
        try:
            search_data = self.env['employee.data'].search(
                [('email_employee', '=', self.env.user.login)])
            email = search_data.mapped('email_employee')[0]
            return email
        except:
            return ''

    # Tambahin nama user (first_name + last_name)
    reporter_name = fields.Char(
        String="Reporter Name", readonly=True, default=get_name_user)
    department_reporter = fields.Char(
        String="Reporter Department", readonly=True, default=get_department_user)
    reporter_email = fields.Char(
        String="Reporter Email", readonly=True, default=get_email)
    check_is_reporter_login = fields.Boolean(string="is reporter login", compute="get_user_login_reporter", default=True)
    temporary_location_selection = fields.Selection(site_list['name'],
                                                    string="Sites Selection", default="Haus Office Meruya",required=True)

    priority = fields.Selection(
        [('0', 'Not Important'), ('1', 'Low'), ('2', 'Medium'), ('3', 'High')], string='Priority', default='1',required=True)

    state = fields.Selection(
        [('open', 'Open'),('not_solved', 'Not Solved'), ('solved', 'Solved'),('overdue', 'Overdue')], default='open', string="State",required=True)
    detail_of_issue = fields.Text(string="Details Of Issue")


    # kirim email notifikasi ketika issue dibuat
    def notif_email(self):
        attachment = self.env['ir.attachment'].create({
            'name': 'attachment.pdf',
            'datas': self.issue_attachment,
            'type': 'binary'})
        template_data = {
            'subject': 'Haus Issue Letter',
            'body_html': f'<h1>Dear {self.employee_name}</h1> <h2> kamu mendapatkan masalah/issue berupa {self.issue_problem} dari {self.reporter_name} di cabang {self.temporary_location_selection} </h2>  <p> pada tanggal <b>{self.created_at}</b> dengan kategori {self.issue_category.name} dan prioritas {self.priority} dengan deadline <b>{self.issue_due_date}</b> dengan catatan {self.issue_comment} </p>',
            'email_from': 'erphaus@gmail.com',
            'auto_delete': True,
            'email_to': self.employee_email,
            'attachment_ids': [(4, attachment.id)]
        }
        mail_id = self.env['mail.mail'].sudo().create(template_data)
        mail_id.sudo().send()

    # fungsi untuk mengubah status issue menjadi solved
    def solved_issue(self):
        self.state = "solved"
        self.notif_solved_email()

    # kirim email notifikasi ketika issue solved
    def notif_solved_email(self):
        template_data = {
            'subject': 'Haus Solved Issue Letter',
            'body_html': f'<h1>Dear {self.reporter_name}</h1> <h2> issue kamu dengan judul {self.issue_problem} telah selesai di {self.temporary_location_selection} </h2>  <p> pada tanggal <b>{self.created_at}</b> dengan kategori {self.issue_category.name} dan prioritas {self.priority} dengan deadline <b>{self.issue_due_date}</b> dengan catatan {self.issue_comment} </p>',
            'email_from': 'erphaus@gmail.com',
            'auto_delete': True,
            'email_to': self.reporter_email,
        }
        mail_id = self.env['mail.mail'].sudo().create(template_data)
        mail_id.sudo().send()

    # fungsi untuk mengubah status issue menjadi not solved
    def not_solved_issue(self):
        self.state = "not_solved"
        self.notif_not_solved_email()

    # kirim email notifikasi ketika issue solved
    def notif_not_solved_email(self):
        template_data = {
            'subject': 'Haus Not Solved Issue Letter',
            'body_html': f'<h1>Dear {self.reporter_name}</h1> <h2> issue kamu dengan judul {self.issue_problem} belum selesai di {self.temporary_location_selection} </h2>  <p> pada tanggal <b>{self.created_at}</b> dengan kategori {self.issue_category.name} dan prioritas {self.priority} dengan deadline <b>{self.issue_due_date}</b> dengan catatan {self.issue_comment} </p>',
            'email_from': 'erphaus@gmail.com',
            'auto_delete': True,
            'email_to': self.reporter_email,
        }
        mail_id = self.env['mail.mail'].sudo().create(template_data)
        mail_id.sudo().send()

    @api.depends('check_is_reporter_login')
    def get_user_login_reporter(self):
        user_crnt = self._uid
        if self.env.user.login == self.reporter_email:
            self.check_is_reporter_login = True
        else:
            self.check_is_reporter_login = False



    def issue_requested_list(self):
        return{
            'name': 'Requested Issue',
            "type": "ir.actions.act_window",
            "help": "No Request Yet !!!",
            "res_model": self._name,
            "view_mode": "tree,form",
            "domain": [('assigned_employee.email_employee', '=', self.env.user.login)],
            "context": {'delete': False,'create':False},
        }

    def your_requested_issue_list(self):
        return{
            'name': 'Your Requested Issue',
            "type": "ir.actions.act_window",
            "help": "No Request Yet !!!",
            "res_model": self._name,
            "view_mode": "tree,form",
            "domain": [('reporter_email', '=', self.env.user.login)],
            "context": {},
        }

    def sending_auto_overdue(self,dict_var):
        search_data = self.env['crm.issue'].search([('issue_problem','=',dict_var['issues']), ('reporter_name','=',dict_var['reporter_name']),
        ('reporter_email','=',dict_var['reporter_email']),('reporter_name','=',dict_var['reporter_name']),('issue_category.name','=',dict_var['category']),('issue_due_date','=',dict_var['due_date']),
        ('temporary_location_selection','=',dict_var['sites_selection'])])

        if search_data:
            search_data.write({
                'state':'overdue'
            })
        for involved_user in dict_data['list_involved_user']:
            template_data = {
            'subject': 'Haus Questioner CRM',
            'body_html': '{}, issue {} telah Overdue'.format(involved_user[1],dict_var['issues']),
            'email_from': 'erphaus@gmail.com',
            'auto_delete': True,
            'email_to': involved_user[0],
            }
            mail_id = self.env['mail.mail'].sudo().create(template_data)
            mail_id.sudo().send()
            assigned_user.append([email_data,name_data])
    
    def sending_reminder_due_date(self,dict_var):
        for involved_user in dict_data['list_involved_user']:
            template_data = {
            'subject': 'Haus Questioner CRM',
            'body_html': '{}, issue {} Akan Overdue besok harap cek issue yang di assign kan ke anda'.format(involved_user[1],dict_var['issues']),
            'email_from': 'erphaus@gmail.com',
            'auto_delete': True,
            'email_to': involved_user[0],
            }
            mail_id = self.env['mail.mail'].sudo().create(template_data)
            mail_id.sudo().send()
            assigned_user.append([email_data,name_data])

        # User Coordinates
    latitude = fields.Float("latitude", digits=(16, 5))
    longitude = fields.Float("longitude", digits=(16, 5))

    is_near_one_km = fields.Boolean(default=True)

    @api.depends('latitude', 'longitude')
    def _compute_isnear(self):
        for i in range(len(site_list["name"])):
            if self.temporary_location_selection == site_list["name"][0]:
                index = i
                break
        xlat = radians(float(self.latitude))
        xlon = radians(float(self.longitude))
        ylat = radians(float(site_list["location"][index][0]))
        ylon = radians(float(site_list["location"][index][1]))
        dist = 6371.01 * acos(sin(xlat)*sin(ylat) + cos(xlat)*cos(ylat)*cos(xlon - ylon))

        if dist > 1:
            self.is_near_one_km = False
        else:
            self.is_near_one_km = True

class CrmActivityCheckin(models.Model):
    _name = "crm.activity.checkin"
    _description = "CRM Group Of assigned Users"
    _rec_name = "involved_employee"

    def write(self,vals):
        try:
            vals['involved_employee_status']
        except:
            vals['involved_employee_status'] = self.involved_employee_status
        
        if vals['involved_employee_status'] == 'done':
            search_data = self.env['employee.data'].search([('id','=',self.involved_employee.id)])
            user_name = search_data.first_name_employee
            
            send_email_to = self.reporter_issue_email
            template_data = {
            'subject': 'Haus Questioner CRM',
            'body_html': '{} Telah Menyelesaikan Checkin Issue {}'.format(user_name,self.issue_name),
            'email_from': 'erphaus@gmail.com',
            'auto_delete': True,
            'email_to': send_email_to,
            }
            mail_id = self.env['mail.mail'].sudo().create(template_data)
            mail_id.sudo().send()
        rec = super(CrmActivityCheckin, self).create(vals)
        return rec

    
    def get_current_user(self):
        data = self.env['employee.data'].search([('email_employee','=',self.env.user.login)], limit=1)
        return data

    id_issue = fields.Many2one('crm.issue')
    reporter_issue_email = fields.Char(related='id_issue.reporter_email')
    issue_name = fields.Char(related="id_issue.issue_problem")
    involved_employee = fields.Many2one("employee.data", string="Employee", default=get_current_user, readonly=True)
    involved_employee_name = fields.Char(related='involved_employee.first_name_employee')
    involved_employee_email = fields.Char(related='involved_employee.email_employee')
    involved_employee_desc = fields.Text(string="Description")
    involved_employee_attachments = fields.Binary(string='Attachments', attachment=True)
    file_involved_employee_attachments = fields.Char("File Name")
    involved_employee_status = fields.Selection([
        ('done','Done'),
        ('ongoing','Ongoing'),
        ('not_done','Not Done'),
    ], string="Status Of Checkin",required=True)
    current_assigned_user_login = fields.Boolean(string='is user login?',compute='_is_current_assigned_user_login')

    @api.depends('involved_employee_email')
    def _is_current_assigned_user_login(self):
        if self.involved_employee_email == self.env.user.login:
            self.current_assigned_user_login = True
        else:
            self.current_assigned_user_login = False


