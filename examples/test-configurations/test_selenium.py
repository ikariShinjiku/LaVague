# CONFIG FILE FOR TESTING ONLY

from llama_index.llms.openai import OpenAI
from lavague.prompts import SELENIUM_PROMPT
from lavague.defaults import (
    DefaultEmbedder,
    default_python_code_extractor,
    default_get_selenium_driver,
)


# default LLM for testing
class LLM(OpenAI):
    def __init__(self):
        super().__init__(api_key=None)


# default prompt
prompt_template = SELENIUM_PROMPT

# default embedder
embedder = DefaultEmbedder()

# default driver
get_driver = default_get_selenium_driver

# Random test cleaning function - won't be used
cleaning_function = default_python_code_extractor
