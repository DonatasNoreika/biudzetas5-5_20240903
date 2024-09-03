from models.irasas import Irasas


class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymas, isigyta):
        super().__init__(suma)
        self.atsiskaitymas = atsiskaitymas
        self.isigyta = isigyta

    def __str__(self):
        return f"Išlaidos: {self.suma} (atsiskaitymo būdas - {self.atsiskaitymas}, įsigyta - {self.isigyta})"
