import pytest
##Questão:

##1. Escreva uma função qualquer com no mínimo 3 argumentos de entrada.

##2. Construa o planejamento dos casos de testes determinando os valores de entrada e valores de saída esperados.

##3. Escreva os testes automatizados para cada caso de teste definido. Inclua também ValueError e TypeError. Escolher Pytest ou Unittest para implementação.

##4. Subir tudo junto em um arquivo zipado, 

##- Print e código da função;

##- Print e código do teste automatizado;

##- Print da execução.

def CalcularDesconto(precoUnitario:float,quantidade:int,desconto:float,nomeItem:str ):
    if not isinstance(precoUnitario, (int, float)) or not isinstance(desconto, (int, float)):
        raise TypeError("Os valores de preco e desconto devem ser numéricos.")
    if not isinstance(nomeItem, str):
        raise TypeError("A nome do item deve ser uma string.")
    if not isinstance(quantidade,int):
        raise TypeError("A quantidade deve ser um numero inteiro")
    if quantidade  < 0:
        raise ValueError("quantidade deve ser maior que 0")
    if precoUnitario < 0:
        raise ValueError("O preço não pode ser negativo.")
    if not 0 <= desconto <= 100:
        raise ValueError("O desconto deve estar entre 0 e 100.")
    
    precoTotal = precoUnitario*quantidade
    descontoaplicado = precoTotal* (desconto/100)
    totalLiquido = precoTotal-descontoaplicado
    dici = {"Nome": nomeItem,"precodesconto": totalLiquido}
    return dici
    
    
def test_calculo_preco_total():
    assert CalcularDesconto(10.0, 5, 10,"batom")["precodesconto"] == 45.0  # 10 * 5 - 10% de desconto
    assert CalcularDesconto(50.0, 2, 20,"batom")["precodesconto"] == 80.0  # 50 * 2 - 20% de desconto
    assert CalcularDesconto(30.0, 3, 50,"batom")["precodesconto"] == 45.0  # 50% de desconto
    assert CalcularDesconto(0, 10, 10,"batom")["precodesconto"] == 0.0  # Preço zero

def test_valores_invalidos():
    with pytest.raises(ValueError):
        CalcularDesconto(-10, 5, 10, "batom")  # Preço negativo
    with pytest.raises(ValueError):
        CalcularDesconto(10, -5, 10, "batom")  # Quantidade negativa
    with pytest.raises(ValueError):
        CalcularDesconto(10, 5, -10, "batom")  # Desconto negativo
    with pytest.raises(ValueError):
        CalcularDesconto(10, 5, 110, "batom")  # Desconto maior que 100

def test_tipos_invalidos():
    with pytest.raises(TypeError):
        CalcularDesconto("dez", 5, 10, "batom")  # Preço não numérico
    with pytest.raises(TypeError):
        CalcularDesconto(10, 5, "dez", "batom")  # Desconto não numérico
    with pytest.raises(TypeError):
        CalcularDesconto(10, "cinco", 10, "batom")  # Quantidade não numérica
    with pytest.raises(TypeError):
        CalcularDesconto(10, 5, 10, 123)  # Nome do item não é string

