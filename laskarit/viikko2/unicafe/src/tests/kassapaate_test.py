import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self) -> None:
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaate_on_alustettu_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # testaa vaihtorahat
    def test_syo_edullisesti_palauttaa_vaihtorahat_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(vaihtoraha, 500 - 240)
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(vaihtoraha, 0)

    def test_syo_maukkaasti_palauttaa_vaihtorahat_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(800)
        self.assertEqual(vaihtoraha, 400)
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(vaihtoraha, 0)
    

    # Testaa osto kirjaukset käteisellä
    def test_edullinen_ostos_kateisella_kirjataan(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_ostos_kateisella_kirjataan(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    # Testaa ostokirjaukset kortilla
    def test_edullinen_ostos_kortilla_kirjataan(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_ostos_kortilla_kirjataan(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    
    # Testaa rahan lataaminen kortille
    def testaa_lataa_rahaa_kortille_kasvattaa_saldoja(self):
        summa = 500
        vanha_saldo_kortti = self.maksukortti.saldo
        vanha_saldo_kassapaate = self.kassapaate.kassassa_rahaa
        
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, summa)
        self.assertEqual(self.maksukortti.saldo, vanha_saldo_kortti + summa)
        self.assertEqual(self.kassapaate.kassassa_rahaa, vanha_saldo_kassapaate + summa)


    # Testaa että ostot käteisellä ei suoriteta jos ei ole saldoa
    def test_syo_edullisesti_kateisella_ei_suorita_ostoa(self):
        maksu = 200
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(maksu)
        
        self.assertEqual(vaihtoraha, maksu)

    def test_syo_maukkaasti_kateisella_ei_suorita_ostoa(self):
        maksu = 300
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(maksu)
        
        self.assertEqual(vaihtoraha, maksu)

        # Testaa että ostot kortilla ei suoriteta jos ei ole saldoa
    def test_syo_edullisesti_kortilla_ei_suorita_ostoa(self):
        kortti = Maksukortti(200)
        vastaus = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(vastaus, False)

    def test_syo_maukkaasti_kortilla_ei_suorita_ostoa(self):
        kortti = Maksukortti(200)
        vastaus = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(vastaus, False)


    # testaa että kortille lataaminen ei onnistu jos summa on negatiivinen
    def test_lataa_rahaa_kortille_ei_suorita_jos_negatiivinen_summa(self):
        vanha_saldo_kortti = self.maksukortti.saldo
        vanha_saldo_kassapaate = self.kassapaate.kassassa_rahaa

        vastaus = self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(vastaus, None)
        self.assertEqual(self.kassapaate.kassassa_rahaa, vanha_saldo_kassapaate)
        self.assertEqual(self.maksukortti.saldo, vanha_saldo_kortti)