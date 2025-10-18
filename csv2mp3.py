import os
import pandas as pd
from TTS.api import TTS
from pydub import AudioSegment 

# Initialize TTS model (Coqui TTS)
# "tts_models/de/thorsten/tacotron2-DDC" for German
# "tts_models/en/ljspeech/tacotron2-DDC" for English
tts_de = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=False, gpu=False)

output_folder = "mp3_output/"
os.makedirs(output_folder, exist_ok=True)
 
# Loop through CSV and generate MP3 files
csv_files = [f for f in os.listdir(".") if f.endswith(".csv")]
for csv_file in csv_files:
    output_all = f"{output_folder}{csv_file}.mp3" 
    
    # Load CSV, format: German,English
    df = pd.read_csv(csv_file)
 
    allwords = ""
    for idx, row in df.iterrows():
        german_word = row['German']
        english_word = row['English']
        allwords = allwords + german_word + " is " + english_word  + ". "

    tts_de.tts_to_file(text=allwords, file_path=output_all)
    print(f"{output_all} file is generated!")