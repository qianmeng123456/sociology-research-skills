---
name: questionnaire-design-guide
description: 设计或审查问卷题型、Likert 题项及计分规则；完整社会学问卷设计优先使用 sociological-survey-design。
metadata:
  version: 0.1.0
  upstream_commit: bf44b3cd617fa94c8a1b254c5d1987142ca3d631
  adaptation: sociology-reviewed-entrypoint
---

# 问卷题项与量表基础

适用于具体题项与测量设计。先识别是在改编成熟工具，还是开发尚未验证的新题项。

## 工作方式

1. 明确构念、受访人群、语言、调查模式与用途，区分事实、行为、态度和知识测量。
2. 查询量表原始来源、版本、授权与适用人群；自编题标为候选题，不能称为成熟量表。
3. 检查一题多问、前提假定、诱导、回忆期和选项覆盖。量尺点数、中点和不知道选项依据构念与人群决定。
4. 正反向计分按合法取值下界加上界减原值；先隔离拒答、不适用等缺失码。定义最少有效题数及合成分规则。
5. 先认知访谈和流程预测试，再按模型复杂度设计测量验证样本。EFA 与 CFA 的探索、确认数据应区分。

## 交付

题项文本、来源状态、响应选项、编码及计分规则、逐项修改理由、测量验证计划。

## 方法修订与适用边界

不固定每构念加入 2–3 道反向题；反向措辞可能引入方法因子。30–50 人不等于足够完成因子分析。α 不是单维性或效度证明，不以提高 α 为唯一删题目标；因子数结合理论、平行分析和碎石图。相关系数的固定阈值不能普遍证明聚合或区分效度。不按缺失比例自动删除或均值插补。

保留原始数据和处理记录；缺少数据时交付设计或代码草稿，不能填写虚构的样本量、系数、引文或已经完成的检验。代码执行前核对用户文件、软件版本与官方接口，只报告实际运行结果。

## 来源与按需参考

本入口是社会学适配版，基于 [Wentor AI 原版](https://github.com/wentorai/research-plugins/blob/bf44b3cd617fa94c8a1b254c5d1987142ca3d631/skills/analysis/wrangling/questionnaire-design-guide/SKILL.md) 整理，原版按 MIT 许可保留。需要原始示例或更多方法背景时读取 [上游快照](references/upstream.md) 的相关章节。快照保留了尚未逐段修复的简化规则与示例；本入口的修订是使用条件，不应直接复制快照代码作为经过验证的分析。

核对依据：

- [Pew：题目措辞与题序](https://www.pewresearch.org/writing-survey-questions/)
- [CDC：认知访谈](https://www.cdc.gov/nchs/ccqder/question-evaluation/cognitive-interviewing.html)
