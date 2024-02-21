from tortoise.custom_models import Experimentation
from tortoise.custom_stories import *
from tortoise.custom_api import generate_sentence_and_save

if __name__ == "__main__":
    experimentations = [

        Experimentation("_andrew_latheron", story_3, "ultra_fast", tts_init={}, parameters={}),
        Experimentation("_andrew_latheron", story_3, "fast", tts_init={}, parameters={}),
        Experimentation("_andrew_latheron", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={.2}),
        Experimentation("_andrew_latheron", story_3, "fast",
                        tts_init={"kv_cache": True, "half": True, "use_deepspeed": True}, parameters={.2}),
        Experimentation("_andrew_latheron", story_4, "fast", tts_init={"kv_cache": True, "half": True}, parameters={.2}),

        Experimentation("_chirs_redish", story_3, "ultra_fast", tts_init={}, parameters={}),
        Experimentation("_chirs_redish", story_3, "fast", tts_init={}, parameters={}),
        Experimentation("_chirs_redish", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={.2}),
        Experimentation("_chirs_redish", story_3, "fast",
                        tts_init={"kv_cache": True, "half": True, "use_deepspeed": True}, parameters={.2}),
        Experimentation("_chirs_redish", story_4, "fast", tts_init={"kv_cache": True, "half": True}, parameters={.2}),

    ]

    generate_sentence_and_save(experimentations)