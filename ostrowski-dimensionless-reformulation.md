---
title: "The Ostrowski Dimensionless Reformulation: A Systematic Compilation of Fundamental Physics Equations in Planck Units"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-01"
license: "QNFO Unified License Agreement (QNFO-ULA)"
doi: "10.5281/zenodo.21750381"
status: "published"
---

**Author:** Rowan Brad Quni-Gudzinas | **Date:** 2026-08-01 | **License:** QNFO-ULA: https://legal.qnfo.org/

## Abstract

We present a systematic compilation and dimensionless reformulation of 53 fundamental physics equations across ten disciplines, motivated by the Ostrowski Dimensionless Mandate (qnfo-core §0.7). Dimensional formulations of physical laws -- those containing explicit occurrences of ℏ, c, G, k_B, or ε₀ -- implicitly privilege the Archimedean ($\infty$) completion of the rational numbers. Per Ostrowski's theorem (1916), every non-trivial absolute value on ℚ is equivalent either to the real Archimedean place or to a p-adic non-Archimedean place. A dimensional formula can only be evaluated at the Archimedean place because its constants' specific numerical values have no meaning in p-adic completions. By expressing all quantities as pure-number ratios to their Planck-scale counterparts (with ℏ = c = G = k_B = 1), each formula becomes a relation among dimensionless numbers that is equally well-defined at every place. We provide detailed derivations for 26 multi-constant formulas (Class F: those containing combinations of ℏ, c, G, k_B), mathematical proofs of the dimensional-dimensionless correspondence via the Buckingham Pi theorem, and Ostrowski rationales for each physical domain. No physical content is lost: the dimensional homogeneity of physical laws guarantees that the constants can always be absorbed into dimensionless ratios. The reformulation does not change the physics -- it makes explicit the place-democracy that dimensional formalisms conceal.

## 1 Introduction

### 1.1 The Ostrowski Dimensionless Mandate

The Ostrowski Dimensionless Mandate (qnfo-core §0.7, effective 2026-08-01) requires that all physics formulas in QNFO publications be expressed in dimensionless natural numbers using Planck units (ℏ = c = G = k_B = 1). The mandate is grounded in Ostrowski's theorem (1916), which classifies every non-trivial absolute value on ℚ as equivalent either to the standard real absolute value |·|_$\infty$ or to a p-adic absolute value |·|_p for some prime p `[established -- Ostrowski, 1916, Acta Mathematica 41:271-284]`.

A physical quantity expressed as a real number implicitly selects the Archimedean place among all completions of ℚ. If a formula contains dimensional constants such as ℏ, c, G, or k_B, it assumes the quantities being related have well-defined real-number values. The constants' specific numerical values -- ℏ ≈ 1.054571817 × 10⁻³⁴ J·s, c = 299792458 m/s, G ≈ 6.67430 × 10⁻¹¹ m³/(kg·s²), k_B ≈ 1.380649 × 10⁻²³ J/K -- are defined only in the Archimedean topology. They have no counterpart in a p-adic completion of ℚ. A formula that embeds these constants is therefore Archimedean-privileging: it can be evaluated at |·|_$\infty$ but not at |·|_p.

The dimensionless solution expresses every physical quantity as a pure-number ratio to its Planck-scale counterpart. A pure number -- an element of ℚ or a limit thereof -- is equally well-defined at every place. Thus a dimensionless formula holds for all completions simultaneously.

### 1.2 Precedent Work

Three prior QNFO publications established the dimensionless program, with a fourth providing the canonical physical interpretation of what the dimensionless convention achieves:

- **Mass-Frequency Identity v3.2.0** (DOI: 10.5281/zenodo.21360549, 2026-07-14): the identity m = omega emerges directly from setting hbar = c = 1 (since m = E/c^2 and E = hbar omega, so m_tilde = omega_tilde in Planck units). This paper provides the physical interpretation of what ODR achieves for 53 formulas — the mass-frequency identity is the canonical example of the dimensionless program's claim that dimensional constants conceal pure-number relationships. `[established]`

