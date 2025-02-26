from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

def generate_script(subject, video_length, creativity, deep_think, api_key):
    title_template = ChatPromptTemplate.from_messages(
        [
            ("human", "为'{subject}'这个主题的视频想一个吸引人的标题，只回复唯一一个你觉得最实用的标题")
        ]
    )
    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             """你是一位短视频频道的博主。根据以下标题和相关信息，为短视频频道写一个可以爆火的视频脚本。
             视频标题：{title}，视频时长：{duration}分钟，生成的脚本的长度尽量遵循视频时长的要求。
             要求：开头抓住限球，中间提供干货内容，结尾有惊喜，脚本格式也请按照【开头、中间，结尾】分隔。
             整体内容的表达方式要尽量轻松有趣，吸引年轻人。
             请在最后给出制作的Tips，比如：如何拍摄、如何剪辑、如何配音、用什么画风、插入特效的时机、隐藏动线等等。
             """)
        ]
    )

    model_name = "deepseek-reasoner" if deep_think else "deepseek-chat"
    print("Using model: ", model_name)

    model = ChatOpenAI(
        model=model_name,
        api_key=api_key,
        temperature=creativity,
        base_url="https://api.deepseek.com"
    )

    title_chain = title_template | model
    script_chain = script_template | model
    print("#" * 25 + " subject " + "#" * 25)
    print(subject)

    title_response = title_chain.invoke({"subject": subject})
    print("#" * 25 + " title_response " + "#" * 25)
    print(title_response)

    title = title_response.content
    print("#" * 25 + " title " + "#" * 25)
    print(title)

    script_response = script_chain.invoke({"title": title, "duration": video_length})
    print("#" * 25 + " script_response " + "#" * 25)
    print(script_response)

    script = script_response.content
    print("#" * 25 + " script " + "#" * 25)
    print(script)

    return title, script
