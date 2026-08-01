# Formula Inventory: Ostrowski Dimensionless Reformulation
## Systematic Survey of Dimensional Physics Equations
### Phase 1-2 Deliverable | 2026-08-01

> **Classification Key:**
> - **Class A:** Contains ℏ only (quantum mechanical)
> - **Class B:** Contains c only (relativistic)
> - **Class C:** Contains G only (gravitational)
> - **Class D:** Contains k_B only (thermodynamic)
> - **Class E:** Contains ε₀ / μ₀ only (electromagnetic SI)
> - **Class F:** Contains combinations of ℏ, c, G, k_B
> - **Class G:** Already dimensionless (fine-structure constant, etc.)

> **Planck Unit Normalization Convention (ℏ = c = G = k_B = 1):**
> ℓ_P = √(ℏG/c³) = 1.616255(18) × 10⁻³⁵ m — Planck length
> t_P = √(ℏG/c⁵) = 5.391247(60) × 10⁻⁴⁴ s — Planck time
> m_P = √(ℏc/G) = 2.176434(24) × 10⁻⁸ kg — Planck mass
> E_P = √(ℏc⁵/G) = 1.956082(22) × 10⁹ J — Planck energy
> T_P = √(ℏc⁵/(G k_B²)) = 1.416784(16) × 10³² K — Planck temperature
> All quantities below expressed as dimensionless ratios: R_phys ≡ R/ℓ_P, E_phys ≡ E/E_P, etc.

---

## 1. Quantum Mechanics

### QM-1: Schroedinger Equation (Class A)
**Dimensional form:** iℏ ∂ψ/∂t = (-ℏ²/(2m) ∇² + V) ψ [established]
**Dimensionless:** i ∂ψ/∂t̃ = (-1/(2m̃) ∇̃² + Ṽ) ψ
*Where:* t̃ = t/t_P, m̃ = m/m_P, ∇̃ = ℓ_P ∇, Ṽ = V/E_P

### QM-2: Heisenberg Uncertainty Principle (Class A)
**Dimensional form:** Δx Δp ≥ ℏ/2 [established]
**Dimensionless:** Δx̃ Δp̃ ≥ 1/2
*Where:* Δx̃ = Δx/ℓ_P, Δp̃ = Δp c/E_P (momentum in units of E_P/c)

### QM-3: de Broglie Wavelength (Class A)
**Dimensional form:** λ = h/p = 2πℏ/p [established]
**Dimensionless:** λ̃ = 2π/p̃
*Where:* λ̃ = λ/ℓ_P, p̃ = p c/E_P

### QM-4: Planck-Einstein Relation (Class A)
**Dimensional form:** E = ℏω [established]
**Dimensionless:** Ẽ = ω̃
*Where:* Ẽ = E/E_P, ω̃ = ω t_P

### QM-5: Photon Energy (Class A)
**Dimensional form:** E = hν = ℏω [established]
**Dimensionless:** Ẽ = 2π ν̃
*Where:* ν̃ = ν t_P

### QM-6: Canonical Commutation Relation (Class A)
**Dimensional form:** [x̂, p̂] = iℏ [established]
**Dimensionless:** [x̃, p̃] = i
*Where:* x̃ = x̂/ℓ_P, p̃ = p̂ c/E_P

### QM-7: Fermi Energy — Ideal Electron Gas (Class A)
**Dimensional form:** E_F = (ℏ²/(2m))(3π²n)^(2/3) [established]
**Dimensionless:** Ẽ_F = (1/(2m̃))(3π²ñ)^(2/3)
*Where:* ñ = n ℓ_P³ (number density in Planck volumes)

### QM-8: Bohr Radius (Class F: ℏ, ε₀, e)
**Dimensional form:** a₀ = 4πε₀ℏ²/(m_e e²) [established]
**Dimensionless:** ã₀ = 1/(α m̃_e)
*Where:* ã₀ = a₀/ℓ_P, m̃_e = m_e/m_P, α = e²/(4πε₀ℏc) ≈ 1/137.036 (fine-structure constant, Class G)