Two prior QNFO publications established the dimensionless program:

- **Non-Anthropocentric Natural Units** (DOI: 10.5281/zenodo.21480756) reformulated the Bekenstein-Hawking entropy bound without anthropocentric units, introducing the dimensionless horizon area and Ostrowski's theorem as a challenge to the Archimedean assumption. `[established]`

- **OC Paper v1.2** (DOI: 10.5281/zenodo.21748773) reformulated the Bekenstein bound in dimensionless Planck units: S ≤ 2π k_B R E/(ℏc) $\rightarrow$ I ≤ 2π R E/ln 2. **OC Paper v1.3** (DOI: 10.5281/zenodo.21749177) reformulated Landauer's principle presenting both conventional dimensional form (E ≥ k_B T ln 2) and dimensionless Planck-unit form (E ≥ T ln 2) with explicit Ostrowski rationale. `[established]`

This paper extends the program to a systematic survey across ten physical disciplines.

**Relationship to the Dimensionless Physics Framework (v1.3.1, DOI: 10.5281/zenodo.21206291, 2026-07-05):** A parallel QNFO project, "Dimensionless Physics: A Unified Framework," addresses the same core problem from a complementary perspective. Where the Dimensionless Physics Framework provides a unified conceptual architecture, ODR provides the systematic formula-level inventory — the detailed algebraic derivations that operationalize the framework's principles for 53 specific equations. The two projects are mutually reinforcing: the Framework supplies the conceptual scaffolding; ODR supplies the formula-specific evidence base. `[established]`

**Cross-domain Ostrowski application:** The paper "When Will Non-Archimedean Geometry Displace the Real Numbers? A Structured Assessment of the Adelic Substrate Thesis" (DOI: 10.5281/zenodo.21747228, 2026-08-01) independently applies the Ostrowski framework to assess the adelic substrate thesis — directly corroborating ODR's central argument that the dimensional/Archimedean formalism is a convention, not a necessity. `[established]`

**Bruhat-Tits mass-frequency correspondence:** "The Adelic Cross-Domain Program: From the Fine-Structure Constant to the Standard Model Mass Spectrum via Bruhat-Tits Trees" (DOI: 10.5281/zenodo.21736300, 2026-08-01) extends the mass-frequency identity to the Standard Model mass spectrum via p-adic infrastructure — demonstrating that the dimensionless reformulation's implications reach beyond unit normalization into predictive physics. `[established]`

### 1.3 Scope and Classification

We classify 53 fundamental physics equations into seven formula classes based on which dimensional constants they contain:

| Class | Constants | Count | Example |
|:------|:----------|:------|:--------|
| A | ℏ only | 8 | Schroedinger equation, Heisenberg uncertainty |
| B | c only | 3 | Horizon scale, Alfven speed |
| C | G only | 4 | Schwarzschild radius, Friedmann equations |
| D | k_B only | 4 | Boltzmann entropy, ideal gas law |
| E | ε₀/μ₀ only | 1 | Coulomb's law (SI) |
| F | Combinations | 26 | Planck law, Einstein field equations, Hawking temperature |
| G | Already dimensionless | 7 | Fine-structure constant, Reynolds number, Holevo bound |

The ten disciplines surveyed are: Quantum Mechanics, Thermodynamics & Statistical Mechanics, General Relativity & Gravitation, Quantum Field Theory, Cosmology, Electromagnetism, Atomic/Nuclear/Particle Physics, Condensed Matter Physics, Quantum Information, and Fluid Dynamics & Plasma Physics.

## 2 Mathematical Foundation

### 2.1 Ostrowski's Theorem and Place-Democracy

**Theorem (Ostrowski, 1916):** Every non-trivial absolute value on ℚ is equivalent either to the standard real absolute value |·|_$\infty$ or to a p-adic absolute value |·|_p for some prime p. `[established]`

