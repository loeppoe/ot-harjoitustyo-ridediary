import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_lataus_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")
        
    def test_ota_rahaa_toimii_oikein(self):
        self.assertTrue(self.maksukortti.ota_rahaa(5))
           
    def test_saldo_muuttuu_oikein(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")

    def test_ota_rahaa_saldo_ei_muutu(self):    
        self.assertFalse(self.maksukortti.ota_rahaa(5000))