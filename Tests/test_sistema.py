from Sistema.SistemaAdopcion import SistemaAdopcion
from Sistema.Adoptante import Adoptante
from Sistema.Perro import Perro

def test_adoptar():
    sistema = SistemaAdopcion()
    tobi = Perro('Tobi', 'Labrador', 3, 'Jugueton', 50, 'saludable', 'grande')
    roberto = Adoptante('roberto', 30303030, 'roberto@gmail.com')
    registro = sistema.registrarse(roberto)
    cargadoPerro = sistema.cargarPerro(tobi)
    
    assert registro is True
    assert cargadoPerro is True
    assert tobi in sistema.perros