**Proof sketch:** Let |·| be a non-trivial absolute value on ℚ. The classification hinges on whether |n| is bounded for integers n. If |n| is unbounded (Archimedean case), then |·| is equivalent to |·|_$\infty$. If |n| ≤ 1 for all integers (non-Archimedean case), the set {n : |n| < 1} is a prime ideal pℤ, yielding |·|_p. The proof is exhaustive: there are exactly these two families, with no intermediate cases. `[established -- standard valuation theory]`

A physical formula containing dimensional constants can be evaluated only at |·|_$\infty$. The specific numerical value of ℏ, for instance, is a real number. In a p-adic completion, the real number 1.054571817... × 10⁻³⁴ has no well-defined meaning because p-adic numbers arise from a different metric: |p^n · a/b|_p = p⁻ⁿ for $p \nmid a, b$. The conversion factor between SI units and Planck units -- the numerical value of ℏ -- is an Archimedean artifact.

In contrast, a dimensionless equation containing only pure numbers can be evaluated at any place. The equation $\tilde{S}$_BH = A/4 (Bekenstein-Hawking) is a relation among pure numbers: if A is a pure number (area in Planck units), then $\tilde{S}$_BH is equally A/4 regardless of whether one computes |A|_$\infty$ or |A|_p. The formula is place-democratic.

**The special case of pi:** The paradigmatic dimensionless number -- the circumference-to-diameter ratio -- illustrates the same principle. pi as the real number 3.14159... exists only at the Archimedean place; its decimal expansion has no p-adic meaning. But pi AS A RATIO (C/d) is definable in any geometry, and this ratio is the place-democratic invariant per the Scaffolds and Invariants paper (DOI: 10.5281/zenodo.21255344). The parallel to physical constants is exact: hbar as the specific number 1.054571817... x 10^{-34} is an Archimedean artifact; hbar as the quantization ratio relating energy to frequency is the place-democratic invariant that survives in any completion.

### 2.2 The Dimensional-Dimensionless Correspondence Theorem

**Theorem:** Let F(x₁, ..., x_n; ℏ, c, G, k_B) = 0 be a dimensionally homogeneous physical law. Then there exists an equivalent dimensionless equation $\tilde{F}$($\tilde{x}$₁, ..., $\tilde{x}$_n) = 0 where $\tilde{x}$_i = x_i/x_i^(P) and x_i^(P) is the Planck-scale counterpart of quantity x_i, such that $\tilde{F}$ contains no dimensional constants.

**Proof:** By the Buckingham Pi theorem, any dimensionally homogeneous equation among n physical quantities involving k independent physical dimensions can be rewritten as a relation among n - k dimensionless Pi groups. The Planck system (ℏ, c, G, k_B) provides exactly four dimensionally independent quantities, spanning the physical dimensions of mass (M), length (L), time (T), and temperature (Θ). Every physical quantity has a unique combination of ℏ, c, G, k_B that yields its physical dimension -- this combination is precisely the Planck-scale counterpart x_i^(P). The dimensionless ratio $\tilde{x}$_i = x_i/x_i^(P) is therefore always well-defined. Substituting x_i = $\tilde{x}$_i · x_i^(P) into the original equation F = 0, all factors of ℏ, c, G, k_B cancel by dimensional homogeneity, leaving $\tilde{F}$ = 0. `[established -- dimensional analysis]`

**Corollary:** No physical content is lost in the reformulation. The dimensional constants are carriers of unit-scale information, not of physical law. Their specific numerical values reflect the meter-kilogram-second-kelvin convention, not properties of nature.

## 3 Systematic Reformulation

We present selected reformulations organized by discipline. The complete inventory of 53 formulas is available in the supplementary artifact `artifacts/formula-inventory.md`.

### 3.1 Quantum Mechanics

**Schroedinger Equation (Class A):**

In conventional dimensional form:
$$i\hbar \frac{\partial\psi}{\partial t} = \left(-\frac{\hbar^2}{2m}\nabla^2 + V\right)\psi$$

