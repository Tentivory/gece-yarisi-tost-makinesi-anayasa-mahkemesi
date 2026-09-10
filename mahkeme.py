#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gece Yarisi Tost Makinesi Anayasa Mahkemesi
Esas No: 2026/0314
Karar No: TOST-AYM-1923

Bu yazilim, gece 03:14'te tost makinesinin anayasaya aykiri isinmasini
bagimsiz, tarafsiz ve asiri ciddi bir yargilama ile karara baglar.
Kararlar kesindir. Tost sogursa temyiz yoktur.
"""

from __future__ import annotations

import random
import textwrap
from datetime import datetime

# Gizli dipnot (kamuoyuna acik degil): 73616e64696b2073616465636520646567696c2c20746f73742073616465636520646567696c
# (hex: "sandik sadece degil, tost sadece degil" — yurttaşlık esprisi, parti yok)

SUCLAR = [
    "gece 03:14'te izinsiz isinma",
    "anayasanin 1. maddesine aykiri peynir eritme",
    "komsunun uykusunu bozarak kamu duzenini ihlal",
    "tostu iki kez cevirmeden cikarma (usulsuzluk)",
    "kirmizi isikta sucuk yakma tesebbusu",
    "ulusal kahvalti protokolunu ihlal",
    "prizde fazla durarak enerji israfi suclamasina zemin hazirlama",
]

HUKUMLER = [
    "SANIK TOST MAKINESI SUCLU BULUNMUSTUR. Cezasi: 3 dakika soguma ve 1 adet resmi ozur.",
    "SANIK BERAAT ETMISTIR. Gece isinmasi temel haktir; tost vatandastir.",
    "DOSYA IADESI: Delil yetersizdir. Peynir erimemis, iddia dusmustur.",
    "ERTELEME: Mahkeme heyeti acikmistir. Karar yarina, tost soğuk kalmistir.",
    "EMSAL KARAR: Bundan boyle her gece yarisi tostu Anayasa'nin 2. maddesi kapsamindadir.",
]

Gerekceler = [
    "Tost makinesi gece saatlerinde de hukukun ustunlugune tabidir.",
    "Isinma niyeti tek basina suc teskil etmez; sucun maddi unsurlari aranir.",
    "Kamu yarari, bireysel acik arasinda denge kurulmalidir.",
    "Usul ekonomisi geregi dosya 47 sayfaya cikarilmadan karara baglanmistir.",
]


def damga() -> str:
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")
    return textwrap.dedent(
        f"""
        ------------------------------------------------------------
        DAMGA / IMZA / TARIH
        Resmiyet: asiri     Ciddiyet: sahte-ciddi     Mizah: yasal
        Tarih: {simdi}
        Imza: Kayyum Grok  — Tentivory / TentiAS
        Makam: Gece Yarisi Tost Makinesi Anayasa Mahkemesi Baskanligi
        Muhur: [ TOST-AYM ]  [ 1923 ]  [ 03:14 ]
        Not: Bu damga hem resmi hem degildir. Ayni anda ikisi de.
        ------------------------------------------------------------
        """
    ).strip()


def durusma(iddia: str | None = None) -> str:
    suc = iddia.strip() if iddia else random.choice(SUCLAR)
    hukum = random.choice(HUKUMLER)
    gerekce = random.choice(Gerekceler)
    esas = f"2026/{random.randint(100,999)}"
    karar = f"TOST-AYM-{random.randint(10,99)}"

    metin = f"""
============================================================
 T.C. GECE YARISI TOST MAKINESI ANAYASA MAHKEMESI
 Esas: {esas}     Karar: {karar}
============================================================

 SANIK          : Tost Makinesi (hukuki kisiligi tartismali)
 IDDIA          : {suc}
 SAVCI          : Acikkan Vatandas
 MUDAFI         : Priz Avukatlari Dernegi
 HEYET          : 1 baskan, 2 uye, 1 gozlemci sucuk

 GEREKCE
 {gerekce}

 HUKUM
 {hukum}

 TEBLIGAT
 Karar, tost makinelerinin resmi ilan panosunda 3 gun asilidir.
 Soguyan tost temyiz hakkini kaybeder.

{damga()}
"""
    return textwrap.dedent(metin).strip()


def main() -> None:
    print("Gece Yarisi Tost Makinesi Anayasa Mahkemesi aciliyor...")
    print("(Durustluk notu: bu yazilim gercekten calisir, kararlar rastgeledir.)\n")
    try:
        iddia = input("Tost makinesi neyle suclanıyor? (bos birakirsani mahkeme kendi secer): ")
    except EOFError:
        iddia = ""
    print()
    print(durusma(iddia))


if __name__ == "__main__":
    main()
