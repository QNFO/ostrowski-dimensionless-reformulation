# MathJax-SVG Pipeline Stress Test — Edge Cases & Failure Modes

Purpose: prove the MathJax-SVG → CDP print pipeline renders EVERYTHING a
physics paper can throw at it, professionally, every time.

## 1. Long Display Equations (overflow risk)

The Einstein field equations in Planck units:

$$
R_{\mu\nu} - \frac{1}{2}R\,g_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi T_{\mu\nu}
$$

A very long inline equation inside a sentence: the dimensionless
Schrödinger equation $i\hbar\frac{\partial\psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\psi + V\psi$ must
render inline without breaking the line into garbage.

A long aligned multi-line derivation:

$$
\begin{aligned}
\tilde{F} &= \frac{\tilde{q}_1\tilde{q}_2}{\tilde{r}^2} = \frac{\alpha}{\tilde{r}^2} \\
\tilde{F}_{ee} &= \frac{\alpha}{\tilde{r}^2} = \frac{1}{137.036\,\tilde{r}^2}
\end{aligned}
$$

## 2. Matrices

$$
M = \begin{pmatrix} m_e & 0 & 0 \\ 0 & m_\mu & 0 \\ 0 & 0 & m_\tau \end{pmatrix}, \qquad
\mathbf{v}(\tilde{m}) = \begin{pmatrix} v_2 \\ v_3 \\ v_5 \end{pmatrix}
$$

## 3. Large delimiters / cases

$$
f(x) = \begin{cases} x^2 & x \geq 0 \\ -x^2 & x < 0 \end{cases}, \qquad
\left\langle \psi \middle| \hat{H} \middle| \psi \right\rangle = \sum_n E_n |c_n|^2
$$

## 4. Sums, integrals, products with limits

$$
Z(\beta) = \sum_{n=0}^{\infty} e^{-\beta E_n}, \qquad
\int_0^{\infty} x^{s-1} e^{-x} dx = \Gamma(s), \qquad
\prod_{p \leq \infty} \alpha_p^{-1} = \frac{1}{\alpha}
$$

## 5. Math inside tables

| Quantity | Dimensional | Dimensionless | Notes |
|:---------|:------------|:--------------|:------|
| Action $S$ | $[ML^2T^{-1}]$ | $\tilde{S} = S/\hbar$ | $\hbar = 1$ |
| Entropy $S$ | $[ML^2T^{-2}K^{-1}]$ | $\tilde{S}_{BH} = A/4$ | Bekenstein |
| Temp $T$ | $[K]$ | $\tilde{T} = T/T_P$ | $T_P = \sqrt{\hbar c^5/Gk_B^2}$ |

## 6. Headings with math

### The fine-structure constant $\alpha = e^2/4\pi\epsilon_0\hbar c$

Section content discussing $\alpha \approx 1/137.036$ as a cross-ratio.

## 7. Unicode math in PROSE (the old font-fallback killer)

The p-adic absolute value $|\cdot|_p$ notation, the adele ring $\mathbb{A}_{\mathbb{Q}}$,
Planck's constant ℏ, the rationals ℚ, reals ℝ, integers ℤ, complex ℂ,
and approximate equality ≈, proportional ∝, less-or-equal ≤, greater-or-equal ≥,
times ×, minus −, superscripts 10⁻³⁴ m³ s⁻², subscripts ℚ₃ ℚ₅ x₁ x₂,
Greek α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ σ τ υ φ χ ψ ω, ℓ, ∂, ∇, ∞, ∑, ∏, ∫.

## 8. Code blocks (long lines, overflow)

```python
def hensel_code(x, primes=[2, 3, 5, 7, 11]):
    """Compute the Hensel code of rational x — this line is intentionally long to test overflow wrapping."""
    return tuple(x % p**3 for p in primes)  # very long comment about modulo prime powers exceeding tolerance
```

## 9. Blockquote with math

> The reformulation does not change the physics. It makes explicit the
> place-democracy that dimensional formulations conceal: $\tilde{m} = \tilde{\omega}$
> holds at every completion of $\mathbb{Q}$ per Ostrowski's theorem (1916).

## 10. Nested lists with math

1. First-level item with $E = mc^2$
   - Nested item: $\lambda_C = \hbar/mc$
     - Deeper: $\alpha = r_e/\lambda_C$
2. Second item with display math
   $$\tilde{S} = \frac{A}{4} = 4\pi\tilde{M}^2$$

## 11. Multi-page table (header repetition)

| # | Formula | Dimensionless | Domain |
|:--|:--------|:--------------|:-------|
| 1 | $E = \hbar\omega$ | $\tilde{E} = \tilde{\omega}$ | QM |
| 2 | $p = \hbar k$ | $\tilde{p} = \tilde{k}$ | QM |
| 3 | $F = ma$ | $\tilde{F} = \tilde{m}\tilde{a}$ | CM |
| 4 | $E = mc^2$ | $\tilde{E} = \tilde{m}$ | SR |
| 5 | $F = G m_1 m_2/r^2$ | $\tilde{F} = \tilde{m}_1\tilde{m}_2/\tilde{r}^2$ | GR |
| 6 | $S = k_B \ln\Omega$ | $\tilde{S} = \ln\Omega$ | Thermo |
| 7 | $E = k_B T$ | $\tilde{E} = \tilde{T}$ | Thermo |
| 8 | $E = h\nu$ | $\tilde{E} = 2\pi\tilde{\nu}$ | QM |
| 9 | $\Delta x\Delta p \geq \hbar/2$ | $\Delta\tilde{x}\Delta\tilde{p} \geq 1/2$ | QM |
| 10 | $V = -Gm/r$ | $\tilde{V} = -\tilde{m}/\tilde{r}$ | GR |
| 11 | $\rho = m/V$ | $\tilde{\rho} = \tilde{m}/\tilde{V}$ | CM |
| 12 | $P = F/A$ | $\tilde{P} = \tilde{F}/\tilde{A}$ | CM |
| 13 | $W = Fd$ | $\tilde{W} = \tilde{F}\tilde{d}$ | CM |
| 14 | $KE = \frac{1}{2}mv^2$ | $\tilde{KE} = \frac{1}{2}\tilde{m}\tilde{v}^2$ | CM |
| 15 | $PE = mgh$ | $\tilde{PE} = \tilde{m}\tilde{g}\tilde{h}$ | CM |
| 16 | $p = mv$ | $\tilde{p} = \tilde{m}\tilde{v}$ | CM |
| 17 | $F = qE$ | $\tilde{F} = \tilde{q}\tilde{E}$ | EM |
| 18 | $E = qV$ | $\tilde{E} = \tilde{q}\tilde{V}$ | EM |
| 19 | $c = \lambda\nu$ | $\tilde{c} = \tilde{\lambda}\tilde{\nu} = 1$ | EM |
| 20 | $T_H = \hbar c^3/8\pi G k_B M$ | $\tilde{T}_H = 1/8\pi\tilde{M}$ | BH |

## 12. Malformed math (resilience)

This should NOT crash the page: $E = \frac{1}{2}mv^2$ is fine but
$\int_0^\infty$ without closing brace and $\begin{aligned} broken should render as red error or skip, never break layout.

## 13. Special characters in text

Ampersand & less-than < greater-than > quotes "quoted" 'single' — these must
be HTML-escaped correctly, with math $a < b$ and $x > y$ and $\&$ symbols.

## 14. Consecutive display equations

$$
\tilde{E} = \tilde{\omega}
$$

$$
\tilde{p} = \tilde{k}
$$

$$
\tilde{m} = \tilde{\omega}
$$

## 15. Very deep heading levels

#### Level 4 heading
##### Level 5 heading

## 16. Links and DOIs

See DOI: 10.5281/zenodo.21749884 (concept) and
[the GitHub repository](https://github.com/QNFO/ostrowski-dimensionless-reformulation).

## 17. Long unbreakable tokens

The URL https://papers.qnfo.org/papers/ostrowski-dimensionless-reformulation/ is long
and should wrap or be contained. Also thisverylongunbreakablewordabcdefghijklmnopqrstuvwxyz0123456789 repeated should not overflow the page.

## 18. Fractions and radicals nested

$$
\tilde{\rho} = \frac{3\tilde{H}^2}{8\pi\tilde{G}}, \qquad
\sqrt{\frac{\tilde{\ell}_P^2}{\tilde{t}_P^2}} = 1, \qquad
e^{i\pi} + 1 = 0
$$

## 19. Empty math and edge tokens

Empty: $ $ and $$ $$ should not produce blank artifacts or errors.

## 20. Final mixed-content paragraph

The Bruhat–Tits tree $\mathcal{T}_p$ has $(p+1)$-valent vertices, the adelic
product $\mathbb{A}_{\mathbb{Q}} = \prod_p' \mathbb{Q}_p \times \mathbb{R}$
is locally compact, and the Tate thesis yields $\zeta$-functional equations —
all rendered professionally with STIX Two Text, page numbers, and no glyph fallback.
