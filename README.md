# atividade_1


# atividade_2

## Criando uma rede neural de aprendizado profundo

Exercício do livro de Russel&Norvig

Passo 1:
Vamos usar o conjunto de dados MNIST. O conjunto de dados MNIST consiste em 60.000 amostras de treinamento e 10.000 amostras de teste de imagens de dígitos manuscritas. As imagens têm tamanho 28 × 28 pixels e a saída pode ficar entre 0–9 .



# atividade_pandas

##Projeto: Aluguel de bicicleta IAC 
Passo a passo sobre o trabalho prático 2.

Este trabalho consiste na análise de um “dataset” que traz informações sobre aluguéis de bicicletas por
hora.

O dataset pode ser encontrado no arquivo anexado no AVA, onde temos as seguintes variáveis:
‒ rec_id: índice do registro de locação;
‒ datetime: data;
‒ season: estação do ano (1: inverno, 2: primavera, 3: verão, 4: outono). Relativo ao hemisfério norte;
‒ year: ano (0: 2021, 1:2022);
‒ month: mês (1 a 12);
‒ hour: hora do dia (0 a 23);
‒ is_holiday: booleano indicando feriado;
‒ weekday: dia da semana (0: domingo, 1: segunda-feira, …, 6: sábado);
‒ is_workingday: booleano indicando dia útil;
‒ weather_condition: (1: limpo, 2: nublado, 3: chuva leve, 4: chuva forte);
‒ temp: temperatura escalada entre 0 e 1. Valor original em graus Celsius: -8 a 39;
‒ atemp: sensação térmica escalada entre 0 e 1. Valor original em graus Celsius: -16 a 50;
‒ humidity: humidade relativa (0 a 1);
‒ windspeed: velocidade do vento escalada entre 0 e 1 (máximo original: 67);
‒ casual: número de locações para usuários casuais;
‒ registered: número de locações para usuários registrados;
‒ total_count: contador total de aluguéis (casual+registered).

Utilizando os dados disponibilizados, faça um programa, capaz de implementar e calcular os conceitos de
Naive Bayes, usando a linguagem de programação que você achar mais adequada (C, Python outra
qualquer).

Obs.: Se você optar em usar o Python, deveremos usar apenas os modulos pandas e numpy e então deve-se
iniciar importando-os e em seguida carregando o dataset em um “pandas” dataframe (neste caso
chamamos ele de df_bike).

Lembre-se que este trabalho consiste em manipular os dados para responder questões acerca deles e é isto
que vamos fazer agora!

Questão 1 — Qual o tamanho desse dataset (número de linhas, número de colunas)?

Questão 2 — Qual a média da coluna windspeed?

Questão 3 — Qual a média da coluna temp?

Questão 4 — Quantos registros de locações existem para o ano de 2021 (número de linhas, número de
colunas)?

Questão 5 — Quantos registros de locações existem para o ano de 2022 (número de linhas, número de
colunas)?

Questão 6 — Quantas locações de bicicletas foram efetuadas em 2021?

Questão 7 — Quantas locações de bicicletas foram efetuadas em 2022?

Questão 8 — Qual estação do ano contém a maior média de locações de bicicletas?

Questão 9 — Qual estação do ano contém a menor média de locações de bicicletas?

Questão 11 — Qual horário do dia contém a menor média de locações de bicicletas?

Questão 12 — Que dia da semana contém a maior média de locações de bicicletas?

Questão 13 — Que dia da semana contém a menor média de locações de bicicletas?

Questão 14 — Às quartas-feiras (weekday = 3), qual o horário do dia contém a maior média de locações de
bicicletas?

Questão 15 — Aos sábados (weekday = 6), qual o horário do dia contém a maior média de locações de
bicicletas
