import ascvid
import time
a=ascvid.audio.Audio(ascvid.mp.VideoFileClip("tests/rick.ogv"))
a.play()
time.sleep(5)
a.pause()
time.sleep(1)
a.resume()
time.sleep(5)
