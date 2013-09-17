pelican-list-bugs
=================

Automatically link bug/issue references in content to a tracker.

By default it will link pull-requests and issues for github
in the following formats::

    * I should reiview PR mozilla/bedrock#1.
    * Don't forget to watch issue twbs/bootstrap#2.

It will also link to Mozilla's bugzilla instance::

    Need a laugh? Read bug 765645.

You can easily replace these or add to them with a setting:

.. code:: python

    BUG_TRACKERS = {
        # key is the regex
        r'issue +(?P<bug_repo>[a-z1-9-_/]+)#(?P<bug_id>\d+)':
        # value is URL template with keywoard substitutions
        'https://github.com/{bug_repo}/issue/{bug_id}',
    }

You can also import ``BUG_TRACKERS`` from ``pelican_bugs`` and modify it.
If you need to alter how the links look, you can set ``BUG_LINK_TEMPLATE``.
The link template can use ``bug_url`` and ``bug_text`` keywords:

.. code:: python

    # default template
    BUG_LINK_TEMPLATE = '<a href="{bug_url}">{bug_text}</a>'
