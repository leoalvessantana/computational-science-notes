# Chapter 2 — Why Quantum Computing?

## 1. The Cost of Simulating Nature

In the previous chapter, we mentioned Richard Feynman's key observation: simulating quantum systems on classical computers becomes exponentially difficult as the system grows [1]. It's time to understand exactly what that means — and why it matters so much.

When physicists want to simulate a quantum system — a molecule, a material, a chemical reaction — they need to describe its full quantum state. Classically, this means storing a list of numbers (called *amplitudes*) that describe every possible configuration the system could be in.

The problem is that the number of these configurations doesn't grow linearly with the size of the system. It grows **exponentially**.

<!-- ```{figure} /_static/figures/ch2_fig1-1.png
:name: fig-ch2-1-1
:alt: Linear vs exponential growth

Linear growth vs exponential growth as system size increases.
````-->

A single particle with two possible states requires storing 2 numbers. Two particles require 4. Three particles require 8. This is not a coincidence — for *n* particles, classical simulation requires storing **2ⁿ** numbers.

```text
n particles  →  2ⁿ numbers to store

 1 particle  →            2
 2 particles →            4
 3 particles →            8
10 particles →         1,024
20 particles →     1,048,576
```

For small systems, this is manageable. But this exponential growth escalates far faster than most people's intuition expects.





## 2. Exponential State Spaces: A Concrete Look

Let's push this further, because the numbers involved are genuinely staggering.

To classically store the full quantum state of just **50 particles**, you would need to store roughly **2⁵⁰ ≈ 1.13 × 10¹⁵** numbers. Each number typically requires a few bytes of memory — so this quickly reaches into the petabytes.

Now push to **300 particles**. The number of amplitudes required, **2³⁰⁰**, exceeds most physical estimates of the number of atoms in the observable universe.

```{note}
This is not a limitation of current technology — it is a fundamental mathematical barrier. No amount of engineering improvement, faster processors, or additional storage will ever be enough to overcome exponential growth of this scale.
```

This is precisely the wall Feynman identified: classical computers are, in principle, unable to simulate even modestly sized quantum systems efficiently [1]. If nature routinely performs these "computations" through the ordinary behavior of atoms and molecules, then a computer built from quantum components — one that operates *natively* using these same principles — should be able to represent such states without needing to enumerate every configuration explicitly.

This isn't merely a faster way of doing the same thing classical computers do. It's a fundamentally different strategy for representing information.




## 3. Computational Complexity: P, NP, and Beyond

To understand where quantum computers genuinely help — and where they don't — it's useful to introduce, at an intuitive level, how computer scientists classify the difficulty of problems.

Some problems can be solved efficiently, meaning the time required grows reasonably (polynomially) as the input grows. These form a class called **P** (Polynomial time).

Other problems are much harder to *solve*, but easy to *verify* once a candidate solution is given. These form a class called **NP**.

```text
P   → Problems that can be *solved* efficiently
NP  → Problems that can be *verified* efficiently
```

A famous open question in computer science — whether P equals NP — remains unresolved and is beyond the scope of this book. What matters here is a related, more specific question: **where do quantum computers fit into this picture?**

Quantum computers are believed to efficiently solve a class of problems called **BQP** (Bounded-error Quantum Polynomial time). Some problems inside BQP are believed to sit *outside* of P — meaning no known classical algorithm can solve them efficiently, but a quantum computer can.

```{important}
Quantum computers are not believed to solve NP-complete problems efficiently in general. The advantage they offer is real, but narrower and more specific than science fiction often suggests.
```

This distinction matters. Quantum computing is not a magic wand that dissolves all computational difficulty — it's a precise tool that changes the rules for a specific, well-defined set of problems.





## 4. Where Quantum Computers Provide an Advantage

With this framing in place, we can now be concrete about where quantum advantage actually shows up.

**Grover's Algorithm** [2] is traditionally introduced as a method for searching an unsorted database containing *N* items. Classically, finding a specific item requires checking up to *N* entries one by one. Grover's algorithm reduces this to approximately *√N* queries, providing a quadratic speedup.

However, it is important to understand how this speedup is achieved. A common misconception is that a quantum computer simply checks every item simultaneously. It does not. Instead, Grover's algorithm exploits the principle of **quantum interference** introduced in the previous section. One way to visualize this process is to imagine an audio mixing console: over a sequence of carefully designed operations, the algorithm gradually "turns up the volume" (increases the probability amplitude) of the correct answer while "turning down the volume" of the incorrect ones.

```text
Classical search:  up to N steps
Grover's search:   about √N steps
```


For a database containing one million items, this corresponds to reducing roughly one million search steps to only about one thousand.

Another landmark example is **Shor's Algorithm** [3], which addresses the problem of integer factorization—the task of decomposing a large integer into its prime factors. This problem forms the foundation of much of modern public-key cryptography because the best known classical algorithms become prohibitively expensive as the numbers grow larger.

Shor's algorithm provides a polynomial-time algorithm for integer factorization, representing a dramatic asymptotic speedup over the best known classical algorithms. This result is the primary reason quantum computing has attracted so much attention from the fields of cryptography and cybersecurity.

Beyond search and factoring, quantum computers are expected to be useful in several other areas, including:

- **Quantum simulation** — the original motivation discussed earlier in this chapter, allowing quantum systems to simulate other quantum systems efficiently [1].
- **Combinatorial optimization**, through algorithms that will be introduced later in this book.
- **Certain machine learning tasks**, an active and rapidly evolving area of research.

These algorithms and applications will be revisited later in the book, once we have developed the mathematical tools needed to understand how they work.



## 5. Honest Limitations: What Quantum Computers Cannot Do (Yet)

It would be misleading to conclude this chapter without discussing the current limitations of quantum hardware.

Today's quantum computers operate in what is commonly known as the **NISQ era** (*Noisy Intermediate-Scale Quantum*), a term introduced by physicist John Preskill in 2018 [4]. The name highlights two fundamental characteristics of today's devices:

- **Noisy:** qubits are extremely fragile. Interactions with the surrounding environment—such as heat, electromagnetic fields, or even microscopic vibrations—cause **decoherence**, gradually destroying the quantum information before a computation can be completed.

- **Intermediate-scale:** although today's processors range from tens to over one thousand physical qubits [5], this is still far below the millions of physical qubits that are expected to be required for large-scale, fault-tolerant quantum computation.

```{note}
Fault-tolerant quantum computers—the kind capable of running algorithms such as Shor's algorithm on cryptographically relevant numbers—will likely require millions of physical qubits protected by quantum error correction. Achieving this remains one of the greatest engineering challenges in the field.
```

This naturally raises an important question:

**If fault-tolerant quantum computers do not yet exist, are today's quantum processors actually useful?**

The answer is **yes**.

To make practical use of current hardware, researchers have developed **Variational Quantum Algorithms (VQAs)**, including the **Variational Quantum Eigensolver (VQE)** and the **Quantum Approximate Optimization Algorithm (QAOA)**.

These algorithms adopt a **hybrid quantum-classical approach**. Rather than asking a fragile quantum processor to execute a long and complex computation on its own, the work is divided between two machines. A classical computer performs the optimization of the algorithm's parameters, while the quantum processor acts as a specialized coprocessor, evaluating quantum circuits that would be computationally expensive to simulate classically.

Because the quantum circuits remain relatively short, the computation is much less vulnerable to decoherence. This hybrid strategy currently represents one of the most promising directions for near-term quantum computing and has become one of the central research topics in the NISQ era.

It is important to keep this distinction in mind. The algorithms presented in the previous section are mathematically proven to provide quantum speedups, but the large-scale fault-tolerant hardware required to realize their full potential has not yet been built. Until then, hybrid quantum-classical algorithms provide a practical way to extract meaningful computational value from today's quantum processors.

Given their practical importance, we will revisit these hybrid approaches later in the book. We will explore the underlying theory first, and then learn how to implement these algorithms step by step using modern quantum programming frameworks.


## 6. Setting Expectations for the Rest of This Book

By now, the motivation should be clear: quantum computers are not faster classical computers, nor a universal solution to every computational problem. They are specialized machines that offer genuine, mathematically grounded advantages for a specific — but important — class of problems, chief among them quantum simulation, integer factorization, and unstructured search.

Understanding *why* they can do this requires understanding *how* quantum information is represented and manipulated — which is exactly where this book turns next.

The next chapters will build, piece by piece, the mathematical language needed to describe qubits precisely — starting with the linear algebra that underlies all of quantum mechanics.

---

## References

[1] Feynman, R. P. (1982). Simulating physics with computers. *International Journal of Theoretical Physics*, 21(6-7), 467–488.

[2] Grover, L. K. (1996). A fast quantum mechanical algorithm for database search. *Proceedings of the 28th Annual ACM Symposium on the Theory of Computing (STOC)*, 212–219. arXiv:quant-ph/9605043.

[3] Shor, P. W. (1997). Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer. *SIAM Journal on Computing*, 26(5), 1484–1509. arXiv:quant-ph/9508027.

[4] Preskill, J. (2018). Quantum computing in the NISQ era and beyond. *Quantum*, 2, 79. arXiv:1801.00862.

[5] Wikipedia contributors. Noisy intermediate-scale quantum computing. *Wikipedia, The Free Encyclopedia*. Retrieved July 2026.
````
