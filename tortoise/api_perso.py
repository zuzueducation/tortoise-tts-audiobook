import argparse
import os
import time

import torch
import torchaudio

from api import TextToSpeech, MODELS_DIR
from utils.audio import load_voices
from datetime import datetime
from stories import *

def generate_sentence(text="test", voice="train_mouse", preset="ultra_fast", use_deepspeed=True, folder_result: str="warm_up", sentence_number: str = "1"):


    kv_cache = True
    half = True
    output_path = "results/" + folder_result + "/"
    model_dir = MODELS_DIR
    candidates = 1
    seed = None
    produce_debug_state = True
    cvvp_amount = .0

    os.makedirs(output_path, exist_ok=True)
    tts = TextToSpeech(models_dir=model_dir, use_deepspeed=use_deepspeed, kv_cache=kv_cache, half=half)

    selected_voices = voice.split(',')
    for k, selected_voice in enumerate(selected_voices):
        if '&' in selected_voice:
            voice_sel = selected_voice.split('&')
        else:
            voice_sel = [selected_voice]
        voice_samples, conditioning_latents = load_voices(voice_sel)

        gen, dbg_state = tts.tts_with_preset(text, k=candidates, voice_samples=voice_samples,
                                             conditioning_latents=conditioning_latents,
                                             preset=preset, use_deterministic_seed=seed,
                                             return_deterministic_state=True, cvvp_amount=cvvp_amount)
        if isinstance(gen, list):
            for j, g in enumerate(gen):
                torchaudio.save(os.path.join(output_path, f'{selected_voice}_{k}_{j}.wav'), g.squeeze(0).cpu(), 24000)
        else:
            torchaudio.save(os.path.join(output_path,f'{selected_voice}_{str(sentence_number)}.wav'), gen.squeeze(0).cpu(), 24000)

        if produce_debug_state:
            os.makedirs('debug_states', exist_ok=True)
            torch.save(dbg_state, f'debug_states/do_tts_debug_{selected_voice}.pth')


start_time = time.time()
now = datetime.now()
formatted_now = now.strftime('%Y%m%d_%H_%M_%S') + '_' + str(int(now.microsecond / 1000)).zfill(3)






print(f"load models")
# generate_sentence(text="text", voice="train_mouse", preset='ultra_fast', use_deepspeed=False)
print("warm up done")



list_duration = []

for i, sentence in enumerate(story_2, start=1):
    start_time_loop = time.time()
    print(f"sentence number {i} in progress on {len(story_2)}")

    voice = "Jason_Pumarada"
    pcm_audio = generate_sentence(text=sentence, voice=voice, preset='ultra_fast', use_deepspeed=False, folder_result = f"{formatted_now}_{voice}", sentence_number = str(i) )

    end_time_loop = time.time()
    duration_loop = round(end_time_loop - start_time_loop, 2)

    print(f"sentence number {i} took {duration_loop}")
    list_duration.append(duration_loop)
    print(f"nb car {len(sentence)}, time per 100 char: {len(sentence) / duration_loop * 100}")

end_time = time.time()
for i, result in enumerate(list_duration, start = 1):
    print(f"sentence {i} took {str(result)} s")


print(f"it took {round(end_time - start_time, 2)}")
