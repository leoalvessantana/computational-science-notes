# Capítulo 1 — Introdução

<!-- ```{contents}
:local:
:depth: 2
``` -->


## 1.1 Por Que Mais Um Livro?

A computação quântica é um dos campos mais fascinantes da ciência moderna. Ela reúne física, matemática, ciência da computação e teoria da informação em uma forma inteiramente nova de pensar sobre computação.

Infelizmente, muitos materiais de estudo assumem conhecimento prévio demais ou introduzem o assunto por meio de um formalismo matemático pesado desde o início. Como resultado, muitos leitores acham a computação quântica muito mais intimidadora do que realmente precisa ser.

Este livro adota uma abordagem diferente. Seu objetivo é construir intuição primeiro, introduzir matemática apenas quando ela se tornar necessária, e conectar constantemente conceitos abstratos com exemplos práticos e implementações reais.

Outra motivação para este livro é que a computação quântica é um campo em rápida evolução. Novos algoritmos, arquiteturas de hardware, frameworks de programação e resultados experimentais surgem a cada ano. Embora os livros didáticos tradicionais forneçam uma excelente base, eles são naturalmente limitados ao estado da área no momento em que foram publicados.

Como este livro é mantido como um recurso online vivo, ele é projetado para evoluir junto com o próprio campo. Novos capítulos, explicações atualizadas, descobertas recentes e tecnologias emergentes serão incorporados ao longo do tempo, garantindo que os leitores sempre tenham acesso a material que reflita o estado atual da computação quântica.






## 1.2 Da Física Clássica à Mecânica Quântica

### A Ascensão da Física Clássica

Por séculos, nossa compreensão do universo foi moldada pela **Física Clássica**. Seus fundamentos foram estabelecidos no século XVII, quando Isaac Newton introduziu um arcabouço matemático capaz de descrever o movimento dos objetos com precisão notável.

As leis do movimento de Newton e sua lei da gravitação universal explicavam fenômenos que iam da queda de uma maçã às órbitas dos planetas. Pela primeira vez, a natureza parecia obedecer a um pequeno conjunto de leis matemáticas elegantes.

Esse sucesso inspirou uma ideia poderosa: se conhecemos o estado atual de um sistema e as leis que o governam, deveríamos ser capazes de prever seu futuro. O universo passou a ser visto como um vasto mecanismo determinístico, no qual cada evento decorria inevitavelmente de condições anteriores.

<!-- ```{figure} /_static/figures/ch1_fig2-1.png
:name: fig-2-1
:alt: O universo determinístico de Newton

O universo determinístico de Newton. Ilustração mostrando Newton, movimento planetário.
``` -->



### A Expansão da Física Clássica

Ao longo dos dois séculos seguintes, a física clássica continuou a se expandir. A termodinâmica descreveu calor e energia, enquanto James Clerk Maxwell unificou eletricidade e magnetismo em uma única teoria.

As equações de Maxwell não apenas explicaram fenômenos elétricos e magnéticos, mas também revelaram que a própria luz é uma onda eletromagnética. Essa notável unificação demonstrou que fenômenos naturais aparentemente não relacionados poderiam ser descritos por um único arcabouço matemático.

Ao final do século XIX, a física clássica havia alcançado um sucesso extraordinário. Ela descrevia com precisão o movimento dos corpos celestes, o comportamento de máquinas térmicas, a propagação da luz e inúmeros fenômenos do cotidiano.

Muitos cientistas acreditavam que a física estava essencialmente completa, restando apenas algumas questões não resolvidas.

<!-- ```{figure} /_static/figures/ch1_fig2-2.png
:name: fig-2-2
:alt: O triunfo da Física Clássica

O triunfo da Física Clássica. Ilustração combinando máquinas a vapor, eletricidade, magnetismo e ondas eletromagnéticas.
``` -->

No entanto, a natureza ainda guardava algumas surpresas.



### Os Limites da Física Clássica

Apesar de seu sucesso extraordinário, a física clássica não conseguia explicar diversas observações experimentais.

A princípio, essas discrepâncias pareciam problemas isolados. No entanto, elas acabariam revelando que a descrição clássica da natureza era fundamentalmente incompleta.

O primeiro grande desafio veio do estudo da **radiação de corpo negro**.

Segundo a física clássica, um objeto quente deveria emitir uma quantidade infinita de energia em comprimentos de onda muito curtos — uma previsão impossível conhecida como **catástrofe do ultravioleta**.

