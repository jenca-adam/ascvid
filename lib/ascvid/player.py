from PIL import Image
import moviepy.editor as mp
import sys
import os
import time
import cursor
import threading
def show_frame(fr,char):
    tw=os.get_terminal_size().columns
    th=os.get_terminal_size().lines

    sys.stdout.write('\033[H')
    sys.stdout.flush()
    d=Image.fromarray(fr)
    d=d.resize((d.width,d.height//2))
    wd=d.width-tw
    hd=d.height-th
    scale=1
    if wd>0 and hd>0 and wd>=hd:
        scale=tw/d.width
    elif wd>0 and hd>0:
        scale=th/d.height
    elif wd>0:
        scale=tw/d.width
    elif hd>0:
        scale=th/d.height

    d=d.resize((int(d.width*scale),int(d.height*scale)))

    pix=d.load()
    lines=[]

    for y in range(d.height):
        line=''
        for x in range(d.width):
            r,g,b,*foo=pix[x,y]
            line+=f"\x1b[38;2;{r};{g};{b}m{char}"
        lines.append(line+'\x1b[0m')
    os.system("clear")
    print('\n'.join(lines))
def play_vid(vid,hide_cursor=True,play_audio=True,fps=None,char="\u2588"):
    vid=mp.VideoFileClip(vid)
    fps = fps or vid.fps
    if fps!=vid.fps and fps!="max":
        vid.set_fps(fps)
    process=None
    if hide_cursor:
        cursor.hide()
    if play_audio and vid.audio is not None:
        thread=threading.Thread(target=vid.audio.preview,daemon=True)
        thread.start()
    os.system("clear")
    try:
        for frame in vid.iter_frames():
            show_frame(frame,char)
            if fps!="max":
                time.sleep(1/fps)
    finally:
        cursor.show()
        sys.stdout.write("\x1b[0m")
        sys.stdout.flush()
        os.system("clear")
            

