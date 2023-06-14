# """
# 对各个llm模型进行单元测试
# """
def validate_path():
    import os, sys
    dir_name = os.path.dirname(__file__)
    root_dir_assume = os.path.abspath(os.path.dirname(__file__) +  '/..')
    os.chdir(root_dir_assume)
    sys.path.append(root_dir_assume)
    
validate_path() # validate path so you can run from base directory
if __name__ == "__main__":
    from toolbox import get_conf, ChatBotWithCookies
    from request_llm.bridge_chatgpt_fncall import predict_no_ui_long_connection
    # from request_llm.bridge_moss import predict_no_ui_long_connection
    # from request_llm.bridge_jittorllms_pangualpha import predict_no_ui_long_connection
    # from request_llm.bridge_jittorllms_llama import predict_no_ui_long_connection
    proxies, WEB_PORT, LLM_MODEL, CONCURRENT_COUNT, AUTHENTICATION, CHATBOT_HEIGHT, LAYOUT, API_KEY = \
        get_conf('proxies', 'WEB_PORT', 'LLM_MODEL', 'CONCURRENT_COUNT', 'AUTHENTICATION', 'CHATBOT_HEIGHT', 'LAYOUT', 'API_KEY')

    llm_kwargs = {
        'max_length': 512,
        'top_p': 1,
        'api_key': API_KEY,
        'llm_model': LLM_MODEL,
        'temperature': 1,
    }

    functions = [
        {
            "name": "get_current_weather",  # The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.
            "description": "Get the current weather in a given location",   # The description of what the function does.
            "parameters": { # The parameters the functions accepts, described as a JSON Schema object. See the guide for examples, and the JSON Schema reference for documentation about the format.
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
            },
        }
    ]

    result = predict_no_ui_long_connection(inputs="Get the current weather in Beijing", 
                                        llm_kwargs=llm_kwargs,
                                        history=[],
                                        sys_prompt=functions)
    print('final result:', result)


    result = predict_no_ui_long_connection(inputs="what is a hero?", 
                                        llm_kwargs=llm_kwargs,
                                        history=["hello world"],
                                        sys_prompt="")
    print('final result:', result)

    result = predict_no_ui_long_connection(inputs="如何理解传奇?", 
                                        llm_kwargs=llm_kwargs,
                                        history=[],
                                        sys_prompt="")
    print('final result:', result)

    # # print(result)
    # from multiprocessing import Process, Pipe
    # class GetGLMHandle(Process):
    #     def __init__(self):
    #         super().__init__(daemon=True)
    #         pass
    #     def run(self):
    #         # 子进程执行
    #         # 第一次运行，加载参数
    #         def validate_path():
    #             import os, sys
    #             dir_name = os.path.dirname(__file__)
    #             root_dir_assume = os.path.abspath(os.path.dirname(__file__) +  '/..')
    #             os.chdir(root_dir_assume + '/request_llm/jittorllms')
    #             sys.path.append(root_dir_assume + '/request_llm/jittorllms')
    #         validate_path() # validate path so you can run from base directory

    #         jittorllms_model = None
    #         import types
    #         try:
    #             if jittorllms_model is None:
    #                 from models import get_model
    #                 # availabel_models = ["chatglm", "pangualpha", "llama", "chatrwkv"]
    #                 args_dict = {'model': 'chatrwkv'}
    #                 print('self.jittorllms_model = get_model(types.SimpleNamespace(**args_dict))')
    #                 jittorllms_model = get_model(types.SimpleNamespace(**args_dict))
    #                 print('done get model')
    #         except:
    #             # self.child.send('[Local Message] Call jittorllms fail 不能正常加载jittorllms的参数。')
    #             raise RuntimeError("不能正常加载jittorllms的参数！")
            
    # x = GetGLMHandle()
    # x.start()


    # input()