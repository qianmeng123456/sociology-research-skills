---
name: iv-regression-guide
description: 实施工具变量与 2SLS 分析，评估工具相关性、识别假设和弱工具稳健推断。
metadata:
  version: 0.1.0
  upstream_commit: bf44b3cd617fa94c8a1b254c5d1987142ca3d631
  adaptation: sociology-reviewed-entrypoint
---

# 工具变量与弱识别

解释工具为何带来可用变异及估计所针对的人群。

## 工作方式

1. 写明内生变量、工具、外生控制、时间顺序与排除限制的具体机制。
2. 两阶段使用一致样本、相同外生控制和截距约定，以专门 IV 估计器获取正确标准误。
3. 报告条件首阶段、工具联合检验、partial R² 及匹配异方差/聚类设定的弱识别诊断。
4. 弱工具风险下考虑 Anderson–Rubin 等适用推断；解释相关临界值的适用假设。
5. 报告简约式、2SLS、区间、局部解释和工具无效的敏感性；过度识别检验仅在过度识别时适用。

## 交付

工具论证、首阶段与结构结果、诊断及弱识别限制。

## 方法修订与适用边界

F>10 不是通用强工具证明，Stock–Yogo 临界值不能无条件套到所有稳健统计量。过度识别不拒绝不证明排除限制；手工第二阶段 OLS 的常规标准误不适用。

保留原始数据和处理记录；缺少数据时交付设计或代码草稿，不能填写虚构的样本量、系数、引文或已经完成的检验。代码执行前核对用户文件、软件版本与官方接口，只报告实际运行结果。

## 来源与按需参考

本入口是社会学适配版，基于 [Wentor AI 原版](https://github.com/wentorai/research-plugins/blob/bf44b3cd617fa94c8a1b254c5d1987142ca3d631/skills/analysis/econometrics/iv-regression-guide/SKILL.md) 整理，原版按 MIT 许可保留。需要原始示例或更多方法背景时读取 [上游快照](references/upstream.md) 的相关章节。快照保留了尚未逐段修复的简化规则与示例；本入口的修订是使用条件，不应直接复制快照代码作为经过验证的分析。
