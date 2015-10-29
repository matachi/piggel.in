=================================================
CalDAV and CardDAV synchronization in Thunderbird
=================================================

:date: 2015-10-29 15:30
:tags: CalDAV, CardDAV, Thunderbird, mail, ownCloud
:lang: en
:slug: caldav-and-carddav-sync-in-thunderbird

I have `Thunderbird <https://apps.fedoraproject.org/packages/thunderbird>`_
38.3.0 installed from Fedora's repository (``# dnf install thunderbird``), and
my plan is to use it more frequently in the future for my mail. I have one
professional email account on `Namecheap
<https://www.namecheap.com/hosting/email.aspx>`_ with my own domain address,
one student email account on my university and one general email account on
Gmail. The point with using Thunderbird would be to unify these three accounts
into one program to make it more manageable.

One critical step for this to work is to get CardDAV integration in
Thunderbird. I'm running a `DigitalOcean <https://www.digitalocean.com/>`_ VPS
with CentOS 7 where I have `ownCloud <https://owncloud.org/>`_ installed, which
I'm using for syncing files to my `computers
<https://software.opensuse.org/download/package?project=isv:ownCloud:desktop&package=owncloud-client>`_
and my `phone
<https://f-droid.org/repository/browse/?fdfilter=owncloud&fdid=com.owncloud.android>`_.
However, I'm also using ownCloud as a CardDAV and CalDAV server for storing and
syncing my contacts and scheduled calendar events.

On hover.com I found a very good and short `guide
<https://help.hover.com/entries/64466064-CalDAV-and-CardDAV-Synchronization-for-Thunderbird>`_
(backed up to [1]_ and [2]_) for how to get CalDAV and CardDAV synchronization
through the Thunderbird extensions `Lightning
<https://addons.mozilla.org/en-US/thunderbird/addon/lightning/>`_ and `SOGo
Connector <http://www.sogo.nu/english/downloads/frontends.html>`_. It worked
great, and at a first glance the syncing seems to work flawlessly. Note though
that it seems important to first set up CalDAV to be able to do the CardDAV
synchronization.

.. [1] `<https://archive.is/TZfja>`_
.. [2] `<https://web.archive.org/web/20150910162914/https://help.hover.com/entries/64466064-CalDAV-and-CardDAV-Synchronization-for-Thunderbird>`_

