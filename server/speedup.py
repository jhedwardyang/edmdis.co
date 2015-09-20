from pydub import AudioSegment
import bpm_detection
import argparse

# wav (filename), newbpm (>oldbpm)
# returns audiosegment
def speed(wav, newbpm):
	oldbpm,peaks = bpm_detection.bpm_detection(wav,3)
	oldsong = AudioSegment.from_wav(wav)
	print oldbpm
	print newbpm
	rate = int(newbpm)/oldbpm

	print rate
	newsong = oldsong.speedup(rate)
	return newsong

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert wav to faster/slower bpm')
    parser.add_argument('--filename', required=True,
                   help='.wav file for processing')
    parser.add_argument('--bpm', required=True,
    				help='bpm int')
    parser.add_argument('--output', required=True,
    				help='.wav output file')
    args = parser.parse_args()
    audseg = speed(args.filename, args.bpm);
    audseg.export(args.output, format="wav")
