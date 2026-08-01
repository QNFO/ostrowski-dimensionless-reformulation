# Red Team Memo: Running Couplings and Archimedean Decimals
## ODR v1.6 → v1.7 Audit | 2026-08-02
### Severity: 1 HARD (systematic), 4 SOFT (per-formula annotations)

---

## §1 The Core Finding

**α = 1/137.036 is NOT a compliant dimensionless constant.** It is:

1. **A running coupling** — α(Q²) varies from 1/137.036 (Q²→0, IR limit) to 1/127.9 (Q² = M_Z²), a **7.14% change**. The paper's 29 formulas using α as a fixed number each silently use the IR Archimedean value.
2. **A base-10 Archimedean decimal** — 137.036 is the value of the inverse ratio α⁻¹ = 4πε₀ℏc/e² *projected into the real numbers at the IR scale*. Per the user directive: *"If it's a decimal or base-10 quantity/'constant' that's only one completion not compliant with Ostrowski/Tate."* The decimal is one completion's one-scale projection.
3. **Not a rational number** — α = e²/(4πε₀ℏc) involves e and π (transcendentals), so α ∉ ℚ. Its exact value exists only in the Archimedean completion; at any p-adic place, α's decimal expansion is meaningless (per the C2 red-team finding already fixed in v1.6).

**The compliant form:** α is a **running ratio** α(Q̃²) = r_e(Q̃)/λ̄_C(Q̃), where Q̃ = Q/E_P is the dimensionless momentum transfer. The ratio form is place-democratic (each quantity is a ratio to its Planck-scale counterpart); the decimal 1/137.036 is the IR limit of this ratio evaluated in the Archimedean completion.

---

## §2 Formulas Affected (29 total)

### §2.1 HARD — formulas presenting α as a fixed constant (must be amended)

| # | Formula | Location | Fix |
|:--|:--------|:---------|:----|
| 1 | α = e²/(4πε₀ℏc) ≈ 1/137.036 | §3.7, QFT-3, EM-6 | α(Q̃²), IR value is 1/137.036 |
| 2 | ã₀ = 1/(α m̃_e) | QM-8, §3.7, §5 | ã₀(Q̃) = 1/(α(Q̃) m̃_e), evaluate at Q̃ = α m̃_e |
| 3 | R̃_∞ = α² m̃_e/(4π) | QM-9 | α(Q̃²) at hydrogen scale |
| 4 | σ̃_T = (8π/3)(α/m̃)² | QFT-4 | α(Q̃²) at Thomson scale (IR — fine but annotate) |
| 5 | R̃_K = 2π/α ≈ 861 | CM-1, §3.6 | 2π/α(Q̃²) — note QH uses α at Landau-level scale |
| 6 | Z̃₀ = 4π/α | EM-3 | annotate scale |
| 7 | P̃ = (2α/3)(q̃²ã²) | EM-4 (Larmor) | α(Q̃²) at radiation scale |
| 8 | Ẽ_n = -(α² m̃_e)/(2n²) | AN-1 (Hydrogen) | α(Q̃²) at binding scale |
| 9 | R̃_H = 2π/(ν α) | CM-1 | annotate |
| 10 | G̃₀ = 4α | CM-3 | annotate |
| 11 | λ̃_L = √(m̃/(ñ_s α)) | CM-4 (London) | α at zero-frequency limit (IR — fine, annotate) |
| 12 | λ̃_D = √(T̃/(4πα ñ)) | FP-1 (Debye) | annotate |
| 13 | ω̃_p = √(4πα ñ/m̃) | FP-2 (plasma) | annotate |
| 14 | F̃ = α(q̃₁q̃₂)/r̃² | EM-1 (Coulomb) | α(1/r̃²) — Q̃ ~ 1/r̃ |
| 15 | μ̃_B = ẽ/(2m̃_e) | EM-5 | fine (no α) — verify |
| 16 | ã₀/λ̃_C = 1/(2πα) ≈ 21.8 | §2.4 C_5 | 1/(2πα(Q̃)) — the 21.8 is IR value |

### §2.2 SOFT — other running quantities presented as constants

| # | Quantity | Issue | Fix |
|:--|:---------|:------|:----|
| 17 | sin²θ_W ≈ 0.23 | Weinberg angle RUNS with energy (0.2312 at M_Z MS-bar vs 0.23 low-E) | sin²θ_W(Q̃²) |
| 18 | G_F ≈ 1.166×10⁻⁵ GeV⁻² | Fermi constant is scale-dependent | G̃_F(Q̃²) |
| 19 | n_s ≈ 0.965 | scalar spectral index — pivot-scale dependent (0.965 at k* = 0.05 Mpc⁻¹) | n_s(k̃*) annotate |
| 20 | σ ≈ 5.670×10⁻⁸ | Stefan-Boltzmann — π²/60 is exact, no running (thermo OK) | ✅ no fix |

### §2.3 VERIFIED — genuinely scale-independent dimensionless quantities

| Quantity | Reason |
|:---------|:-------|
| π²/60 (σ̃) | exact geometric number, no running |
| 1/8π (T̃_H coefficient) | geometric, no running |
| 1/(8πM̃) | depends only on M̃ (Schwarzschild) |
| 1/ln2 (Landauer, Bekenstein saturation) | pure number |
| 2.821 (Wien ω̃_max/T̃) | solution of transcendental equation, scale-free |
| 21.8 → 1/(2πα) | IS running (see #16) — exception |

---

## §3 The Correct Compliant Statement

```markdown
**Running couplings (v1.7 correction):** α, sin²θ_W, and G_F are not fixed
dimensionless constants — they are *running functions* of the dimensionless
energy scale Q̃ = Q/E_P:

    α(Q̃²)  — QED coupling, runs 1/137.036 (Q̃→0) → 1/127.9 (Q̃ = M_Z/E_P)
    sin²θ_W(Q̃²) — Weinberg angle, runs with scale
    G̃_F(Q̃²) — dimensionless Fermi constant, scale-dependent

The value 1/137.036 is the IR limit of α(Q̃²) evaluated in the Archimedean
completion — one scale at one place. The Ostrowski/Tate-compliant statement
is the running ratio α(Q̃²) = r_e(Q̃)/λ̄_C(Q̃), which is place-democratic in
form and evaluated at the relevant scale in practice. Every formula in §3
that writes "α" implicitly means "α(Q̃²) at the formula's characteristic
energy scale" — for atomic physics that is the IR value (1/137.036); for
Z-pole physics it is 1/127.9; for Planck-scale physics the value is
determined by the running equation itself.
```

---

## §4 Action Items (this kaizen/red-team pass)

1. **[HARD]** Add §2.5 "Running Couplings and the Scale-Dependence of Dimensionless Quantities" to the paper
2. **[HARD]** Amend §3.7 fine-structure/Weinberg entries with running-coupling annotations
3. **[HARD]** Amend §5 conclusion "Nature's deepest constants are already dimensionless (α ≈ 1/137...)" — add running caveat
4. **[SOFT]** Annotate the 16 formulas in §2.1 with α(Q̃²) scale notes
5. **[SOFT]** Rebuild PDF, mojibake scan, commit as v1.7

---

*Red-team executed per qnfo-core §0.0 certainty calibration. Finding: [established] — QED running coupling verified (PDG: α⁻¹(M_Z) = 127.9, α⁻¹(0) = 137.036).*