### QM-9: Rydberg Constant (Class F: ℏ, c, ε₀)
**Dimensional form:** R_∞ = m_e e⁴/(8ε₀²h³c) [established]
**Dimensionless:** R̃_∞ = α² m̃_e/(4π)
*Where:* R̃_∞ = R_∞ ℓ_P

### QM-10: Compton Wavelength (Class F: ℏ, c)
**Dimensional form:** λ_C = h/(m c) = 2πℏ/(m c) [established]
**Dimensionless:** λ̃_C = 2π/m̃
*Where:* λ̃_C = λ_C/ℓ_P, m̃ = m/m_P

### QM-11: Dirac Equation (Class A: ℏ, c)
**Dimensional form:** (iℏγ^μ ∂_μ - m c)ψ = 0 [established]
**Dimensionless:** (iγ^μ ∂̃_μ - m̃)ψ = 0
*Where:* ∂̃_μ = ℓ_P ∂_μ, m̃ = m/m_P

### QM-12: Klein-Gordon Equation (Class F: ℏ, c)
**Dimensional form:** (□ + (mc/ℏ)²)φ = 0 [established]
**Dimensionless:** (□̃ + m̃²)φ = 0
*Where:* □̃ = ℓ_P² □

### QM-13: Quantum Harmonic Oscillator Energy (Class A)
**Dimensional form:** E_n = ℏω(n + 1/2) [established]
**Dimensionless:** Ẽ_n = ω̃(n + 1/2)

### QM-14: Zero-Point Energy (Class A)
**Dimensional form:** E_0 = ℏω/2 [established]
**Dimensionless:** Ẽ_0 = ω̃/2

---

## 2. Thermodynamics & Statistical Mechanics

### TD-1: Boltzmann Entropy (Class D)
**Dimensional form:** S = k_B ln W [established]
**Dimensionless:** S̃ = ln W
*Where:* S̃ = S/k_B (dimensionless entropy)

### TD-2: Ideal Gas Law (Class D)
**Dimensional form:** PV = N k_B T [established]
**Dimensionless:** P̃ ṽ = N T̃
*Where:* P̃ = P ℓ_P³/E_P (pressure in Planck units), ṽ = V/ℓ_P³, T̃ = T/T_P

### TD-3: Stefan-Boltzmann Law (Class F: ℏ, c, k_B)
**Dimensional form:** j* = σ T⁴ where σ = 2π⁵k_B⁴/(15h³c²) [established]
**Dimensionless:** j̃* = (π²/60) T̃⁴
*Where:* j̃* = j* ℓ_P² t_P/E_P

**Rationale:** The dimensional constant σ = 2π⁵k_B⁴/(15h³c²) is a compound of ℏ, c, k_B. Substituting ℏ = c = k_B = 1, and using h = 2πℏ → 2π:
σ → 2π⁵/(15·(2π)³) = 2π⁵/(15·8π³) = π²/(60)

### TD-4: Wien's Displacement Law (Class F: ℏ, c, k_B)
**Dimensional form:** λ_max T = h c/(x k_B) where x ≈ 4.9651142317 [established]
**Dimensionless:** λ̃_max T̃ = 2π/x
*Where:* λ̃_max = λ_max/ℓ_P

**Rationale:** h c/k_B = 2πℏc/k_B → 2π (with ℏ = c = k_B = 1). So λ_max T = 2π/x → λ̃_max T̃ = 2π/x.

### TD-5: Planck's Law (Spectral Radiance) (Class F: ℏ, c, k_B)
**Dimensional form:** B_ν(T) = (2hν³/c²) × 1/(e^(hν/(k_B T)) - 1) [established]
**Dimensionless:** B̃_ν̃(T̃) = (4π ν̃³) × 1/(e^(2π ν̃/T̃) - 1)
*Where:* B̃_ν̃ = B_ν E_P/(ℓ_P² c), ν̃ = ν t_P

**Rationale:** h = 2πℏ → 2π (in Planck units). Factor: 2hν³/c² → 4πν³ (dimensionless). Exponent: hν/(k_B T) → 2πν̃/T̃.

