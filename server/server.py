import web
import match
import mp3towav
import isolate
import speedup


urls = (
  '/(.*)', 'process'
)
app = web.application(urls, globals())

class process:        
  def GET(self, name):

    user_data = web.input(input_song='../songs/loseyourself.mp3')
    print 'start'

    target_wav = '../songs/' + user_data.input_song[:-4] + '.wav'
    mp3towav.mp3towav(user_data.input_song, target_wav);
    print 'done conversion'

    print 'isolating', target_wav
    isolate.isolate(target_wav)
    print 'done isolation'


    bpm = None
    if user_data.input_song == 'animals.wav':
        bpm = 95
    elif user_data.input_song == 'payphone.wav':
        bpm = 110
    elif user_data.input_song == 'sugar.wav':
        bpm = 121
    elif user_data.input_song == 'loseyourself.wav':
        bpm = 116
    elif user_data.input_song == 'baby.wav':
        bpm = 128

    print 'speeding up', target_wav[:-4] + "_high.wav"
    speedup.ver3(target_wav[:-4] + "_high.wav")
    print 'done speedup'

    hi_wav = target_wav[:-4] + '_high-128.wav'
    audseg = match.match('bg/bg128_pop.wav', hi_wav);
    audseg.export('../www/public/uploads/edm_' + target_wav[9:-4] + "_finalpop.wav", format="wav")

    audseg = match.match('bg/bg128_calvinharris.wav', hi_wav);
    audseg.export('../www/public/uploads/edm_' + target_wav[9:-4] + "_finalcalvin.wav", format="wav")

    audseg = match.match('bg/bg128_oncelydian.wav', hi_wav);
    audseg.export('../www/public/uploads/edm_' + target_wav[9:-4] + "_finaloncelydian.wav", format="wav")
    print 'done export'

    return target_wav[:-4] + "_final.wav"

if __name__ == "__main__":
  app.run()