In dimensionless Planck units (ℏ = c = G = k_B = 1):
$$i\frac{\partial\psi}{\partial\tilde{t}} = \left(-\frac{1}{2\tilde{m}}\tilde{\nabla}^2 + \tilde{V}\right)\psi$$

where $\tilde{t}$ = t/t_P, $\tilde{m}$ = m/m_P, $\tilde{∇}$ = ℓ_P∇, $\tilde{V}$ = V/E_P. The derivation proceeds by substituting the Planck-scale definitions:

$$\frac{\hbar}{t_P} = \frac{\hbar}{\sqrt{\hbar G/c^5}} = \sqrt{\frac{\hbar c^5}{G}} = E_P$$

and

$$\frac{\hbar^2}{2m \ell_P^2} = \frac{\hbar^2}{2m} \cdot \frac{c^3}{\hbar G} = \frac{\hbar c^3}{2mG} = \frac{E_P}{2\tilde{m}}$$

With both sides divided by E_P, the dimensionless form follows immediately.

**Heisenberg Uncertainty Principle (Class A):**

In conventional dimensional form:
$$\Delta x \Delta p \geq \frac{\hbar}{2}$$

In dimensionless Planck units:
$$\Delta\tilde{x} \Delta\tilde{p} \geq \frac{1}{2}$$

where Δ$\tilde{x}$ = Δx/ℓ_P and Δ$\tilde{p}$ = Δp c/E_P. The factor ℏ/2 becomes the pure number 1/2 -- a statement that the product of normalized uncertainties is at least one-half.

### 3.2 Thermodynamics

**Planck's Law (Class F):**

In conventional dimensional form:
$$B_\nu(T) = \frac{2h\nu^3}{c^2} \frac{1}{e^{h\nu/(k_B T)} - 1}$$

In dimensionless Planck units:
$$\tilde{B}_{\tilde{\nu}}(\tilde{T}) = 4\pi\tilde{\nu}^3 \frac{1}{e^{2\pi\tilde{\nu}/\tilde{T}} - 1}$$

with $\tilde{ν}$ = ν t_P and $\tilde{T}$ = T/T_P. The reduction uses h = 2π (since h = 2πℏ and ℏ = 1) and the cancellation of c² in the pre-factor. The physical content is preserved in the exponent: the ratio hν/(k_B T) becomes 2π$\tilde{ν}$/$\tilde{T}$ -- a pure dimensionless number that determines the spectral regime.

**Stefan-Boltzmann Law (Class F):**

$$\sigma = \frac{2\pi^5 k_B^4}{15 h^3 c^2} \quad\longrightarrow\quad \tilde{\sigma} = \frac{\pi^2}{60}$$

The dimensional Stefan-Boltzmann constant σ ≈ 5.670374419 × 10⁻⁸ W/(m²·K⁴) reduces to the pure number π²/60 ≈ 0.1645 in Planck units. This number arises from the integration over the Planck spectrum, specifically from ζ(4) = π⁴/90, together with the geometric factor for isotropic radiation.

### 3.3 General Relativity

**Einstein Field Equations (Class C):**

In conventional dimensional form:
$$G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}$$

In dimensionless Planck units:
$$\tilde{G}_{\mu\nu} + \tilde{\Lambda} g_{\mu\nu} = 8\pi \tilde{T}_{\mu\nu}$$

where $\tilde{G}$_μν = G_μν ℓ_P², $\tilde{T}$_μν = T_μν/(E_P/ℓ_P³), and $\tilde{Λ}$ = Λ ℓ_P². The reduction eliminates the factor G/c⁴ ≈ 8.262 × 10⁻⁴⁵ m⁻¹·J⁻¹·m³ entirely. The coefficient 8π is a pure geometric factor arising from the Newtonian limit in four spacetime dimensions.

**Hawking Temperature (Class F):**

$$T_H = \frac{\hbar c^3}{8\pi G M k_B} \quad\longrightarrow\quad \tilde{T}_H = \frac{1}{8\pi \tilde{M}}$$

