---
name: panel-data-guide
description: 处理个体与时间索引，设计固定效应、随机效应或相关随机效应面板分析。
metadata:
  version: 0.1.0
  upstream_commit: bf44b3cd617fa94c8a1b254c5d1987142ca3d631
  adaptation: sociology-reviewed-entrypoint
---

# 面板研究

从个体内变化、时间变化和选择机制解释面板系数。

## 工作方式

1. 核对 ID×时间唯一性、波次间隔、流失、不平衡和关键变量个体内变异。
2. 区分 within 与 between 目标；依据未观测个体效应与协变量相关性选择 FE、RE 或 Mundlak 形式。
3. 评估时间效应、序列相关、共同冲击、聚类层级及少集群问题。
4. 动态模型需说明滞后结局、短面板偏差和工具构造；GMM 检查工具膨胀、序列相关及有效性假设。
5. 报告单位数、时期数、观察数、识别所依赖的变化及样本流失敏感性。

## 交付

索引验证、模型依据、代码、样本结构及系数解释。

## 方法修订与适用边界

Hausman 检验不应单独决定 FE/RE，也不自动验证因果性。个体 FE 不处理所有随时间变化的混杂；时间不变变量的主效应通常不能由个体 FE 识别。

保留原始数据和处理记录；缺少数据时交付设计或代码草稿，不能填写虚构的样本量、系数、引文或已经完成的检验。代码执行前核对用户文件、软件版本与官方接口，只报告实际运行结果。

## 来源与按需参考

本入口是社会学适配版，基于 [Wentor AI 原版](https://github.com/wentorai/research-plugins/blob/bf44b3cd617fa94c8a1b254c5d1987142ca3d631/skills/analysis/econometrics/panel-data-guide/SKILL.md) 整理，原版按 MIT 许可保留。需要原始示例或更多方法背景时读取 [上游快照](references/upstream.md) 的相关章节。快照保留了尚未逐段修复的简化规则与示例；本入口的修订是使用条件，不应直接复制快照代码作为经过验证的分析。