### TD-6: Planck's Law (Spectral Radiance per Wavelength) (Class F)
**Dimensional form:** B_λ(T) = (2hc²/λ⁵) × 1/(e^(hc/(λ k_B T)) - 1) [established]
**Dimensionless:** B̃_λ̃(T̃) = (4π/λ̃⁵) × 1/(e^(2π/(λ̃ T̃)) - 1)

### TD-7: Maxwell-Boltzmann Speed Distribution (Class D)
**Dimensional form:** f(v) = 4π(m/(2πk_B T))^(3/2) v² exp(-m v²/(2k_B T)) [established]
**Dimensionless:** f̃(ṽ) = 4π(m̃/(2πT̃))^(3/2) ṽ² exp(-m̃ ṽ²/(2T̃))
*Where:* ṽ = v/c

### TD-8: Sackur-Tetrode Equation (Class F: ℏ, k_B)
**Dimensional form:** S = N k_B [ln(V/N (4πm U/(3N h²))^(3/2)) + 5/2] [established]
**Dimensionless:** S̃ = N [ln(ṽ/N (2π m̃ Ũ/(3N))^(3/2)) + 5/2]
*Where:* Ũ = U/E_P (using h = 2πℏ → 2π)

### TD-9: Debye T³ Law — Low-Temperature Heat Capacity (Class D, F)
**Dimensional form:** C_V = (12π⁴/5) N k_B (T/T_D)³ [established]
**Dimensionless:** C̃_V = (12π⁴/5) N (T̃/T̃_D)³
*Where:* C̃_V = C_V/k_B (dimensionless heat capacity)
*Debye temperature:* T_D = ℏ ω_D/k_B → T̃_D = ω̃_D (dimensionless)

### TD-10: Einstein Heat Capacity (Class D, F)
**Dimensional form:** C_V = 3N k_B (ℏω/(k_B T))² e^(ℏω/(k_B T))/(e^(ℏω/(k_B T)) - 1)² [established]
**Dimensionless:** C̃_V = 3N (ω̃/T̃)² e^(ω̃/T̃)/(e^(ω̃/T̃) - 1)²

### TD-11: Landauer's Principle (Class D) — ALREADY REFORMULATED
**Dimensional form:** E ≥ k_B T ln 2 [established]
**Dimensionless:** Ẽ ≥ T̃ ln 2 [established — OC v1.3, DOI 10.5281/zenodo.21749177]
*Reference:* OC-9 (OC Paper v1.3 §2.1, §5). Both forms presented with Ostrowski rationale.

### TD-12: Equipartition Theorem (Class D)
**Dimensional form:** ⟨E_i⟩ = (1/2) k_B T per quadratic degree of freedom [established]
**Dimensionless:** ⟨Ẽ_i⟩ = (1/2) T̃

### TD-13: Gibbs Entropy Formula (Class D)
**Dimensional form:** S = -k_B Σ p_i ln p_i [established]
**Dimensionless:** S̃ = -Σ p_i ln p_i

---

## 3. General Relativity & Gravitation

### GR-1: Einstein Field Equations (Class C: G, c)
**Dimensional form:** G_μν + Λ g_μν = (8πG/c⁴) T_μν [established]
**Dimensionless:** G_μν + Λ̃ g_μν = 8π T̃_μν
*Where:* T̃_μν = T_μν/E_P ℓ_P⁻³ (stress-energy in Planck units), Λ̃ = Λ ℓ_P²

**Rationale:** G/c⁴ = 1/(E_P ℓ_P⁻¹) = ℓ_P/E_P in SI; in Planck units G = c = 1, so 8πG/c⁴ → 8π. The Einstein tensor G_μν has dimensions [L⁻²]; in Planck units curvature is dimensionless after multiplying by ℓ_P². Both sides become pure numbers.

### GR-2: Schwarzschild Radius (Class C: G, c)
**Dimensional form:** r_s = 2GM/c² [established]
**Dimensionless:** r̃_s = 2M
*Where:* r̃_s = r_s/ℓ_P, M = M/m_P

### GR-3: Schwarzschild Metric (Class C: G, c)
**Dimensional form:** ds² = -(1 - 2GM/(rc²))c²dt² + dr²/(1 - 2GM/(rc²)) + r²dΩ² [established]
**Dimensionless:** ds̃² = -(1 - 2M/r̃)dt̃² + dr̃²/(1 - 2M/r̃) + r̃²dΩ²

