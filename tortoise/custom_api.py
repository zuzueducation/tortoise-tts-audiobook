import os
import time
from datetime import datetime

import torchaudio

from tortoise.api import TextToSpeech
from tortoise.custom_models import Experimentation
from tortoise.utils.audio import load_voice


def generate_sentence_and_save(experimentations: Experimentation):
    for i, exp in enumerate(experimentations, start=1):
        start_time_exp = time.time()
        total_experimentations = len(experimentations)
        print(f"exp {i} on {total_experimentations}")

        now = datetime.now()
        formatted_now = now.strftime('%Y%m%d_%H_%M_%S') + '_' + str(int(now.microsecond / 1000)).zfill(3)

        list_duration = []
        voice_samples, conditioning_latents = load_voice(exp.voice_name)

        output_path = os.path.join("results", f"{formatted_now}_{exp.voice_name}")
        os.makedirs(output_path, exist_ok=True)

        tts = TextToSpeech(**exp.tts_init)
        print("tts initialized")

        for i, text in enumerate(exp.texts, start=1):
            start_time_loop = time.time()
            print(f"sentence number {i} in progress on {len(exp.texts)}")

            exp.parameters.update(exp.preset)
            print(exp.parameters)

            gen = tts.tts(text, voice_samples=voice_samples, conditioning_latents=conditioning_latents, **exp.parameters)

            torchaudio.save(os.path.join(output_path, f'{exp.voice_name}_{i}.wav'), gen.squeeze(0).cpu(), 24000)
            end_time_loop = time.time()
            duration_loop = round(end_time_loop - start_time_loop, 2)

            print(f"sentence number {i} took {duration_loop} with nb car {len(text)}")
            list_duration.append(duration_loop)

        end_time_exp = time.time()
        duration_exp = round(end_time_exp - start_time_exp, 2)
        print(f"experimentation took {duration_exp}")
        with open(os.path.join(output_path, "exp_info.txt"), "w") as f:
            f.write(str(exp))
            f.write(f"\nexperimentation took: {duration_exp} \n")
            total_number_of_cars = sum(len(text) for text in exp.texts)
            f.write(
                f"\ntotal nb of cars: {total_number_of_cars}, car/s: {round(total_number_of_cars / duration_exp, 2)} \n\n")
            for i, result in enumerate(list_duration, start=1):
                f.write(
                    f"text {i} took {str(result)} with {len(exp.texts[i - 1])}, car/s: {round(len(exp.texts[i - 1]) / duration_loop, 2)} \n")
