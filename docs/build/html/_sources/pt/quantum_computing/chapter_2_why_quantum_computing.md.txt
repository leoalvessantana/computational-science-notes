# Capítulo 2 — Por Que Computação Quântica?

## 2.1 O Custo de Simular a Natureza

No capítulo anterior, mencionamos a observação fundamental de Richard Feynman: simular sistemas quânticos em computadores clássicos se torna exponencialmente difícil à medida que o sistema cresce [1]. É hora de entender exatamente o que isso significa — e por que isso importa tanto.

Quando físicos querem simular um sistema quântico — uma molécula, um material, uma reação química — eles precisam descrever seu estado quântico completo. Classicamente, isso significa armazenar uma lista de números (chamados de *amplitudes*) que descrevem cada configuração possível em que o sistema poderia estar.

O problema é que o número dessas configurações não cresce linearmente com o tamanho do sistema. Ele cresce **exponencialmente**.

<!-- ```{figure} /_static/figures/ch2_fig1-1.png
:name: fig-ch2-1-1
:alt: Crescimento linear vs exponencial

Crescimento linear vs crescimento exponencial à medida que o tamanho do sistema aumenta.
````-->

Uma única partícula com dois estados possíveis exige armazenar 2 números. Duas partículas exigem 4. Três partículas exigem 8. Isso não é coincidência — para *n* partículas, a simulação clássica exige armazenar **2ⁿ** números.

```text
n partículas  →  2ⁿ números a armazenar

 1 partícula   →            2
 2 partículas  →            4
 3 partículas  →            8
