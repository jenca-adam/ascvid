.. image:: asc.png

``ascvid`` is an ASCII video player with quite exact results. It is mostly advised to be used under Linux, but it might work on Mac too.
Here is a little showcase of what it can do: 

.. image:: rick.gif

It requires a Truecolor terminal to work. The produced graphics aren't blinking as in other ASCII video players, however, the videos might lag a bit if your terminal is zoomed out.
``ascvid`` also supports audio! It's a true video player.

Installation
============

.. code-block:: console
   
   python3 -m pip install ascvid

CLI Options
===========

.. code-block:: console
        
   Usage: python -m ascvid [OPTIONS] FILE

        Options:
          -H, --hide-cursor  Hide the cursor while playing the video
          -A, --no-audio     Don't play audio stream
          -f, --fps TEXT     Number of FPS the video's supposed to run at. If None,
                             it's determined from the video. If "max", ascvid will try
                             its best to keep the video from lagging
          -c, --char TEXT    Character to be used while rendering the video frames
          --help             Show this message and exit.





