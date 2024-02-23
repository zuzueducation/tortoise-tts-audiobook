from dataclasses import dataclass

@dataclass
class Experimentation:
    voice_name:str
    texts: [str]
    preset: str
    tts_init: {}
    parameters: {}
    parameters_preset = {}


    @staticmethod
    def merger_with_check(d1, d2):
        for key in d2:
            if key not in d1:
                raise KeyError(f"Key {key} does not exist")
            d1[key] = d2[key]
        return d1


    def __post_init__(self):
        presets = {
            'ultra_fast': {'num_autoregressive_samples': 16, 'diffusion_iterations': 30, 'cond_free': False},
            'fast': {'num_autoregressive_samples': 96, 'diffusion_iterations': 80},
            'standard': {'num_autoregressive_samples': 256, 'diffusion_iterations': 200},
            'high_quality': {'num_autoregressive_samples': 256, 'diffusion_iterations': 400},
        }

        tts_init_default = {"kv_cache": False,
                    "use_deepspeed": False,
                    "half": False}

        parameters_default = {'temperature': .8, 'length_penalty': 1.0, 'repetition_penalty': 2.0,
                    'top_p': .8,
                    'cond_free_k': 2.0, 'diffusion_temperature': 1.0}

        self.tts_init = Experimentation.merger_with_check(tts_init_default, self.tts_init)
        self.parameters = Experimentation.merger_with_check(parameters_default, self.parameters)
        self.parameters_preset = presets[self.preset]


    def __str__(self):
            result = f'voice Name: {self.voice_name}\n\n'
            result += f'\npreset: {self.preset}\n'
            result += '\ntext:\n' + '\n'.join(self.texts)
            result += '\n\ntts init:\n'
            for key, value in self.tts_init.items():
                result += f'  {key}: {value}\n'
            result += '\nparameters:\n'
            for key, value in self.parameters.items():
                result += f'  {key}: {value}\n'
            return result

