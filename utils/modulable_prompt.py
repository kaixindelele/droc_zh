from utils.io.io_utils import read_py
from utils.string_utils import str_to_dict, dict_to_str
import re

class modulable_prompt:
    """
    可模块化的提示类
    """

    def __init__(self, backbone_path, content_path) -> None:
        """
        初始化函数

        参数:
        - backbone_path: 提示的骨架文件路径
        - content_path: 提示的内容文件路径
        """
        self.backbone = read_py(backbone_path)
        self.content_str = read_py(content_path)
        self.content_dict = str_to_dict(self.content_str)
        self.prompt = None
        self.form_prompt()

    def form_prompt(self):
        """
        根据骨架和内容生成提示
        """
        self.prompt = self.backbone.replace("{}", self.content_str)
    
    def update_content(self, new_content):
        """
        更新提示的内容

        参数:
        - new_content: 新的内容
        """
        ind = list(self.content_dict.keys())[-1] + 1
        self.content_dict.update({ind: new_content})
        self.content_str = dict_to_str(self.content_dict)
        self.form_prompt()

    def add_constraints(self, constraint):
        """
        添加约束条件

        参数:
        - constraint: 约束条件，可以是字符串或字符串列表
        """
        if type(constraint) == str:
            constraint = [constraint]
        for c in constraint:
            lines = self.backbone.split('\n')
            rules_start_index = lines.index("Rules:")
            for i, line in enumerate(lines):
                if line.startswith('Object state'):
                    rules_end_index = i - 1
                    break
            existing_rules = "\n".join(lines[rules_start_index + 1 : rules_end_index])
            new_rule_number = len(re.findall(r"\d+\.", existing_rules)) + 1
            new_rule = f"{new_rule_number}. {c}"
            updated_rules_section = f"{existing_rules.strip()}\n{new_rule}"
            self.backbone = self.backbone.replace(existing_rules, updated_rules_section)
            self.form_prompt()

    def get_prompt(self):
        """
        获取提示
        """
        return self.prompt

    def set_object_state(self, obj_state):
        """
        设置对象状态

        参数:
        - obj_state: 对象状态
        """
        lines = self.backbone.split('\n')
        new_lines = []
        for line in lines:
            if line.startswith("Object state:"):
                new_lines.append(f"Object state: {obj_state}")
            else:
                new_lines.append(line)
        self.backbone = '\n'.join(new_lines)
        self.form_prompt()

if __name__ == '__main__':
    prompt_codepolicy = modulable_prompt('prompts/prompt_plan_backbone.txt', 
                                         'prompts/prompt_plan_content.txt')
    prompt_codepolicy.add_constraints('The scissors should be put into a drawer that is not full.')
    print(prompt_codepolicy.get_prompt())
