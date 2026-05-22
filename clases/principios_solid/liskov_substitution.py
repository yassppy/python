## Si pones el método fly() en la clase Bird supones que todas las aves vuelan pero no es así.
## Ya que el pinguino rompe con esa condición, por eso realizas otra subclase para voladores, nadadores de esa forma.
## Las subclases se comportan de acuerda a la jerarquia sin contradiciones como en pinguino y otras aves heredan lo necesario.

class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        print("Volando...")

class SwimmingBird(Bird):
    def swim(self):
        print("Nadando...")

class Duck(FlyingBird, SwimmingBird):
    pass

class Penguin(Bird):
    pass