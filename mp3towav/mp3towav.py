# CMD line argument: file name (str)

from pydub import AudioSegment
import sys

def mp3towav(file_name):
    fin = AudioSegment.from_file("raw/%s.mp3" % file_name, format="mp3")
    fin.export("wav/%s.wav" % file_name, format="wav")
    print('done.')

if __name__ == "__main__":
    mp3towav(sys.argv[1])







