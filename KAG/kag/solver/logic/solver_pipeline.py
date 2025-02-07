import copy
import logging
from kag.common.registry import Registrable

# from kag.solver.implementation.default_generator import DefaultGenerator
# from kag.solver.implementation.default_reasoner import DefaultReasoner
# from kag.solver.implementation.default_reflector import DefaultReflector
from kag.interface.solver.kag_generator_abc import KAGGeneratorABC
from kag.interface.solver.kag_memory_abc import KagMemoryABC
from kag.interface.solver.kag_reasoner_abc import KagReasonerABC
from kag.interface.solver.kag_reflector_abc import KagReflectorABC
from kag.interface.solver.base_model import LFExecuteResult

logger = logging.getLogger(__name__)


class SolverPipeline(Registrable):
    def __init__(
        self,
        reflector: KagReflectorABC,
        reasoner: KagReasonerABC,
        generator: KAGGeneratorABC,
        memory: KagMemoryABC,
        max_iterations=3,
        **kwargs
    ):
        """
        初始化思考和行动循环类。

        :param max_iterations: 限制思考和行动循环的最大迭代次数，默认为3。
        :param reflector: 用于反思任务的反思器实例。
        :param reasoner: 用于任务推理的推理器实例。
        :param generator: 用于生成行动的生成器实例。
        :param memory: 指定内存存储类型。
        """
        super().__init__(**kwargs)
        self.max_iterations = max_iterations

        self.reflector = reflector
        self.reasoner = reasoner
        self.generator = generator
        self.memory = memory
        self.param = kwargs

    def run(self, question, **kwargs):
        """
        简洁地输出问题的答案。

        参数：
        - question (str): 需要回答的问题。

        返回：
        - tuple: 答案。
        """
        instruction = question
        if_finished = False
        logger.debug("输入指令:{}".format(instruction))
        trace_log = []
        present_instruction = instruction
        run_cnt = 0
        memory = copy.copy(self.memory)

        while not if_finished and run_cnt < self.max_iterations:
            run_cnt += 1
            logger.debug("当前指令为:{}".format(present_instruction))
            # 尝试解决当前指令并获取答案、支持事实和历史日志
            reason_res: LFExecuteResult = self.reasoner.reason(
                present_instruction, **kwargs
            )

            # 从支持事实中提取证据
            memory.save_memory(
                reason_res.kg_exact_solved_answer,
                reason_res.get_support_facts(),
                instruction,
            )
            history_log = reason_res.get_trace_log()
            history_log["present_instruction"] = present_instruction
            history_log["present_memory"] = memory.serialize_memory()
            trace_log.append(history_log)

            # 基于当前内存和指令反思当前指令
            if_finished, present_instruction = self.reflector.reflect_query(
                memory, present_instruction
            )

        response = self.generator.generate(instruction, memory)
        return response, trace_log

    def get_kg_answer_num(self):
        """
        获取来自知识图谱的直接答案数量。
        调试信息

        返回：
            int: 来自知识图谱的直接答案数量。
        """
        return self.reasoner.kg_direct

    def get_total_sub_question_num(self):
        """
        获取解决问题的子问题总数。
        调试信息

        返回：
            int: 子问题的总数。
        """
        return self.reasoner.sub_query_total