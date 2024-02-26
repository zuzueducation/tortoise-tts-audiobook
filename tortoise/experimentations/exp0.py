from tortoise.custom_models import Experimentation
from custom_stories import *
from tortoise.custom_api import generate_sentence_and_save

if __name__ == "__main__":
    experimentations = [


        # voices
        Experimentation("_bk_adbl_031393", story_db_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_bk_adbl_031393", story_db_4, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_bk_adbl_031393", story_db_34, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_bk_adbl_031393", story_db_36, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_bk_adbl_031393", story_db_37, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_bk_adbl_031393", story_4, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),

        Experimentation("_andrew_latheron_long", story_db_3, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_andrew_latheron_long", story_db_4, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_andrew_latheron_long", story_db_34, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_andrew_latheron_long", story_db_36, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_andrew_latheron_long", story_db_37, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),
        Experimentation("_andrew_latheron_long", story_4, "fast", tts_init={"kv_cache": True, "half": True}, parameters={}),

    ]

    generate_sentence_and_save(experimentations)