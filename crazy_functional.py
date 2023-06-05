from toolbox import HotReload  # HotReload 的意思是热更新，修改函数插件后，不需要重启程序，代码直接生效


def get_crazy_functions():
    function_plugins = {}

    try:
        from crazy_functions.Latex输出PDF结果 import Latex翻译中文并重新编译PDF
        function_plugins.update({
            "[先输入arxiv论文网址] Latex翻译/Arixv翻译+重构PDF": {
                "Color": "stop",
                "AsButton": True,
                # "AdvancedArgs": True,
                # "ArgsReminder": "",
                "Function": (Latex翻译中文并重新编译PDF)
            }
        })
    except:
        print('Load function plugin failed')
    ###################### 第n组插件 ###########################
    return function_plugins
