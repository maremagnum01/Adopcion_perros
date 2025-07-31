from Sistema.Perro import Perro

def test_crear_perro():
    perro = Perro("Rocky", "Labrador", 4, "Jugueton", 40, "saludable", "mediano")
    
    assert perro.nombre == "Rocky"
    assert perro.raza == "Labrador"
    assert perro.edad == 4
    assert perro.temperamento == "Jugueton"
    assert perro.peso == 40