10 partículas  →         1.024
20 partículas  →     1.048.576
```

Para sistemas pequenos, isso é administrável. Mas esse crescimento exponencial se acelera muito mais rápido do que a intuição da maioria das pessoas espera.





## 2.2 Espaços de Estados Exponenciais: Um Olhar Concreto

Vamos levar isso ainda mais adiante, porque os números envolvidos são genuinamente surpreendentes.

Para armazenar classicamente o estado quântico completo de apenas **50 partículas**, seria necessário armazenar aproximadamente **2⁵⁰ ≈ 1,13 × 10¹⁵** números. Cada número tipicamente exige alguns bytes de memória — então isso rapidamente alcança a escala de petabytes.

Agora vamos até **300 partículas**. O número de amplitudes necessárias, **2³⁰⁰**, excede a maioria das estimativas físicas do número de átomos no universo observável.

```{note}
Isso não é uma limitação da tecnologia atual — é uma barreira matemática fundamental. Nenhuma quantidade de melhoria de engenharia, processadores mais rápidos ou armazenamento adicional jamais será suficiente para superar um crescimento exponencial dessa escala.
```

Esta é precisamente a barreira que Feynman identificou: computadores clássicos são, em princípio, incapazes de simular eficientemente até mesmo sistemas quânticos de tamanho modesto [1]. Se a natureza realiza rotineiramente essas "computações" por meio do comportamento ordinário de átomos e moléculas, então um computador construído a partir de componentes quânticos — um que opera *nativamente* usando esses mesmos princípios — deveria ser capaz de representar tais estados sem precisar enumerar explicitamente cada configuração.

Isso não é meramente uma forma mais rápida de fazer a mesma coisa que computadores clássicos fazem. É uma estratégia fundamentalmente diferente para representar informação.




## 2.3 Complexidade Computacional: P, NP e Além

Para entender onde os computadores quânticos realmente ajudam — e onde não ajudam —, é útil introduzir, em nível intuitivo, como cientistas da computação classificam a dificuldade dos problemas.

Alguns problemas podem ser resolvidos eficientemente, o que significa que o tempo necessário cresce razoavelmente (de forma polinomial) à medida que a entrada cresce. Esses formam uma classe chamada **P** (tempo Polinomial).

Outros problemas são muito mais difíceis de *resolver*, mas fáceis de *verificar* uma vez que uma solução candidata é fornecida. Esses formam uma classe chamada **NP**.

```text
P   → Problemas que podem ser *resolvidos* eficientemente
NP  → Problemas que podem ser *verificados* eficientemente
```

Uma famosa questão em aberto na ciência da computação — se P é igual a NP — permanece sem solução e está fora do escopo deste livro. O que importa aqui é uma questão relacionada, mais específica: **onde os computadores quânticos se encaixam nesse quadro?**

Acredita-se que os computadores quânticos resolvam eficientemente uma classe de problemas chamada **BQP** (tempo Polinomial Quântico com erro limitado). Acredita-se que alguns problemas dentro de BQP estejam *fora* de P — o que significa que nenhum algoritmo clássico conhecido consegue resolvê-los eficientemente, mas um computador quântico consegue.

```{important}
Não se acredita que os computadores quânticos resolvam problemas NP-completos de forma eficiente em geral. A vantagem que eles oferecem é real, mas mais estreita e específica do que a ficção científica costuma sugerir.
```

Essa distinção importa. A computação quântica não é uma varinha mágica que dissolve toda dificuldade computacional — é uma ferramenta precisa que muda as regras para um conjunto específico e bem definido de problemas.





## 2.4 Onde os Computadores Quânticos Oferecem Vantagem

Com esse enquadramento estabelecido, podemos agora ser concretos sobre onde a vantagem quântica de fato aparece.

O **Algoritmo de Grover** [2] é tradicionalmente apresentado como um método para buscar em um banco de dados não ordenado contendo *N* itens. Classicamente, encontrar um item específico exige verificar até *N* entradas, uma por uma. O algoritmo de Grover reduz isso a aproximadamente *√N* consultas, proporcionando um ganho de velocidade quadrático.

No entanto, é importante entender como esse ganho é alcançado. Um equívoco comum é pensar que um computador quântico simplesmente verifica todos os itens simultaneamente. Não é o caso. Em vez disso, o algoritmo de Grover explora o princípio da **interferência quântica** apresentado na seção anterior. Uma forma de visualizar esse processo é imaginar uma mesa de mixagem de áudio: ao longo de uma sequência de operações cuidadosamente projetadas, o algoritmo gradualmente "aumenta o volume" (aumenta a amplitude de probabilidade) da resposta correta enquanto "diminui o volume" das incorretas.

```text
Busca clássica:  até N passos
Busca de Grover: cerca de √N passos
```


Para um banco de dados contendo um milhão de itens, isso corresponde a reduzir aproximadamente um milhão de passos de busca para apenas cerca de mil.

Outro exemplo marcante é o **Algoritmo de Shor** [3], que aborda o problema da fatoração de inteiros — a tarefa de decompor um número inteiro grande em seus fatores primos. Esse problema constitui a base de grande parte da criptografia de chave pública moderna, porque os melhores algoritmos clássicos conhecidos se tornam proibitivamente custosos à medida que os números crescem.

O algoritmo de Shor fornece um algoritmo de tempo polinomial para a fatoração de inteiros, representando um ganho assintótico dramático em relação aos melhores algoritmos clássicos conhecidos. Esse resultado é a principal razão pela qual a computação quântica atraiu tanta atenção dos campos da criptografia e da cibersegurança.

Além da busca e da fatoração, espera-se que os computadores quânticos sejam úteis em várias outras áreas, incluindo:

- **Simulação quântica** — a motivação original discutida anteriormente neste capítulo, permitindo que sistemas quânticos simulem outros sistemas quânticos eficientemente [1].
- **Otimização combinatória**, por meio de algoritmos que serão apresentados mais adiante neste livro.
- **Certas tarefas de aprendizado de máquina**, uma área de pesquisa ativa e em rápida evolução.

Esses algoritmos e aplicações serão revisitados mais adiante no livro, uma vez que tenhamos desenvolvido as ferramentas matemáticas necessárias para entender como eles funcionam.



## 2.5 Limitações Honestas: O Que os Computadores Quânticos Ainda Não Conseguem Fazer

Seria enganoso encerrar este capítulo sem discutir as limitações atuais do hardware quântico.

Os computadores quânticos de hoje operam no que é comumente conhecido como a **era NISQ** (*Noisy Intermediate-Scale Quantum*, ou Quântica Ruidosa de Escala Intermediária), termo introduzido pelo físico John Preskill em 2018 [4]. O nome destaca duas características fundamentais dos dispositivos atuais:

- **Ruidosa (Noisy):** os qubits são extremamente frágeis. Interações com o ambiente ao redor — como calor, campos eletromagnéticos ou até mesmo vibrações microscópicas — causam **decoerência**, destruindo gradualmente a informação quântica antes que uma computação possa ser concluída.

- **Escala intermediária (Intermediate-scale):** embora os processadores atuais variem de dezenas a mais de mil qubits físicos [5], isso ainda está muito abaixo dos milhões de qubits físicos que se espera que sejam necessários para uma computação quântica tolerante a falhas e em larga escala.

```{note}
Computadores quânticos tolerantes a falhas — do tipo capaz de executar algoritmos como o de Shor em números criptograficamente relevantes — provavelmente exigirão milhões de qubits físicos protegidos por correção de erros quânticos. Alcançar isso continua sendo um dos maiores desafios de engenharia da área.
```

Isso naturalmente levanta uma questão importante:

**Se computadores quânticos tolerantes a falhas ainda não existem, os processadores quânticos de hoje são realmente úteis?**

A resposta é **sim**.

Para fazer uso prático do hardware atual, pesquisadores desenvolveram os **Algoritmos Quânticos Variacionais (VQAs)**, incluindo o **Variational Quantum Eigensolver (VQE)** e o **Quantum Approximate Optimization Algorithm (QAOA)**.

Esses algoritmos adotam uma **abordagem híbrida quântico-clássica**. Em vez de pedir a um processador quântico frágil que execute sozinho uma computação longa e complexa, o trabalho é dividido entre duas máquinas. Um computador clássico realiza a otimização dos parâmetros do algoritmo, enquanto o processador quântico atua como um coprocessador especializado, avaliando circuitos quânticos que seriam computacionalmente custosos de simular classicamente.

Como os circuitos quânticos permanecem relativamente curtos, a computação fica muito menos vulnerável à decoerência. Essa estratégia híbrida atualmente representa uma das direções mais promissoras para a computação quântica de curto prazo e se tornou um dos temas centrais de pesquisa na era NISQ.

É importante ter essa distinção em mente. Os algoritmos apresentados na seção anterior têm ganhos quânticos matematicamente comprovados, mas o hardware tolerante a falhas em larga escala necessário para realizar todo o seu potencial ainda não foi construído. Até lá, os algoritmos híbridos quântico-clássicos oferecem uma forma prática de extrair valor computacional significativo dos processadores quânticos de hoje.

Dada sua importância prática, revisitaremos essas abordagens híbridas mais adiante no livro. Exploraremos primeiro a teoria subjacente, e então aprenderemos a implementar esses algoritmos passo a passo usando frameworks modernos de programação quântica.


## 2.6 Definindo Expectativas para o Restante Deste Livro

A esta altura, a motivação deve estar clara: computadores quânticos não são computadores clássicos mais rápidos, nem uma solução universal para todo problema computacional. Eles são máquinas especializadas que oferecem vantagens genuínas e matematicamente fundamentadas para uma classe específica — mas importante — de problemas, entre os quais se destacam a simulação quântica, a fatoração de inteiros e a busca não estruturada.

Entender *por que* eles conseguem fazer isso exige entender *como* a informação quântica é representada e manipulada — que é exatamente para onde este livro se volta a seguir.

Os próximos capítulos construirão, peça por peça, a linguagem matemática necessária para descrever qubits com precisão — começando pela álgebra linear que fundamenta toda a mecânica quântica.

---

## Referências

[1] Feynman, R. P. (1982). Simulating physics with computers. *International Journal of Theoretical Physics*, 21(6-7), 467–488.

[2] Grover, L. K. (1996). A fast quantum mechanical algorithm for database search. *Proceedings of the 28th Annual ACM Symposium on the Theory of Computing (STOC)*, 212–219. arXiv:quant-ph/9605043.

[3] Shor, P. W. (1997). Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer. *SIAM Journal on Computing*, 26(5), 1484–1509. arXiv:quant-ph/9508027.

[4] Preskill, J. (2018). Quantum computing in the NISQ era and beyond. *Quantum*, 2, 79. arXiv:1801.00862.

[5] Wikipedia contributors. Noisy intermediate-scale quantum computing. *Wikipedia, The Free Encyclopedia*. Retrieved July 2026.