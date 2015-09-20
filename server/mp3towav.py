# edmdis.co

# USAGE
# mp3towav(filename, output), returns nothing, saves to file output
#   filename: .mp3
#   output: output .wav
# OR
# python mp3towav.py --filename <.mp3> --output <.wav>

from pydub import AudioSegment
import argparse

def test():
	print 'asdf'

def mp3towav(filename, output):
	song = AudioSegment.from_mp3(filename);
	song.export(output, format="wav")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert .mp3 to wav')
    parser.add_argument('--filename', required=True,
                   help='.mp3 file for processing')
    parser.add_argument('--output', required=True,
    				help='.wav file for output')
    args = parser.parse_args()
    mp3towav(args.filename, args.output);
