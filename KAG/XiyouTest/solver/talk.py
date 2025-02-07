import json
import logging
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from tqdm import tqdm

from kag.common.benchmarks.evaluate import Evaluate
from kag.solver.logic.solver_pipeline import SolverPipeline
from kag.common.conf import KAG_CONFIG
from kag.common.registry import import_modules_from_path

from kag.common.checkpointer import CheckpointerManager


def qa(query):
    resp = SolverPipeline.from_config(KAG_CONFIG.all_config["kag_solver_pipeline"])
    answer, traceLog = resp.run(query)
    print(f"\n\nAnswer: {answer}\n")
    return answer


if __name__ == "__main__":
    import_modules_from_path("./prompt")
    print("欢迎使用知识图谱问答系统！")
    print("输入 'quit' 或 'exit' 可以退出程序")

    while True:
        print("\n请输入您的问题：")
        query = input().strip()

        if query.lower() in ['quit', 'exit']:
            print("感谢使用，再见！")
            break

        if not query:
            print("问题不能为空，请重新输入")
            continue

        try:
            qa(query)
        except Exception as e:
            print(f"处理问题时出现错误: {str(e)}")
            print("请尝试重新提问")