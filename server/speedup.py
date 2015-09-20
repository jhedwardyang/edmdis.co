from pydub import AudioSegment
import bpm_detection
import argparse
import os.path

# wav (filename), newbpm (>oldbpm)
# returns audiosegment
def ver3(filename,bpm=None):
    oldbpm,peaks = bpm_detection.bpm_detection(filename,3)
    oldsong = AudioSegment.from_wav(filename)
    if(bpm):
        oldbpm = bpm
    # if (oldbpm < 140):
    #     rate1 = 140/oldbpm
    #     song140 = oldsong.speedup(rate1)
    #     song140.export(os.path.splitext(filename)[0] + "-140.wav", format="wav")
    print oldbpm
    if (oldbpm < 127):
        rate2 = 128/oldbpm
        song128 = oldsong.speedup(rate2)
        song128.export(os.path.splitext(filename)[0] + "-128.wav", format="wav")
    else:
        oldsong.export(os.path.splitext(filename)[0] + "-128.wav", format="wav")
    # if (oldbpm < 86):
    #     rate3 = 86/oldbpm
    #     song86 = oldsong.speedup(rate3)
    #     song86.export(os.path.splitext(filename)[0] + "-86.wav", format="wav")
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert wav to faster/slower bpm')
    parser.add_argument('--filename', required=True,
                   help='.wav file for processing')
    args = parser.parse_args()
    ver3 (args.filename);
