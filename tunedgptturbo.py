import openai
from apikeys import keys

openai.api_key = keys

model = 'gpt-3.5-turbo'


def get_completion(prompt, model='gpt-3.5-turbo'):
    messages = [{
        'role': 'user', 'content': prompt
    }]

    # message = prompt

    completion = openai.ChatCompletion.create(
        model=model, messages=messages, temperature=0, max_tokens=1024,
    )

    return completion['choices'][0]['message']['content']


text = f'''Check the documentation for the specific API method you were calling and make sure you are sending valid and 
complete parameters. You may need to review the parameter names, types, values, and formats, and ensure they match the 
documentation.'''
prompt = f'''用一句话总结三个分隔符的分隔的文本。{text}'''
# res = get_completion(prompt)

text = f'''亚马逊新款双面磨毛瑜伽裤女 亲肤裸感瑜伽九分裤 高腰提臀瑜伽'''
prompt = f'''输出三个分隔符中的电商标题所包含的所有可能的卖点标签，并说明各标签对应的具体内容。以json的格式输出。{text}'''
# '{
# "亲肤": "采用亲肤面料，舒适透气，不易产生过敏反应",
# "裸感": "磨毛面料贴合肌肤，穿着舒适，仿佛裸着一样",
# "高腰": "高腰设计，能够有效提拉腰部线条，展现身材曲线",
# "提臀": "瑜伽裤采用提臀设计，能够有效提升臀部线条，让身材更加迷人",
# "瑜伽": "适合瑜伽运动，能够提供舒适的运动体验，让身体更加柔软灵活"
# }'
# res = get_completion(prompt)

# 给定成功的训练案例
prompt = f'''
你的任务是以同下列一致的对话风格回答问题。

<学生>：请告诉我地球的卫星是哪一颗，这个卫星叫什么名字，以及它的起源。
<老师>：亲爱的小朋友，让老师告诉你这个关于天文知识的问题。
我们生活的地球有一颗卫星，有科学家曾推测在很多很多年以前，地球因为受到了地外小星星的撞击，导致地球的一部分物质发生了解体，进而从地球上分离了出去，形成了地球的卫星。
这颗卫星的名字叫月球。人类已经实现了登陆月球这样的壮举，未来人类还将会在月球上展开更多的科研工作。你们要好好学习新的知识，为人类天文探索贡献力量，用你们的知识造就全人类更美好的未来！
小朋友们，你们知道问题的答案了吗？

<学生>：请告诉我想学习计算机技术，我应该学习哪些知识，如何制定学习计划呢？
'''
res = get_completion(prompt)
