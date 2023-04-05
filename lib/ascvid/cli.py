from .player import play_vid
import click

@click.command()
@click.argument("file")
@click.option("--hide-cursor","-H",default=False,is_flag=True,help="Hide the cursor while playing the video")
@click.option("--no-audio","-A",is_flag=True,default=False,help="Don't play audio stream")
@click.option("--fps","-f",default=None,help="Number of FPS the video's supposed to run at. If None, it's determined from the video. If \"max\", ascvid will try its best to keep the video from lagging")
@click.option("--char","-c",default='\u2588',type=str,help="Character to be used while rendering the video frames")
def main(file,hide_cursor,no_audio,fps,char):
    if fps and fps!="max":
        fps=int(fps)
    play_audio=not no_audio
    play_vid(file,hide_cursor,play_audio,fps,char)
