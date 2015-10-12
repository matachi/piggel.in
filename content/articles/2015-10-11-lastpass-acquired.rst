=======================================
Time to look for a LastPass alternative
=======================================

:date: 2015-10-11 13:00
:tags: LastPass, Pass, KeePass, password manager
:lang: en

A couple of days ago LastPass `announced
<https://blog.lastpass.com/2015/10/lastpass-joins-logmein.html/>`_ that they
have been acquired by the company LogMeIn. Apparently their `long-term goal
<https://investor.logmeininc.com/about-us/investors/news/press-release-details/2015/LogMeIn-to-Acquire-Password-Management-Leader-LastPass/default.aspx>`_
is to merge LastPass with `Meldium <https://www.meldium.com/>`_ which they
acquired last year:

    Following the close of the deal, LogMeIn plans to bring complementary
    capabilities of its early identity management investments, including those
    of Meldium, which it acquired in September 2014, into LastPass.  In the
    near-term, both the Meldium and LastPass product lines will continue to be
    supported, with longer-term plans to center around a singular identity
    management offering based on the LastPass service and brand.

People on `Hacker News <https://news.ycombinator.com/item?id=10359491>`_ and
`Reddit
<https://www.reddit.com/r/sysadmin/comments/3o3c74/logmein_to_acquire_lastpass/>`_
are overall very upset and many are now looking for alternatives to LastPass.
One user made a nice `post
<https://www.reddit.com/r/sysadmin/comments/3o3c74/logmein_to_acquire_lastpass/cvtrzha>`_
with a list of 15 alternative services.

I very much liked LastPass and I have been a premium customer for about 5
years.  LastPass felt like a serious, small company with one single focus which
you could trust. I have no experience with LogMeIn, but people in the above
mentioned comments fields seem to be afraid about the direction they might
steer LastPass in. I think LastPass is more or less feature complete and I
don't like that they will merge it with Meldium. Meldium gives me a bad
feeling.

Two self-managed alternatives I have been looking at are `KeePass
<http://keepass.info/>`_ and `Pass <http://www.passwordstore.org/>`_. Both are
open source and support Linux, Firefox and Android. However, where KeePass is a
Windows application which has been ported to Linux with the help of Mono, Pass
is a more "true" Linux application. I like that Pass is primarily a terminal
application which utilizes GPG for encryption and Git for syncing.

I installed KeePass and the Firefox add-on `KeeFox <http://keefox.org/>`_,
since KeePass seems to be highly popular. However, I think KeePass feels like a
quite bloated and heavy setup, and its GUI radiates a Windows aura which
disgusts me.

.. image:: |filename|/images/keepass.jpg
   :alt: Screenshot of KeePass
   :class: img-responsive center-block

My next step is to give Pass and its Firefox add-on `passff
<https://github.com/jvenant/passff>`_ a shot.

