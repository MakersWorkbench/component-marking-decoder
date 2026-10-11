#!/usr/bin/env python3
"""Copy the tool from the repository root into the Drupal module's assets folder.

Run from anywhere:  python scripts/sync_drupal_module.py

The Drupal module (drupal/tmwb_component_identifier) ships its own copy of the
tool so it can be installed on its own. This script keeps that copy in sync.
It only writes inside the module's assets folder.
"""
import shutil
from pathlib import Path

root = Path(__file__).resolve().parent.parent
assets = root / 'drupal' / 'tmwb_component_identifier' / 'assets'
(assets / 'js').mkdir(parents=True, exist_ok=True)
(assets / 'images').mkdir(parents=True, exist_ok=True)

copied = []
shutil.copy2(root / 'decoder.css', assets / 'decoder.css'); copied.append('decoder.css')
for js in sorted((root / 'js').glob('*.js')):
    shutil.copy2(js, assets / 'js' / js.name); copied.append('js/' + js.name)
for name in ('LICENSE', 'NOTICE'):
    shutil.copy2(root / name, assets / name); copied.append(name)
shutil.copy2(root / 'wiki' / 'images' / 'overview.png', assets / 'images' / 'decoder-overview.png'); copied.append('images/decoder-overview.png')

print('Synced %d files into %s' % (len(copied), assets.relative_to(root)))
for c in copied:
    print('  ', c)
