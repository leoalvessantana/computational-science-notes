# Chapter 1 — Introduction

<!-- ```{contents}
:local:
:depth: 2
``` -->


## 1. Why Another Book?

Quantum computing is one of the most fascinating fields in modern science. It brings together physics, mathematics, computer science, and information theory into an entirely new way of thinking about computation.

Unfortunately, many learning resources either assume too much prior knowledge or introduce the subject through heavy mathematical formalism from the very beginning. As a result, many readers find quantum computing far more intimidating than it actually needs to be.

This book takes a different approach. Its goal is to build intuition first, introduce mathematics only when it becomes necessary, and consistently connect abstract concepts with practical examples and real implementations.

Another motivation for this book is that quantum computing is a rapidly evolving field. New algorithms, hardware architectures, programming frameworks, and experimental results appear every year. While traditional textbooks provide an excellent foundation, they are naturally limited to the state of the field at the time they are published.

Because this book is maintained as a living online resource, it is designed to evolve alongside the field itself. New chapters, updated explanations, recent discoveries, and emerging technologies will be incorporated over time, ensuring that readers always have access to material that reflects the current state of quantum computing.






## 2. From Classical Physics to Quantum Mechanics

### 2.1 The Rise of Classical Physics

For centuries, our understanding of the universe was shaped by **Classical Physics**. Its foundations were laid in the seventeenth century, when Isaac Newton introduced a mathematical framework capable of describing the motion of objects with remarkable precision.

Newton's laws of motion and his law of universal gravitation explained phenomena ranging from the fall of an apple to the orbits of the planets. For the first time, nature appeared to obey a small set of elegant mathematical laws.

This success inspired a powerful idea: if we know the current state of a system and the laws governing it, we should be able to predict its future. The universe came to be viewed as a vast deterministic clockwork, where every event followed inevitably from previous conditions.

<!-- ```{figure} /_static/figures/ch1_fig2-1.png
:name: fig-2-1
:alt: Newton's deterministic universe

Newton's deterministic universe. Illustration showing Newton, planetary motion.
``` -->



### 2.2 The Expansion of Classical Physics

Over the next two centuries, classical physics continued to expand. Thermodynamics described heat and energy, while James Clerk Maxwell unified electricity and magnetism into a single theory.

Maxwell's equations not only explained electrical and magnetic phenomena but also revealed that light itself is an electromagnetic wave. This remarkable unification demonstrated that seemingly unrelated natural phenomena could be described by a single mathematical framework.

By the end of the nineteenth century, classical physics had achieved extraordinary success. It accurately described the motion of celestial bodies, the behavior of heat engines, the propagation of light, and countless everyday phenomena.

Many scientists believed that physics was essentially complete, with only a few unresolved questions remaining.

<!-- ```{figure} /_static/figures/ch1_fig2-2.png
:name: fig-2-2
:alt: The triumph of Classical Physics

The triumph of Classical Physics. Illustration combining steam engines, electricity, magnetism, and electromagnetic waves.
``` -->

However, nature still had a few surprises in store.



### 2.3 The First Cracks

Despite its extraordinary success, classical physics could not explain several experimental observations.

At first, these discrepancies appeared to be isolated problems. However, they would eventually reveal that the classical description of nature was fundamentally incomplete.

The first major challenge came from the study of **blackbody radiation**.

According to classical physics, a hot object should emit an infinite amount of energy at very short wavelengths — an impossible prediction known as the **ultraviolet catastrophe**.

Only a few years later, another puzzle emerged: the **photoelectric effect**, where light could eject electrons from a metal surface in ways that classical wave theory failed to explain.

At nearly the same time, physicists struggled to understand why atoms are stable. According to classical electromagnetism, orbiting electrons should continuously lose energy and collapse into the nucleus. Yet atoms clearly exist.

These and other puzzles suggested that something was fundamentally missing from our understanding of nature.

<!-- ```{figure} /_static/figures/ch1_fig2-3.png
:name: fig-2-3
:alt: The limitations of Classical Physics -->

<!-- The limitations of Classical Physics. Timeline highlighting the blackbody radiation problem, the photoelectric effect, and atomic stability.
``` -->



### 2.4 The Birth of Quantum Mechanics

