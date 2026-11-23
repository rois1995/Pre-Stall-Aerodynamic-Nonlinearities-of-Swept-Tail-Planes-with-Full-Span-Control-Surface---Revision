# Forward-swept moment-reference consistency check

This is a supplementary reproducibility note, **not** a separate manuscript result.

## Source and condition

Original retained postprocessing: `Phase1B.zip / phase1b/tables/component_coefficients.csv`, geometry II, zero dihedral, control deflection 20 degrees, direct RANS states, total (pressure plus viscous) coefficient, incidence 0 and 2 degrees, moments evaluated about the geometry-II numerical aerodynamic center.

- Numerical aerodynamic-center abscissa: `x_A,RANS = -0.003618 m`.
- Experimental aerodynamic-center abscissa: `x_A,WT = -0.0492 m`.
- Geometry-II mean aerodynamic chord: `MAC = 0.6282 m`.
- At incidence 0: `CFz = 0.785133`, `CM_A,RANS = -0.173629`.
- At incidence 2: `CFz = 0.880349`, `CM_A,RANS = -0.156809`.

## Pole transport

With the coefficient-reference area and MAC unchanged, moment transport in the manuscript is

`CM(x1) = CM(x0) + (x1 - x0) * CFz / MAC`.

Between the two states,

`Delta CFz = 0.880349 - 0.785133 = 0.095216`

`Delta CM_RANS,own = -0.156809 - (-0.173629) = +0.016820`.

Moving that increment to the **experimental** center:

`Delta CM_RANS,WTpole = +0.016820 + (-0.0492 - (-0.003618)) * 0.095216 / 0.6282 = +0.0099112`.

The measured moment increment about the experimental aerodynamic center over the same incidence interval is approximately `+0.019` (manuscript, Section V.B). Thus both increments remain positive; the apparent closer agreement of `+0.0168` versus `+0.019` would depend on comparing **different** fitted moment poles.

The manuscript reports `+0.0099` about the experimental moment pole, with the body-normal-force increment shown to make the calculation independently verifiable.

## Interpretation

- This is exact pole transport for the **stored numerical coefficient increments**, to the precision of the archived values.
- It does not modify the surface force, computed pressure field, or any numerical solution.
- It does not create a new verification study or turn the corresponding WT lift disagreement into quantitative agreement.
- Do not transport raw force increments between differing coefficient reference areas or chords; the above formula is applied solely to the geometry-II numerical state with its own normalization.
