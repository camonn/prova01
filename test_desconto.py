import pytest
from desconto import calcular_desconto


@pytest.mark.parametrize("valor, tipo, esperado", [
    (0, "COMUM", 0.00),        
    (50, "COMUM", 0.00),       
    (99.99, "COMUM", 0.00),    
    (50, "VIP", 2.50),         
])
def test_faixa_sem_desconto(valor, tipo, esperado):
    assert calcular_desconto(valor, tipo) == pytest.approx(esperado)


@pytest.mark.parametrize("valor, tipo, esperado", [
    (100, "COMUM", 10.00),     
    (300, "COMUM", 30.00),     
    (499.99, "COMUM", 50.00),  
    (100, "VIP", 15.00),       
    (300, "VIP", 45.00),       
])
def test_faixa_dez_por_cento(valor, tipo, esperado):
    assert calcular_desconto(valor, tipo) == pytest.approx(esperado)


@pytest.mark.parametrize("valor, tipo, esperado", [
    (500, "COMUM", 100.00),    
    (700, "COMUM", 140.00),    
    (500, "VIP", 125.00),      
])
def test_faixa_vinte_por_cento(valor, tipo, esperado):
    assert calcular_desconto(valor, tipo) == pytest.approx(esperado)


@pytest.mark.parametrize("valor, tipo, esperado", [
    (1000, "COMUM", 200.00),   
    (800, "VIP", 200.00),      
    (1500, "COMUM", 200.00),   
    (2000, "VIP", 200.00),     
])
def test_regra_do_teto(valor, tipo, esperado):
    assert calcular_desconto(valor, tipo) == pytest.approx(esperado)


@pytest.mark.parametrize("tipo", ["vip", "Vip", "vIp", " VIP "])  
def test_vip_sem_diferenciar_maiusculas(tipo):
    assert calcular_desconto(300, tipo) == pytest.approx(45.00)


@pytest.mark.parametrize("tipo", ["comum", "Comum"])  
def test_comum_sem_diferenciar_maiusculas(tipo):
    assert calcular_desconto(300, tipo) == pytest.approx(30.00)


@pytest.mark.parametrize("valor", [-1, -100.50])  
def test_valor_negativo_gera_erro(valor):
    with pytest.raises(ValueError):
        calcular_desconto(valor, "COMUM")


@pytest.mark.parametrize("valor", ["300", None, True])  
def test_valor_nao_numerico_gera_erro(valor):
    with pytest.raises(TypeError):
        calcular_desconto(valor, "COMUM")


@pytest.mark.parametrize("tipo", ["", "GOLD", "   "])  
def test_tipo_cliente_desconhecido_gera_erro(tipo):
    with pytest.raises(ValueError):
        calcular_desconto(300, tipo)


@pytest.mark.parametrize("tipo", [None, 123])  
def test_tipo_cliente_nao_texto_gera_erro(tipo):
    with pytest.raises(TypeError):
        calcular_desconto(300, tipo)