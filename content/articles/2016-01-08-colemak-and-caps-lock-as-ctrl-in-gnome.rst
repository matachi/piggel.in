====================================================================================
How to set Caps Lock as Ctrl with Colemak keyboard layout in Gnome 3—the correct way
====================================================================================

:date: 2016-01-08 15:00
:tags: Linux, Gnome, Colemak, Ctrl
:lang: en
:slug: caps-lock-as-ctrl-with-colemak-in-gnome-3

The keyboard layout Colemak comes built-in on all Linux distributions I have
tried, making it easy for me as a Colemak user to settle in. The only thing I
change with regards to the keyboard layout is the position of the Ctrl key,
which is placed in the same place as in Qwerty. I am used to have it where the
Caps Lock is located, making it more reachable which I find very appealing
being a Vim and terminal user.

Colemak made Caps Lock act as an additional Backspace key. I agree that it is
more useful than Caps Lock, however, in Vim and in Bash there are so many ways
to delete text that leaving the home row is seldom necessary. To set the Caps
Lock key to act as Ctrl, we first need to install Gnome Tweak Tool::

    $ sudo dnf install gnome-tweak-tool

Next, open Gnome Tweak Tool and select *Typing* from the sidebar.

Here there are several ways to make Caps Lock to act as Ctrl. However, through
my time as a Colemak user, I have discovered that a couple of those options are
faulty.

* **Caps Lock key behavior > Make Caps Lock an additional Ctrl**.

  This option causes strange behaviors in PyCharm. Try to edit your keymap by
  adding a keyboard shortcut to any action. When pressing down Caps Lock it
  appears as ``Caps Lock``; then press down an additional key, for instance A,
  and it appears as ``Ctrl + A``.

  I believe this is the cause of some strange behavior with the Switcher, which
  is trigged by pressing ``Ctrl + Tab``. When releasing the keys the Switcher
  is not closed.  Instead you have to press ``Enter`` to confirm the tab
  switch, which is really annoying.

* **Ctrl key position > Swap Ctrl and Caps Lock**.

  This option causes problems in Gnome Terminal. When pressing ``Ctrl +
  Shift``, which is required when for instance pasting text with ``Ctrl + Shift
  + V``, the letter in front of the cursor is deleted. I guess that Colemak's
  original behavior for the Caps Lock key, i.e. Backspace, takes precedence for
  a moment.

* **Ctrl key position > Caps Lock as Ctrl**.

  This option works fine in both PyCharm and Gnome Terminal.

Please share your own experiences if you are one of the minority with this
fringe setup. Sadly I do not (yet) have a comment field on this blog, but I can
be reached on Twitter at `@DanielJonss <https://twitter.com/DanielJonss>`_.

