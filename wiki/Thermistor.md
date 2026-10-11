# Thermistor

A thermistor is a resistor whose resistance changes a lot with temperature. There are two kinds.

- **NTC** (negative temperature coefficient): resistance **drops** as the temperature rises. Used for temperature sensing and for limiting the surge current when a power supply switches on.
- **PTC** (positive temperature coefficient): resistance **jumps up sharply** above a certain temperature. Used as a self-resetting fuse and in heaters.

## What does the marking mean?

The marking is usually the resistance at 25 °C.

- `103` = 10 x 1,000 = 10 kΩ at 25 °C (the most common value for sensors).
- `502` = 5 kΩ.
- `103AT-2` is a Semitec part: 10 kΩ at 25 °C, with a B value of 3435 K.
- `NTC 10K B3950` means 10 kΩ at 25 °C and a beta of 3950 K.
- `10D-9` is a large inrush limiter: 10 Ω at 25 °C, 9 mm disc.

The **B value (beta)** describes how steeply the resistance changes with temperature. A higher B means a bigger change.

## How do I use the tab?

1. Click **Thermistor**.
2. Type the marking, for example `103`, `NTC 10K B3950`, `103AT-2`, `502 3435`, `10D-9`, or `PTC 120R`.
3. Enter a **temperature in °C** to look up the resistance at that temperature (for example 60).
4. Read the type, resistance at 25 °C, B value, the lookup, and a table of resistance from −20 to 125 °C.

## How does the tool find the resistance at another temperature?

It uses the beta equation: R(T) = R25 x e^(B x (1/T − 1/298.15)), with temperatures in kelvin. For a 10 kΩ, B 3950 sensor, that gives about 2.49 kΩ at 60 °C. The beta equation is accurate to a few percent near room temperature and less so at the extremes. For precise work, use the maker's resistance-temperature table.

## Gotchas

- **No B value?** For a plain NTC like `103`, the tool assumes 3950 K, the common value for 10 kΩ sensor probes, and says so. A different part can have a different B (a 103AT-2 is 3435 K).
- **PTC markings.** The number is the cold resistance at 25 °C. PTC behavior depends on the part's trip temperature, so the tool does not give a curve.
- **Inrush limiters get hot.** A part like `10D-9` heats up in use and lowers its resistance. Mount it clear of other components.
- **A thermistor is not a thermometer by itself.** You need a circuit (usually a voltage divider and an ADC) and a conversion like the one above.

## Related guides

[Fuse](Fuse), [Varistor](Varistor).
