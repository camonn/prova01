\# Testes Unitários – Função calcular\_desconto



Projeto de QA para validar a regra de descontos progressivos do e-commerce, usando Python e Pytest.



\## Como executar



&#x20;   python -m pip install pytest

&#x20;   python -m pytest -v



\## Cenários de teste



\- CT01 a CT04 – Faixa sem desconto: R$ 0, R$ 50, R$ 99,99 (R$ 0) e VIP com R$ 50 (R$ 2,50).

\- CT05 a CT09 – Faixa de 10%: R$ 100 (R$ 10), R$ 300 (R$ 30), R$ 499,99 (R$ 50), VIP com R$ 100 (R$ 15), VIP com R$ 300 (R$ 45).

\- CT10 a CT12 – Faixa de 20%: R$ 500 (R$ 100), R$ 700 (R$ 140), VIP com R$ 500 (R$ 125).

\- CT13 a CT16 – Teto de R$ 200: comum com R$ 1000, VIP com R$ 800, comum com R$ 1500, VIP com R$ 2000 (todos R$ 200).

\- CT17 a CT22 – Maiúsculas/minúsculas: "vip", "Vip", "vIp", " VIP " (R$ 45); "comum", "Comum" (R$ 30).

\- CT23 a CT32 – Dados inesperados: valor negativo (ValueError), valor não numérico (TypeError), tipo de cliente vazio ou desconhecido (ValueError), tipo de cliente que não é texto (TypeError).



\## Bugs encontrados



1\. Fronteira de R$ 100 excluída: a condição `valor\_compra > 100` deixava a compra de exatamente R$ 100 sem desconto. Corrigido para `>= 100`.

2\. VIP sensível a maiúsculas/minúsculas: "vip" ou "Vip" não recebiam os 5% extras. Corrigido com `.strip().upper()`.

3\. Falta de validação: valores negativos, tipos de cliente inválidos e entradas que não são texto eram aceitos. Adicionadas validações com ValueError e TypeError.



\## Resultados



\- Código original: 14 falhas, 18 aprovações

\- Código corrigido: 32 aprovações