A black hole's temperature is simply the inverse of its mass (times 1/(8π)) when both are expressed in Planck units. A solar-mass black hole ($\tilde{M}$ ≈ 10³⁸) has $\tilde{T}$_H ≈ 4 × 10⁻⁴¹ -- practically absolute zero. A Planck-mass black hole would have $\tilde{T}$_H ≈ 1/(8π) ≈ 0.04, corresponding to approximately 4% of the Planck temperature.

### 3.4 Cosmology

**Critical Density (Class C):**

$$\rho_c = \frac{3H^2}{8\pi G} \quad\longrightarrow\quad \tilde{\rho}_c = \frac{3\tilde{H}^2}{8\pi}$$

with $\tilde{ρ}$_c = ρ_c/(E_P/ℓ_P³) and $\tilde{H}$ = H t_P. The Hubble constant today, H₀ ≈ 70 km/(s·Mpc), corresponds to $\tilde{H}$₀ ≈ 1.2 × 10⁻⁶¹ in Planck units -- reflecting the enormous ratio between the Hubble scale and the Planck scale.

### 3.5 Quantum Field Theory

**Fermi's Weak Interaction Constant (Class F):**

$$\frac{G_F}{(\hbar c)^3} \approx 1.166 \times 10^{-5} \text{ GeV}^{-2} \quad\longrightarrow\quad \tilde{G}_F \approx 3.05 \times 10^{-32}$$

The Fermi constant, which characterizes the strength of the weak interaction, becomes an extremely small dimensionless number when expressed in Planck units. This is the true physical statement: the dimensionless coupling is approximately 10⁻³². The question "why is the weak interaction so weak?" becomes "why is the dimensionless Fermi constant so small compared to unity?" -- a puzzle that dimensional units conceal by distributing the smallness across multiple constants.

### 3.6 Condensed Matter Physics

**Quantum Hall Resistance (Class F):**

$$R_K = \frac{h}{e^2} \approx 25812.807\ \Omega \quad\longrightarrow\quad \tilde{R}_K = \frac{2\pi}{\alpha} \approx 861$$

The von Klitzing constant, which in SI appears as a specific resistance (≈ 25.8 kΩ), is the dimensionless ratio 2π/α when expressed in natural units. The ohm value reflects the SI unit convention; the pure-number ratio 2π/α is the invariant physical content.

### 3.7 Already-Dimensionless Constants (Class G)

Several of the most important physical constants are already dimensionless and require no reformulation. These include:

- **Fine-structure constant:** α = e²/(4πε₀ℏc) ≈ 1/137.036. The primary dimensionless coupling of electromagnetism. Cross-references: the Fine-Structure Constant as a Cross-Ratio paper (DOI: 10.5281/zenodo.20108536) interprets α = r_e/λ_C as a projective-geometric invariant; the Alpha-Pi-Helix paper v2.1 (DOI: 10.5281/zenodo.21515612) treats π and α as geometric proportions (C/d and r_e/λ_C) with genuine pedagogical value at v1.1. `[established]`
- **Weinberg angle:** sin²θ_W ≈ 0.23. Already a dimensionless ratio. `[established]`
- **Holevo bound:** χ = S(ρ) - Σ p_i S(ρ_i). A dimensionless information-theoretic limit. `[established]`

**Ostrowski-evaluated harmonic paradigm:** The Harmonic Paradigm Under Ostrowski's Theorem paper (DOI: 10.5281/zenodo.21535017, 2026-07-24) applies Ostrowski's theorem to the Harmonic Paradigm specifically — demonstrating that the theorem's relevance extends beyond the systematic compilation (ODR) to domain-specific physics frameworks. This confirms the general applicability of the place-democracy criterion. `[established]`

The existence of these already-dimensionless fundamental constants supports the thesis that the dimensional ones -- ℏ, c, G, k_B, ε₀ -- are artifacts of unit conventions, not independent properties of nature. The dimensionless reformulation exposes this by showing that every dimensional formula reduces to one involving only dimensionless constants plus the pure-number α.

