# -*- coding: utf-8 -*-
"""
Pelican Link Bugs
=================

Automatic bug tracker linking for Pelican.
"""

import logging
import re
from itertools import chain

from pelican import signals


logger = logging.getLogger(__name__)


def setup_bug_trackers(pelican):
    pelican.settings.setdefault('BUG_TRACKERS', {
        # bugzilla
        r'bug +(?P<bug_id>\d+)': '<a href="https://bugzilla.mozilla.org/show_bug.cgi?id={bug_id}">'
                                 '{bug_text}</a>',
        # github issues
        r'issue +(?P<bug_repo>[a-z1-9-_/]+)#(?P<bug_id>\d+)': '<a href="https://github.com/'
                                                              '{bug_repo}/issue/{bug_id}">'
                                                              '{bug_text}</a>',
        # github pull requests
        r'pr +(?P<bug_repo>[a-z1-9-_/]+)#(?P<bug_id>\d+)': '<a href="https://github.com/'
                                                           '{bug_repo}/pull/{bug_id}">'
                                                           '{bug_text}</a>',
    })


def replace_bug_references(generator):
    """Replace bug references in the article text."""
    bug_trackers = generator.context.get('BUG_TRACKERS')

    content_key = 'pages' if 'pages' in generator.context else 'articles'

    for page in chain(generator.context[content_key], generator.translations):
        for tracker_re, template in bug_trackers.items():
            for match in re.findall(tracker_re, page._content, re.I):
                bug_text = match[0]
                bug_ctx = match.groupdict()
                bug_ctx['bug_text'] = bug_text
                replacement = template.format(**bug_ctx)
                page._content = page._content.replace(bug_text, replacement)


def register():
    """Plugin registration."""
    signals.initialized.connect(setup_bug_trackers)
    signals.article_generator_finalized.connect(replace_bug_references)
    signals.pages_generator_finalized.connect(replace_bug_references)