In 1900, Max Planck proposed a bold solution to the blackbody radiation problem [1]. He suggested that energy is exchanged in discrete packets, later called **quanta**. Although introduced as a mathematical assumption, this idea marked the birth of quantum theory.

Only five years later, Albert Einstein extended Planck's hypothesis to explain the photoelectric effect [2], proposing that light itself behaves as if it were composed of individual particles, now known as **photons**.

In 1913, Niels Bohr introduced a new model of the atom in which electrons occupy discrete energy levels [3], providing the first successful explanation for atomic stability.

The revolution continued when Louis de Broglie proposed that matter, like light, also possesses wave-like properties [4]. This surprising idea was later confirmed experimentally and became known as **wave-particle duality**.

Building on these discoveries, Erwin Schrödinger developed the wave equation describing the evolution of quantum systems [5], while Werner Heisenberg introduced matrix mechanics and formulated the uncertainty principle [6]. Finally, Paul Dirac unified many of these ideas into a powerful mathematical framework and developed the notation still widely used today [7].


<!-- ```{figure} /_static/figures/ch1_fig2-4.png
:name: fig-2-4
:alt: Timeline of the birth of Quantum Mechanics -->

<!-- Timeline of the birth of Quantum Mechanics: Planck → Einstein → Bohr → de Broglie → Schrödinger → Heisenberg → Dirac.
``` -->



### 2.5 A New Picture of Reality

Together, these discoveries transformed our understanding of nature.

The universe was no longer viewed as a perfectly predictable clockwork governed solely by classical laws. Instead, it became clear that, at microscopic scales, reality follows principles that differ profoundly from our everyday intuition.

Concepts such as quantization, wave-particle duality, superposition, uncertainty, and probability became fundamental ingredients of the new theory.

Quantum mechanics was not the result of a single discovery or the work of one scientist. It emerged over decades through the contributions of many researchers, forming one of the most successful scientific theories ever developed.

Today, quantum mechanics provides the foundation for countless modern technologies, including lasers, semiconductors, magnetic resonance imaging, atomic clocks, and, ultimately, quantum computing.

<!-- ```{figure} /_static/figures/ch1_fig2-5.png
:name: fig-2-5
:alt: From Classical Physics to Quantum Mechanics

From Classical Physics to Quantum Mechanics.
``` -->

```text
Classical Physics
       │
       ▼
Unexplained Experiments
       │
       ▼
Quantum Theory
       │
       ▼
Quantum Mechanics
       │
       ▼
Modern Quantum Technologies
```







## 3. From Quantum Mechanics to Quantum Computing

### 3.1 Computation Is Physical

The development of quantum mechanics revolutionized our understanding of nature. But for several decades, these discoveries seemed to belong exclusively to physics.

At first glance, quantum mechanics and computation appear to be unrelated fields. One describes the behavior of matter and energy at microscopic scales, while the other focuses on processing information.

In reality, however, computation has always been constrained by the laws of physics.

Every computer, from the earliest mechanical calculators to today's most advanced supercomputers, is ultimately a physical machine. Every stored bit, every electrical signal, and every logical operation is implemented by a physical system obeying the laws of nature.

The first electronic computers were built using vacuum tubes and, later, transistors. Although their architecture evolved dramatically over time, they all relied on the principles of classical physics and classical electronics.

For decades, this distinction hardly mattered. Classical computers were extraordinarily successful, and classical physics provided an accurate description of the devices used to build them.

But a natural question eventually emerged:

```{epigraph}
If nature itself behaves according to the laws of quantum mechanics, shouldn't computation also follow those same laws?
```

This seemingly simple question would give rise to an entirely new model of computation.

<!-- ```{figure} /_static/figures/ch1_fig3-1.png
:name: fig-3-1
:alt: Computation as a physical process

Computation as a physical process. Illustration showing the evolution from mechanical gears to vacuum tubes, transistors, integrated circuits, and finally quantum processors.
``` -->



### 3.2 The Birth of Quantum Computing

The first ideas connecting quantum mechanics and computation appeared in the early 1980s.

In 1980, **Paul Benioff** demonstrated that a computer could, in principle, be described using the mathematical framework of quantum mechanics [8].

