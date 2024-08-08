"""contains transcription functions"""

import vosk
from ...configs import *
from deepmultilingualpunctuation import PunctuationModel
from .logger import logData

def transcribe_audio(audio_path, output_path):
    """converts audio data from input path 
    to text data and stores it in output path

    Args:
        audio_path (str): path of audio data
        output_path (str): path of transcription

    Returns:
        str: transcription
    """
    logData('Getting audio at:' + str(audio_path) + ' and storing it at ' + str(output_path))

    model = None
    recognizer = None
    raw_result = None
    text_result = None

    # Load model
    try:
        model = vosk.Model("./iic-group10/vosk-model-small-en-us-0.15")
        recognizer = vosk.KaldiRecognizer(model, 16000)
    except Exception as e:
        logData(e)

    # Transcribe text
    try: 
        logData("Starting Transcription ...")
        with open(audio_path, "rb") as audio:
            while True:
                data = audio.read(4000)
                if len(data) == 0:
                    break
                recognizer.AcceptWaveform(data)
        raw_result = recognizer.FinalResult()
    except Exception as e:
        logData(e)


    # Punctuate text
    logData('Starting punctuation ...')
    punctuation_model = PunctuationModel()
    text_result = punctuation_model.restore_punctuation(raw_result)
    text_result = text_result.replace('text', '').replace('{', '').replace('\\', '').replace('\"', '').replace(':', '').replace('-', '').replace('}', '')

    # Save transcription
    try:
        with open(output_path,'w') as f:
            f.write(text_result)
    except Exception as e:
        logData(e)
    logData('Succesfully saved text: ' + str(text_result))
    return text_result