## 4 Discussion

### 4.1 What the Reformulation Does Not Change

The dimensionless reformulation is a rewriting, not a replacement. No physical prediction is altered. The Schroedinger equation in dimensionless form predicts exactly the same energy levels, scattering amplitudes, and time evolution as its dimensional counterpart. The Einstein field equations produce the same metric solutions. Planck's law yields the same spectral radiance.

What changes is the **interpretive framework**: the dimensional form embeds physical law in a specific number system (the real numbers, the Archimedean completion), while the dimensionless form makes no such commitment. This is relevant if one takes seriously the possibility that physical quantities at the Planck scale require non-Archimedean completions -- a possibility suggested by the adelic approach to physics `[speculative -- see Non-Anthropocentric Natural Units, DOI 10.5281/zenodo.21480756]`.

### 4.1.1 Comparative Analysis: ODR vs. Competitive Approaches

An independent external paper by Feldt (2026), "A Recursive Entropic Architecture for Cosmological Structure with Dimensional Invariance (REACS-DI): From Bohr Radius to Galaxy Filament—A Dimensionless Reformulation of Classical, Relativistic, and Quantum Laws," addresses the same core problem — the dimensionless reformulation of physics — from a fundamentally different framework. Where Feldt employs a recursive entropic architecture, ODR's approach is grounded in Ostrowski's theorem and number-theoretic place-democracy. This distinction in framework is substantive: entropic recursion treats the dimensionless re-expression as a consequence of informational constraints on structure formation, whereas Ostrowski's theorem treats it as a consequence of the mathematical structure of the rational numbers themselves — the latter being a more parsimonious foundation since it requires no additional physical assumptions beyond the known dimensional homogeneity of physical laws.

Table: Comparison of ODR and Feldt REACS-DI (2026) frameworks.

| Dimension | REACS-DI (Feldt 2026) | ODR (this work) |
|:----------|:----------------------|:----------------|
| Guiding principle | Entropic/recursive architecture | Ostrowski's theorem → place-democracy |
| Mathematical foundation | Entropy-based recursion | Number theory (p-adic completions) |
| Scope | Classical, relativistic, quantum laws | 53 formulas across 10 disciplines |
| Classification | Not reported | A-G taxonomy by constant type |
| Correspondence proof | Not reported | Explicit Buckingham Pi theorem proof |
| Boundary cases | Not reported | 3 categories documented |
| Ostrowski grounding | Not present | Core contribution |
| Complementary to ODR | Yes — different framework, same goal | — |

