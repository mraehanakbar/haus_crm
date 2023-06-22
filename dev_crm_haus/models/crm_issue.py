from email.policy import default
import math
import requests
from requests import get
from odoo import api, fields, models, http, _
from datetime import datetime

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

    # Define Some Fields Or Function Here
    issue_problem = fields.Char(String="Problem", required=True)
    issue_category = fields.Many2one(
        "crm.category", String="Category", required=True)

    issue_due_date = fields.Datetime(String="Due Date")
    issue_comment = fields.Text(String="Comment")
    issue_attachment = fields.Binary("Attachment", attachment=True)

    

    employee_id = fields.Many2one(
    "employee.data", String="Employee", defaults = lambda self: self.env.user, required=True)
    department = fields.Selection(String="Departemen", related='employee_id.organization_employee')

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
    
    #Tambahin nama user (first_name + last_name)
    reporter_name = fields.Char(String="Reporter Name", readonly=True ,default=get_name_user)
    department_reporter = fields.Char(String="Halo", readonly=True ,default=get_department_user)

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


    temporary_location_selection = fields.Selection(site_list['name'],
                                                    string="Sites Selection", default="Haus Office Meruya")

    priority = fields.Selection(
        [('0', 'Not Important'), ('1', 'Low'), ('2', 'Medium'), ('3', 'High')], string='Priority', default='1')

    state = fields.Selection(
        [('not_solved', 'Not Solved'), ('solved', 'Solved')], default='not_solved', string="State")

    # kirim email notifikasi ketika issue dibuat
    def notif_email(self):
        attachment = self.env['ir.attachment'].create({
            'name': 'attachment.pdf',
            'datas': self.issue_attachment,
            'type': 'binary'})
        template_data = {
            'subject': 'Haus Issue Letter',
            'body_html': f'<h1>Dear {self.employee_name}</h1> <h2> kamu mendapatkan masalah/issue berupa {self.issue_problem} dari {self.reporter_name} di cabang {self.temporary_location_selection} </h2>  <p> pada tanggal <b>{self.created_at}</b> dengan kategori {self.issue_category.name} dan prioritas {self.priority} dengan deadline <b>{self.issue_due_date}</b> dengan catatan {self.issue_comment} </p>',
            'email_from': 'hrdummyhaus1@gmail.com',
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
            'email_from': 'hrdummyhaus1@gmail.com',
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
            'email_from': 'hrdummyhaus1@gmail.com',
            'auto_delete': True,
            'email_to': self.reporter_email,
        }
        mail_id = self.env['mail.mail'].sudo().create(template_data)
        mail_id.sudo().send()
        
    # fungsi untuk mengirim email ketika deadline kurang 3 hari
    @api.model
    def send_deadline_email(self):
        deadline_date = self.issue_due_date - timedelta(days=3)
        records = self.search([('issue_due_date', '=', deadline_date)])
        if records:
            template_data = {
                'subject': 'Haus Deadline Issue Letter',
                'body_html': f'Deadline issue kamu dengan judul {self.issue_problem} akan berakhir dalam 3 hari di {self.temporary_location_selection}',
                'email_from': 'hrdummyhaus1@gmail.com',
                'auto_delete': True,
                'email_to': self.employee_email,
            }
            mail_id = self.env['mail.mail'].sudo().create(template_data)
            mail_id.sudo().send()

    check_is_reporter_login = fields.Boolean(
    string="Reporter Login? ", default=True, compute='get_user_login_reporter')

    @api.depends('check_is_reporter_login')
    def get_user_login_reporter(self):
        user_crnt = self._uid
        if self.env.user.login == self.reporter_email:
            self.check_is_reporter_login = True
        else:
            self.check_is_reporter_login = False

#   -->GEO User Location<--
    latitude = fields.Float(string='Latitude',)
    longitude = fields.Float(string='Longitude',)
    is_nearby = fields.Boolean('Is nearby?', default=False)

    #Onchange Based on field temporary_location_selection
    @api.onchange('temporary_location_selection')
    def _onchange_temporary_location_selection(self):
        def is_nearby_calc(lat1, lon1, lat2, lon2):
            radius = 6371  # km
            dlat = math.radians(lat2 - lat1)
            dlon = math.radians(lon2 - lon1)
            a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
                math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
                math.sin(dlon / 2) * math.sin(dlon / 2))
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            d = radius * c
            return d #Distance in KM

        i = 0
        for site_name, _ in site_list['name']:
            if site_name == self.temporary_location_selection:
                distance =  is_nearby_calc(
                    lat1 = self.latitude,
                    lon1 = self.longitude,
                    lat2 = site_list['location'][i][0],
                    lon2 = site_list['location'][i][1],
                )
                #Untuk Debugging
                self.issue_problem = f'lat:{self.latitude}; long:{self.longitude}'
                if distance < 1:
                    self.is_nearby = True
                    self.issue_comment = f'distance: {distance}'
                else:
                    self.is_nearby = False
                    self.issue_comment = f'distance: {distance}'
                break
            i += 1
