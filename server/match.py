from pydub import AudioSegment
import bpm_detection
import argparse

def match(filename1,filename2):
	song1 = AudioSegment.from_wav(filename1)
	song2 = AudioSegment.from_wav(filename2)
	bpm1,peaks1 = bpm_detection.bpm_detection(filename1,3)
	bpm2,peaks2 = bpm_detection.bpm_detection(filename2,3)
	song1_match = song1
	song2_match = song2
	music = song1_match.overlay(song2_match, position=0)
	return music

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Put songs together')
    parser.add_argument('--filename1', required=True,
                   help='.wav file for processing')
    parser.add_argument('--filename2', required=True,
                   help='.wav file for processing')
    parser.add_argument('--output', required=True,
    				help='.wav output file')
    args = parser.parse_args()
    audseg = match(args.filename1, args.filename2);
    audseg.export(args.output, format="wav")
