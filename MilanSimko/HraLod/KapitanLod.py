import random
import time

class ShipSimulator:
    def __init__(self):
        # Počáteční stav lodi
        self.ship_name = "SS Explorer"
        self.speed = 10        # rychlost v uzlech
        self.heading = 0       # směr (stupně, 0 = sever)
        self.fuel = 100        # procent zbytkového paliva
        self.distance = 0      # celková ujetá vzdálenost (na simulovaném časovém intervalu)
        self.is_running = True
        # Postava Milan Šimko jako kapitán
        self.captain = "Ing. Milan Šimko, PhD"

    def display_status(self):
        print("\n--- Stav lodi ---")
        print(f"Lod: {self.ship_name}")
        print(f"Rychlost: {self.speed} uzlů")
        print(f"Směr: {self.heading}°")
        print(f"Palivo: {self.fuel}%")
        print(f"Ujetá vzdálenost: {self.distance} km")
        print("------------------\n")

    def captain_comment(self):
        # Několik komentářů od Milana Šimka dle aktuální situace
        if self.fuel < 20:
            comment = "Palivo klesá! Musíme najít přístav nebo omezit rychlost!"
        elif self.speed > 20:
            comment = "Držme kurz, ale pozor – příliš vysoká rychlost může zkomplikovat manévry."
        else:
            comments = [
                "Plujeme hladce, tým. Udržujte pozornost!",
                "Dobrá práce, lodní posádko! Vše běží dle plánu.",
                "Nádherná plavba, ale nezapomínejte na kontrolu paliva."
            ]
            comment = random.choice(comments)
        print(f"{self.captain} říká: \"{comment}\"\n")

    def random_event(self):
        # Náhodná událost, která může ovlivnit stav lodi
        event_chance = random.randint(1, 100)
        if event_chance < 15:
            # Například bouře
            print("!!! Bouřlivá bouře zasáhla loď! Rychlost se snižuje a palivo se rychle spotřebovává.")
            self.speed = max(5, self.speed - 5)
            self.fuel = max(0, self.fuel - 10)
        elif 15 <= event_chance < 25:
            # Setkání s překážkou (např. nečekaný vítr)
            print("!!! Nečekaný vítr změnil kurz. Proveďte korekci směru!")
            # Událost neovlivní palivo ani rychlost, ale vyžaduje reakci.
        # Jinak se nic speciálního nestane

    def process_command(self, command):
        # Zpracování příkazů uživatele
        if command.lower() in ["konec", "exit", "quit"]:
            self.is_running = False
            print("Simulace ukončena.")
        elif command.lower() in ["zrychli", "zrychlete"]:
            self.speed += 5
            self.fuel = max(0, self.fuel - 3)
            print("Zvyšujeme rychlost...")
        elif command.lower() in ["zpomal", "zpomalení"]:
            self.speed = max(0, self.speed - 5)
            print("Snižujeme rychlost...")
        elif command.lower() in ["zatáčej doleva", "zatáčej levým směrem"]:
            self.heading = (self.heading - 15) % 360
            print("Provádíme zatáčku doleva...")
        elif command.lower() in ["zatáčej doprava", "zatáčej pravým směrem"]:
            self.heading = (self.heading + 15) % 360
            print("Provádíme zatáčku doprava...")
        else:
            print("Neznámý příkaz. Zkuste: zrychli, zpomal, zatáčej doleva, zatáčej doprava, konec.")

    def run_simulation(self):
        print("Spouštím lodní simulátor...")
        print(f"Kapitán: {self.captain}\n")
        time.sleep(1)
        
        while self.is_running and self.fuel > 0:
            self.display_status()
            self.captain_comment()
            
            # Simulace ujeté vzdálenosti a spotřeby paliva
            self.distance += self.speed * 0.1  # zjednodušený výpočet vzdálenosti
            self.fuel = max(0, self.fuel - self.speed * 0.05)
            
            # Spuštění náhodné události
            self.random_event()
            
            command = input("Zadejte příkaz (zrychli, zpomal, zatáčej doleva, zatáčej doprava, konec): ")
            self.process_command(command)
            time.sleep(1)
        
        if self.fuel <= 0:
            print("Kriticky nízké palivo. Simulace ukončena - loď se nedokáže dál pohybovat.")
        print("Děkujeme za využití lodního simulátoru s Milanem Šimkem!")

if __name__ == "__main__":
    simulator = ShipSimulator()
    simulator.run_simulation()