import wave

def wav_to_snu(wav_filename, snu_filename):
    # Abrir o arquivo WAV
    with wave.open(wav_filename, 'rb') as wav_file:
        # Ler todos os dados do arquivo WAV
        audio_data = wav_file.readframes(wav_file.getnframes())
    
    # Escrever os dados no arquivo SNU
    with open(snu_filename, 'wb') as snu_file:
        snu_file.write(audio_data)

# Exemplos de uso
wav_filename = 'ES/_01_01/alog_01_01.exa.wav'
snu_filename = 'ES/_01_01/alog_01_01.exa.snu'
wav_to_snu(wav_filename, snu_filename)