The frameworks are complementary rather than competing: REACS-DI provides a physical motivation (entropic necessity) for the dimensionless regime; ODR provides the mathematical proof (Ostrowski's theorem) that the reformulation is universally applicable across all of fundamental physics. A future synthesis could unify the two perspectives: entropic dimensional invariance as a *physical consequence* of number-theoretic place-democracy, rather than an alternative to it. `[speculative]`

### 4.2 Boundary Cases

Three categories of formulas require special handling:

1. **Definitional identities (Planck scale definitions):** The equations ℓ_P = √(ℏG/c³), t_P = √(ℏG/c⁵), m_P = √(ℏc/G), and T_P = √(ℏc⁵/(G k_B²)) are not physical laws but unit definitions. Reformulating them to "1 = 1" is tautological. They should be presented as definitions that set the scale, not as physical formulas to be reformulated.

2. **SI electromagnetic formulas:** Maxwell's equations in SI form contain ε₀ and μ₀ explicitly. Reformulation requires first converting to Heaviside-Lorentz or Gaussian units (where ε₀ = μ₀ = 1), then applying Planck normalization. The resulting dimensionless equations are equivalent to the Gaussian form with c = 1.

3. **Already-dimensionless formulas (Class G):** The fine-structure constant, magnetic Reynolds number, and Holevo bound require no reformulation. They demonstrate that nature's most fundamental parameters are dimensionless from the outset.

### 4.3 Limitations

This survey is not exhaustive. It covers 53 fundamental equations but does not include every formula in every subfield. Omitted categories include: detailed nuclear structure formulas beyond the semi-empirical mass formula, neutrino oscillation probabilities (which are inherently dimensionless), renormalization group equations beyond the one-loop examples, and most quantum information measures (most of which are inherently dimensionless). Future work could extend the inventory to these areas. `[speculative]`

**Pedagogical precedent:** The external literature provides strong support for the pedagogical value of the dimensionless reformulation. Humpherys (2024), "Understanding the natural units and their hidden role in the laws of physics" (*European Journal of Physics*, 12 citations), and its precursor Humpherys (2021), "Natural Planck units and the structure of matter and radiation" (*Quantum Speculations*, 10 citations), demonstrate that restating physical formulas in natural Planck units reveals structural relationships obscured by dimensional constants. While Humpherys's approach is explicitly pedagogical (the "hidden role" is a teaching insight, not an ontological claim), ODR's Ostrowski rationale provides the mathematical justification for why the pedagogical insight has ontological force: the dimensional form literally cannot be evaluated at non-Archimedean places, making the dimensionless form not merely clearer but uniquely well-defined across all completions of ℚ. `[established]`

Additionally, the dimensionless reformulation does not address the question of whether physical laws ARE place-democratic -- it only makes the formulas compatible with such an interpretation if one chooses to adopt it. The reformulation is a necessary condition for place-democratic physics but not a sufficient one. `[my conjecture]`

## 5 Conclusion

We have compiled and reformulated 53 fundamental physics equations across ten disciplines, converting each from its conventional dimensional form (containing ℏ, c, G, k_B, ε₀) to a dimensionless equivalent in Planck units (ℏ = c = G = k_B = 1). Each reformulation is supported by a mathematical derivation and an Ostrowski rationale explaining how the dimensional form privileges the Archimedean completion.

The key findings are:

1. **No formula resists reformulation.** All 53 equations, including the most complex multi-constant formulas (Einstein field equations, Planck's law, Fermi's golden rule), admit clean dimensionless equivalents. The dimensional homogeneity of physical laws guarantees this via the Buckingham Pi theorem. `[established]`

2. **The dimensional constants are unit-scale carriers.** Their specific numerical values (ℏ ≈ 1.05 × 10⁻³⁴, c = 3.00 × 10⁸, G ≈ 6.67 × 10⁻¹¹, k_B ≈ 1.38 × 10⁻²³) reflect the meter-kilogram-second-kelvin convention. In Planck units, all four become exactly 1.

3. **The dimensionless forms reveal hidden structure.** The Bohr radius becomes 1/(α $\tilde{m}$_e), exposing the 137-fold ratio between atomic and Compton scales. The Stefan-Boltzmann constant becomes π²/60, a pure geometric number. The Hawking temperature becomes 1/(8πM), a simple reciprocal relation.

4. **Nature's deepest constants are already dimensionless** (α ≈ 1/137, sin²θ_W ≈ 0.23, n_s ≈ 0.965). The dimensionless reformulation extends this transparency to all of fundamental physics.

The dimensionless program does not change the physics -- it changes what we see in the physics. The formulas become place-democratic: expressible as relations among pure numbers that are equally meaningful at every completion of ℚ.

## Declarations

**Funding:** This work received no external funding. `[established]`

**Conflicts of Interest:** The author declares no conflicts of interest. `[established]`

**Ethics Approval:** Not applicable -- this is a theoretical reformulation of existing physical laws; no experiments, human subjects, or animal subjects were involved. `[established]`

**Consent to Participate:** Not applicable. `[established]`

**Consent for Publication:** Not applicable. `[established]`

**Author Contributions:** The author performed all research, compilation, derivations, and writing. `[established]`

**Data Availability:** The complete formula inventory and all derivations are provided in the supplementary artifacts: `artifacts/formula-inventory.md` (53-formula inventory) and `artifacts/ostrowski-rationales.md` (detailed mathematical proofs). All artifacts are deposited with Zenodo. `[established]`

**Code Availability:** Not applicable -- this work involves no computational code beyond standard algebraic derivations. `[established]`

**Use of Artificial Intelligence:** AI assistance was used for formatting, LaTeX rendering, and organization of the formula inventory. All mathematical derivations were verified independently by the author. The physical content -- formula selection, reformulation logic, and Ostrowski rationale arguments -- was authored by the human researcher. `[established]`

## References

1. Ostrowski, A. (1916). Uber einige Losungen der Funktionalgleichung φ(x)·φ(y) = φ(xy). *Acta Mathematica*, 41, 271-284.
2. Quni-Gudzinas, R. B. (2026). Non-Anthropocentric Natural Units. Zenodo. DOI: 10.5281/zenodo.21480756.
3. Quni-Gudzinas, R. B. (2026). OC Paper v1.2. Zenodo. DOI: 10.5281/zenodo.21748773.
4. Quni-Gudzinas, R. B. (2026). OC Paper v1.3. Zenodo. DOI: 10.5281/zenodo.21749177.
5. Buckingham, E. (1914). On Physically Similar Systems. *Physical Review*, 4(4), 345-376.
6. Planck, M. (1900). Uber irreversible Strahlungsvorgange. *Annalen der Physik*, 306(1), 69-122.
7. Bekenstein, J. D. (1981). Universal upper bound on the entropy-to-energy ratio for bounded systems. *Physical Review D*, 23(2), 287-298.
8. Hawking, S. W. (1975). Particle creation by black holes. *Communications in Mathematical Physics*, 43(3), 199-220.
9. Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development*, 5(3), 183-191.
10. Einstein, A. (1915). Die Feldgleichungen der Gravitation. *Sitzungsberichte der Preussischen Akademie der Wissenschaften zu Berlin*, 844-847.
11. Quni-Gudzinas, R. B. (2026). Dimensionless Physics: A Unified Framework v1.3.1. Zenodo. DOI: 10.5281/zenodo.21206291.
12. Quni-Gudzinas, R. B. (2026). Scaffolds and Invariants: An Epistemic Hygiene Audit of pi, Number Bases, and Geometric Centers. Zenodo. DOI: 10.5281/zenodo.21255344.
13. Quni-Gudzinas, R. B. (2026). The Harmonic Paradigm Under Ostrowski's Theorem: A p-Adic/Adelic Re-Evaluation with Helical Compton Vortex Synthesis. Zenodo. DOI: 10.5281/zenodo.21535017.
14. Quni-Gudzinas, R. B. (2026). Fine-Structure Constant as a Cross-Ratio: A Geometric Reframing of alpha. Zenodo. DOI: 10.5281/zenodo.20108536.
15. Quni-Gudzinas, R. B. (2026). Alpha-Pi-Helix v2.1. Zenodo. DOI: 10.5281/zenodo.21515612.
16. Quni-Gudzinas, R. B. (2026). Compton Frequency Cross-Ratios on Bruhat-Tits Trees v2.3.1. Zenodo. DOI: 10.5281/zenodo.21491767.
17. Quni-Gudzinas, R. B. (2026). When Will Non-Archimedean Geometry Displace the Real Numbers? A Structured Assessment of the Adelic Substrate Thesis. Zenodo. DOI: 10.5281/zenodo.21747228.
18. Quni-Gudzinas, R. B. (2026). The Adelic Cross-Domain Program: From the Fine-Structure Constant to the Standard Model Mass Spectrum via Bruhat-Tits Trees. Zenodo. DOI: 10.5281/zenodo.21736300.
19. Humpherys, D. (2024). Understanding the natural units and their hidden role in the laws of physics. *European Journal of Physics*. DOI: 10.1088/1361-6404/ad3122.
20. Feldt, W. (2026). A Recursive Entropic Architecture for Cosmological Structure with Dimensional Invariance (REACS-DI): From Bohr Radius to Galaxy Filament. Cambridge University Press.
