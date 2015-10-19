=========================
Installed pass and passff
=========================

:date: 2015-10-19 11:20
:tags: pass, passff, password manager
:lang: en

The other day `I wrote <{filename}2015-10-11-lastpass-acquired.rst>`_ that I
were looking at LastPass alternatives. At that time I had given KeyPass a shot,
but now I have had time to try `pass <http://www.passwordstore.org/>`_ and its
Firefox extension `passff <https://github.com/jvenant/passff>`_. Compared to
LastPass and KeyPass, it's an extremely lightweight setup, which I really like.

Exporting your passwords from LastPass is very easy:

1. Visit `<https://lastpass.com/?&ac=1>`_.
2. Expand *Tools* in the left sidebar.
3. Expand *Advanced tools*.
4. Select *Export*.
5. A new window opens with your passwords as a .csv table.
6. Hit *Ctrl+S* to save it to your HDD.

I know that there's a `Ruby script
<http://git.zx2c4.com/password-store/tree/contrib/importers/lastpass2pass.rb>`_
for importing LastPass passwords into pass. However, I got an error when I
tried to run it and I'm not fluent with Ruby. So rather than trying to
understand the script, I wrote a short Python script that goes through the
password list and imports them into pass according to my own preferences:

.. raw:: html

    <script src="https://gist.github.com/matachi/f52257bfee070023b134.js"></script>

Run it in the following way::

    $ chmod u+x lastpass2pass.py
    $ ./lastpass2pass.py my_passwords.csv

And they are now imported into pass!

**Note**, I have only written the script for my own needs on my own machine. I
recommend you to go through the imported passwords to verify that they look as
you expect. For example, count them (use ``pass | wc -l`` to get a rough
count), check the passwords' metadata if it's all there, check Unicode
characters, check special characters in your passwords, etc. I don't guarantee
anything, so I recommend you to read through the script and tweak it to your
own taste.

Installing pass on Fedora is super easy::

    $ sudo dnf install pass

What took me some time to figure out is that pass relies on ``gpg2``, and
**not** ``gpg``. So you will need to create a key with ``gpg2 --gen-key``. Then
get the key's ID::

    $ gpg2 --list-keys
    /home/matachi/.gnupg/pubring.kbx
    --------------------------------
    pub   rsa2048/79474561 2015-10-18
    uid         [ultimate] My name <email@example.com>
    sub   rsa2048/C623D74B 2015-10-18

And init pass with the key ID::

    $ pass init 79474561

Now look at `<http://www.passwordstore.org/>`_ and
`<http://git.zx2c4.com/password-store/about/>`_ to a sense of what you can do
with pass.
