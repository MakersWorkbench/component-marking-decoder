# Capacitor

Capacitors come in many types, and each type is marked differently. This tab decodes the markings on ceramic, film, SMD, tantalum, and electrolytic capacitors, and converts between pF, nF, and µF.

## What units does a capacitor use?

| Unit | Symbol | In farads |
|---|---|---|
| Picofarad | pF | 10⁻¹² |
| Nanofarad | nF | 10⁻⁹ |
| Microfarad | µF | 10⁻⁶ |

1 µF = 1,000 nF = 1,000,000 pF. Most codes are in picofarads, and the tool shows the answer in pF, nF, and µF.

## How do I use the tab?

1. Click **Capacitor**. Leave **Code → Value** selected.
2. Choose the **type** pill that matches your part, or leave it on **Auto**: SMD ceramic, SMD tantalum, Radial tantalum, SMD electrolytic, Radial electrolytic, Ceramic disc, or Film. The picture and the polarity notes change with the type.
3. Type the marking.
4. Read **Capacitance**, the conversions, **Tolerance**, **Voltage**, and the working.

To go the other way, click **Value → Code** and type something like `100nF`, `0.1uF`, or `4.7pF`. You get the code to look for.

## What do the common markings mean?

### 3-digit code (ceramic and film)

The first two digits are the value in pF and the third is the number of zeros.

- `104` = 10 followed by four zeros = 100,000 pF = 100 nF = 0.1 µF.
- `223` = 22,000 pF = 22 nF.
- `105` = 1,000,000 pF = 1 µF.
- If the third digit is **8** the multiplier is x0.01, and **9** means x0.1. So `229` is 2.2 pF.

### Tolerance letter

A letter after the digits gives the tolerance. `104K` is 100 nF ±10%.

| Letter | Tolerance |
|---|---|
| B | ±0.1 pF |
| C | ±0.25 pF |
| D | ±0.5 pF |
| F | ±1% |
| G | ±2% |
| H | ±3% |
| J | ±5% |
| K | ±10% |
| M | ±20% |
| P | +100% / −0% |
| Z | +80% / −20% |

### Voltage prefix

Some parts add a two-character voltage code in front. `2A104J` is 100 nF, ±5%, 100 V, because `2A` means 100 V. The tool's reference tables list all the voltage codes (for example `1H` = 50 V, `1E` = 25 V, `2E` = 250 V).

### Notation with a unit letter

A unit letter can replace the decimal point. `4n7` is 4.7 nF, `4p7` is 4.7 pF, and `u47` is 0.47 µF.

### EIA-198 (two characters, SMD)

Tiny ceramic and tantalum chips sometimes use a letter and a digit. The letter is the value from a table and the digit is the power of ten, in pF. `S3` is S = 4.7, times 10³ pF, so 4.7 nF. The letters are case sensitive. The full letter table is in the tool's reference section.

### SMD tantalum

- **Capacitance code first, voltage letter after:** `107C` = 100 µF, C = 16 V. `475A` = 4.7 µF, A = 10 V. `226V` = 22 µF, V = 35 V.
- **Voltage letter first:** `G475` = 4.7 µF at 4 V.
- A second line, if there is one, is a lot or date code and can be ignored.
- Voltage letters: e = 2.5 V, G = 4 V, J = 6.3 V, A = 10 V, C = 16 V, D = 20 V, E = 25 V, V = 35 V, T or H = 50 V.

### Printed in full (electrolytic and radial tantalum)

Large capacitors have room for the value, so they print it. Examples: `100uF 25V`, `470uF 25V 105°C` (the last number is the temperature rating), `100 16` (100 µF, 16 V), `2.2 25+` (2.2 µF, 25 V, + marks the positive lead).

## How do I tell which end is which? (Polarity)

Ceramic and film capacitors are not polarized, so either way round works. The others are polarized and **reversing them can destroy them**:

- **Tantalum (SMD):** the stripe or bevel marks the **positive** end.
- **Radial tantalum:** a **+** is printed next to the positive lead.
- **Aluminum electrolytic:** the stripe (SMD: the dark bar or tinted segment on top) marks the **negative** end. On a new leaded part, the shorter lead is negative.

The tool draws each type with these markings labeled.

## Gotchas

- **`107C` could be two things.** A `C` after three digits can be a ceramic tolerance (±0.25 pF) or a tantalum 16 V code. The tool treats it as tantalum when the value is 1 µF or larger. Choose a type to force it.
- **Bare `100 16`.** Two plain numbers are read as µF and volts, because that is how printed electrolytics look. A 3-digit number not ending in 0 with a voltage, like `104 50`, is read as a ceramic code plus 50 V.
- **Most SMD ceramics are unmarked.** If there is no print, measure it with a capacitance meter.
- **Lowercase `a` in EIA-198.** The DigiKey table lists it as 2.6, while some others show 2.5. The tool tells you when it sees `a`.

## Related guides

[Trimmer Capacitor](Trimmer-Capacitor), [Inductor](Inductor), [Accuracy and Sources](Accuracy-and-Sources).