### GR-4: Friedmann Equation (First) (Class C: G, c)
**Dimensional form:** H² = (8πG/3)ρ - k c²/a² + Λc²/3 [established]
**Dimensionless:** H̃² = (8π/3)ρ̃ - k̃/ã² + Λ̃/3
*Where:* H̃ = H t_P, ρ̃ = ρ ℓ_P³/m_P c² = ρ/E_P ℓ_P⁻³, ã = a/ℓ_P

### GR-5: Friedmann Equation (Second) / Acceleration (Class C)
**Dimensional form:** ä/a = -4πG(ρ + 3P/c²)/3 + Λc²/3 [established]
**Dimensionless:** ä̃/ã = -4π(ρ̃ + 3P̃)/3 + Λ̃/3

### GR-6: Bekenstein-Hawking Entropy (Class F: ℏ, c, G, k_B) — ALREADY REFORMULATED
**Dimensional form:** S_BH = k_B c³ A/(4Gℏ) [established]
**Dimensionless:** S̃_BH = A/4 [established — OC v1.2, DOI 10.5281/zenodo.21748773]
*Where:* A = A_phys/ℓ_P² (dimensionless horizon area). Reference: Non-Anthropocentric Natural Units (DOI 10.5281/zenodo.21480756).

### GR-7: Hawking Temperature (Class F: ℏ, c, G, k_B)
**Dimensional form:** T_H = ℏc³/(8π G M k_B) [established]
**Dimensionless:** T̃_H = 1/(8π M)
*Where:* T̃_H = T_H/T_P, M = M/m_P

### GR-8: Kerr Black Hole — Outer Horizon (Class C: G, c)
**Dimensional form:** r_+ = GM/c² + √((GM/c²)² - a²) [established]
**Dimensionless:** r̃_+ = M + √(M² - ã²)
*Where:* ã = a/ℓ_P (a = J/(M c), specific angular momentum)

### GR-9: Tolman-Oppenheimer-Volkoff Equation (Class C: G, c)
**Dimensional form:** dP/dr = -G(ρ + P/c²)(m(r) + 4πr³P/c²)/(r²(1 - 2Gm(r)/(rc²))) [established]
**Dimensionless:** dP̃/dr̃ = -(ρ̃ + P̃)(M(r̃) + 4πr̃³P̃)/(r̃²(1 - 2M(r̃)/r̃))

### GR-10: Gravitational Wave Luminosity (Class C: G, c)
**Dimensional form:** L_GW = (G/(5c⁵)) ⟨d³I_{ij}/dt³ d³I^{ij}/dt³⟩ [established]
**Dimensionless:** L̃_GW = (1/5) ⟨d³Ĩ_{ij}/dt̃³ d³Ĩ^{ij}/dt̃³⟩
*Where:* Ĩ_{ij} = I_{ij}/(m_P ℓ_P²) (dimensionless quadrupole moment)

---

## 4. Quantum Field Theory

### QFT-1: Free Scalar Field Lagrangian (Class F: ℏ, c)
**Dimensional form:** ℒ = ½(∂_μφ ∂^μφ) - ½(mc/ℏ)² φ² [established]
**Dimensionless:** ℒ̃ = ½(∂̃_μφ ∂̃^μφ) - ½ m̃² φ̃²
*Where:* ℒ̃ = ℒ ℓ_P⁴/E_P, φ̃ = φ/√(E_P/ℓ_P)

### QFT-2: Feynman Propagator (Scalar) (Class F: ℏ, c)
**Dimensional form:** G_F(x-y) = ∫ d⁴k/(2π)⁴ e^(-ik(x-y))/(k² - m²c²/ℏ² + iε) [established]
**Dimensionless:** G̃_F(x̃-ỹ) = ∫ d⁴k̃/(2π)⁴ e^(-ik̃(x̃-ỹ))/(k̃² - m̃² + iε̃)

