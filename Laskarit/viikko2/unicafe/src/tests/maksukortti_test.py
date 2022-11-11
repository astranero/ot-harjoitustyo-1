import unittest
from maksukortti import Maksukortti

# Kortin saldo alussa oikein
# Rahan lataaminen kasvattaa saldoa oikein
# Rahan ottaminen toimii:
    # Saldo vähenee oikein, jos rahaa on tarpeeksi
    # Saldo ei muutu, jos rahaa ei ole tarpeeksi
    # Metodi palauttaa True, jos rahat riittivät ja muuten False

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    # saldo on oikein
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    # lataaminen kasvattaa saldoa oikein
    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    # saldo vähenee oikein jos rahaa on
    def test_saldo_vahenee_oikein_jos_on_rahaa(self):
        self.maksukortti.ota_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.00 euroa")

    # saldo ei vahene jos ei ole rahaa
    def test_saldo_ei_vahenee_jos_ei_rahaa(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    # Palauttaa True jos oli rahaa ja muussa tapauksessa False
    def test_palauttaa_oikean_arvon_kun_saldo_vahenee(self):
        vastaus = self.maksukortti.ota_rahaa(1000)
        self.assertEqual(vastaus, True)
        vastaus2 = self.maksukortti.ota_rahaa(1000)
        self.assertEqual(vastaus2, False)
