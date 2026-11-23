# Responses to reviewers — Second round

**Manuscript:** Pre-Stall Load Redistribution on Swept Tailplane Models with Full-Span Controls

We thank the reviewers for their re-evaluation. The second revision makes the propagated experimental lift uncertainty visible in the reference polar, clarifies the Abstract and geometric terminology, and shortens the paper without removing its principal results. Section and figure references below refer to the revised source. Final page numbers should be checked against the newly compiled manuscript.

## Reviewer 2 — Experimental C_L error bars

**Comment:** Lift error bars are not apparent in Fig. 4 and other experimental curves. Were these errors omitted or are they much smaller than the moment uncertainties?

**Response:** Thank you for identifying an ambiguity in the figure presentation. The supplied lift uncertainties are nonzero and vary with incidence and control deflection. For the reference model at a 20° control deflection, the propagated lift-coefficient uncertainty magnitude at zero incidence is approximately 0.0133. At the scale of the complete polar, some uncertainty bars were difficult to distinguish from the symbols. We regenerated Fig. 4 with smaller symbols and clearer error-bar caps, and regenerated the WT comparisons in Figs. 5, 11 and 15 using their archived plotted-data records; both $C_L$ and $C_M$ carry their original pointwise propagated uncertainty magnitudes. All four plots use the manuscript's DejaVu Serif/STIX figure style. No uncertainty magnitude has been changed or rescaled. The caption now identifies the error bars, and the Methods continue to distinguish the original propagated uncertainties from repeat-run scatter and from the separate uncertainty-sensitivity analysis.

**Verification:** The regenerated figures preserve the frozen experimental and computed coefficients and original propagated WT uncertainties. The three comparison figures were built successfully in GitHub and visually inspected from the same plotting code. Their small error bars remain physically small at full-polar scale; the Fig. 4 caption also reports a representative $u(C_L)$. 

## Reviewer 1 — Meaning of “63% of the total lift departure”

**Response:** We agree that the term *departure* was insufficiently informative in the Abstract. We now use *shortfall in lift growth relative to the preceding fitted incidence trend*. In the reference numerical case at a 20° control deflection, total lift increases by +0.0242 over 0°–2° incidence, rather than by the +0.1348 expected from the preceding trend. The shortfall is therefore −0.1106, of which −0.0692 (approximately 63%) comes from the fixed surface. That surface nevertheless gains +0.0593 in actual lift. This is a share of the computed lift-growth shortfall, not a loss of total lift or a percentage of its coefficient. The mathematical definition and sensitivity results remain in the Methods, Results and Appendix.

## Reviewer 1 — “Undeformed” terminology

**Response:** We have replaced the confusing wording with *geometric semispan*, *reference semiplanform area*, *spanwise coordinate* and *reference planform*, as appropriate. *Undeflected* is reserved for describing the control in its neutral position. The reference area used in the coefficient normalization remains unchanged when the wing is rotated to the positive-dihedral configuration.

## Reviewer 1 — Abstract specificity

**Response:** We have rewritten the Abstract to state the principal physical findings directly, without relying on undefined symbols, exact incidence intervals or an inventory of numerical values. It now explains that the fixed surface continues gaining lift while accounting for about two-thirds of the **total** lift-growth shortfall relative to the preceding incidence trend; the control contributes more strongly to the pitching-moment departure. It also specifies the incidence-dependent dihedral effect and the inboard-concentrated aft-loading changes of the forward-swept planform, and keeps the central evidence in plain scientific language. The detailed numerical comparisons and their accuracy context remain in the Results.

## Reviewer 1 — Wordiness and grid selection

**Response:** We agree and have condensed the article as an integrated argument. The Introduction now synthesizes the relevant literature more directly, the Methods retain reproducibility-critical details without repeating definitions, and the Conclusions are substantially shorter. The cited nominal-grid sentence now reports actual grid sizes, measured grid sensitivity and the computational tradeoff rather than referring vaguely to the demands of the campaign. By the same automated text-count procedure applied before and after this round, the narrative text, including the Appendix but excluding the Abstract, Nomenclature, equations, figure/table contents and references, decreased from approximately **7,655 to 5,048 words**, a reduction of about **34%**. This count includes the Results and Appendix concision pass, not only the Introduction and Methods.

## Reviewer 1 — Nomenclature repetition

**Response:** We have removed explanations that merely repeat the Nomenclature. We retain the sign and moment-reference conventions, uncertainty provenance, fitted-trend departure definition, and chordwise-shear construction because they are necessary to interpret or reproduce the scientific comparisons, not simply to define symbols.

## Reviewer 1 — Length and full-article focus

**Response:** We appreciate the reviewer's repeated concern. We have materially shortened and focused the paper while preserving the linked evidence that makes it an archival research contribution: the different surface contributions to lift-growth shortfall and pitching moment, the spatial moment-arm explanation, and the different incidence-dependent load distributions with dihedral and sweep. The revision removes repeated narration rather than the analyses needed to substantiate these conclusions. We therefore respectfully retain the full-article format.

## Scientific consistency of the final manuscript

The updated planform discussion compares numerical and experimental pitching-moment increments about a common pole. The computed increment is approximately +0.0168 about its own fitted aerodynamic center and +0.0099 after transport to the experimental center, using the archived body-normal-force increment; the experimental increment is approximately +0.019. Both remain positive, while the quantitative comparison is now reference-consistent. The surface-load analysis, source data, and conclusions about load redistribution are unchanged.

The revision also avoids implying that lifting-line and vortex-lattice approaches cannot predict spanwise loading or moment arms. The dihedral discussion continues to emphasize its measured and computed force/moment contributions, with force projection used only as supporting context.

## Production checks

- Final manuscript source, data-driven Fig. 4, and regenerated Figs. 5, 11 and 15 are committed to main.
- The article-wide LaTeX diff against commit `32a95a48` is compiled and stored under `revision_materials/`.
- The tracked `main.pdf` should be verified against the latest commit's source after its compilation workflow finishes.
- Separate Reviewer 1 and Reviewer 2 response PDFs use the previously established LaTeX response-letter structure; final page numbers may be inserted after checking the newly compiled manuscript.
