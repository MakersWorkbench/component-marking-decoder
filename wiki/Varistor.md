# Varistor

A varistor, usually called a **MOV** (metal oxide varistor), is a surge protector. Under normal voltage it barely conducts. When a voltage spike goes above its rating, it suddenly conducts and shunts the spike away from the circuit it protects. You find them across the mains input of power supplies and power strips.

## What does the marking mean?

Take `14D471K`:

- **14**: the disc diameter, 14 mm. Larger discs absorb more surge energy.
- **D**: disc type.
- **471**: the varistor voltage, measured at 1 mA. The first two digits are the value and the third is the number of zeros, so 47 x 10 = 470 V.
- **K**: the tolerance, ±10%.

Another style, from TDK/EPCOS, is `S14K275`: a 14 mm disc, K = ±10%, and **275 V AC** maximum working voltage. (Its 1 mA voltage is about 430 V.)

## How do I use the tab?

1. Click **Varistor**.
2. Type the marking, for example `14D471K`, `10D391K`, `7N271K`, `20D561K`, or `S14K275`.
3. Read the results: varistor voltage, disc size, maximum AC and DC working voltage, clamping range, and whether it suits 120 V or 230 V mains.

## What do the working voltages mean?

- **Max AC working voltage:** the highest continuous AC (RMS) voltage the varistor should see. For a 14D471K this is 300 V.
- **Max DC working voltage:** the highest continuous DC voltage. For a 14D471K, 385 V.
- **Clamping range:** the voltage the part lets through during a big surge, roughly 1.6 to 1.8 times the varistor voltage. This is an estimate.

The AC and DC ratings are derived from standard ratios, about 0.64 and 0.82 times the 1 mA voltage. They match the catalog values for 14D471K (300 V AC, 385 V DC) and S14K275 (275 V AC, 350 V DC), but always confirm against your datasheet.

## Which one fits my mains voltage?

Pick an AC rating at least 10 to 15 percent above your normal supply voltage.

- **120 V mains:** about 150 V AC rating or more (for example 14D241K).
- **230 V mains:** about 275 V AC rating or more (for example 14D431K, also sold as S14K275).

## Gotchas

- **Fuse the line.** A varistor can fail short or overheat after a large surge, so always put a fuse in series on the supply side.
- **They wear out.** Each big surge degrades the part. A varistor that has taken a hit may not protect the next one.
- **Tolerance letters other than K are not confirmed** by the sources used, so the tool flags them. Check the datasheet.
- **Different makers, different codes.** The `14D471K` style is common at several makers. Other makers use other schemes, and the tool recognizes only the formats shown above.

**Safety:** mains voltage is dangerous. This tool is for identifying parts, not for designing mains protection. Use a datasheet and follow your local electrical codes.

## Related guides

[Fuse](Fuse), [Thermistor](Thermistor).