Apenas alguns anos depois, surgiu outro enigma: o **efeito fotoelétrico**, no qual a luz conseguia ejetar elétrons de uma superfície metálica de maneiras que a teoria ondulatória clássica não conseguia explicar.

Quase ao mesmo tempo, os físicos lutavam para entender por que os átomos são estáveis. De acordo com o eletromagnetismo clássico, elétrons em órbita deveriam perder energia continuamente e colapsar sobre o núcleo. No entanto, os átomos claramente existem.

Esses e outros enigmas sugeriam que algo fundamental estava faltando em nossa compreensão da natureza.

<!-- ```{figure} /_static/figures/ch1_fig2-3.png
:name: fig-2-3
:alt: As limitações da Física Clássica -->

<!-- As limitações da Física Clássica. Linha do tempo destacando o problema da radiação de corpo negro, o efeito fotoelétrico e a estabilidade atômica.
``` -->



### O Nascimento da Mecânica Quântica

Em 1900, Max Planck propôs uma solução ousada para o problema da radiação de corpo negro [1]. Ele sugeriu que a energia é trocada em pacotes discretos, mais tarde chamados de **quanta**. Embora introduzida como uma suposição matemática, essa ideia marcou o nascimento da teoria quântica.

Apenas cinco anos depois, Albert Einstein estendeu a hipótese de Planck para explicar o efeito fotoelétrico [2], propondo que a própria luz se comporta como se fosse composta de partículas individuais, hoje conhecidas como **fótons**.

Em 1913, Niels Bohr introduziu um novo modelo do átomo no qual os elétrons ocupam níveis discretos de energia [3], fornecendo a primeira explicação bem-sucedida para a estabilidade atômica.

A revolução continuou quando Louis de Broglie propôs que a matéria, assim como a luz, também possui propriedades ondulatórias [4]. Essa ideia surpreendente foi posteriormente confirmada experimentalmente e ficou conhecida como **dualidade onda-partícula**.

Com base nessas descobertas, Erwin Schrödinger desenvolveu a equação de onda que descreve a evolução dos sistemas quânticos [5], enquanto Werner Heisenberg introduziu a mecânica matricial e formulou o princípio da incerteza [6]. Por fim, Paul Dirac unificou muitas dessas ideias em um poderoso arcabouço matemático e desenvolveu a notação ainda amplamente utilizada hoje [7].


<!-- ```{figure} /_static/figures/ch1_fig2-4.png
:name: fig-2-4
:alt: Linha do tempo do nascimento da Mecânica Quântica -->

<!-- Linha do tempo do nascimento da Mecânica Quântica: Planck → Einstein → Bohr → de Broglie → Schrödinger → Heisenberg → Dirac.
``` -->



### Uma Nova Visão da Realidade

Juntas, essas descobertas transformaram nossa compreensão da natureza.

O universo deixou de ser visto como um mecanismo perfeitamente previsível, governado apenas por leis clássicas. Em vez disso, ficou claro que, em escalas microscópicas, a realidade segue princípios que diferem profundamente de nossa intuição cotidiana.

Conceitos como quantização, dualidade onda-partícula, superposição, incerteza e probabilidade tornaram-se ingredientes fundamentais da nova teoria.

A mecânica quântica não foi resultado de uma única descoberta ou do trabalho de um único cientista. Ela emergiu ao longo de décadas por meio das contribuições de muitos pesquisadores, formando uma das teorias científicas mais bem-sucedidas já desenvolvidas.

Hoje, a mecânica quântica fornece a base para inúmeras tecnologias modernas, incluindo lasers, semicondutores, ressonância magnética, relógios atômicos e, por fim, a computação quântica.

<!-- ```{figure} /_static/figures/ch1_fig2-5.png
:name: fig-2-5
:alt: Da Física Clássica à Mecânica Quântica

Da Física Clássica à Mecânica Quântica.
``` -->





## 1.3 Da Mecânica Quântica à Computação Quântica

### A Computação É Física

O desenvolvimento da mecânica quântica revolucionou nossa compreensão da natureza. Mas, por várias décadas, essas descobertas pareciam pertencer exclusivamente à física.

À primeira vista, mecânica quântica e computação parecem ser campos não relacionados. Um descreve o comportamento da matéria e da energia em escalas microscópicas, enquanto o outro se concentra no processamento de informação.

Na realidade, porém, a computação sempre esteve limitada pelas leis da física.

