
# 提示概述

## 计划级别（高级）
1. **hl_backbone.txt**：用于生成高级计划的提示骨干。有关详细信息，请参阅`utils/modulable_prompt.py`。
2. **hl_cap_backbone.txt**：用于为基准Code-as-Policy生成高级计划的提示骨干。
3. **hl_cap_content.txt**：用于为基准Code-as-Policy生成高级计划的提示内容。
4. **hl_content.txt**：用于生成高级计划的提示内容。
5. **hl_corr.txt**：解释高级修正。
6. **hl_retrieval.txt**：根据语义相似性从知识库中检索高级知识。
7. **get_constraint_feature.txt**：确定哪些先前任务与当前任务的相同对象进行交互。

## 技能级别（低级）
1. **ll_backbone.txt**：用于生成低级技能的提示骨干。
2. **ll_content.txt**：用于生成低级技能的提示内容。
3. **ll_corr_nohist.txt**：解释无历史基线的低级修正。
4. **ll_corr.txt**：解释低级修正。
5. **ll_distill.txt**：从交互历史中提炼低级知识。
6. **ll_retrieval.txt**：从知识库中检索低级知识。
7. **get_task_feature.txt**：获取给定任务的与任务相关的知识类型。
8. **hist_retrieval.txt**：检索相关的交互历史以解释修正。

## 功能性
1. **change_frame.txt**：根据修正确定当前参考框架是否需要更改。
2. **get_ini_obj_state.txt**：要求LLM推断对象的初始状态。
3. **update_obj_state.txt**：在完成技能后更新对象的状态。
4. **get_pos_scale.txt**：获取修正中模糊距离表达式（例如，“有点”）的比例。
5. **get_pose_from_str.py**：根据对象查询获取参考框架（姿势）。
6. **get_task_pose_str.txt**：确定抓取给定对象的抓取姿势，该对象由对象的几何属性表示。
7. **is_planning_error.txt**：根据修正确定错误是计划级别（高级）还是技能级别。

## 解析
1. **parse_name.txt**：将LLMs生成的开放世界对象名称解析为CLIP候选对象名称。
2. **parse_ori.py**：将方向的文本描述解析为numpy数组。
3. **parse_plan.txt**：将文本计划解析为给定格式。
4. **parse_pos.py**：将位置的文本描述解析为numpy数组。
5. **replace_des_with_val.txt**：用值替换交互历史中位置的文本描述。
6. **replace_true_name.txt**：用对象的真实名称替换对象名称中的模糊引用。
7. **get_obj_name_from_task.txt**：从任务的句子描述中提取对象的名称。
8. **get_query_obj.txt**：从完整对象名称中提取视觉特征描述。
