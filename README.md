# Desafio 1 senior vs 3 júniors

(README baseado em [YuriKanegae/desafio-1-1s-vs-3j](https://github.com/YuriKanegae/desafio-1-1s-vs-3j/blob/main/README.md))

Minha tentativa de implementar o desafio da codecon: [1 sênior vs. 3 júniors](https://www.youtube.com/watch?v=AFtRYXJVO-4). Não medi o tempo gasto para implementar. Os endpoints implementados seguem na tabela abaixo.


| ENDPOINT                      | **Implementado?** |
|-------------------------------|:----------:|
| **POST /users**               |      ✅     |
| **GET /superusers**           |      ✅     |
| **GET /top-countries**        |      ✅     |
| **GET /team-insights**        |      ✅     |
| **GET /active-users-per-day** |      ❌     |
| **GET /evaluation**           |      ❌     |

O código foi implementado, testado e executado com Python versão 3.13.3, com
ambiente virtual criado usando Micromamba versão 1.5.8.

O arquivo `data_exploration.ipynb` usa pandas versão 2.2.2 e numpy versão 1.26.4.
O notebook foi criado e executado usando outro ambiente virtual (Python versão
3.12.3), este criado com a mesma versão do Micromamba citado anteriormente.
O propósito desse notebook foi fazer uma aferição mais rápida dos valores esperados
de retorno, analisando diretamente os jsons como DataFrames. Eu criei e rodei este
notebook no VSCode, mas as versões de kernel do Jupyter seguem abaixo:

```
IPython          : 8.22.2
ipykernel        : 6.29.3
jupyter_client   : 8.6.1
jupyter_core     : 5.7.2
jupyter_server   : 2.14.0
jupyterlab       : 4.1.6
```

Repositório original com os dados de teste: https://github.com/codecon-dev/desafio-1-1s-vs-3j

Para tirar dúvidas/dar sugestões, podem me contactar via inaciogmedeiros@gmail.com.