Todo computador, desde as primeiras calculadoras mecânicas até os supercomputadores mais avançados de hoje, é, em última análise, uma máquina física. Cada bit armazenado, cada sinal elétrico e cada operação lógica é implementado por um sistema físico que obedece às leis da natureza.

Os primeiros computadores eletrônicos foram construídos usando válvulas e, mais tarde, transistores. Embora sua arquitetura tenha evoluído drasticamente ao longo do tempo, todos eles se baseavam nos princípios da física clássica e da eletrônica clássica.

Por décadas, essa distinção pouco importou. Os computadores clássicos foram extraordinariamente bem-sucedidos, e a física clássica fornecia uma descrição precisa dos dispositivos usados para construí-los.

Mas uma pergunta natural acabou surgindo:

```{epigraph}
Se a própria natureza se comporta de acordo com as leis da mecânica quântica, a computação também não deveria seguir essas mesmas leis?
```

Essa pergunta aparentemente simples daria origem a um modelo de computação inteiramente novo.

<!-- ```{figure} /_static/figures/ch1_fig3-1.png
:name: fig-3-1
:alt: A computação como um processo físico

A computação como um processo físico. Ilustração mostrando a evolução de engrenagens mecânicas para válvulas, transistores, circuitos integrados e, finalmente, processadores quânticos.
``` -->



### O Nascimento da Computação Quântica

As primeiras ideias conectando mecânica quântica e computação surgiram no início da década de 1980.

Em 1980, **Paul Benioff** demonstrou que um computador poderia, em princípio, ser descrito usando o arcabouço matemático da mecânica quântica [8].

Pouco depois, em 1981, **Richard Feynman** fez uma observação profunda [9]. Ele argumentou que simular sistemas quânticos em computadores clássicos se torna exponencialmente difícil à medida que o tamanho do sistema aumenta. Como a própria natureza é mecânico-quântica, ele propôs construir computadores que operassem segundo princípios quânticos.

Essa ideia representou uma mudança radical de perspectiva. Em vez de forçar computadores clássicos a imitar sistemas quânticos, por que não construir computadores que fossem quânticos desde o início?

Alguns anos depois, em 1985, **David Deutsch** introduziu o conceito de um computador quântico universal [10], fornecendo os fundamentos teóricos para um modelo de computação completamente novo.

Juntas, essas ideias marcaram o nascimento da computação quântica como disciplina científica.


<!-- ```{figure} /_static/figures/ch1_fig3-2.png
:name: fig-3-2
:alt: O nascimento da computação quântica

O nascimento da computação quântica. Linha do tempo: Benioff (1980) → Feynman (1981) → Deutsch (1985).
``` -->






### Um Novo Modelo de Computação

Computadores quânticos não são simplesmente versões mais rápidas de computadores clássicos.

Em vez disso, eles processam informação usando os princípios da mecânica quântica. Sua unidade fundamental de informação, o **qubit**, comporta-se de acordo com leis quânticas, e não clássicas.

Isso permite que algoritmos quânticos explorem fenômenos como superposição, interferência e emaranhamento para resolver certos problemas de maneiras que não têm equivalente clássico.

É importante enfatizar, porém, que os computadores quânticos **não têm o objetivo de substituir os computadores clássicos**. Os computadores clássicos continuam sendo a melhor escolha para a esmagadora maioria das tarefas computacionais do dia a dia.

Em vez disso, os computadores quânticos são dispositivos especializados projetados para enfrentar problemas que se tornam proibitivamente difíceis para máquinas clássicas, como simulação quântica, fatoração de inteiros, certos problemas de otimização e outros desafios computacionais que surgem naturalmente na ciência e na engenharia.

Os capítulos seguintes introduzirão gradualmente os conceitos necessários para entender como essas máquinas notáveis funcionam, começando pela pergunta fundamental:

> **O que torna um computador quântico diferente de um computador clássico?**

<!-- ```{figure} /_static/figures/ch1_fig3-3.png
:name: fig-3-3
:alt: Da Física à Computação

Da Física à Computação. Um diagrama conceitual ilustrando como novos princípios físicos deram origem a um novo modelo de computação.
``` -->






## 1.4 Onde a Computação Clássica Encontra Dificuldades

Se os computadores quânticos se baseiam em princípios físicos fundamentalmente diferentes, uma pergunta importante surge naturalmente:

**Por que precisamos deles?**

