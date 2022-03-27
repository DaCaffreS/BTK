def cevre(kisa,uzun):
    return kisa+uzun
def alan(kisa,uzun):
    return (kisa*uzun)
kisa_kenar=int(input("Kısa Kenar:"))
uzun_kenar=int(input("Uzun Kenar:"))
print("Dikdörtgenin çevresi:",cevre(kisa_kenar,uzun_kenar))
print("Dikdörtgenin alanı:",alan(kisa_kenar,uzun_kenar))