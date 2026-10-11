# Resistor Bands

This tab reads the colored stripes on through-hole resistors and works in reverse too.

## How do resistor color bands work?

A resistor is too small to print "4,700 ohms" on it, so manufacturers paint stripes. Each color stands for a number. You read the stripes in order, like digits, and the last stripes tell you a multiplier and how precise the value is.

| Color | Digit | Multiplier | Tolerance | Temp. coefficient |
|---|---|---|---|---|
| Black | 0 | x1 | | 250 ppm/K |
| Brown | 1 | x10 | ±1% | 100 ppm/K |
| Red | 2 | x100 | ±2% | 50 ppm/K |
| Orange | 3 | x1k | | 15 ppm/K |
| Yellow | 4 | x10k | | 25 ppm/K |
| Green | 5 | x100k | ±0.5% | 20 ppm/K |
| Blue | 6 | x1M | ±0.25% | 10 ppm/K |
| Violet | 7 | x10M | ±0.1% | 5 ppm/K |
| Grey | 8 | x100M | ±0.05% | 1 ppm/K |
| White | 9 | x1G | | |
| Gold | | x0.1 | ±5% | |
| Silver | | x0.01 | ±10% | |

A resistor with no tolerance stripe is ±20%.

## How many bands does my resistor have?

| Bands | Stripes mean |
|---|---|
| 3 | digit, digit, multiplier (tolerance is ±20%) |
| 4 | digit, digit, multiplier, tolerance |
| 5 | digit, digit, digit, multiplier, tolerance |
| 6 | digit, digit, digit, multiplier, tolerance, temperature coefficient |

More digits mean a more precise resistor. Five and six band resistors are usually 1% or better.

## How do I decode a resistor?

1. Choose **3 Band**, **4 Band**, **5 Band**, or **6 Band** at the top.
2. Set each dropdown to the color on your resistor, starting from the end where the stripes are closest together.
3. Read **Resistance**, **Minimum**, and **Maximum**. Minimum and Maximum show the range the real resistor can fall in because of its tolerance. A 6-band resistor also shows its **Temperature coefficient**.

The picture updates as you pick colors, with each band labeled (1st Band, 2nd Band, Multiplier, Tolerance, and so on).

**Example, 4 band:** yellow, violet, red, brown. Digits 4 and 7, multiplier x100, so 4,700 ohms, which is 4.7 kΩ. Brown means ±1%. Range 4.653 kΩ to 4.747 kΩ.

**Example, 6 band:** green, blue, black, orange, violet, red. Digits 5, 6, 0, multiplier x1k, so 560 kΩ. Violet means ±0.1%. Red means 50 ppm/K.

## What does temperature coefficient mean?

It says how much the resistance drifts when the temperature changes. 50 ppm/K means that for each degree of temperature change, the resistance changes by 50 parts per million. Most projects never need to think about it. It matters in precision measurement circuits.

## How do I find the colors for a value? (Value to Bands)

1. Click **Value → Bands**.
2. Type a value, for example `4.7kΩ 1%`, `4k7`, `220`, or `2.2M`. Add a tolerance like `1%` if you want one. Add `50ppm` to get a 6-band resistor.
3. Choose **Auto** for the band count, or force 3, 4, 5, or 6.

The tool picks 4 bands when the value needs two digits and the tolerance is 1, 2, 5, or 10 percent. It switches to 5 bands for three-digit values like 4.72 kΩ, or for tolerances of 0.1, 0.25, or 0.5 percent. If you give no tolerance, it assumes 5 percent (1 percent when the value needs three digits).

`0` gives a single black band, which marks a zero-ohm jumper.

## Gotchas

- **Which end is the start?** Read from the end where the stripes are closer together. The tolerance stripe sits slightly apart.
- **Gold and silver as a multiplier.** In the third position of a 4-band resistor they mean x0.1 and x0.01, so brown, black, gold is 1 Ω, not 10.
- **Colors age.** Red can look like orange and brown can look like black on an old part. When in doubt, check the value with a meter.
- **Out of range.** The bands can express about 0.1 Ω up to the gigaohms. The tool will tell you if your value is outside that.

## Related guides

[SMD Resistor](SMD-Resistor) for printed numbers on chip resistors, and [Pot and Trimmer](Pot-and-Trimmer) for adjustable ones.
