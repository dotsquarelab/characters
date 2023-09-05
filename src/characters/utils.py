from langchain import PromptTemplate
from langchain.callbacks import get_openai_callback
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory

from . import prompts_template as prompts


def get_model(
    character,
    model_name="gpt-3.5-turbo-16k",
    verbose=False,
):
    prompt = PromptTemplate(
        input_variables=["history", "human_input"],
        template=prompts.THREE_CHARACTER_TEMPLATE,
        partial_variables={"character": character},
    )

    memory = ConversationBufferWindowMemory(
        k=10,
        ai_prefix="AI",
        human_prefix="Human",
    )
    chain = LLMChain(
        llm=ChatOpenAI(temperature=1.2, model=model_name),
        prompt=prompt,
        verbose=verbose,
        memory=memory,
    )
    return chain


def chat(chain, msg):
    with get_openai_callback() as callback:
        output = chain.run(msg)
        print(f"Total Tokens: {callback.total_tokens}")
        print(f"Prompt Tokens: {callback.prompt_tokens}")
        print(f"Completion Tokens: {callback.completion_tokens}")
        print(f"Total Cost (USD): ${callback.total_cost}")

    return output
