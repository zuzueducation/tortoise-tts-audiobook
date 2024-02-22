from tortoise.custom_models import Experimentation
from tortoise.experimentations.custom_stories import *
from tortoise.custom_api import generate_sentence_and_save

if __name__ == "__main__":
    experimentations = [


        # voices
        Experimentation("_andrew_latheron", story_5, "fast", tts_init={"kv_cache": True, "half": True}, parameters={"temperature":.2}),
        Experimentation("_andrew_latheron", story_5, "fast",
                        tts_init={"kv_cache": True, "half": True, "use_deepspeed": True}, parameters={"temperature":.2}),
        Experimentation("_andrew_latheron", story_4, "fast", tts_init={"kv_cache": True, "half": True}, parameters={"temperature":.2}),

        Experimentation("_chirs_redish", story_5, "ultra_fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_chirs_redish", story_5, "fast", tts_init={"kv_cache": True, "half": True}, parameters={"temperature":.2}),
        Experimentation("_chirs_redish", story_5, "fast",
                        tts_init={"kv_cache": True, "half": True, "use_deepspeed": True}, parameters={"temperature":.2}),
        Experimentation("_chirs_redish", story_4, "fast", tts_init={"kv_cache": True, "half": True}, parameters={"temperature":.2}),

        # long sample
        Experimentation("_andrew_latheron_long", story_5, "fast", tts_init={"kv_cache": True, "half": True}, parameters={"temperature":.2}),

        #very short sample
        Experimentation("_andrew_latheron_short", story_5, "fast", tts_init={"kv_cache": True, "half": True}, parameters={"temperature":.2}),

    ]

    generate_sentence_and_save(experimentations)