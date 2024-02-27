from tortoise.custom_models import Experimentation
from .custom_stories import *
from tortoise.custom_api import generate_sentence_and_save

if __name__ == "__main__":
    experimentations = [


        # voices
        Experimentation("_bk_harp_006115", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_bk_peng_004302", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_bk_podm_004281", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_bk_reco_000784", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_jenna_rose_stein", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_tina_merryman", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_tracey_rose", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),

    ]

    generate_sentence_and_save(experimentations)