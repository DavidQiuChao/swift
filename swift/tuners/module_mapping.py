import dataclasses
from collections import OrderedDict


@dataclasses.dataclass
class ModelKeys:

    model_type: str = None

    module_list: str = None

    mlp: str = None

    down_proj: str = None

    attention: str = None

    o_proj: str = None

    q_proj: str = None

    k_proj: str = None

    v_proj: str = None

    qkv_proj: str = None

    qk_proj: str = None


LLAMA_KEYS = ModelKeys(
    **{
        'module_list': 'model.layers',
        'mlp': 'model.layers.{}.mlp',
        'down_proj': 'model.layers.{}.mlp.down_proj',
        'attention': 'model.layers.{}.self_attn',
        'o_proj': 'model.layers.{}.self_attn.o_proj',
        'q_proj': 'model.layers.{}.self_attn.q_proj',
        'k_proj': 'model.layers.{}.self_attn.k_proj',
        'v_proj': 'model.layers.{}.self_attn.v_proj',
    })

MISTRAL_KEYS = LLAMA_KEYS
QWEN2_KEYS = LLAMA_KEYS
YI_KEYS = LLAMA_KEYS
GEMMA_KEYS = LLAMA_KEYS
INTERNLM_KEYS = LLAMA_KEYS
DEEPSEEK_KEYS = LLAMA_KEYS
OPENBUDDY_KEYS = LLAMA_KEYS
XVERSE_KEYS = LLAMA_KEYS
ORION_KEYS = LLAMA_KEYS
BLUELM_KEYS = LLAMA_KEYS
ZIYA_KEYS = LLAMA_KEYS
SKYWORK_KEYS = LLAMA_KEYS

CHATGLM_KEYS = ModelKeys(
    **{
        'module_list': 'transformer.encoder.layers',
        'mlp': 'transformer.encoder.layers.{}.mlp',
        'down_proj': 'transformer.encoder.layers.{}.mlp.dense_4h_to_h',
        'attention': 'transformer.encoder.layers.{}.self_attention',
        'o_proj': 'transformer.encoder.layers.{}.self_attention.dense',
        'qkv_proj':
        'transformer.encoder.layers.{}.self_attention.query_key_value',
    })

BAICHUAN_KEYS = ModelKeys(
    **{
        'module_list': 'model.layers',
        'mlp': 'model.layers.{}.mlp',
        'down_proj': 'model.layers.{}.mlp.down_proj',
        'attention': 'model.layers.{}.self_attn',
        'qkv_proj': 'model.layers.{}.self_attn.W_pack',
    })

YUAN_KEYS = ModelKeys(
    **{
        'module_list': 'model.layers',
        'mlp': 'model.layers.{}.mlp',
        'down_proj': 'model.layers.{}.mlp.down_proj',
        'attention': 'model.layers.{}.self_attn',
        'qk_proj': 'model.layers.{}.self_attn.qk_proj',
        'o_proj': 'model.layers.{}.self_attn.o_proj',
        'q_proj': 'model.layers.{}.self_attn.q_proj',
        'k_proj': 'model.layers.{}.self_attn.k_proj',
        'v_proj': 'model.layers.{}.self_attn.v_proj',
    })

CODEFUSE_KEYS = ModelKeys(
    **{
        'module_list': 'gpt_neox.layers',
        'mlp': 'model.layers.{}.mlp',
        'down_proj': 'model.layers.{}.mlp.dense_4h_to_h',
        'attention': 'model.layers.{}.attention',
        'o_proj': 'model.layers.{}.attention.dense',
        'qkv_proj': 'model.layers.{}.attention.query_key_value',
    })

PHI2_KEYS = ModelKeys(
    **{
        'module_list': 'transformer.h',
        'mlp': 'transformer.h.{}.mlp',
        'down_proj': 'transformer.h.{}.mlp.c_proj',
        'attention': 'transformer.h.{}.mixer',
        'o_proj': 'transformer.h.{}.mixer.out_proj',
        'qkv_proj': 'transformer.h.{}.mixer.Wqkv',
    })

QWEN_KEYS = ModelKeys(
    **{
        'module_list': 'transformer.h',
        'mlp': 'transformer.h.{}.mlp',
        'down_proj': 'transformer.h.{}.mlp.fc2',
        'attention': 'transformer.h.{}.attn',
        'o_proj': 'transformer.h.{}.attn.c_proj',
        'qkv_proj': 'transformer.h.{}.attn.c_attn',
    })

MODEL_KEYS_MAPPING = OrderedDict([
    ('llama', LLAMA_KEYS),
    ('mistral', MISTRAL_KEYS),
    ('qwen1half', QWEN2_KEYS),
    ('yi', YI_KEYS),
    ('gemma', GEMMA_KEYS),
    ('internlm', INTERNLM_KEYS),
    ('deepseek', DEEPSEEK_KEYS),
    ('openbuddy', OPENBUDDY_KEYS),
    ('xverse', XVERSE_KEYS),
    ('orion', ORION_KEYS),
    ('bluelm', BLUELM_KEYS),
    ('ziya', ZIYA_KEYS),
    ('skywork', SKYWORK_KEYS),
    ('chatglm', CHATGLM_KEYS),
    ('baichuan', BAICHUAN_KEYS),
    ('yuan', YUAN_KEYS),
    ('codefuse', CODEFUSE_KEYS),
    ('phi2', PHI2_KEYS),
    ('qwen', QWEN_KEYS),
])