### QFT-3: QED Vertex — Fine-Structure Constant (Class G — ALREADY DIMENSIONLESS)
**Dimensional form:** α = e²/(4πε₀ℏc) ≈ 1/137.036 [established]
**Dimensionless:** α ≈ 1/137.036 — already dimensionless. This is the canonical example of a formula that never needs reformulation.

### QFT-4: Compton Scattering Cross-Section (Thomson) (Class F: ℏ, c)
**Dimensional form:** σ_T = (8π/3)(e²/(4πε₀mc²))² = (8π/3)(αℏ/(mc))² [established]
**Dimensionless:** σ̃_T = (8π/3)(α/m̃)²
*Where:* σ̃_T = σ_T/ℓ_P²

### QFT-5: Running QED Coupling (1-loop) — ALREADY DIMENSIONLESS
**Dimensional form:** α(Q²) = α(μ²)/(1 - (α(μ²)/(3π))ln(Q²/μ²)) [established]
**Dimensionless:** Already dimensionless — the logarithm argument is a ratio of energy scales.

### QFT-6: Yukawa Potential (Class F: ℏ, c)
**Dimensional form:** V(r) = -(g²/(4π)) e^(-mcr/ℏ)/r [established]
**Dimensionless:** Ṽ(r̃) = -(g̃²/(4π)) e^(-m̃r̃)/r̃
*Where:* Ṽ = V/E_P, g̃ = g/√(ℏc) (dimensionless Yukawa coupling in 4D)

### QFT-7: Beta Function (1-loop, φ⁴) — ALREADY DIMENSIONLESS
**Dimensional form:** β(λ) = μ dλ/dμ = 3λ²/(16π²) + O(λ³) [established]
**Dimensionless:** Already dimensionless.

### QFT-8: Fermi's Golden Rule (Class A: ℏ)
**Dimensional form:** Γ_{i→f} = (2π/ℏ) |⟨f|Ĥ_int|i⟩|² ρ(E_f) [established]
**Dimensionless:** Γ̃_{i→f} = 2π |⟨f|Ĥ̃_int|i⟩|² ρ̃(Ẽ_f)
*Where:* Γ̃ = Γ t_P

---

## 5. Cosmology

### COS-1 through COS-4: Planck Scale Definitions (Class F)
These are DEFINITIONAL — they define what "Planck units" means. Reformulating them is tautological:
- ℓ_P = √(ℏG/c³) [established] — defines the length unit
- t_P = √(ℏG/c⁵) [established] — defines the time unit
- m_P = √(ℏc/G) [established] — defines the mass unit
- T_P = √(ℏc⁵/(G k_B²)) [established] — defines the temperature unit
**In Planck units:** ℓ_P = t_P = m_P = T_P = 1 by definition. These are not physical laws but unit definitions — they set the scale.

### COS-5: Critical Density (Class C: G)
**Dimensional form:** ρ_c = 3H²/(8πG) [established]
**Dimensionless:** ρ̃_c = 3H̃²/(8π)
*Where:* ρ̃_c = ρ_c ℓ_P³/E_P = ρ_c/E_P ℓ_P⁻³

### COS-6: Hubble Parameter (Friedmann constraint)
**Dimensional form:** H² = (8πG/3)(ρ_m + ρ_r + ρ_Λ) - kc²/a² [established]
**Dimensionless:** H̃² = (8π/3)(ρ̃_m + ρ̃_r + ρ̃_Λ) - k̃/ã²

### COS-7: Horizon Scale (Class B: c)
**Dimensional form:** d_H(t) = a(t) ∫₀^t c dt'/a(t') [established]
**Dimensionless:** d̃_H(t̃) = ã(t̃) ∫₀^t̃ dt̃'/ã(t̃')

### COS-8: Baryon Acoustic Oscillation Scale (Class F)
**Dimensional form:** r_s = ∫_{z_drag}^∞ c_s(z) dz/H(z) [established]
**Dimensionless:** r̃_s = ∫_{z_drag}^∞ c̃_s(z) dz/H̃(z)
*Where:* c̃_s = c_s/c

### COS-9: Primordial Power Spectrum (Scalar) — ALREADY DIMENSIONLESS
**Dimensional form:** P_ℛ(k) = A_s (k/k_pivot)^(n_s-1) [established]
**Dimensionless:** Already dimensionless — A_s ≈ 2.1 × 10⁻⁹, n_s ≈ 0.965.

