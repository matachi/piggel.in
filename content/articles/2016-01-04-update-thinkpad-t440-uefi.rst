===============================================
Update BIOS/UEFI on ThinkPad T440 running Linux
===============================================

:date: 2016-01-04 16:00
:tags: ThinkPad, Linux, UEFI
:lang: en
:slug: update-thinkpad-t440-uefi

I have a ThinkPad T440 with only Fedora installed. The UEFI-version I had
installed was version 2.32, which I installed almost a year ago. Since then
several new versions have been released, where 2.36 is the very latest when
typing this. The following steps are what I did to update the UEFI/BIOS on my
laptop.

Be warned though, you might brick the computer and/or void its warranty. This
worked for me, but I cannot guarantee it will work for you.

1. Visit Lenovo's `support page
   <http://support.lenovo.com/uu/en/products/laptops-and-netbooks/thinkpad-t-series-laptops/thinkpad-t440?tabName=downloads>`_
   and download "BIOS Update Bootable CD." In my case, with 2.36, it is called
   ``gjuj23us.iso``.

2. Download `geteltorito.pl
   <http://userpages.uni-koblenz.de/~krienke/ftp/noarch/geteltorito/geteltorito.pl>`_::

    $ wget http://userpages.uni-koblenz.de/~krienke/ftp/noarch/geteltorito/geteltorito.pl

3. Extract from the .iso-file a USB compatible image::

    $ perl geteltorito.pl -o bios.iso gjuj23us.iso

4. Write the image to your USB stick::

    $ sudo dd if=bios.iso of=/dev/sdX bs=512K

   **WARNING!** Be very careful with what drive you write to, i.e. sd\ **X**!
   It will completely overwrite all partitions on that media, so make sure it
   is not your OS, backup HDD, etc.

5. Now reboot the computer, press F12 at startup and choose to boot the USB
   stick. You will now enter the UEFI/BIOS updater. Follow its instructions and
   read the information pages carefully.

6. Done!

Visit `this <http://www.thinkwiki.org/wiki/BIOS_update_without_optical_disk>`_
page and `this
<http://mattoncloud.org/2014/05/15/fedora-20-on-a-thinkpad-x1-carbon/>`__ page
for additional information. Those are the two sources I used.

