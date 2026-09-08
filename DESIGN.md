# 设计决策与共同迭代

## 已确认

2026-09-08，用户选择“先做通用社会学研究工具集，优先问卷设计”，随后明确选择“先给完整初稿，再一起逐轮修改”。两项偏好已写入问卷技能与工作流入口。尚未选择常用软件，因此不预设必须 Stata 或必须 Python。

## 对原对话清单的落实

16 个具体基础技能保持原名称：questionnaire-design-guide、survey-data-processing、power-analysis-guide、missing-data-handling、hypothesis-testing-guide、sem-guide、causal-inference-guide、panel-data-guide、iv-regression-guide、robustness-checks、stata-analyst-guide、stata-data-cleaning、text-mining-guide、network-visualization-guide、publication-figures-guide、meta-analysis-guide。

原对话泛称 `literature-review` 拆为已核实来源的 `systematic-review-guide` 与 `literature-review-writing`；`academic-writing` 采用 `scientific-writing-guide`；`c2` 采用同源且名称明确的 `qualitative-research-guide`，没有声称安装原 Diverga 的 c2。`hypothesis-generation` 由自建 `sociological-theory-analysis` 覆盖理论到假设转换。因此基础来源20个，加7个自建，共27个，而不是原样安装全部候选包。

## 自建范围

按对话设计4个专用技能：社会理论、问卷、质性访谈编码、计算文本测量。另加抽样、可复现报告和跨阶段工作流3个，衔接基础方法。混合方法的整合决策放入工作流。网络研究通过网络定义与指标边界增强原有可视化入口。

问卷技能完整任务交付问卷、操作化、编码/跳题、偏误修改理由和预测试方案；局部改题不触发整套流程。量表来源待核实、自编题和真实验证结果分别标注。

## 已识别并修订的方法问题

适配入口取代原版作为操作指导；原版保留为参考。逐项修订见 `sources/foundation-specs.json` 与生成的每个入口，主要包括固定反向题、固定预测试人数、α/因子阈值、未限制有效题数的量表合成、缺失机制误判、前趋势等同识别、弱工具诊断及主题分析的一致性要求。没有宣称对每个上游代码块做过完整学术或运行审计。

本版本保留按需选择和渐进读取，不添加全局 AGENTS.md、不改已有技能、不安装统计软件、不部署调查或公开研究材料。

## 当前验证与下一步

已编写中文问卷演示和本地技术校验，演示明确为合成情境。技术测试不能替代真实受访者预测试，也不能证明所有技能在不同课题上都表现可靠。

使用节奏已共同确定。下一步可选一份真实研究问题或现有问卷试用，记录输出中真正需要修改的决策，更新项目后同步个人技能目录。完整技能集的文件交付与安装可以验证；实际研究中的可用性还需使用反馈，不能把文件检查等同于研究方法已经验证。
