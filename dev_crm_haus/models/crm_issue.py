from email.policy import default
from math import radians, sin, cos, acos
import requests
from requests import get
from odoo import api, fields, models, http, _
from datetime import datetime, timedelta
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
        ('HAUS! JKT- GEMPOL RAYA', 'HAUS! JKT - GEMPOL RAYA '),
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
        (-7.0611259, 110.4262594),
        (-6.2279219, 106.8536194),
        (-6.2307846, 106.9324388),
        (-6.2363236, 106.5816351),
        (-6.2007176, 106.7828242),
        (-6.194567, 106.8000964),
        (-6.9222817, 107.6430881),
        (-6.220733, 106.9168877),
        (-6.1358162, 106.8235596),
        (-6.264949, 106.9394229),
        (-6.2150184, 106.6019186),
        (-6.2471408, 106.9994353),
        (-6.1977074, 106.8593855),
        (-6.2755608, 106.8463213),
        (-6.2114359, 106.8416363),
        (-6.1270133, 106.8546103),
        (-6.115927632325443, 106.90793361626861),
        (-6.325300705649493, 106.70894545204256),
        (-6.310442191563008, 106.79355944040222),
        (-6.336672227924867, 106.8556169845825),
        (-6.300997185217326, 106.85908149992602),
        (-6.176746296260202, 106.70944944040063),
        (-6.898269337981991, 107.64359740325078),
        (-6.3988970776935075, 106.8774622808794),
        (-6.872549803003375, 107.55495592691682),
        (-6.393342566123217, 106.79563947770747),
        (-6.333908383724949, 106.92352347438099),
        (-6.343412320140023, 106.90870730971467),
        (-6.268952935472817, 106.99886567294158),
        (-6.251629203528347, 107.08708629436966),
        (-6.940088938799229, 107.66694026554195),
        (-6.215861549798408, 107.03294285389322),
        (-6.112954769471216, 106.571833555744),
        (-6.400376090219431, 106.83954566959733),
        (-6.330062521006743, 106.86700347962658),
        (-6.227663986808095, 106.8902936287611),
        (-6.346160404694089, 106.80432874739763),
        (-6.326156417090553, 106.81957828270848),
        (-6.394857517503807, 106.85139083669937),
        (-6.2481103659237585, 107.00603328763678),
        (-6.27889897526512, 106.83935296553392),
        (-6.567115107705874, 106.80080039344244),
        (-6.588514733836455, 106.79702385574939),
        (-6.5900578401018475, 106.78641243987701),
        (-6.28217393949244, 106.76132189437008),
        (-6.247725138647101, 106.83418045681465),
        (-6.256613514411855, 106.70424336105229),
        (-6.3995308, 106.8123894),
        (-6.295093039116308, 106.84154795389414),
        (-6.197136399496007, 106.75323789312318),
        (-6.185915761224074, 106.81711790708506),
        (-6.479864478757981, 106.86372310306824),
        (-6.1852678033732635, 107.00837696485769),
        (-6.211312342590514, 106.73783682505716),
        (-6.314422074950858, 106.76946774554379),
        (-6.638343941478415, 106.83211153670223),
        (-6.267154005414829, 106.97402190786188),
        (-6.236030117361777, 106.52385551553357),
        (-6.216082775928805, 106.82480286738522),
        (-6.562823174007476, 106.73257866738923),
        (-6.244909190358439, 106.81561098272947),
        (-6.934596070274961, 107.71938304372902),
        (-6.1804683978318735, 106.63051511156479),
        (-6.28908372666245, 106.70428980389188),
        (-6.271181160681297, 106.91205054973238),
        (-7.003449269995897, 107.61462229051543),
        (-6.1757952298982, 106.87015279807264),
        (-6.277557210162581, 106.80029513669808),
        (-6.169465460228763, 106.77238716923651),
        (-6.165761992865134, 106.72459816738464),
        (-6.116824629104174, 106.78140355944788),
        (1, 1),  # rawamangun ga nemu
        (-6.972559986307745, 107.63514872838745),
        (-6.1457440488657005, 106.70072445204038),
        (-6.262212562214131, 106.86538482876148),
        (-6.114501570117455, 106.88155410362778),
        (-6.139208361081501, 106.86288193556665),
        (-6.302457569811877, 106.67178318087824),
        (-6.940819837480411, 107.62844378273778),
        (-6.235559321204564, 106.62076903669754),
        (-6.257335565587353, 106.85575652505756),
        (-6.185399766288607, 107.00951846632788),
        (-6.229274576924845, 106.95532095389329),
        (-6.185986631059124, 106.98077135389282),
        (-6.1533605435632355, 106.79580603189306),
        (-6.328823541922718, 107.28997736923847),
        (-6.484268491486774, 106.84310618273224),
        (-7.299649932024479, 112.77107849623411),
        (-7.337810637164049, 112.73752522507075),
        (-7.268133525445651, 112.79608702321792),
        (-7.308666592691285, 112.67447779332531),
        (-7.331204816893479, 112.7780605502027),
        (-7.290130982206451, 112.6551285673981),
        (-7.261071765234731, 112.66759845390555),
        (-7.298316509719598, 112.75567182692211),
        (-7.308743301016201, 112.73487802110229),
        (-6.269966012634382, 106.73039710971386),
        (-7.206423043382805, 107.89450023856102),
        (-6.1237057683014235, 106.17223167902424),
        (-7.807984057269567, 110.37766098274875),
        (-7.777953348686752, 110.3370997674044),
        (-7.744812172949031, 110.37353349809187),
        (-7.74407795108482, 110.37330852203225),
        (-7.758548094194466, 110.38156545761609),
        (-7.804423211325308, 110.35083919835684),
        (-6.170613027046576, 106.6182535673846),
        (-6.915139731259296, 107.65313881342534),
        (-6.379505920857053, 106.81388919807493),
        (-6.695682223428855, 108.57361089430609),
        (-6.736280478836424, 108.52956316553933),
        (-7.8097278057850925, 110.38759809994473),
        (-7.771831816863411, 110.40937763671643),
        (-7.688393147488541, 110.41879955946715),
        (-6.921283326869446, 106.92268306739356),
        (-6.92041, 106.931),
        (-6.217477883450136, 106.34959995468806),
        (-6.717008774020249, 108.55038785277529),
        (-6.960728145215593, 107.56012765575387),
        (-6.187652264153272, 106.82394325389284),
        (-6.017439669311534, 106.04911712690684),
        (-7.561402275040791, 110.81499207904173),
        (-7.534910985781006, 110.83626898644904),
        (-7.551109885556036, 110.82957802842493),
        (-7.547517646586366, 110.7700731060256),
        (-7.551270159043201, 110.85934679152284),
        (-7.3643159859745735, 112.73488807903912),
        (-7.143040417768477, 112.61577620740773),
        (-7.451977859429996, 112.69791158572863),
        (-7.30845526765687, 112.72133466739831),
        (-7.280947146260755, 112.71684888088994),
        (-7.447827717567374, 112.71967204682758),
        (-7.439550306654653, 112.70370038644786),
        (-6.975317347034271, 110.39057977109806),
        (-6.963912796812199, 107.5931716650137),
        (-6.207431041100696, 106.75881888828489),
        (-6.985167904191542, 110.44829630972232),
        (-7.794488037397175, 110.3654464302935),
        (-6.23070478772185, 106.67878356113017),
        (-6.959963757699464, 110.44005354625834),
        (-6.846235946484415, 107.49001765760441),
        (-6.569619851186895, 106.81193558643724),
        (-6.230297349891127, 106.72544207902546),
        (-6.277691159872639, 107.18179314416462),
        (-6.419558931416396, 107.47187424040347),
        (-6.264368927819007, 106.77551115944941),
        (-6.258901060932581, 106.78963954040165),
        (-6.254626049095986, 106.6017784385496),
        (-6.254251565799071, 107.27231078804604),
        (-6.26106112264995, 106.7314616507073),
        (-6.170152660118426, 106.9018055115646),
        (-6.560032502108797, 106.76655759987716),
        (-6.588472101913354, 106.79700239807741),
        (-6.893841, 106.786186),
        (-6.184169050710427, 106.60368889919444),
        (-6.19492814973688, 106.65784750876489),
        (-6.420047670281343, 106.82874894410736),
        (-6.300388360743241, 106.68968050136307),
        (-6.245491575770345, 106.78429026114863),
        (-6.450681557362375, 106.80092423940052),
        (-6.195986136713143, 106.6950340557449),
        (-6.1430376112831055, 106.6815754364322),
        (-6.197989272732751, 106.61461436517514),
        (-6.601542288347586, 106.77343646925063),
        (-6.1705274269476185, 106.59557815204077),
        (-6.193809838831623, 106.50016062704037),
        (-6.149190888575189, 106.71853764040037),
        (-6.311288384354136, 106.7224179866983),
        (-6.25657435144064, 106.56092693601877),
        (-6.456693338665484, 107.03496344781158),
        (-6.364821886405428, 106.86593079354554),
        (-6.619163345802431, 106.78321575204595),
        (-6.410042826050325, 106.7548872692394),
        (-6.342605435668724, 106.71933512876248),
        (-6.199343094966318, 106.68544114077648),
        (-6.615171568470218, 106.81604269599744),
        (-6.446281709059968, 106.82852512797099),
        (-6.369555033501031, 106.91557536441799),
        (-6.21331600573855, 106.97852582785522),
        (-6.1027829863752565, 106.1551471532356),
        (-6.152570903123638, 106.78370330320675),
        (-6.3116613710389595, 106.93799936553435),
        (-6.259357757604723, 107.14667421799516),
        (-6.2876226577264465, 106.94301992505798),
        (-6.204208493274739, 106.87101388178739),
        (-6.484458666301561, 106.8176180976288),
        (-6.728727961732034, 108.56524384742035),
        (-6.736800888616858, 108.54998290548698),
        (-6.375733106769155, 106.80136960786312),
        (-6.244145059683831, 106.96739932082515),
        (-6.202017560388985, 106.76977543144372),
        (-6.269027588229759, 106.99920899569325),
        (-6.885933864219305, 107.61470126368924),
        (-6.871471313018215, 107.55506790101924),
        (-6.547586100095768, 106.82307791289769),
        (-6.896247604702588, 106.89978266259884),
        (-6.6096888344402975, 106.80422256780585),
        (-6.320533975965364, 107.01604259807426),
        (-6.145680029911377, 106.7008746338941),
        (-6.879542819286791, 107.6033793673929),
        (-6.311679482291182, 107.16509722893232),
        (-6.286145021770733, 107.03233845389397),
        (-6.248904761812652, 106.94580626738555),
        (-6.160020998838785, 106.75376690674601),
        (-6.220048038815127, 107.00281527252255),
        (-6.567096715628179, 107.76326366553731),
        (-6.177738983996747, 106.83105601658987),
        (-6.197669324385017, 106.98996263803423),
        (-6.136059813871376, 106.73239128087636),
        (-6.3923113752767895, 106.82311382208998),
        (-6.539314571298138, 107.44401910732142),
        (-6.473033828072042, 106.84446712210035),
        (-6.954927395515325, 107.77284681157396),
        (1, 1), # grand wisata ganemu coi
        (-6.265028129051987, 106.98736194452064),
        (1, 1), # plaza cibubur ganemu coi
        (-6.196783723579407, 106.75339331157866),
        # (-6.190187278589172, 106.76495195153555),
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
                search_data = self.env['employee.data'].search(
                    [('id', '=', results[i])])
                email_data = search_data.mapped('email_employee')[0]
                name_data = search_data.mapped('first_name_employee')[0]
                template_data = {
                    'subject': 'Haus Questioner CRM',
                    'body_html': 'Hai {}, Kamu Telah Mendapat Issue {} oleh {}'.format(name_data, vals['issue_problem'], vals['reporter_name']),
                    'email_from': 'erphaus@gmail.com',
                    'auto_delete': True,
                    'email_to': email_data,
                }
                mail_id = self.env['mail.mail'].sudo().create(template_data)
                mail_id.sudo().send()
                assigned_user.append([email_data, name_data])

            scheduled_list = {
                'list_involved_user': assigned_user,
                'reporter_name': vals['reporter_name'],
                'reporter_email': vals['reporter_email'],
                'issues': vals['issue_problem'],
                'due_date': vals['issue_due_date'],
                'category': self.env['crm.category'].search([('id', '=', vals['issue_category'])]).name,
                'sites_selection': vals['temporary_location_selection'],
            }

            model_ref = 'dev_crm_haus.model_crm_issue'
            model = self.env.ref(model_ref, raise_if_not_found=False)
            ScheduledAction = self.env['ir.cron']
            due_date_str = scheduled_list['due_date']
            due_date_format = '%Y-%m-%d %H:%M:%S'
            due_date = datetime.strptime(due_date_str, due_date_format)
            next_call = due_date - timedelta(1)

            action = ScheduledAction.create({
                'name': 'auto overdue issue {} by {} category {} sites {}'.format(scheduled_list['issues'], scheduled_list['reporter_name'], scheduled_list['category'], scheduled_list['sites_selection']),
                        'model_id': model.id,
                        'state': 'code',
                        'code': 'model.sending_auto_overdue(dict_var={})'.format(scheduled_list),
                        # Set the interval number (e.g., 1 for daily)
                        'interval_number': 1,
                        'nextcall': scheduled_list['due_date'],
                        # Set the interval type (e.g., days, weeks, months, etc.)
                        'interval_type': 'minutes',
                        'numbercall': 1,  # Set to -1 to run indefinitely or set a specific number for limited runs
                        'active': True,  # Set to True to activate the scheduled action
            })
            second_action = ScheduledAction.create({
                'name': 'overdue reminder issue {} by {} category {} sites {}'.format(scheduled_list['issues'], scheduled_list['reporter_name'], scheduled_list['category'], scheduled_list['sites_selection']),
                        'model_id': model.id,
                        'state': 'code',
                        'code': 'model.sending_reminder_due_date(dict_var={})'.format(scheduled_list),
                        # Set the interval number (e.g., 1 for daily)
                        'interval_number': 1,
                        'nextcall': next_call,
                        # Set the interval type (e.g., days, weeks, months, etc.)
                        'interval_type': 'minutes',
                        'numbercall': 1,  # Set to -1 to run indefinitely or set a specific number for limited runs
                        'active': True,  # Set to True to activate the scheduled action
            })

        except:
            pass
        res = super(CrmIssue, self).create(vals)
        return res

    def write(self, vals):
        old_user = self.assigned_employee.mapped('email_employee')
        assigned_user = []
        try:
            if vals['assigned_employee']:
                results = vals['assigned_employee'][0][2]
                for i in range(len(results)):
                    search_data = self.env['employee.data'].search(
                        [('id', '=', results[i])])
                    email_data = search_data.mapped('email_employee')[0]
                    name_data = search_data.mapped('first_name_employee')[0]
                    if email_data not in old_user:
                        template_data = {
                            'subject': 'Haus Questioner CRM',
                            'body_html': 'Hai {}, Kamu Telah Mendapat Issue {} oleh {}'.format(name_data, self.issue_problem, self.reporter_name),
                            'email_from': 'erphaus@gmail.com',
                            'auto_delete': True,
                            'email_to': email_data,
                        }
                        mail_id = self.env['mail.mail'].sudo().create(
                            template_data)
                        mail_id.sudo().send()
                    assigned_user.append([email_data, name_data])

                    scheduled_list = {
                        'list_involved_user': assigned_user,
                        'reporter_name': self.reporter_name,
                        'reporter_email': self.reporter_email,
                        'issues': self.issue_problem,
                        'due_date': self.issue_due_date,
                        'category': self.issue_category.name,
                        'sites_selection': self.temporary_location_selection,
                    }
                    cron_search_overdue = self.env['ir.cron'].search([('name', '=', 'auto overdue issue {} by {} category {} sites {}'.format(
                        self.issue_problem, self.reporter_name, self.issue_category.name, self.temporary_location_selection))])
                    if cron_search_overdue:
                        cron_search_overdue.write({
                            'code': 'model.sending_auto_overdue(dict_var={})'.format(scheduled_list),
                        })
                    cron_search_overdue_reminder = self.env['ir.cron'].search([('name', '=', 'overdue reminder issue {} by {} category {} sites {}'.format(
                        self.issue_problem, self.reporter_name, self.issue_category.name, self.temporary_location_selection))])

        except:
            pass

        try:
            if vals['state'] == 'solved':
                vals['issue_solved_date'] = datetime.today()
                if self.env.user.login == self.reporter_email:
                    template_data = {
                        'subject': 'Haus Questioner CRM',
                        'body_html': 'Hai {}, Issue anda yang Bernama {} Telah Solved oleh {}'.format(user.first_name_employee, self.issue_problem, self.env.user.name),
                        'email_from': 'erphaus@gmail.com',
                        'auto_delete': True,
                        'email_to': self.reporter_email,
                    }
                    mail_id = self.env['mail.mail'].sudo().create(
                        template_data)
                    mail_id.sudo().send()
                    assigned_user.append([email_data, name_data])

                for user in assigned_employee:
                    template_data = {
                        'subject': 'Haus Questioner CRM',
                        'body_html': 'Hai {}, Issue {} Telah Solved oleh {}'.format(user.first_name_employee, self.issue_problem, self.env.user.name),
                        'email_from': 'erphaus@gmail.com',
                        'auto_delete': True,
                        'email_to': user.email_employee,
                    }
                    mail_id = self.env['mail.mail'].sudo().create(
                        template_data)
                    mail_id.sudo().send()
                    assigned_user.append([email_data, name_data])
        except:
            pass

        print(self.assigned_employee)
        res = super(CrmIssue, self).write(vals)
        return res

    # Define Some Fields Or Function Here
    issue_problem = fields.Char(required=True)
    issue_category = fields.Many2one(
        "crm.category", String="Category", required=True)
    issue_due_date = fields.Datetime(string="Due Date")
    issue_created_date = fields.Date(string="Created Date", readonly=True)
    issue_solved_date = fields.Date(string="Solved Date", readonly=True)
    issue_comment = fields.Text(String="Comment")
    issue_attachment = fields.Binary("Attachment", attachment=True)
    assigned_employee = fields.Many2many(
        'employee.data', string="Assigned Users", domain="[('current_status_employee','=','Active')]", required=True)
    issue_checkin = fields.One2many(
        'crm.activity.checkin', 'id_issue', string="Issue Checkin")
    issue_status = fields.Selection(
        [('drafted', 'Drafted'), ('submitted', 'Submitted')], default='drafted')
    # Tambahin fungsi get_name_user

    def get_name_user(self):
        try:
            search_data = self.env['employee.data'].search(
                [('email_employee', '=', self.env.user.login), ('current_status_employee', '=', 'Active')])
            name = search_data.mapped('first_name_employee')[0]
           # last_name = search_data.mapped('last_name_employee')[0]
            return name
        except:
            return ''

    def get_department_user(self):
        try:
            search_data = self.env['employee.data'].search(
                [('email_employee', '=', self.env.user.login)])
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
    check_is_reporter_login = fields.Boolean(
        string="is reporter login", compute="get_user_login_reporter", default=True)
    temporary_location_selection = fields.Selection(site_list['name'],
                                                    string="Sites Selection", default="Haus Office Meruya", required=True)

    priority = fields.Selection(
        [('0', 'Not Important'), ('1', 'Low'), ('2', 'Medium'), ('3', 'High')], string='Priority', default='1', required=True)

    state = fields.Selection(
        [('open', 'Open'), ('not_solved', 'Not Solved'), ('solved', 'Solved'), ('overdue', 'Overdue')], default='open', string="State", required=True)
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
        return {
            'name': 'Requested Issue',
            "type": "ir.actions.act_window",
            "help": "No Request Yet !!!",
            "res_model": self._name,
            "view_mode": "tree,form",
            "domain": [('assigned_employee.email_employee', '=', self.env.user.login)],
            "context": {'delete': False, 'create': False},
        }

    def your_requested_issue_list(self):
        return {
            'name': 'Your Requested Issue',
            "type": "ir.actions.act_window",
            "help": "No Request Yet !!!",
            "res_model": self._name,
            "view_mode": "tree,form",
            "domain": [('reporter_email', '=', self.env.user.login)],
            "context": {},
        }

    def sending_auto_overdue(self, dict_var):
        search_data = self.env['crm.issue'].search([('issue_problem', '=', dict_var['issues']), ('reporter_name', '=', dict_var['reporter_name']),
                                                    ('reporter_email', '=', dict_var['reporter_email']), ('reporter_name', '=', dict_var['reporter_name']), (
                                                        'issue_category.name', '=', dict_var['category']), ('issue_due_date', '=', dict_var['due_date']),
                                                    ('temporary_location_selection', '=', dict_var['sites_selection'])])

        if search_data:
            search_data.write({
                'state': 'overdue'
            })
        for involved_user in dict_data['list_involved_user']:
            template_data = {
                'subject': 'Haus Questioner CRM',
                'body_html': '{}, issue {} telah Overdue'.format(involved_user[1], dict_var['issues']),
                'email_from': 'erphaus@gmail.com',
                'auto_delete': True,
                'email_to': involved_user[0],
            }
            mail_id = self.env['mail.mail'].sudo().create(template_data)
            mail_id.sudo().send()
            assigned_user.append([email_data, name_data])

    def sending_reminder_due_date(self, dict_var):
        for involved_user in dict_data['list_involved_user']:
            template_data = {
                'subject': 'Haus Questioner CRM',
                'body_html': '{}, issue {} Akan Overdue besok harap cek issue yang di assign kan ke anda'.format(involved_user[1], dict_var['issues']),
                'email_from': 'erphaus@gmail.com',
                'auto_delete': True,
                'email_to': involved_user[0],
            }
            mail_id = self.env['mail.mail'].sudo().create(template_data)
            mail_id.sudo().send()
            assigned_user.append([email_data, name_data])

        # User Coordinates
    latitude = fields.Float("latitude", digits=(16, 5))
    longitude = fields.Float("longitude", digits=(16, 5))

    is_near_one_km = fields.Float(compute="_compute_isnear")

    @api.depends('latitude', 'longitude')
    def _compute_isnear(self):
        index = 0
        for i in range(len(site_list["name"])):
            if self.temporary_location_selection == site_list["name"][0]:
                index = i
                break
        xlat = radians(float(self.latitude))
        xlon = radians(float(self.longitude))
        ylat = radians(float(site_list["location"][index][0]))
        ylon = radians(float(site_list["location"][index][1]))
        dist = 6371.01 * acos(sin(xlat)*sin(ylat) +
                              cos(xlat)*cos(ylat)*cos(xlon - ylon))


        self.is_near_one_km = dist
        # if dist > 1:
        #     self.is_near_one_km = False
        # else:
        #     self.is_near_one_km = True