A resposta não é que os computadores clássicos sejam inadequados. Pelo contrário, eles estão entre as maiores conquistas tecnológicas da história humana. De smartphones e laptops a satélites e supercomputadores, os computadores clássicos resolvem bilhões de problemas todos os dias com extraordinária eficiência.

Para a esmagadora maioria das tarefas computacionais, os computadores clássicos são exatamente a ferramenta certa.

No entanto, nem todo problema escala com facilidade.

À medida que os problemas se tornam maiores e mais complexos, o número de soluções possíveis frequentemente cresce de forma exponencial. Esse fenômeno, conhecido como **explosão combinatória**, rapidamente torna muitas tarefas computacionais intratáveis, mesmo para os supercomputadores mais poderosos do mundo.

Para alguns problemas, adicionar mais processadores ou construir hardware mais rápido simplesmente não é suficiente.

É aqui que a computação quântica se torna interessante.

Ao explorar as leis da mecânica quântica, os computadores quânticos oferecem formas fundamentalmente diferentes de processar informação — possibilitando abordagens inteiramente novas para problemas que, na prática, são inalcançáveis apenas por computadores clássicos.

O próximo capítulo tornará essa afirmação concreta, examinando problemas específicos nos quais os computadores quânticos oferecem uma vantagem genuína e mensurável.

É importante, no entanto, manter expectativas realistas.

`````{important}
Computadores quânticos não são substitutos dos computadores clássicos.
`````

Eles são **computadores especializados projetados para tipos específicos de problemas**. Assim como as unidades de processamento gráfico (GPUs) complementam as CPUs tradicionais em vez de substituí-las, espera-se que os processadores quânticos trabalhem junto com os computadores clássicos, cada um sendo usado onde tem melhor desempenho.
<!-- 
`````{figure} /_static/figures/ch1_fig4-1.png
:name: fig-4-1
:alt: Computação Clássica vs. Quântica

Computação Clássica vs. Quântica. Computadores quânticos complementam, em vez de substituir, os computadores clássicos.
````-->

```text
Tarefas do Dia a Dia
         │
         ▼
Computadores Clássicos

Problemas Extremamente Complexos
         │
         ▼
Computadores Quânticos
```








## 1.5 Bits e Qubits: Um Primeiro Olhar

Todo modelo de computação é construído sobre uma unidade fundamental de informação.

Na computação clássica, essa unidade é o **bit**.

Imagine uma moeda em repouso sobre uma mesa. Ela só pode estar mostrando Cara ou Coroa. É exatamente assim que funciona um bit clássico — ele é estritamente um **0** ou um **1**. Toda informação digital — de textos e imagens a vídeos e softwares — é, em última análise, codificada como longas sequências desses bits discretos e imóveis.


```text
Bit

0

1
```

Os computadores quânticos, no entanto, são construídos a partir de uma unidade de informação diferente, conhecida como **qubit**, ou **bit quântico**.


Diferentemente de um bit clássico, um qubit é governado pelas leis da mecânica quântica. Para entender a diferença, imagine pegar aquela mesma moeda e girá-la sobre a mesa. Enquanto ela está girando, ela é Cara ou Coroa? A resposta é nenhuma das duas, e, de certa forma, uma mistura contínua de ambas. Ela existe em um estado dinâmico e intermediário, que carrega probabilidades variadas de cair em 0 ou 1 quando você finalmente a para (mede).

Como um qubit não está limitado a apenas dois estados rígidos, precisamos de uma forma mais rica de descrevê-lo. Seu estado pode ser representado geometricamente como qualquer ponto na superfície de uma esfera, conhecida como **Esfera de Bloch**.

<!-- ```{figure} /_static/figures/ch1_fig5-1.png
:name: fig-5-1
:alt: Um bit clássico e um qubit