Shortly afterward, in 1981, **Richard Feynman** made a profound observation [9]. He argued that simulating quantum systems on classical computers becomes exponentially difficult as the size of the system increases. Since nature itself is quantum mechanical, he proposed building computers that operate according to quantum principles instead.

This idea represented a radical shift in perspective. Rather than forcing classical computers to imitate quantum systems, why not build computers that are quantum from the beginning?

A few years later, in 1985, **David Deutsch** introduced the concept of a universal quantum computer [10], providing the theoretical foundations for a completely new model of computation.

Together, these ideas marked the birth of quantum computing as a scientific discipline.


<!-- ```{figure} /_static/figures/ch1_fig3-2.png
:name: fig-3-2
:alt: The birth of quantum computing

The birth of quantum computing. Timeline: Benioff (1980) → Feynman (1981) → Deutsch (1985).
``` -->






### 3.3 A New Model of Computation

Quantum computers are not simply faster versions of classical computers.

Instead, they process information using the principles of quantum mechanics. Their fundamental unit of information, the **qubit**, behaves according to quantum laws rather than classical ones.

This allows quantum algorithms to exploit phenomena such as superposition, interference, and entanglement to solve certain problems in ways that have no classical counterpart.

It is important to emphasize, however, that quantum computers are **not intended to replace classical computers**. Classical computers remain the best choice for the overwhelming majority of everyday computational tasks.

Instead, quantum computers are specialized devices designed to tackle problems that become prohibitively difficult for classical machines, such as quantum simulation, integer factorization, certain optimization problems, and other computational challenges that arise naturally in science and engineering.

The following chapters will gradually introduce the concepts needed to understand how these remarkable machines work, beginning with the fundamental question:

> **What makes a quantum computer different from a classical one?**

<!-- ```{figure} /_static/figures/ch1_fig3-3.png
:name: fig-3-3
:alt: From Physics to Computation

From Physics to Computation. A conceptual diagram illustrating how new physical principles gave rise to a new model of computation.
``` -->

```text
Classical Physics
         │
         ▼
Classical Computers
         │
         ▼
Quantum Mechanics
         │
         ▼
Quantum Computing
```





## 4. Where Classical Computing Struggles

If quantum computers are based on fundamentally different physical principles, an important question naturally follows:

**Why do we need them?**

The answer is not that classical computers are inadequate. On the contrary, they are among the greatest technological achievements in human history. From smartphones and laptops to satellites and supercomputers, classical computers solve billions of problems every day with extraordinary efficiency.

For the overwhelming majority of computational tasks, classical computers are exactly the right tool.

However, not every problem scales gracefully.

As problems become larger and more complex, the number of possible solutions often grows exponentially. This phenomenon, known as the **combinatorial explosion**, quickly makes many computational tasks intractable, even for the world's most powerful supercomputers.

For some problems, adding more processors or building faster hardware is simply not enough.

This is where quantum computing becomes interesting.

By exploiting the laws of quantum mechanics, quantum computers offer fundamentally different ways of processing information — enabling entirely new approaches to problems that are, for all practical purposes, unreachable by classical computers alone.

The next chapter will make this claim concrete, examining specific problems where quantum computers offer a genuine and measurable advantage.

It is important to keep realistic expectations, however.

`````{important}
Quantum computers are not replacements for classical computers.
`````

They are **specialized computers designed for specific kinds of problems**. Just as graphics processing units (GPUs) complement traditional CPUs rather than replacing them, quantum processors are expected to work alongside classical computers, each being used where it performs best.
<!-- 
`````{figure} /_static/figures/ch1_fig4-1.png
:name: fig-4-1
:alt: Classical vs. Quantum Computing

Classical vs. Quantum Computing. Quantum computers complement rather than replace classical computers.
````-->

```text
Everyday Tasks
         │
         ▼
Classical Computers

Extremely Complex Problems
         │
         ▼
Quantum Computers
```








## 5. Bits and Qubits: A First Look

Every model of computation is built upon a fundamental unit of information.

In classical computing, this unit is the **bit**.

Imagine a coin lying flat on a table. It can only be showing Heads or Tails. This is exactly how a classical bit works — it is strictly a **0** or a **1**. Every piece of digital information — from text and images to videos and  software — is ultimately encoded as long sequences of these discrete, unmoving bits.


```text
Bit

