from tortoise.custom_models import Experimentation
from custom_stories import *
from tortoise.custom_api import generate_sentence_and_save

if __name__ == "__main__":
    experimentations = [


        # voice 1
        Experimentation("_amy_faal", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_anna_stephan", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_chandrika_chlevi", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_emma_powel", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_emma_powel_long", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_sally_walker", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),

        # voice 2
        Experimentation("_amy_faal", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={"temperature":.2, "top_p": .1}),
        Experimentation("_anna_stephan", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={"temperature":.2, "top_p": .1}),
        Experimentation("_chandrika_chlevi", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={"temperature":.2, "top_p": .1}),
        Experimentation("_emma_powel", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={"temperature":.2, "top_p": .1}),
        Experimentation("_emma_powel_long", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={"temperature":.2, "top_p": .1}),
        Experimentation("_sally_walker", story_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={"temperature":.2, "top_p": .1}),


    ]

    generate_sentence_and_save(experimentations)