Um bit clássico e um qubit. Ilustração comparando um bit clássico (0 ou 1) com um qubit representado na Esfera de Bloch.
``` -->

Neste momento, não há necessidade de entender a matemática por trás dessa representação. A Esfera de Bloch simplesmente fornece um mapa visual útil para nossa "moeda girando".

O significado matemático dos qubits, dos estados quânticos e da Esfera de Bloch será desenvolvido progressivamente ao longo dos capítulos seguintes.





## 1.6 Como os Computadores Quânticos Computam?

Embora os computadores quânticos sejam construídos sobre princípios físicos que diferem fundamentalmente daqueles dos computadores clássicos, seu fluxo de trabalho computacional geral é, à primeira vista, surpreendentemente semelhante.

Toda computação começa com informação clássica fornecida pelo usuário. Essa informação é então codificada no estado de um ou mais qubits, preparando o sistema quântico para executar um algoritmo quântico.

Em seguida, o processador quântico aplica uma sequência de operações conhecidas como **portas quânticas**. Juntas, essas portas formam um **circuito quântico**, que evolui o estado quântico de acordo com o algoritmo em execução.

É aqui que surge a diferença fundamental em relação à computação clássica. Enquanto as portas lógicas clássicas simplesmente transformam bits de 0 para 1 (ou vice-versa), as portas quânticas modificam as **amplitudes de probabilidade** dos estados quânticos. Como essas amplitudes se comportam matematicamente como ondas, elas podem se combinar por meio do fenômeno da **interferência**.

Uma analogia útil é imaginar ondulações na superfície de um lago. Quando duas ondas se encontram, elas podem se reforçar mutuamente, produzindo uma onda maior (**interferência construtiva**), ou podem se cancelar parcial ou completamente (**interferência destrutiva**). Durante a execução de um algoritmo quântico, as amplitudes de probabilidade associadas a diferentes estados quânticos evoluem exatamente dessa forma.

A ideia central por trás do design de algoritmos quânticos é organizar cuidadosamente as portas quânticas de modo que as amplitudes associadas a respostas incorretas interfiram destrutivamente, enquanto aquelas correspondentes à resposta correta interfiram construtivamente. Em outras palavras, um computador quântico **não** simplesmente "tenta todas as respostas possíveis ao mesmo tempo". Em vez disso, ele projeta a evolução do estado quântico de modo que medir a resposta correta se torne muito mais provável.

Por fim, os qubits são **medidos**. A medição converte a informação quântica em informação clássica, produzindo uma sequência de bits que pode ser interpretada pelo usuário. Como a medição quântica é inerentemente probabilística, uma única execução pode não revelar a resposta correta com certeza absoluta. Por esse motivo, muitos algoritmos quânticos são executados múltiplas vezes (chamadas de **shots**), permitindo que o resultado correto seja inferido a partir da distribuição dos resultados de medição.

```text
        Entrada Clássica
               │
               ▼
      Codificação em Qubits
               │
               ▼
        Circuito Quântico
        (Portas Quânticas)
               │
               ▼
           Medição
               │
               ▼
       Saída Clássica
```

À primeira vista, esse fluxo de trabalho pode parecer simples. No entanto, cada etapa se baseia em conceitos que não têm equivalente clássico. Entender como a informação é codificada, manipulada e medida em um sistema quântico é a chave para compreender por que os computadores quânticos podem resolver certos problemas com mais eficiência do que os computadores clássicos.

Nos capítulos seguintes, exploraremos cada etapa desse fluxo de trabalho em detalhes, começando pela unidade fundamental de informação quântica: o **qubit**.


<!-- 
```{figure} /_static/figures/ch1_fig6-1.png
:name: fig-6-1
:alt: O fluxo de trabalho da computação quântica