0

1
```

Quantum computers, however, are built from a different unit of information known as the **qubit**, or **quantum bit**.


Unlike a classical bit, a qubit is governed by the laws of quantum mechanics. To understand the difference, imagine taking that same coin and spinning it on the table. While it is spinning, is it Heads or Tails? The answer is neither, and in a way, a continuous blend of both. It exists in a dynamic, intermediate state that carries varying probabilities of landing on 0 or 1 once you finally stop it (measure it).

Because a qubit is not limited to just two rigid states, we need a richer way to describe it. Its state can be represented geometrically as any point on the surface of a sphere, known as the **Bloch Sphere**.

<!-- ```{figure} /_static/figures/ch1_fig5-1.png
:name: fig-5-1
:alt: A classical bit and a qubit

A classical bit and a qubit. Illustration comparing a classical bit (0 or 1) with a qubit represented on the Bloch Sphere.
``` -->

At this stage, there is no need to understand the mathematics behind this representation. The Bloch Sphere simply provides a useful visual map for our "spinning coin."

The mathematical meaning of qubits, quantum states, and the Bloch Sphere will be developed progressively throughout the following chapters.





## 6. How Do Quantum Computers Compute?

Although quantum computers are built upon physical principles that differ fundamentally from those of classical computers, their overall computational workflow is, at first glance, surprisingly similar.

Every computation begins with classical information provided by the user. This information is then encoded into the state of one or more qubits, preparing the quantum system to execute a quantum algorithm.

Next, the quantum processor applies a sequence of operations known as **quantum gates**. Together, these gates form a **quantum circuit**, which evolves the quantum state according to the algorithm being executed.

This is where the fundamental difference from classical computing emerges. While classical logic gates simply transform bits from 0 to 1 (or vice versa), quantum gates modify the **probability amplitudes** of quantum states. Because these amplitudes behave mathematically like waves, they can combine through the phenomenon of **interference**.

A useful analogy is to imagine ripples on the surface of a lake. When two waves meet, they may reinforce one another, producing a larger wave (**constructive interference**), or they may partially or completely cancel each other out (**destructive interference**). During the execution of a quantum algorithm, the probability amplitudes associated with different quantum states evolve in exactly this way.

The central idea behind quantum algorithm design is to carefully arrange quantum gates so that the amplitudes associated with incorrect answers interfere destructively, while those corresponding to the correct answer interfere constructively. In other words, a quantum computer does **not** simply "try every possible answer at the same time." Instead, it engineers the evolution of the quantum state so that measuring the correct answer becomes much more likely.

Finally, the qubits are **measured**. Measurement converts the quantum information into classical information, producing a string of bits that can be interpreted by the user. Because quantum measurement is inherently probabilistic, a single execution may not reveal the correct answer with complete certainty. For this reason, many quantum algorithms are executed multiple times (called **shots**), allowing the correct result to be inferred from the distribution of measurement outcomes.

```text
        Classical Input
               │
               ▼
      Encode into Qubits
               │
               ▼
        Quantum Circuit
        (Quantum Gates)
               │
               ▼
         Measurement
               │
               ▼
       Classical Output
```

At first glance, this workflow may appear straightforward. However, each stage relies on concepts that have no classical counterpart. Understanding how information is encoded, manipulated, and measured in a quantum system is the key to understanding why quantum computers can solve certain problems more efficiently than classical computers.

In the following chapters, we will explore each stage of this workflow in detail, beginning with the fundamental unit of quantum information: the **qubit**.


<!-- 
```{figure} /_static/figures/ch1_fig6-1.png
:name: fig-6-1
:alt: The quantum computation workflow

