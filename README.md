# Caramelo: A Saga do Bolo de Rolo Dourado
## Descrição do Jogo
Caramelo: A Saga do Bolo de Rolo Dourado é um jogo bidimensional inspirado em um dos símbolos mais populares do imaginário brasileiro: o cachorro caramelo. A narrativa acompanha um cão caramelo que tem seu bolo de rolo roubado por um gato de condomínio, dando início à jornada principal do jogo.

Ao longo da jogabilidade, o personagem deve superar desafios e percorrer diferentes plataformas com o objetivo de recuperar o bolo de rolo. Dessa forma, o jogador é estimulado a executar saltos precisos e tomar decisões estratégicas para alcançar o objetivo final, enfrentando obstáculos distribuídos ao longo do cenário.

O projeto foi desenvolvido como um dos requisitos para a conclusão da disciplina de Introdução à Programação. Para a implementação do jogo, utilizou-se a biblioteca Pygame, aliada à aplicação dos principais conceitos abordados ao longo da disciplina, tais como lógica de programação, organização e estruturação de código, além de programação orientada a objetos.

---
## Integrantes da Equipe

  - Pedro Henrique Cabral Galdino dos Santos <phcgs>
  - Felipe José Batista Farias <fjbf>
  - Valquiria Eugenia Silva <ves>
  - Everton Teixeira da Silva Luz <etsl>
  - Irene Maria Colaço Jacques Porsdottir <imcjp>
  - Alany Vitória Borba de Siqueira <avbs2>

---
## Divisão de Trabalho



| Membro                         | Atribuições                                                                |
|--------------------------------|----------------------------------------------------------------------------|
| Pedro Henrique Cabral Galdino dos Santos   | Criação da Tela Inicial e Final do Jogo, imagens do Jogo, Sons e Implementação dos Sprites | 
| Felipe José Batista Farias                 | Criação de Plataforma, Implementação inicial de coletáveis e Contador dos Coletaveis |
| Valquiria Eugenia Silva                    | Criação de Plataforma, Implementação inicial de coletáveis e Contador dos Coletaveis |
| Everton Teixeira da Silva Luz              | Movimentação do Cachorro, Implementação de Telas Inicial e Final e História, Implementação dos Sons, Finalização dos Coletáveis e README|
| Irene Maria Colaço Jacques Porsdottir      | Moviemntação do Cachorro, Implementação de Telas Inicial e Final, História e Implementação dos Sons e Finalização dos Coletáveis |
| Alany Vitória Borba de Siqueira            | Criação da Tela Inicial e Final do Jogo, imagens do Jogo, Sons e Implementação dos Sprites |


---

## Arquitetura do Projeto
```
projetoip_pedro/
├── audio/
├── imagens/
├── sprites/
├── main.py
└── README.md
```

---

## Ferramentas e Justificativas

Para a elaboração do jogo "Caramelo: A Saga do Bolo de Rolo Dourado", foram empregadas diferentes ferramentas que, de forma integrada, possibilitaram a construção dos cenários, o correto funcionamento das mecânicas e a implementação dos recursos sonoros. As tecnologias utilizadas foram:

- **Python**: linguagem de programação adotada como base do projeto, responsável pela implementação da lógica, criação de classes e integração com as demais bibliotecas utilizadas;
- **Pygame**: biblioteca da linguagem Python empregada para o gerenciamento de elementos gráficos, detecção de eventos do teclado, controle das interações do jogador e execução de efeitos sonoros; 
- **os**: módulo nativo da linguagem Python utilizado para manipulação de caminhos de arquivos e diretórios, permitindo o carregamento organizado de imagens, sons e outros recursos do jogo de forma independente do sistema operacional;
- **Visual Studio Code**: ambiente de desenvolvimento escolhido pela equipe devido à sua flexibilidade, facilidade de uso e eficiente integração com o GitHub;
- **GitHub**: plataforma utilizada para o armazenamento do código-fonte, controle de versionamento e colaboração entre os integrantes do grupo;
- **Discord e WhatsApp**: ferramentas adotadas para comunicação, sendo o Discord utilizado principalmente para contato com a monitoria e o WhatsApp para a organização e comunicação interna da equipe.

---

## Conceitos Utilizados

- **Estruturas condicionais**: os comandos if, elif e else foram empregados para a tomada de decisões durante a execução do jogo, permitindo identificar diferentes estados do personagem ao longo da jogabilidade. Esses recursos foram essenciais para o controle da movimentação a partir das entradas do teclado, bem como para o tratamento de eventos como colisões com outros elementos do cenário;

- **Laços de repetição**: as estruturas for e while foram utilizadas para manter o fluxo contínuo de execução do jogo, garantindo a atualização constante da lógica e da renderização até que as condições de término fossem atendidas;

- **Listas**: utilizadas para armazenar e gerenciar conjuntos de dados de forma dinâmica, como sequências de sprites, animações e grupos de elementos do jogo. O uso de listas possibilitou a iteração eficiente sobre esses elementos e facilitou a manipulação de múltiplos objetos durante a execução do programa;

- **Funções**: foram responsáveis por organizar e encapsular as rotinas principais do jogo, concentrando ações executadas repetidamente. Essa abordagem facilitou a atualização do estado do personagem e contribuiu para a legibilidade e manutenção do código; 

- **Programação Orientada a Objetos (POO)**: adotada como base para a organização e modularização do projeto, possibilitando a criação de classes que representam entidades do jogo, como o personagem principal, inimigos e elementos do ambiente. Essa abordagem permitiu o encapsulamento de atributos e comportamentos, além da reutilização de código por meio da instanciação de objetos.

---

## Desafios, Erros e Lições Aprendidas

**Qual foi o maior erro cometido durante o processo de desenvolvimento e como ele foi solucionado?**
O principal equívoco ocorrido ao longo do desenvolvimento do projeto Caramelo: A Saga do Bolo de Rolo Dourado esteve relacionado às fases iniciais de planejamento. A equipe não definiu previamente, de forma clara, o escopo do projeto, nem estabeleceu uma fonte de inspiração bem delimitada. Além disso, não houve critérios objetivos para avaliar a viabilidade da ideia dentro do prazo disponível para a execução. Diante dessa situação, optou-se por buscar orientação junto aos monitores da disciplina, o que possibilitou uma melhor definição das funcionalidades possíveis de serem implementadas. Essa decisão foi fundamental para evitar a priorização inadequada de etapas e garantir o cumprimento dos requisitos propostos de maneira eficiente.

**Qual foi o maior desafio enfrentado durante o projeto? Como ele foi superado?**
O maior desafio identificado pela equipe esteve relacionado ao controle de versionamento do código-fonte. A maior parte dos integrantes não possuía experiência prévia com o uso do GitHub, o que dificultou, inicialmente, a organização e a colaboração no desenvolvimento do projeto. No entanto, por meio de um planejamento mais estruturado, estudo da ferramenta e documentação adequada do código, foi possível superar essa dificuldade. Dessa forma, o versionamento passou a ser utilizado de maneira mais eficiente, permitindo que todos os integrantes contribuíssem ativamente para o projeto.

---

## Instruções de Execução

1. Clone o repositório:
```bash
git clone https://github.com/jaikarla/jogo-ip.git
```

2. Instale as dependências:
```bash
pip install pygame
```

3. Execute o jogo:
```bash
python jogo.py
```

---

## Controles

| Caramelo              | Controles                   | 
|-----------------------|-----------------------------|
| Pular                 | W                           | 
| latir                 | SPACE                       | 
| Mover para a esquerda | A                           |
| Mover para a direita  | D                           | 


  