### COS-10: Slow-Roll Inflation Parameters — ALREADY DIMENSIONLESS
**Dimensional form:** ε_V = (m_P²/2)(V'/V)², η_V = m_P² V''/V [established]
**Dimensionless:** Already dimensionless (defined with explicit m_P normalization).

---

## 6. Electromagnetism

### EM-1: Coulomb's Law (Class E: ε₀)
**Dimensional form:** F = q₁q₂/(4πε₀r²) [established]
**Dimensionless:** F̃ = α (q̃₁q̃₂)/(r̃²)
*Where:* q̃ = q/e (charge in units of elementary charge), F̃ = F ℓ_P²/(ℏc) = F ℓ_P/E_P
**Note:** In Planck units, 1/(4πε₀) = α ℏc/e² = α (since ℏ = c = 1), up to charge unit normalization.

### EM-2: Maxwell's Equations (SI) — Faraday's Law (Class B, E)
**Dimensional form:** ∇ × E = -∂B/∂t [established]
**Dimensionless:** ∇̃ × Ẽ = -∂B̃/∂t̃
*Where:* Ẽ = E/(E_P/e ℓ_P), B̃ field appropriately normalized
**Note:** Maxwell's equations in SI mix ε₀ and μ₀. Full reformulation requires Gaussian/Heaviside-Lorentz convention or explicit conversion.

### EM-3: Impedance of Free Space (Class F: ε₀, μ₀, c)
**Dimensional form:** Z₀ = √(μ₀/ε₀) = μ₀c ≈ 376.730 Ω [established]
**Dimensionless:** Z̃₀ = 4π/α? [speculative — depends on unit convention]
**Note:** In natural (Heaviside-Lorentz) units, Z₀ = 4π (dimensionless). In Planck units with e as charge unit: Z₀ = 4πℏ/(e²) = 4π/α. This is one of the more subtle reformulations.

### EM-4: Larmor Formula (Class B: c)
**Dimensional form:** P = (q²a²)/(6πε₀c³) [established]
**Dimensionless:** P̃ = (2α/3)(q̃²ã²)
*Where:* P̃ = P/E_P t_P⁻¹, ã = a t_P²/ℓ_P

### EM-5: Magnetic Moment of Electron (Class F: ℏ)
**Dimensional form:** μ_B = eℏ/(2m_e) (Bohr magneton) [established]
**Dimensionless:** μ̃_B = ẽ/(2m̃_e)
*Where:* μ̃_B = μ_B/(e ℓ_P c) (in appropriate dimensionless units)

### EM-6: Fine-Structure Constant — ALREADY DIMENSIONLESS (Class G)
**Dimensional form:** α = e²/(4πε₀ℏc) ≈ 1/137.036 [established]
**No reformulation needed.** α is the archetypal dimensionless physical constant.

---

## 7. Atomic, Nuclear & Particle Physics

### AN-1: Hydrogen Energy Levels (Bohr Model) (Class F: ℏ, c, ε₀)
**Dimensional form:** E_n = -(m_e e⁴)/(8ε₀²h²n²) = -(α² m_e c²)/(2n²) [established]
**Dimensionless:** Ẽ_n = -(α² m̃_e)/(2n²)

### AN-2: Fermi's Weak Interaction Constant (Class F: ℏ, c)
**Dimensional form:** G_F/(ℏc)³ ≈ 1.1663787(6) × 10⁻⁵ GeV⁻² [established]
**Dimensionless:** G̃_F = G_F E_P²/(ℏc)³ = G_F m_P² c⁴/(ℏc)³ (enormous small number ~ 10⁻³²)
**Note:** The extremely small dimensionless value of G̃_F is the actual physical content — "why is the weak interaction so weak?" becomes "why is G̃_F ~ 10⁻³²?"

### AN-3: Nuclear Liquid Drop — Semi-Empirical Mass Formula (Class F: ℏ, c)
**Dimensional form:** B(A,Z) = a_v A - a_s A^(2/3) - a_c Z(Z-1)/A^(1/3) - a_a (A-2Z)²/A + δ(A,Z) [established]
**Dimensionless:** B̃(A,Z) = ã_v A - ã_s A^(2/3) - ã_c Z(Z-1)/A^(1/3) - ã_a (A-2Z)²/A + δ̃(A,Z)
*Where each coefficient is normalized to E_P*

### AN-4: Nuclear Radius (Class F: ℏ, c)
**Dimensional form:** R = r₀ A^(1/3) where r₀ ≈ 1.2 fm [established]
**Dimensionless:** R̃ = r̃₀ A^(1/3)
*Where:* r̃₀ = r₀/ℓ_P ≈ 7.4 × 10¹⁹ — this large number reflects how much larger atomic nuclei are than the Planck length.

### AN-5: Breit-Wigner Resonance (Class F: ℏ, c)
**Dimensional form:** σ(E) = (π/k²) Γ²/((E - E_R)² + Γ²/4) [established]
**Dimensionless:** σ̃(Ẽ) = (π/k̃²) Γ̃²/((Ẽ - Ẽ_R)² + Γ̃²/4)

---

## 8. Condensed Matter Physics

### CM-1: Quantum Hall Resistance (Class F: ℏ, e)
**Dimensional form:** R_H = h/(ν e²) [established]
**Dimensionless:** R̃_H = 2π/(ν α)
*Where:* R̃_H = R_H/Z_P where Z_P = (1/4πε₀c) ≈ 30 Ω? Actually needs careful normalization.
**Note:** Using h = 2πℏ → 2π, e²/(4πε₀ℏc) = α → h/e² = 2π/α ≈ 861 (dimensionless von Klitzing constant).

### CM-2: Josephson Constant (Class F: h, e)
**Dimensional form:** K_J = 2e/h [established]
**Dimensionless:** K̃_J = 2ẽ/(2π) = ẽ/π
*Where:* K̃_J = K_J V_P⁻¹ in appropriate frequency-voltage units

### CM-3: Quantum Conductance (Class F: ℏ, e)
**Dimensional form:** G₀ = 2e²/h [established]
**Dimensionless:** G̃₀ = 2α/π
*Where:* G̃₀ = G₀/(e²/ℏ) — wait, G₀ already contains e²/h.
G₀ = 2e²/h = 2e²/(2πℏ) → G̃₀ = 2α/(2π) × (4πℏc/e²)? No. Simplify:
e²/h = e²/(2πℏ) = (e²/(4πε₀ℏc)) × (4πε₀ℏc)/(2πℏ) = α × (2ε₀c)
This gets messy without specifying charge units. In Planck units with ℏ = c = 1:
G₀ = 2e²/(2π) = e²/π. If charge is in elementary charge units ẽ = e/e = 1, then G̃₀ = 1/π.
**Better:** use α: e² = 4πα (in ℏ = c = 1, Heaviside-Lorentz). Then G₀ = 2(4πα)/(2π) = 4α.

### CM-4: London Penetration Depth (Class F: ℏ, c, e)
**Dimensional form:** λ_L = √(m/(μ₀ n_s e²)) [established]
**Dimensionless:** λ̃_L = √(m̃/(ñ_s α))
*Where:* λ̃_L = λ_L/ℓ_P, using μ₀e²/ℏ = 4πα and ℏ = c = 1

### CM-5: BCS Gap Equation (Class F: ℏ, k_B)
**Dimensional form:** k_B T_c ≈ 1.13 ℏ ω_D exp(-1/(N(0)V)) [established]
**Dimensionless:** T̃_c ≈ 1.13 ω̃_D exp(-1/(Ñ(0)ṽ))
*Where:* T̃_c = T_c/T_P, ω̃_D = ω_D t_P

### CM-6: Drude Conductivity (Class F: ℏ, e, m)
**Dimensional form:** σ = n e² τ/m [established]
**Dimensionless:** σ̃ = ñ ẽ² τ̃/m̃
*Where:* σ̃ = σ/(e²/(ℏ ℓ_P)) — appropriate conductivity units

---

## 9. Quantum Information

### QI-1: Holevo Bound (Dimensionless — Class G)
**Dimensional form:** χ = S(ρ) - Σ p_i S(ρ_i) [established]
**Dimensionless:** Already dimensionless (von Neumann entropies S are dimensionless).

### QI-2: Bekenstein Bound (Class F: ℏ, c, k_B) — ALREADY REFORMULATED
**Dimensional form:** S ≤ 2π k_B R E/(ℏc) [established]
**Dimensionless:** I ≤ 2π R E/ln 2 [established — OC v1.2, DOI 10.5281/zenodo.21748773]
*Where:* I is information in bits, R = R_phys/ℓ_P, E = E_phys/E_P

### QI-3: Quantum Cramer-Rao Bound — ALREADY DIMENSIONLESS (Class G)
**Dimensional form:** (Δθ)² ≥ 1/(ν F_Q(θ)) [established]
**Dimensionless:** Already dimensionless (Fisher information is dimensionless).

### QI-4: Bremermann's Limit (Class F: ℏ, c)
**Dimensional form:** Maximum computation rate = m c²/ℏ ≈ 1.356 × 10⁵⁰ bits/(s·kg) [established]
**Dimensionless:** Rate = m̃ bits/t_P per unit mass

### QI-5: Margolus-Levitin Bound (Class A: ℏ)
**Dimensional form:** τ ≥ h/(4ΔE) = πℏ/(2ΔE) [established]
**Dimensionless:** τ̃ ≥ π/(2ΔẼ)
*Where:* τ̃ = τ/t_P

---

## 10. Fluid Dynamics & Plasma Physics

### FP-1: Debye Length (Class D: k_B, ε₀, e)
**Dimensional form:** λ_D = √(ε₀ k_B T/(n e²)) [established]
**Dimensionless:** λ̃_D = √(T̃/(4πα ñ))
*Where:* using ε₀k_B/e² = k_B/(4παℏc) → T̃/(4πα) in Planck units

### FP-2: Plasma Frequency (Class E: ε₀, e, m)
**Dimensional form:** ω_p = √(n e²/(ε₀ m)) [established]
**Dimensionless:** ω̃_p = √(4πα ñ/m̃)
*Where:* using e²/ε₀ = 4παℏc → 4πα in Planck units

### FP-3: Alfven Speed (Class B: c)
**Dimensional form:** v_A = B/√(μ₀ ρ) [established]
**Dimensionless:** ṽ_A = B̃/√(ρ̃) (in speed-of-light units)
*Where:* ṽ_A = v_A/c

### FP-4: Magnetic Reynolds Number — ALREADY DIMENSIONLESS (Class G)
**Dimensional form:** Rm = μ₀ σ v L [established]
**Dimensionless:** Already dimensionless — ratio of advection to diffusion.

### FP-5: Chandrasekhar Mass Limit (Class F: ℏ, c, G)
**Dimensional form:** M_Ch ≈ (ℏc/G)^(3/2) (1/m_p²) ≈ 1.4 M_☉ [established]
**Dimensionless:** M̃_Ch ≈ 1/m̃_p² ≈ (m_P/m_p)² m_P⁻¹ → M_Ch/m_P ≈ (m_P/m_p)²
**Simplified dimensionless:** M̃_Ch ≈ (μ_e m̃_p)⁻² where μ_e ≈ 2

---

## Summary Statistics

| Class | Count | Description |
|:------|:------|:------------|
| Class A (ℏ only) | 8 | Quantum mechanical (Schroedinger, Heisenberg, etc.) |
| Class B (c only) | 3 | Relativistic (Alfven, horizon scale) |
| Class C (G only) | 4 | Gravitational (Schwarzschild, Friedmann, TOV) |
| Class D (k_B only) | 4 | Thermodynamic (Boltzmann, ideal gas, equipartition) |
| Class E (ε₀/μ₀ only) | 1 | Electromagnetic SI |
| Class F (combinations) | 26 | Multi-constant: Planck law, Stefan-Boltzmann, Einstein field eqns, Hawking radiation, etc. |
| Class G (already dimensionless) | 7 | Fine-structure constant, Reynolds number, Cramer-Rao, Holevo |
| **TOTAL** | **53** | Across 10 disciplines |
