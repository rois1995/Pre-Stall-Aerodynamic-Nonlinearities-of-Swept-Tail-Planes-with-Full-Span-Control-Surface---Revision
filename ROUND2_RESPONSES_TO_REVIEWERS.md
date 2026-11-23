# Responses to reviewers — Second round

**Manuscript:** Pre-Stall Load Redistribution on Swept Tailplane Models with Full-Span Controls

We thank the reviewers for their re-evaluation. The second revision makes the propagated experimental lift uncertainty visible in the reference polar, clarifies the Abstract and geometric terminology, and shortens the paper without removing its principal results. Section and figure references below refer to the revised source. Final page numbers should be checked against the newly compiled manuscript.

## Reviewer 2 — Experimental C_L error bars

**Comment:** Lift error bars are not apparent in Fig. 4 and other experimental curves. Were these errors omitted or are they much smaller than the moment uncertainties?

**Response:** Thank you for identifying an ambiguity in the figure presentation. The supplied lift uncertainties are nonzero and vary with incidence and control deflection. For the reference model at a 20° control deflection, the propagated lift-coefficient uncertainty magnitude at zero incidence is approximately 0.0133. At the scale of the complete polar, some uncertainty bars were difficult to distinguish from the symbols. We have replaced Fig. 4 with a reproducible vector plot that explicitly includes the supplied pointwise propagated error bars for both lift and pitching moment, with distinct markers and end caps. No uncertainty magnitude has been changed or rescaled. The caption now identifies the error bars, and the Methods continue to distinguish the original propagated uncertainties from repeat-run scatter and from the separate uncertainty-sensitivity analysis.

**Final figure check required:** Inspect Fig. 4 in the fully compiled manuscript and check that the corresponding experimental uncertainty bars in the other WT comparison figures remain distinguishable at publication size. Their underlying plotting data include the appropriate uncertainty columns, but the final rendered assets must be inspected before making a stronger claim about all figures.

## Reviewer 1 — Meaning of “63% of the total lift departure”

**Response:** We agree that the term *departure* was insufficiently informative in the Abstract. We now use *shortfall in lift growth relative to the preceding fitted incidence trend*. In the reference numerical case at a 20° control deflection, total lift increases by +0.0242 over 0°–2° incidence, rather than by the +0.1348 expected from the preceding trend. The shortfall is therefore −0.1106, of which −0.0692 (approximately 63%) comes from the fixed surface. That surface nevertheless gains +0.0593 in actual lift. This is a share of the computed lift-growth shortfall, not a loss of total lift or a percentage of its coefficient. The mathematical definition and sensitivity results remain in the Methods, Results and Appendix.

## Reviewer 1 — “Undeformed” terminology

**Response:** We have replaced the confusing wording with *geometric semispan*, *reference semiplanform area*, *spanwise coordinate* and *reference planform*, as appropriate. *Undeflected* is reserved for describing the control in its neutral position. The reference area used in the coefficient normalization remains unchanged when the wing is rotated to the positive-dihedral configuration.

## Reviewer 1 — Abstract specificity

**Response:** We have rewritten the Abstract to communicate concrete findings rather than summarize analyses generically. It specifies the 0.111 lift-growth shortfall, the distinct fixed-surface and control-surface contributions, and the result that the computed 45°-dihedral model has a larger lift increase over the identified 0°–2° interval despite a lower absolute lift. It also identifies the more inboard-concentrated aft-loading changes on the forward-swept planform. The final sentence acknowledges the limited experimental–numerical agreement.

## Reviewer 1 — Wordiness and grid selection

**Response:** We agree and have condensed the article as an integrated argument. The Introduction now synthesizes the relevant literature more directly, the Methods retain reproducibility-critical details without repeating definitions, and the Conclusions are substantially shorter. The cited nominal-grid sentence now reports actual grid sizes, measured grid sensitivity and the computational tradeoff rather than referring vaguely to the demands of the campaign. By the same automated text-count procedure applied before and after this round, the narrative text, including the Appendix but excluding the Abstract, Nomenclature, equations, figure/table contents and references, decreased from approximately **7,700 to 6,150 words**, a reduction of about **20%**.

## Reviewer 1 — Nomenclature repetition

**Response:** We have removed explanations that merely repeat the Nomenclature. We retain the sign and moment-reference conventions, uncertainty provenance, fitted-trend departure definition, and chordwise-shear construction because they are necessary to interpret or reproduce the scientific comparisons, not simply to define symbols.

## Reviewer 1 — Length and full-article focus

**Response:** We appreciate the reviewer's repeated concern. We have materially shortened and focused the paper while preserving the linked evidence that makes it an archival research contribution: the different surface contributions to lift-growth shortfall and pitching moment, the spatial moment-arm explanation, and the different incidence-dependent load distributions with dihedral and sweep. The revision removes repeated narration rather than the analyses needed to substantiate these conclusions. We therefore respectfully retain the full-article format.

## Production checklist (not for submission)

- Recompile the entire manuscript with the bibliography and regenerate the tracked main.pdf. The existing PDF in the repository was not regenerated by this source-only revision.
- Inspect the replacement Fig. 4 and the other experimental comparisons at publication size; verify that all WT error bars are visible.
- Recheck pagination, cross-references, colors/markers, and final page citations in this rebuttal.
- The replacement reference polar reads the original pointwise WT coefficient and uncertainty values from figures_revision_measured_uncertainty_data.csv and the associated LaTeX figure source. Its standalone compilation under the AIAA class has been tested; full-manuscript compilation remains a separate check.
