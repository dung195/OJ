from copy import deepcopy

from django.contrib.staticfiles.templatetags.staticfiles import static
from lxml import html


def lazy_load(tree):
    blank = static('blank.gif')
    for img in tree.xpath('.//img'):
        src = img.get('src')
        if src.startswith('data'):
            continue
        noscript = html.Element('noscript')
        noscript.append(deepcopy(img))
        img.addprevious(noscript)
        img.set('data-src', src)
        img.set('src', blank)
        img.set('class', img.get('class') + ' unveil' if img.get('class') else 'unveil')
