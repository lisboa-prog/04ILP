# Desafio Python Ferramenta de Análise de Clima

## Background

A agrometeorologia é crítica para garantir o rendimento da maioria das culturas no campo. Entretanto, os agricultores e proprietários de terras que confiam nos dados de agrometeorologia disponíveis publicamente descobrem frequentemente que as previsões feitas por essas fontes não correspondem ao que eles vêem em seus campos. Esta disparidade pode resultar em grandes perdas, especialmente quando as condições climáticas severas atingem inesperadamente. Portanto, os agricultores só devem usar previsão de agrometeorologia que tenham sido cuidadosamente compiladas, especificamente para seus campos, usando dados de estações de meteo, sensores e satélites.

## Ferramenta de Análise de Clima

Neste exemplo, você criará um script Python para visualizar o clima de mais de 500 cidades em todo o mundo, a distâncias variadas do equador. Para fazer isso, você utilizará uma [biblioteca Python simples](https://pypi.python.org/pypi/citipy), a [API OpenWeatherMap](https://openweathermap.org/api) e criar um modelo representativo do clima nas cidades do mundo.

Seu primeiro requisito é criar uma série de gráficos de dispersão para mostrar os seguintes relacionamentos:

* Temperatura (F) vs. Latitude
* Umidade (%) vs. Latitude
* Nebulosidade (%) vs. Latitude
* Velocidade do Vento (mph) vs. Latitude

Após cada plotagem adicione uma frase ou também explicando o que é o código e analisando.

Seu segundo requisito é executar a regressão linear em cada relacionamento, só que desta vez separando-os em Hemisfério Norte (maior ou igual a 0 graus de latitude) e Hemisfério Sul (menos de 0 graus de latitude):

* Hemisfério Norte - Temperatura (F) vs. Latitude
* Hemisfério Sul - Temperatura (F) vs. Latitude
* Hemisfério Norte - Umidade (%) vs. Latitude
* Hemisfério Sul - Umidade (%) vs. Latitude
* Hemisfério Norte - Nebulosidade (%) vs. Latitude
* Hemisfério Sul - Nebulosidade (%) vs. Latitude
* Hemisfério Norte - Velocidade do Vento (mph) vs. Latitude
* Hemisfério Sul - Velocidade do Vento (mph) vs. Latitude