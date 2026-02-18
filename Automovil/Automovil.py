from dataclasses import dataclass
@dataclass(frozen=True)
class Automovil:
    motor: str
    color: str
    llantas: str
    sonido: str
    interiores: str
    techo_solar: bool
    gps: bool


class ConstruirAutomovil:
    def __init__(self):
        self.motor       = "Diesel"
        self.color       = "Morado"
        self.llantas     = "15 pulgadas"
        self.sonido      = ""
        self.interiores  = "Tela"
        self.techo_solar = False
        self.gps         = False

    def motor_fijo(self, motor):
        self.motor = motor
        return self
    def color_fijo(self, color):
        self.color = color
        return self
    def llantas_fijas(self, llantas):
        self.llantas = llantas
        return self
    def sonido_fijo(self, sonido):
        self.sonido = sonido
        return self
    def interiores_fijo(self, interiores):
        self.interiores = interiores
        return self
    def techo_solar_fijo(self, techo_solar):
        self.techo_solar = techo_solar
        return self
    def gps_fijo(self, gps):
        self.gps = gps
        return self
    def build(self):
        return Automovil(
            self.motor,
            self.color,
            self.llantas,
            self.sonido,
            self.interiores,
            self.techo_solar,
            self.gps
        )

if __name__ == "__main__":
    auto = (ConstruirAutomovil()
            .motor_fijo("Eléctrico")
            .color_fijo("Rojo")
            .llantas_fijas("18 pulgadas")
            .sonido_fijo("Premium")
            .techo_solar_fijo(True)
            .gps_fijo(True)
            .build())
print(auto)