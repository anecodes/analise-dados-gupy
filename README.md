# Análise de dados de vagas da plataforma Gupy

## Introdução

Neste desafio proposto, o objetivo foi o de apresentar dados específicos referentes à oferta de vagas de emprego na [plataforma Gupy](https://portal.gupy.io) e fazer uma análise sobre os dados coletados. Na seção a seguir, será feita a explicação sobre como os dados em questão foram coletados e, em seguida, será feita uma análise quantitativa e uma conclusão geral sobre o material da pesquisa.

## Coleta dos dados

O universo de estudo é composto de empresas que cadastram as vagas de emprego disponíveis em seu banco de vagas. Neste estudo, foi feita uma filtragem para que as vagas analisadas fossem, especificamente, da área de Dados. A técnica utilizada para fazer a busca dos dados referentes às vagas foi a **raspagem de dados web**, ou seja, a mineração e extração de dados de um determinado website a partir de um _bot_ de computador. É importante observar que os seletores de tags, classes e ids, que são atributos obrigatoriamente utilizados pela biblioteca BeautifulSoup e pelo framework Selenium para a raspagem e extração de dados, foram disponibilizados de maneira limitada pelo site Gupy, logo, informações, tais como a modalidade de trabalho, o tipo de trabalho (efetivo ou estágio) e a disponibilidade para a contratação de pessoas com deficiência, não puderam ser incluídas. Neste projeto, as tecnologias utilizadas foram:

- Python (linguagem de programação);
- Selenium (framework de testes);
- BeautifulSoup (biblioteca Python de coleta de dados de arquivos XML e HTML);
- Google Sheets (para a visualização e limpeza dos dados).

Além das tecnologias utilizadas, os parâmetros empregados para a filtragem e posterior análise dos dados foram:

- Empresa responsável;
- Nome da vaga;
- Local da vaga;
- Data de publicação da vaga.

Os dados resultantes dos parâmetros utilizados foram avaliados em tabelas e gráficos, a partir da análise percentual dos perfis buscados pelas vagas disponibilizadas pela plataforma.

## Análise dos dados

### Por cidade

Os dados analisados consistem no conjunto de informações de um total de 413 vagas coletadas através da raspagem de dados web na plataforma Gupy. Em algumas vagas, as informações sobre a _localidade_ da vaga não foram informadas, portanto o valor resultante referente à localidade não é exato. O gráfico a seguir apresenta os valores encontrados referentes à quantidade de vagas por cidade. A maioria das vagas se concentra na cidade de São Paulo (SP), ocupando um total de 36% do total vagas encontradas. Em segundo lugar, vem o Rio de Janeiro (RJ), destacando-se em pouco mais de 10% dos resultados obtidos. Na terceira posição das vagas encontradas na Gupy, encontra-se a cidade de Brasília (DF), que aparece nas pesquisas com aproximadamente 5,6% do total de vagas.

![Percentual de vagas disponíveis por localidade](https://github.com/anecodes/desafio-dados-driva/assets/71999983/33ef6113-f488-49ae-b679-11c430320083)


A partir da análise dos dados obtidos, foi possível concluir que a maioria das vagas disponíveis na área de Dados ainda se concentram nas capitais brasileiras, mais especificamente no eixo Rio-São Paulo, e a menor oferta de vagas é mais concentrada nas cidades pequenas. Além disso, também foi observado, por região, que há uma maior disponibilidade de vagas na área de Dados nas regiões Sudeste e Centro-Oeste.

### Por tipo de cargo

Além da análise feita por cidade, também foi possível ter uma compreensão maior sobre quais são os cargos mais (e menos) ofertados nas vagas de emprego. Do total geral das vagas pesquisadas, pouco menos de 50% das vagas buscadas possuem o título de "Pessoa Analista de Dados", seguido do cargo de "Pessoa Engenheira de Dados", que ocupa pouco menos de 1/5 das vagas encontradas. Já o cargo de "Pessoa arquiteta de vagas" ocupa uma das menores partes do todo, com o total de seis vagas achadas.

![Oferta de vagas por tipo de cargo](https://github.com/anecodes/desafio-dados-driva/assets/71999983/a55ae40d-1da8-429c-b034-f22c605e5a22)


Com base nos resultados obtidos, é possível observar deduzir que as vagas para Análise de Dados não ocupa um número expressivo apenas por ser um título que está em alta atualmente, mas também porque é uma área extremamente ampla, que abrange diversas tarefas, tais como a administração de bancos de dados, a estruturação de sistemas de machine learning e sistemas estatísticos, o suporte aos setores que mais dependem dos dados em uma organização, como o setor financeiro, o tratamento de dados que possam gerar informações importantes para uma importante tomada de decisões, entre outras funções. Já no sentido contrário, observa-se que há uma menor quantidade de vagas para o cargo de Pessoa Arquiteta de Dados, o que pode ocorrer porque o cargo requer uma maior especialização em dados, além de ser, ainda, uma área em crescimento.

### Por mês

Foi possível analisar, também, a quantidade de vagas disponíveis por mês de publicação. No mês atual desta pesquisa - de agosto -, observou-se um grande percentual de vagas – pouco mais de 45% do total encontrado. É possível que esse resultado seja causado por alguns fatores, tais como o fato das vagas ainda serem muito recentes, logo, muitas dessas empresas ainda estão com os seus processos seletivos em aberto. Porém, este é um valor um tanto alto de vagas para o dia do mês em que essa análise foi feita (18 de agosto), o que, provavelmente, possa se justificar pela possibilidade de aumento dos cargos de Dados nas empresas, tanto por questões financeiras, quanto por uma maior adesão à cultura direcionada a dados, ou pela baixa procura das vagas em questão.

![Quantidade de Vagas por Mês](https://github.com/anecodes/desafio-dados-driva/assets/71999983/db74d16a-cc0a-40d2-9905-f869522ac13f)

## Conclusão

Pode-se concluir que, a partir das vagas encontradas durante todo o processo de raspagem de dados, há uma maioria de vagas disponíveis nos grandes centros como São Paulo (SP) e Rio de Janeiro (RJ), logo, sendo essas vagas remotas ou presenciais, é mais provável encontrar vagas na área de Dados nessas localidades. Além disso, das vagas achadas, é mais certo que uma pessoa que está buscando uma vaga em Dados seja contratada como Analista de Dados, que é o cargo com maior disponibilidade pelo país, observando a quantidade de vagas encontradas por localidade. Entende-se, assim, que a área de Dados está em constante crescimento pelas regiões do Brasil, algumas em maior quantidade, outras de maneira não tanto expressiva, mas é uma área que permite constantes mudanças e atualizações na contratação de profissionais.
