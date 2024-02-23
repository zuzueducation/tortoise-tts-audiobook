from tortoise.custom_models import Experimentation
from custom_stories import *
from tortoise.custom_api import generate_sentence_and_save

if __name__ == "__main__":
    experimentations = [


        # voices
        Experimentation("train_mouse", story_5, "ultra_fast", tts_init={"kv_cache": True, "half": True}, parameters={}),

        Experimentation("train_mouse", story_5, "ultra_fast", tts_init={"kv_cache": True, "half": True}, parameters={"return_deterministic_state": True}),

    ]

    generate_sentence_and_save(experimentations)