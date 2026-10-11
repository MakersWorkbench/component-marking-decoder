# Semiconductors

This tab is a lookup, not a calculator. Type a part number and it shows what the part is, which way round it goes, its main ratings, and what it is used for. It covers about 120 common diodes, transistors, MOSFETs, voltage regulators, and ICs.

## How do I use the tab?

1. Click **Semiconductors**.
2. Type a part number, such as `1N4007`, `SS34`, `BAT54`, `BC547`, `IRF540N`, `7805`, `LM317`, or `555`. Dashes and spaces are ignored, and the tool matches on part and family names.
3. You can also type the short code printed on a surface-mount (SMD) part, such as `L4`, `A7`, `M7`, or `1AM`.
4. Pick a result from the list. Use the filter chips (**All, Diodes, Transistors, MOSFETs, Regulators, ICs**) to narrow a broad search.

The detail card shows: package, polarity or pinout, the main specifications, typical use, and notes.

## What categories are included?

- **Diodes:** signal (1N4148, BAV99, BAS16), rectifiers (1N4001 to 1N4007, 1N5400 to 1N5408, M7), Schottky (1N5817 to 1N5819, SS12 to SS36, BAT54), and zeners (1N4728 to 1N4757).
- **Transistors:** 2N3904, 2N3906, PN2222A, BC547, BC557, BC337, BC327, BC847, BC857, S8050, S8550, TIP120, TIP31C, TIP32C, 2N3055.
- **MOSFETs:** 2N7000, BS170, IRF540N, IRFZ44N, IRLZ44N, IRF520, IRF9540N, FQP30N06L, AO3400, AO3401.
- **Regulators:** 7805 and the rest of the 78xx and 79xx families, 78L05, LM317, AMS1117, LM1117, MCP1700, TL431, LM2596.
- **ICs:** NE555, LM358, LM393, TL072, LM386, ATmega328P, 74HC595, L293D, ULN2003.

## How do I find which way round a diode goes?

The card has a **Polarity** row. For most leaded diodes, the **band** is the **cathode**, and current flows from the anode (no band) to the cathode (band) when the diode conducts. Surface-mount diodes show a stripe at the cathode end.

## How do I read a TO-92 transistor pinout?

Hold the part with the flat face toward you and the legs pointing down. Read the legs left to right. The card spells out the order, for example "E, B, C" for emitter, base, collector.

## What are SMD marking codes?

A tiny SOT-23 transistor or diode has room for only a code, not the full part number. For example `L4` is a BAT54 Schottky diode, `A7` is a BAV99, `1AM` is a common MMBT3904 marking, and `T4` is a 1N4148W. You can search by that code. The card shows the **SMD marking** row.

## Gotchas

- **Pinouts differ between manufacturers.** Some TO-92 parts are E-B-C at one maker and C-B-E at another (the BC547 is a well-known example), and the 2N7000 and BS170 differ too. The cards say which maker's order they show. Always check the datasheet for the part in your hand, or test with a meter's diode mode.
- **Marking codes differ by maker.** The same part can carry different SMD codes. The tool lists the common ones and says they vary.
- **Values are typical and rounded.** They are not a substitute for the datasheet, especially for design limits.
- **A part may not be in the list.** If you get no match, try the base part number without package or manufacturer suffixes.

## Related guides

[Accuracy and Sources](Accuracy-and-Sources), [Crystals and Resonators](Crystals-and-Resonators).
