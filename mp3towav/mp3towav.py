# CMD line arguments:
# - file name (str)
# - interval (slicing the audio into *interval* second pieces)

from pydub import AudioSegment
import sys

def mp3towav(file_name, interval = None):
    if file_name.endswith('.mp3'):
        fin = AudioSegment.from_file("raw/%s.mp3" % file_name[:-4], format="mp3")
    elif file_name.endswith('.wav'):
        fin = AudioSegment.from_file("wav256/%s.wav" % file_name[:-4], format="wav")
        
    file_name = file_name[:-4]
    
    if interval:
        # if slicing
        length = int(interval) * 1000
        fout = [fin[i:i + length] for i in range(0, len(fin), length)]
        
        i = 1
        for chunk in fout:
            chunk.export("wav256/%s-pt%d.wav" % (file_name,i), format="wav")
            i +=1
    else:
        # if not slicing
        fin.export("wav256/%s.wav" % file_name, format="wav")

    print('done.')

if __name__ == "__main__":
    mp3towav(sys.argv[1], sys.argv[2])







