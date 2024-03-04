from tortoise.custom_models import Experimentation
from custom_stories import *
from tortoise.custom_api import generate_sentence_and_save

if __name__ == "__main__":
    experimentations = [

        # voice 1
        Experimentation("_amy_faal", story_3_cut_a, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_amy_faal", story_3_cut_b, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),

        Experimentation("_sally_walker", story_3_cut_a, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_sally_walker", story_3_cut_b, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),

    ]

    generate_sentence_and_save(experimentations)