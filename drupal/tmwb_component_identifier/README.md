# TMWB Component Identifier (Drupal module)

Embeds the [Component Marking Decoder](https://github.com/MakersWorkbench/component-marking-decoder) into any Drupal 10 or 11 page. The module is branded TMWB (TheMakersWorkbench.com) but is not tied to any particular site or theme.

## What does it do?

- Adds a text filter, **TMWB Component Identifier Embed**. It replaces a placeholder in your content with the tool.
- Loads the tool's CSS and JavaScript through a normal Drupal library, only on pages that use it.
- Adds a short server-rendered description under the tool (optional), because the tool itself is built by JavaScript and search engines and visitors without JavaScript need real text.
- Adds Schema.org `WebApplication` structured data (JSON-LD) to the page head (optional).
- Sizes everything in pixels and resets a theme's global form styles inside the tool, so it looks the same on any theme, including themes that change the root font size.

## Install

1. Copy this folder to `web/modules/custom/tmwb_component_identifier` (or install it with a Composer path repository).
2. Enable it: `drush en tmwb_component_identifier` (or on the Extend page).
3. Go to **Configuration > Content authoring > Text formats and editors**, edit the format your content uses (for example Full HTML), and enable **TMWB Component Identifier Embed**. Open its settings to turn the description and structured data on or off.
4. Clear caches: `drush cr`.

## Use

In the source view of any content that uses that text format, add a placeholder where the tool should appear:

```html
<div class="tmwb-component-identifier"></div>
```

Optional attributes:

| Attribute | Meaning |
|---|---|
| `data-heading="h2"` | Heading level of the tool's title (`h1` to `h6`, default `h2`). The default is `h2` because the page normally has its own `h1`. |
| `data-solo="on"` | Show the tool without the tab bar and intro. |

You can place the placeholder under any heading in a longer page. Only one tool can appear on a page, because the tool mounts on a fixed element id. Extra placeholders are removed.

## Files

```
tmwb_component_identifier.info.yml        module definition
tmwb_component_identifier.libraries.yml   the library (CSS and JavaScript)
tmwb_component_identifier.module          registers the Twig template
config/schema/                            schema for the filter settings
src/Plugin/Filter/                        the text filter
templates/                                mount point and description
css/                                      page integration styles
assets/                                   the tool (copied from the project, see below)
```

## Updating the tool inside the module

The `assets/` folder is a copy of the tool from the repository root. After changing the tool, refresh it from the repository root:

```bash
python scripts/sync_drupal_module.py
```

Then clear caches on your site.

## License

Apache License 2.0, the same as the rest of the project. The `LICENSE` and `NOTICE` files in `assets/` must stay with the tool. See the repository root for the full terms.
