# Embedding and Customizing

The tool is plain HTML, CSS, and JavaScript with no build step and no dependencies, so it is easy to host, embed, and modify. The conditions are small: keep the license, the copyright and attribution notices, and the NOTICE contents with it, and mark the files you changed (see [License](License)).

## How do I run it locally?

```bash
git clone https://github.com/MakersWorkbench/component-marking-decoder.git
cd component-marking-decoder
python -m http.server 8000
```

Open `http://localhost:8000` in your browser. You can also open `index.html` directly.

## How do I put it on a website?

**Option 1, an iframe.** Upload the folder to your server and embed:

```html
<iframe src="/tools/component-marking-decoder/index.html" title="Component Marking Decoder"
        style="width:100%;min-height:900px;border:0"></iframe>
```

**Option 2, inline.** Copy `decoder.css` and the `js` folder to your site, then add this to your page:

```html
<link rel="stylesheet" href="decoder.css">
<div class="tmwb-dec" id="tmwb-dec"></div>
<script src="js/resistor-logic.js"></script>
<script src="js/smd-logic.js"></script>
<script src="js/cap-logic.js"></script>
<script src="js/ind-logic.js"></script>
<script src="js/parts-data.js"></script>
<script src="js/xtal-logic.js"></script>
<script src="js/passive-logic.js"></script>
<script src="js/app.js"></script>
```

All styles are scoped under `.tmwb-dec`, so the tool will not restyle the rest of your page.

## How do I show just one tab?

Add `?solo` and a tab id after the page address, for example `index.html?solo#cap`. The tab bar and intro are hidden and only that tab shows. The title and the attribution footer always stay.

Tab ids: `res` (Resistor Bands), `smd` (SMD Resistor), `pot`, `net`, `cap`, `tcap`, `ind`, `ferr`, `semi`, `xtal`, `mov`, `therm`, `fuse`, and `about`. A link ending in `#cap` (without `?solo`) opens the full tool on that tab.

## How do I change the title, description, and links?

Open `js/app.js` and edit the `APP` block near the bottom (the project information). It holds the name, intro paragraph, site, repository, wiki, and license links. If you fork the project, point the repository and wiki links at your fork, but keep the "Developed and Maintained by TheMakersWorkbench.com" attribution and the original project link, which carries the NOTICE attribution.

## How do I add a part to the semiconductor list?

Open `js/parts-data.js` and add an entry using the same shape as the others:

```js
add({ id: '1N4148', aliases: ['1N914'], cat: 'Diode', title: 'Small-signal switching diode',
      pkg: 'DO-35 glass axial', polarity: 'Cathode is the banded end.',
      specs: [['Forward drop', '≈0.7 V at 10 mA'], ['Max reverse voltage', '100 V']],
      use: 'General purpose signal diode.', notes: 'Optional extra note.' });
```

Use `pinout:` instead of `polarity:` for transistors and ICs, and add a `marks` list through the `MARKS` table at the bottom for SMD codes. Please cite your source in your pull request.

## Can I use the decoding code in other projects?

Yes. The logic files (`resistor-logic.js`, `smd-logic.js`, `cap-logic.js`, `ind-logic.js`, `passive-logic.js`, `xtal-logic.js`) have no DOM code. They work in the browser and in Node:

```js
const C = require('./js/cap-logic.js');
const r = C.decode('107C');
console.log(C.format(r.pf), r.voltage, r.kind); // 100 µF 16 tantalum
```

Any copy or derivative must keep the license and the NOTICE attribution.

## How do I contribute?

Fork the repository, make your change, and open a pull request. Corrections with a datasheet or standard cited are the most useful.
