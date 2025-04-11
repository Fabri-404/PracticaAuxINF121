from celular import Celular

if __name__ == "__main__":

    celular = Celular()

    print("INSTALANDO APLICACIONES")
    celular.instalar("Binance", 700)
    celular.instalar("TikTok", 220)
    celular.instalar("Kick", 10)
    print("--------------------------")

    print("ESTADO INICIAL")
    celular.porcentaje_bateria()
    print("--------------------------")

    print("USANDO APLICACIONES")
    celular.utilizar("Binance", 20)
    celular.utilizar("TikTok", 17)
    celular.utilizar("Kick", 1)
    print("--------------------------")

    print("ESTADO FINAL")
    celular.porcentaje_bateria()
    print("--------------------------")

    print("AGOTANDO LA BATERIA")
    celular.utilizar("Binance", 1000)
    print("--------------------------")

    print("USO DESPUES DE AGOTAR BATERIA")
    celular.utilizar("Binance", 20)
    celular.porcentaje_bateria()
