
---

# 🧪 Atividade – Testes e Automações com Pytest

Este repositório contém a implementação e os testes automatizados desenvolvidos como **atividade acadêmica da disciplina de *Testes e Automações***.
O objetivo foi aplicar conceitos de **planejamento e execução de testes automatizados** utilizando o framework **Pytest**, garantindo a verificação de diferentes tipos de erros e comportamentos esperados de uma função em Python.

---

## 🎯 **Objetivo da Atividade**

1. Criar uma função com **no mínimo três argumentos de entrada**.
2. Elaborar o **planejamento dos casos de teste**, definindo valores de entrada e resultados esperados.
3. Implementar **testes automatizados** que cubram:

   * Casos de sucesso
   * Erros de valor (`ValueError`)
   * Erros de tipo (`TypeError`)
4. Subir todos os arquivos juntos em formato `.zip`, incluindo:

   * Código da função
   * Código dos testes automatizados
   * Prints da execução dos testes

---

## ⚙️ **Descrição da Função**

A função `CalcularDesconto()` realiza o cálculo do valor total líquido de um item após aplicar um desconto percentual sobre o preço total.

```python
def CalcularDesconto(precoUnitario: float, quantidade: int, desconto: float, nomeItem: str):
    ...
```

### **Parâmetros**

* `precoUnitario (float)` → preço unitário do produto
* `quantidade (int)` → quantidade comprada
* `desconto (float)` → percentual de desconto (0 a 100)
* `nomeItem (str)` → nome do produto

### **Validações**

A função verifica e lança exceções apropriadas quando:

* O tipo dos parâmetros é inválido (`TypeError`)
* O preço ou quantidade são negativos (`ValueError`)
* O desconto está fora da faixa de 0 a 100 (`ValueError`)

### **Retorno**

Um dicionário com:

```python
{
  "Nome": <nomeItem>,
  "precodesconto": <valor_final_com_desconto>
}
```

---

## 🧩 **Casos de Teste Implementados**

Os testes foram escritos com **Pytest** e cobrem:

### ✅ **Casos de sucesso**

| Entrada                | Saída esperada | Descrição                |
| ---------------------- | -------------- | ------------------------ |
| (10.0, 5, 10, "batom") | 45.0           | Desconto de 10% sobre 50 |
| (50.0, 2, 20, "batom") | 80.0           | Desconto de 20%          |
| (30.0, 3, 50, "batom") | 45.0           | Desconto de 50%          |
| (0, 10, 10, "batom")   | 0.0            | Preço zero               |

### ⚠️ **Casos de erro (ValueError)**

* Preço negativo
* Quantidade negativa
* Desconto negativo
* Desconto maior que 100

### ❌ **Casos de erro (TypeError)**

* Preço, quantidade ou desconto com tipo incorreto
* Nome do item não é string

---

## 🧪 **Execução dos Testes**

Para rodar os testes localmente:

```bash
pip install pytest
pytest nome_do_arquivo.py -v
```

O parâmetro `-v` exibe detalhes de cada teste executado.

### 💻 **Exemplo de saída esperada**

```
==================== test session starts ====================
collected 3 items

test_calcular_desconto.py::test_calculo_preco_total PASSED
test_calcular_desconto.py::test_valores_invalidos PASSED
test_calcular_desconto.py::test_tipos_invalidos PASSED

===================== 3 passed in 0.02s =====================
```

---

## 🎓 **Informações Acadêmicas**

* **Disciplina:** Testes e Automações
* **Curso:** Análise e Desenvolvimento de Sistemas (ADS)
* **Período:** 5º Semestre
* **Instituição:** Faculdade Impacta de Tecnologia
* **Linguagem:** Python
* **Framework de Teste:** Pytest

---

## 🧠 **Resumo**

Esta atividade teve como propósito consolidar o aprendizado em:

* Planejamento e escrita de **casos de teste**
* Uso de **testes automatizados** para validar funções
* Tratamento de exceções e verificação de **erros esperados**
* Prática de **boas práticas de validação e verificação de entrada**

---

**📌 Autor:** Felipe Souza Panichi
**🏫 Faculdade Impacta – 5º Semestre de ADS**

---


