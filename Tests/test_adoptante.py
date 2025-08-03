from Sistema.Adoptante import Adoptante

def test_crear_adoptante():
    adoptante = Adoptante("Michael", 40202020, "Michael@test.com", "raza")
    
    assert adoptante.nombre == "Michael"
    assert adoptante.dni == 40202020
    assert adoptante.email == "Michael@test.com"
    assert adoptante.preferencia == "raza"