O fluxo de trabalho da computação quântica.
``` -->






## 1.7 O Que Você Vai Aprender

Este livro foi projetado para construir sua compreensão progressivamente.

Em vez de assumir conhecimento prévio de mecânica quântica ou matemática avançada, introduziremos cada conceito exatamente quando ele se tornar necessário, sempre partindo da intuição em direção ao formalismo — nunca o contrário.

Para manter essa progressão fácil de acompanhar, o livro está organizado em seis partes. Cada parte agrupa um conjunto de capítulos intimamente relacionados em torno de uma única pergunta norteadora.

| Parte | Pergunta Norteadora | Tópicos Abordados |
|------|-------------------|-----------------|
| **I. Motivação** | Por que a computação quântica importa? | Por Que Computação Quântica? |
| **II. Fundamentos Matemáticos** | Que linguagem precisamos para descrever estados quânticos? | Números Complexos · Espaços Vetoriais · Álgebra Linear · Notação de Dirac |
| **III. Informação Quântica** | O que é um qubit, e como ele difere de um bit? | Bits Clássicos · Os Postulados da Mecânica Quântica · Qubits · Esfera de Bloch · Portas Quânticas |
| **IV. Sistemas Multi-Qubit** | O que acontece quando qubits interagem? | Múltiplos Qubits · Produtos Tensoriais · Emaranhamento · Medição · Circuitos Quânticos · Teorema da Não-Clonagem |
| **V. Algoritmos Quânticos** | Como os computadores quânticos ganham vantagem? | Teoria Computacional · Análise de Algoritmos · Algoritmo de Grover · Deutsch–Jozsa · Transformada Quântica de Fourier · Algoritmo de Shor |
| **VI. Aplicações Quânticas** | Para onde isso está caminhando? | Otimização Quântica · Algoritmos Quânticos Variacionais · Aprendizado de Máquina Quântico · Redes Neurais Quânticas |

Em um nível geral, essa progressão se apresenta da seguinte forma:

```text
Motivação → Matemática → Informação Quântica → Sistemas Multi-Qubit → Algoritmos → Aplicações
```

Cada parte se apoia estritamente nas anteriores: a matemática introduzida na Parte II é o que torna os qubits (Parte III) precisos; os qubits são o que torna o emaranhamento e os circuitos (Parte IV) significativos; e somente depois de compreendidos os circuitos é que os algoritmos (Parte V) e suas aplicações (Parte VI) passam a fazer sentido de verdade.

```{note}
Essa estrutura é um **mapa**, não um contrato rígido — alguns capítulos podem ser reordenados ou expandidos à medida que o livro evolui, mas a lógica geral (conceito antes do formalismo, formalismo antes do algoritmo) permanecerá o princípio norteador ao longo de toda a obra.
```






## 1.8 Pré-requisitos

Um dos objetivos deste livro é tornar a computação quântica acessível a leitores de diferentes formações.

Você **não** precisa de conhecimento prévio de mecânica quântica para acompanhar o material.

Da mesma forma, os conceitos matemáticos necessários ao longo do livro — incluindo álgebra linear, números complexos e espaços vetoriais — serão introduzidos progressivamente, à medida que se tornarem relevantes.

Uma familiaridade básica com matemática do ensino médio e conceitos elementares de programação será útil, mas curiosidade e disposição para aprender são muito mais importantes do que conhecimento prévio.






## 1.9 Considerações Finais

A computação quântica desafia muitas das intuições que desenvolvemos na vida cotidiana.

Conceitos como **superposição**, **interferência** e **emaranhamento** podem inicialmente parecer estranhos ou até contraintuitivos. No entanto, essas ideias emergem naturalmente do arcabouço matemático da mecânica quântica e foram confirmadas por décadas de evidências experimentais.

Ao longo deste livro, nosso objetivo não é meramente apresentar equações ou descrever algoritmos. Em vez disso, buscamos desenvolver uma compreensão intuitiva de por que a computação quântica funciona, como seus fundamentos matemáticos surgem, e o que a torna fundamentalmente diferente da computação clássica.

Aprender computação quântica não é simplesmente dominar uma nova tecnologia — é descobrir uma nova forma de pensar sobre informação, computação e o mundo físico.

Bem-vindo ao início dessa jornada.


---

## Referências

[1] Planck, M. (1900). Zur Theorie des Gesetzes der Energieverteilung im Normalspectrum. *Verhandlungen der Deutschen Physikalischen Gesellschaft*, 2, 237–245.

[2] Einstein, A. (1905). Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt. *Annalen der Physik*, 322(6), 132–148.

[3] Bohr, N. (1913). On the constitution of atoms and molecules. *Philosophical Magazine*, 26(151), 1–25.

[4] de Broglie, L. (1924). *Recherches sur la théorie des quanta* (Tese de doutorado, Universidade de Sorbonne, Paris).

[5] Schrödinger, E. (1926). Quantisierung als Eigenwertproblem. *Annalen der Physik*, 384(4), 361–376.

[6] Heisenberg, W. (1927). Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik. *Zeitschrift für Physik*, 43(3–4), 172–198.

[7] Dirac, P. A. M. (1930). *The Principles of Quantum Mechanics*. Oxford University Press.

[8] Benioff, P. (1980). The computer as a physical system: A microscopic quantum mechanical Hamiltonian model of computers as represented by Turing machines. *Journal of Statistical Physics*, 22(5), 563–591.

[9] Feynman, R. P. (1982). Simulating physics with computers. *International Journal of Theoretical Physics*, 21(6–7), 467–488.

[10] Deutsch, D. (1985). Quantum theory, the Church-Turing principle and the universal quantum computer. *Proceedings of the Royal Society of London A*, 400(1818), 97–117.