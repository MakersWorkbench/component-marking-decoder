# FAQ

## Is it free?

Yes. It is free for personal, educational, and commercial use. See [License](License) for the one requirement (keeping the attribution).

## Does it work on my phone?

Yes. The layout adapts to narrow screens. The tab grid becomes four columns on a phone, and the results stack neatly.

## Does it need an internet connection?

The tool runs entirely in your browser. After the page has loaded, it does not send your input anywhere, and it does not need a server to decode anything. The picture and the data are all part of the page.

## Why did it give me two answers?

Some markings are genuinely ambiguous. `47R` can be an EIA-96 code (3.01 Ω) or 47 Ω written in R notation. A `107C` can be a ceramic capacitor with a tolerance letter or a 100 µF 16 V tantalum. The tool shows both readings (or lets you choose the type) rather than guessing silently.

## It says "tolerance not marked." Why?

Many markings do not encode tolerance. A 3-digit SMD resistor code, for example, only gives the value. Where the style usually implies a tolerance, the tool shows the typical one and says it is an estimate. Otherwise, check the datasheet.

## Why does a part number show a different pinout than my datasheet?

Pinouts can differ between manufacturers, even for the same part number. The cards say which maker's order is shown. Your datasheet is the authority for your part.

## A part I need is not in the Semiconductors list. Can I add it?

You can request it by opening an issue, or add it yourself. Entries live in `js/parts-data.js` in the repository. See the [Embedding and Customizing](Embedding-and-Customizing) page. Please include a source for any numbers.

## Can I put it on my own website?

Yes, for commercial and non-commercial sites. You must keep the attribution line and the license intact and visible. See [License](License) and [Embedding and Customizing](Embedding-and-Customizing).

## Can I change it and add features?

Yes. Modifying and adding are allowed. The attribution and license must remain, and you can add your own credit alongside them.

## Why do I see the attribution footer even in a single-tab view?

The attribution is required by the license, so it stays visible in every view, including the one-tab embed.

## How do I report a bug or a wrong value?

[Open an issue](https://github.com/MakersWorkbench/component-marking-decoder/issues). For a wrong value, please include the datasheet or standard that shows the right one.

## Is this a safety tool?

No. It helps you identify parts and learn marking schemes. For mains circuits, fuses, and surge protection, always confirm against the manufacturer datasheet and follow your local electrical codes.
