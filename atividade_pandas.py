import pandas as pd

df_bike = pd.read_csv('bike-sharing.csv')

imprimir = df_bike.to_string()

# 1
celulas = df_bike.size
linhas = len(df_bike)

print('shape =', df_bike.shape)
# print('celulas =', df_bike.size)
# print('linhas =', linhas)

# 2
# print(df_bike.describe())
print("Média da coluna windspeed =", df_bike.windspeed.mean())

# 3
print("Média da coluna temp =", df_bike.temp.mean())

# 4
print('Registros de locações existem para o ano de 2021 =', df_bike[df_bike.year == 0].shape)

# 5
print('Registros de locações existem para o ano de 2022 =', df_bike[df_bike.year == 1].shape)

# 6
print("locações de bicicletas foram efetuadas em 2021 =", df_bike[df_bike.year == 0].total_count.sum())

# 7
print("locações de bicicletas foram efetuadas em 2022 =", df_bike[df_bike.year == 1].total_count.sum())

# 8
# 1: inverno, 2: primavera, 3: verão, 4: outono
print(df_bike.groupby('season').total_count.mean())
print("Estação do ano contém a maior média de locações de bicicletas = 3. verão")

# 9
print("Estação do ano contém a menor média de locações de bicicletas = 1. Inverno")

# 10
print("Horário do dia contém a maior média de locações de bicicletas",
      df_bike.groupby('hour').total_count.mean().sort_values(ascending=False))

# 11
print("Horário do dia contém a menor média de locações de bicicletas",
      df_bike.groupby('hour').total_count.mean().sort_values(ascending=True))

# 12
print("Dia da semana contém a maior média de locações de bicicletas",
      df_bike.groupby('weekday').total_count.mean().sort_values(ascending=False))

# 13
print("Dia da semana contém a menor média de locações de bicicletas",
      df_bike.groupby('weekday').total_count.mean().sort_values(ascending=True))

# 14
print("Às quartas-feiras (weekday = 3), horário do dia contém a maior média de locaçõesde bicicletas",
      df_bike[df_bike.weekday == 3].groupby('hour').total_count.mean().sort_values(ascending=False))

# 15
print("Aos sábados (weekday = 6), horário do dia contém a maior média de locaçõesde bicicletas",
      df_bike[df_bike.weekday == 6].groupby('hour').total_count.mean().sort_values(ascending=False))
