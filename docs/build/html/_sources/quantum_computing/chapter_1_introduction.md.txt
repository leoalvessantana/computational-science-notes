# Chapter 1: Introduction to Quantum Computing

---

## 1. Motivation

Classical computers have transformed the modern world, but they still struggle with certain types of problems such as:

- Simulating quantum systems
- Factoring large numbers efficiently
- Searching unstructured databases at scale

Quantum computing emerges as a new computational paradigm that leverages the principles of quantum mechanics to process information in fundamentally different ways.

---

## 2. Intuition

In classical computing, the basic unit of information is a **bit**, which can be either:

- 0
- 1

In quantum computing, the basic unit is a **qubit**, which behaves differently.

A qubit is not limited to being just 0 or 1. Instead, it can exist in a **superposition** of both states at the same time.

A helpful intuition is:

> A classical bit is like a coin lying on a table (heads or tails).
> A qubit is like a spinning coin — not yet decided.

However, when we measure a qubit, we always get a classical result: 0 or 1.

---

## 3. Mathematical Formulation

A classical bit is represented as:

- 0
- 1

A qubit is represented as a linear combination of basis states:

\[
|\psi\rangle = \alpha |0\rangle + \beta |1\rangle
\]

where:

- \( \alpha \) and \( \beta \) are complex numbers
- \( |\alpha|^2 \) is the probability of measuring 0
- \( |\beta|^2 \) is the probability of measuring 1

Normalization condition:

\[
|\alpha|^2 + |\beta|^2 = 1
\]

This ensures that total probability is always 1.

---

## 4. Visualization

We can visualize a qubit using the **Bloch Sphere** representation.

- The north pole corresponds to |0⟩
- The south pole corresponds to |1⟩
- Any point on the sphere surface represents a valid qubit state

This geometric interpretation helps us understand quantum operations as rotations on a sphere.

---

## 5. Python Example

We can simulate a simple qubit using NumPy.

```python
import numpy as np

# define amplitudes
alpha = 1/np.sqrt(2)
beta = 1/np.sqrt(2)

# probabilities
p0 = abs(alpha)**2
p1 = abs(beta)**2

print("Probability of 0:", p0)
print("Probability of 1:", p1)