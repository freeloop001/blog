# LangSmith 示例
# 需要安装: pip install langchain langchain-openai langsmith

print("=== LangSmith 示例 ===")

# 注意：需要配置 API Key 和 LangSmith
# 以下是示例代码，需要配置环境变量才能运行

# ============ 1. 基本追踪 ============
print("=== 基本追踪 ===")
print("需要配置 API Key 才能运行")
print("设置环境变量:")
print("  export LANGCHAIN_TRACING_V2=true")
print("  export LANGCHAIN_API_KEY='your-key'")
print("  export OPENAI_API_KEY='your-key'")

# 完整代码示例（需要 API Key）
example_code_1 = '''
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langsmith import traceable

# 配置
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-langsmith-key"

llm = ChatOpenAI(model="gpt-4")
prompt = PromptTemplate.from_template("{product}的创始人是谁？")
chain = LLMChain(llm=llm, prompt=prompt)

result = chain.invoke({"product": "Apple"})
print(result["text"])
'''

# ============ 2. 追踪特定函数 ============
print("\n=== 函数追踪 ===")

example_code_2 = '''
from langsmith import traceable

@traceable
def process_user_request(user_input: str) -> str:
    """处理用户请求的函数"""
    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    response = llm.invoke(user_input)
    return response.content

result = process_user_request("解释什么是机器学习")
print(result)
'''

# ============ 3. 自定义追踪数据 ============
print("\n=== 自定义元数据 ===")

example_code_3 = '''
from langsmith.run_helpers import trace
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4")

@traceable(run_type="chain")
def complex_pipeline(input_data: str):
    result1 = llm.invoke(f"总结: {input_data}")
    result2 = llm.invoke(f"翻译成英文: {result1.content}")
    return result2.content

result = complex_pipeline("Python是一门强大的编程语言")
print(result)
'''

# ============ 4. LangChain 集成 ============
print("\n=== LangChain 集成 ===")

example_code_4 = '''
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool

@tool
def calculate(expression: str) -> str:
    """数学计算"""
    return str(eval(expression))

llm = ChatOpenAI(model="gpt-4")
tools = [calculate]

prompt = PromptTemplate.from_template("你是一个助手。{input}")
agent = create_openai_functions_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools)

result = executor.invoke({"input": "计算 (10+5)*2"})
print(result["output"])
'''

print("完整代码示例已保存在变量中")
print("访问 https://smith.langchain.com 查看追踪数据")

print("需要配置环境变量:")
print("  export LANGCHAIN_TRACING_V2=true")
print("  export LANGCHAIN_API_KEY='your-key'")
print("  export OPENAI_API_KEY='your-key'")
print("\n访问 https://smith.langchain.com 查看追踪数据")