The quantum computation workflow.
``` -->






## 7. What You Will Learn

This book is designed to build your understanding progressively.

Rather than assuming prior knowledge of quantum mechanics or advanced mathematics, we will introduce each concept exactly when it becomes necessary, always moving from intuition toward formalism — never the other way around.

To keep this progression easy to navigate, the book is organized into six parts. Each part groups a set of closely related chapters around a single guiding question.

| Part | Guiding Question | Topics Covered |
|------|-------------------|-----------------|
| **I. Motivation** | Why does quantum computing matter? | Why Quantum Computing? |
| **II. Mathematical Foundations** | What language do we need to describe quantum states? | Linear Algebra · Complex Numbers · Vector Spaces · Dirac Notation |
| **III. Quantum Information** | What is a qubit, and how does it differ from a bit? | Classical Bits · Qubits · Bloch Sphere · Quantum Gates |
| **IV. Multi-Qubit Systems** | What happens when qubits interact? | Multiple Qubits · Tensor Products · Entanglement · Measurement · Quantum Circuits · No-Cloning Theorem |
| **V. Quantum Algorithms** | How do quantum computers gain an advantage? | Computational Theory · Algorithm Analysis · Grover's Algorithm · Deutsch–Jozsa · Quantum Fourier Transform · Shor's Algorithm |
| **VI. Quantum Applications** | Where is this heading? | Quantum Optimization · Variational Quantum Algorithms · Quantum Machine Learning · Quantum Neural Networks |

At a high level, this progression looks as follows:

```text
Motivation → Mathematics → Quantum Information → Multi-Qubit Systems → Algorithms → Applications
```

Each part builds strictly on the ones before it: the mathematics introduced in Part II is what makes qubits (Part III) precise; qubits are what make entanglement and circuits (Part IV) meaningful; and only once circuits are understood do algorithms (Part V) and their applications (Part VI) start to make real sense.

```{note}
This structure is a **map**, not a strict contract — some chapters may be reordered or expanded as the book evolves, but the overall logic (concept before formalism, formalism before algorithm) will remain the guiding principle throughout.
```







## 8. Prerequisites

One of the goals of this book is to make quantum computing accessible to readers from different backgrounds.

You do **not** need prior knowledge of quantum mechanics to follow the material.

Likewise, the mathematical concepts required throughout the book — including linear algebra, complex numbers, and vector spaces — will be introduced progressively as they become relevant.

A basic familiarity with high school mathematics and elementary programming concepts will be helpful, but curiosity and willingness to learn are far more important than prior expertise.






## 9. Final Thoughts

Quantum computing challenges many of the intuitions we develop from everyday life.

Concepts such as **superposition**, **interference**, and **entanglement** may initially seem strange or even counterintuitive. Yet these ideas emerge naturally from the mathematical framework of quantum mechanics and have been confirmed by decades of experimental evidence.

Throughout this book, our goal is not merely to present equations or describe algorithms. Instead, we aim to develop an intuitive understanding of why quantum computing works, how its mathematical foundations arise, and what makes it fundamentally different from classical computation.

Learning quantum computing is not simply about mastering a new technology — it is about discovering a new way of thinking about information, computation, and the physical world.

Welcome to the beginning of that journey.


---

## References

[1] Planck, M. (1900). Zur Theorie des Gesetzes der Energieverteilung im Normalspectrum. *Verhandlungen der Deutschen Physikalischen Gesellschaft*, 2, 237–245.

[2] Einstein, A. (1905). Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt. *Annalen der Physik*, 322(6), 132–148.

[3] Bohr, N. (1913). On the constitution of atoms and molecules. *Philosophical Magazine*, 26(151), 1–25.

[4] de Broglie, L. (1924). *Recherches sur la théorie des quanta* (Doctoral dissertation, Sorbonne University, Paris).

[5] Schrödinger, E. (1926). Quantisierung als Eigenwertproblem. *Annalen der Physik*, 384(4), 361–376.

[6] Heisenberg, W. (1927). Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik. *Zeitschrift für Physik*, 43(3–4), 172–198.

[7] Dirac, P. A. M. (1930). *The Principles of Quantum Mechanics*. Oxford University Press.

[8] Benioff, P. (1980). The computer as a physical system: A microscopic quantum mechanical Hamiltonian model of computers as represented by Turing machines. *Journal of Statistical Physics*, 22(5), 563–591.

[9] Feynman, R. P. (1982). Simulating physics with computers. *International Journal of Theoretical Physics*, 21(6–7), 467–488.

[10] Deutsch, D. (1985). Quantum theory, the Church-Turing principle and the universal quantum computer. *Proceedings of the Royal Society of London A*, 400(1818), 97–117.