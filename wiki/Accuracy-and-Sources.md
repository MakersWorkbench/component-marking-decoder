# Accuracy and Sources

How much should you trust what the tool tells you? This page explains how the data was checked and where you need to be careful.

## How was it checked?

Every table and value in the tool was audited against published sources: manufacturer datasheets, distributor references, and standards documents. Where a value could not be confirmed, it was reworded, flagged, or removed. The full record, with a link for each item, is in [SOURCES.md](https://github.com/MakersWorkbench/component-marking-decoder/blob/main/SOURCES.md).

The checks found and fixed real mistakes, for example a wrong capacitor voltage code, color-code tolerance entries that no source supported, and several ratings that vary between makers. Fixing those is the point of keeping a public record.

## What is solid?

- **Color codes and value tables:** resistor colors, the E24 and E96 series (checked value by value against the published list), EIA-96 multipliers, capacitor tolerance letters, and EIA voltage codes.
- **Standards-based codes:** IEC 60127 fuse breaking capacity and speed codes, and the common SMD value codes.
- **Datasheet-backed examples:** the varistor ratings for the `14D471K` and `S14K275`, and the 10.7 MHz filter dot colors.

## What varies between manufacturers?

- **Pinouts.** Some TO-92 parts are wired one way at one maker and the opposite at another (the BC547, 2N3904, PN2222A, and S8050 are examples). The tool states which maker's order it shows.
- **SMD marking codes.** The same part can carry different codes from different makers, and makers often add a prefix or a date code.
- **Ratings.** Maximum current and voltage for the same part number can differ between makers (for example the AMS1117 regulator).

## What is estimated?

- **Tolerance read from an SMD marking.** Most markings do not encode tolerance, so the tool gives the typical one for that style and says so.
- **Varistor AC and DC ratings and clamping range.** Calculated from standard ratios, matched against catalog parts.
- **Thermistor resistance at a temperature.** Uses the beta model.
- **Crystal load capacitors.** Assume about 4 pF of stray capacitance.

## What could not be confirmed?

These are worded cautiously, flagged, or left out:

- The exact value of lowercase `a` in EIA-198 (2.6 in the DigiKey table, 2.5 in some others).
- The Murata resonator characters after the frequency field (tolerance, load capacitance, packaging).
- A few part pin numbers for the LM2596 and MCP1700 (the tool prompts you to check the datasheet).
- Varistor tolerance letters other than K.

## How should I use the results?

1. Treat the tool as a fast first answer and a way to learn the pattern.
2. For anything that matters (a design limit, a safety part, a mains circuit), **confirm with the manufacturer datasheet** for your exact part.
3. When in doubt, measure the part out of circuit with a meter.

## Found a mistake?

Please [open an issue](https://github.com/MakersWorkbench/component-marking-decoder/issues) and cite the datasheet or standard. Corrections with a source are the fastest to fix, and they get added to the public record.
