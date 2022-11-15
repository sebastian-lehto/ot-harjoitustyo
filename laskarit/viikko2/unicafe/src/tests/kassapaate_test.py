import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(100000)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_rahamaara_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myytyja_alussa_oikein(self):
        maara = self.kassapaate.maukkaat + self.kassapaate.edulliset
        self.assertEqual(maara, 0)

    def test_maukkaiden_vaihtoraha_oikea(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)

    def test_edullisten_vaihtoraha_oikea(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)
    
    def test_maukkaiden_vaihtoraha_oikea_kun_raha_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

    def test_edullisten_vaihtoraha_oikea_kun_raha_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_kassassa_oleva_rahamaara_kasvaa_oikein_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kassassa_oleva_rahamaara_kasvaa_oikein_edulliset(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kassassa_oleva_rahamaara_kasvaa_oikein_maukkaat_kun_raha_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassassa_oleva_rahamaara_kasvaa_oikein_edulliset_kun_raha_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myytyjen_maukkauden_maara_kasvaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_myytyjen_edulliste_maara_kasvaa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(400)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_myytyjen_maukkauden_maara_kasvaa_oikein_kun_raha_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_myytyjen_edulliste_maara_kasvaa_oikein_kun_raha_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.edulliset, 0)




    def test_maukkaiden_osto_toimii_kortti(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_edullisten_osto_toimii_kortti(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_maukkaiden_osto_toimii_kortti_kun_saldo_ei_riitä(self):
        kortti = Maksukortti(10)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)

    def test_edullisten_osto_toimii_kortti_kun_saldo_ei_riitä(self):
        kortti = Maksukortti(10)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)

    def test_maukkaiden_maara_kasvaa_kortti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullisten_maara_kasvaa_kortti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaiden_maara_ei_kasva_kortti(self):
        kortti = Maksukortti(10)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisten_maara_ei_kasva_kortti(self):
        kortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaiden_ostossa_saldo_vahenee_kortti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 99600)

    def test_edullisten_ostossa_saldo_vahenee_kortti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 99760)

    def test_maukkaiden_ostossa_saldo_ei_vahene_kortti(self):
        kortti = Maksukortti(10)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 10)

    def test_edullisten_ostossa_saldo_ei_vahene_kortti(self):
        kortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 10)

    def test_kassan_rahamaara_ei_muutu_kortti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_ladattaessa_arvot_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100000)
        kortilla = self.maksukortti.saldo
        kassassa = self.kassapaate.kassassa_rahaa
        s = str(kortilla) + "-" + str(kassassa)
        self.assertEqual(s, "200000-200000")

    def test_kortille_ladattaessa_arvot_oikein_kun_summa_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100000)
        kortilla = self.maksukortti.saldo
        kassassa = self.kassapaate.kassassa_rahaa
        s = str(kortilla) + "-" + str(kassassa)
        self.assertEqual(s, "100000-100000")


