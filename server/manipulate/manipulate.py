# Pydub from https://github.com/jiaaro/pydub#installation

# USAGE
# manipulate(filename, output), returns nothing, saves to file output
#   filename: .wav
#   output: output .wav
# OR
# python manipulate.py --filename <.wav> --output <.wav>


from pydub import AudioSegment
import argparse

def manipulate(filename, output):
	song = AudioSegment.from_wav(filename)
	# song = AudioSegment.from_mp3("never_gonna_give_you_up.mp3")

	animals = AudioSegment.from_wav("../animals.wav")
	beat = AudioSegment.from_wav("../bg128bmp.wav")
	bass = beat.append(beat, crossfade=100).append(beat, crossfade=100)
	music = animals.overlay(bass, position=620)
	music.export("woot.wav", format="wav")



	# pydub does things in milliseconds
	ten_seconds = 10 * 1000

	first_10_seconds = song[:ten_seconds]

	last_5_seconds = song[-5000:]
	# boost volume by 6dB
	beginning = first_10_seconds + 6

	# reduce volume by 3dB
	end = last_5_seconds - 3

	without_the_middle = beginning + end

	without_the_middle.duration_seconds == 15.0
	
	# 1.5 second crossfade
	with_style = beginning.append(end, crossfade=1500)

	# repeat the clip twice
	do_it_over = with_style * 2

	# 2 sec fade in, 3 sec fade out
	awesome = do_it_over.fade_in(2000).fade_out(3000)

	awesome.export(output, format="wav")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process .wav file to do fun stuff.')
    parser.add_argument('--filename', required=True,
                   help='.wav file for processing')
    parser.add_argument('--output', required=True,
    				help='.wav file for output')

    args = parser.parse_args()

    manipulate(args.filename, args.output);
