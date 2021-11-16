import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_tasmaako_saldo(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")

    def test_tasmaako_edulliset_alussa(self):
        self.assertEqual(str(self.kassapaate.edulliset), "0")
    
    def test_tasmaako_maukkaat_alussa(self):
        self.assertEqual(str(self.kassapaate.maukkaat), "0")
    
    def test_toimiiko_maksu_maukkaasti(self):
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(600)), "200")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100400")
    
    def test_toimiiko_maksu_edullisesti(self):
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(600)), "360")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100240")
    
    def test_toimiiko_edullisesti_lasku(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(str(self.kassapaate.edulliset), "2")

    def test_toimiiko_maukkaasti_lasku(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(str(self.kassapaate.maukkaat), "2")
    
    def test_raha_ei_riita_maukkaasti(self):
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(300)), "300")

    def test_raha_ei_riita_edullisesti(self):
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(200)), "200")

    def test_raha_ei_riita_kassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")

    def test_raha_ei_riita_lounaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(str(self.kassapaate.maukkaat), "0")
    
    def test_kortilla_tarpeeksi_rahaa_edullisesti(self):
        self.maksukortti = Maksukortti(1000)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

    def test_kortilla_tarpeeksi_rahaa_maukkaasti(self):
        self.maksukortti = Maksukortti(1000)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))

    def test_kortilla_edullisten_lasku(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.edulliset), "2")

    def test_kortilla_maukkaiden_lasku(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.maukkaat), "2")
    
    def test_kortin_saldo_ei_riita_maukkaat(self):
        self.maksukortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
    
    def test_kortin_saldo_ei_riita_edulliset(self):
        self.maksukortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
    
    def test_kortin_saldo_ei_riita_laskuri(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.edulliset), "0")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")
    
    def test_kassan_saldo_ei_muutu_kortilla_maksettaessa(self):
        self.maksukortti = Maksukortti (1000)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
    
    def test_kortin_lataus_kassan_saldo(self):
        self.maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100500")
    
    def test_kortin_lataus_kortin_saldo(self):
        self.maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")
    
    def test_kortin_lataus_kortin_saldo_negatiivinen(self):
        self.maksukortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")