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
BUG_LINK_TEMPLATE = '<a href="{bug_url}">{bug_text}</a>'
BUG_TRACKERS = {
    # bugzilla
    r'bug +(?P<bug_id>\d+)': 'https://bugzilla.mozilla.org/show_bug.cgi?id={bug_id}',
    # github issues
    r'issue +(?P<bug_repo>[a-z1-9-_/]+)#(?P<bug_id>\d+)': 'https://github.com/'
                                                          '{bug_repo}/issue/{bug_id}',
    # github pull requests
    r'pr +(?P<bug_repo>[a-z1-9-_/]+)#(?P<bug_id>\d+)': 'https://github.com/'
                                                       '{bug_repo}/pull/{bug_id}',
}


def setup_bug_trackers(pelican):
    pelican.settings.setdefault('BUG_TRACKERS', BUG_TRACKERS)
    pelican.settings.setdefault('BUG_LINK_TEMPLATE', BUG_LINK_TEMPLATE)


def replace_bug_references(generator):
    """Replace bug references in the article text."""
    bug_trackers = generator.context.get('BUG_TRACKERS')
    bug_template = generator.context.get('BUG_LINK_TEMPLATE')

    if hasattr(generator, 'pages'):
        all_content = chain(generator.pages, generator.hidden_pages,
                            generator.translations, generator.hidden_translations)
    else:
        all_content = chain(generator.articles, generator.translations)

    for page in all_content:
        for tracker_re, template in bug_trackers.items():
            for match in re.finditer(tracker_re, page._content, re.I):
                kwargs = {
                    'bug_text': match.group(0),
                    'bug_url': template.format(**match.groupdict()),
                }
                logger.debug('Found bug: ' + kwargs['bug_text'])
                replacement = bug_template.format(**kwargs)
                page._content = page._content.replace(kwargs['bug_text'], replacement)


def register():
    """Plugin registration."""
    signals.initialized.connect(setup_bug_trackers)
    signals.article_generator_finalized.connect(replace_bug_references)
    signals.pages_generator_finalized.connect(replace_bug_references)