class CrmActivityCheckin(models.Model):
    _name = "crm.activity.checkin"
    _description = "CRM Group Of assigned Users"
    _rec_name = "involved_employee"

    def write(self, vals):
        try:
            vals['involved_employee_status']
        except:
            vals['involved_employee_status'] = self.involved_employee_status

        if vals['involved_employee_status'] == 'done':
            search_data = self.env['employee.data'].search(
                [('id', '=', self.involved_employee.id)])
            user_name = search_data.first_name_employee

            send_email_to = self.reporter_issue_email
            template_data = {
                'subject': 'Haus Questioner CRM',
                'body_html': '{} Telah Menyelesaikan Checkin Issue {}'.format(user_name, self.issue_name),
                'email_from': 'erphaus@gmail.com',
                'auto_delete': True,
                'email_to': send_email_to,
            }
            mail_id = self.env['mail.mail'].sudo().create(template_data)
            mail_id.sudo().send()
        rec = super(CrmActivityCheckin, self).create(vals)
        return rec

    def get_current_user(self):
        data = self.env['employee.data'].search(
            [('email_employee', '=', self.env.user.login)], limit=1)
        return data

    id_issue = fields.Many2one('crm.issue')
    reporter_issue_email = fields.Char(related='id_issue.reporter_email')
    issue_name = fields.Char(related="id_issue.issue_problem")
    involved_employee = fields.Many2one(
        "employee.data", string="Employee", default=get_current_user, readonly=True)
    involved_employee_name = fields.Char(
        related='involved_employee.first_name_employee')
    involved_employee_email = fields.Char(
        related='involved_employee.email_employee')
    involved_employee_desc = fields.Text(string="Description")
    involved_employee_attachments = fields.Binary(
        string='Attachments', attachment=True)
    file_involved_employee_attachments = fields.Char("File Name")
    involved_employee_status = fields.Selection([
        ('done', 'Done'),
        ('ongoing', 'Ongoing'),
        ('not_done', 'Not Done'),
    ], string="Status Of Checkin", required=True)
    current_assigned_user_login = fields.Boolean(
        string='is user login?', compute='_is_current_assigned_user_login')

    @api.depends('involved_employee_email')
    def _is_current_assigned_user_login(self):
        if self.involved_employee_email == self.env.user.login:
            self.current_assigned_user_login = True
        else:
            self.current_assigned_user_login = False
