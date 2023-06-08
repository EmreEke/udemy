class Insan:
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk):
        self._tc_no = tc_no
        self._ad = ad
        self._soyad = soyad
        self._yas = yas
        self._cinsiyet = cinsiyet
        self._uyruk = uyruk

    def get_tcno(self):
        return self._tc_no

    def set_tc_no(self, value):
        self._tc_no = value
        print("Tc No değiştirildi.")

    def get_ad(self):
        return self._ad

    def set_ad(self, value):
        self._ad = value
        print("Ad değiştirildi.")

    def get_soyad(self):
        return self._soyad

    def set_soyad(self, value):
        self._soyad = value
        print("Soyad değiştirildi.")

    def get_yas(self):
        return self._yas

    def set_yas(self, value):
        self._yas = value
        print("Yaş değiştirildi.")

    def get_cinsiyet(self):
        return self._cinsiyet

    def set_cinsiyet(self, value):
        self._cinsiyet = value
        print("Cinsiyet değiştirildi.")

    def get_uyruk(self):
        return self._uyruk

    def set_uyruk(self, value):
        self._uyruk = value
        print("Uyruk değiştirildi.")

    def __str__(self):
        return f"Tc No: {self._tc_no} Adı: {self._ad} Soyadı: {self._soyad} Yaşı: {self._soyad} Cinsiyeti: {self._cinsiyet} Uyruğu: {self._uyruk}"


i1 = Insan(123456, "Emre", "Eke", 19, "Erkek", "Türk")
print(i1)
i1.set_ad("Naz")
i1.set_soyad("Kaya")
i1.set_tc_no(12345)
i1.set_cinsiyet("Kadın")
i1.set_yas(20)
i1.set_uyruk("Melek")
print(i1)
