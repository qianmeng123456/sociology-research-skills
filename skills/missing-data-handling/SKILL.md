---
name: missing-data-handling
description: 诊断研究数据的缺失模式，比较完整案例、多重插补或其他适用方案并评估敏感性。
metadata:
  version: 0.1.0
  upstream_commit: bf44b3cd617fa94c8a1b254c5d1987142ca3d631
  adaptation: sociology-reviewed-entrypoint
---

# 缺失数据

将缺失机制作为依赖研究过程的假设，并传播处理不确定性。

## 工作方式

1. 先标出应答资格、跳题和各类缺失，描述按变量、波次与群体的缺失模式。
2. 利用采集过程和可观测差异讨论 MCAR、MAR、MNAR；清楚区分诊断证据和不可验证的假设。
3. 说明完整案例分析的适用条件及目标总体变化；采用 MI 时包含结局、预测缺失的辅助变量及分析模型结构，匹配分类、连续和多层变量。
4. 检查插补链、分布、有效范围和 Monte Carlo 误差；每个插补数据单独估计，再用 Rubin 规则及合适自由度汇总。
5. 针对关键结论设计 MNAR 或 delta 敏感性分析，记录分析样本与结果差异。

## 交付

缺失模式、假设依据、处理脚本、汇总结果和敏感性结论。

## 方法修订与适用边界

上游逐个 t 检验不是 Little 的 MCAR 检验；不显著不能确立 MCAR，观测数据通常无法区分 MAR 和 MNAR。单次均值插补不能恢复推断不确定性；结构性跳题不默认插补。上游 pooling 示例未实现其注释所称的完整 Barnard–Rubin 小样本修正。

保留原始数据和处理记录；缺少数据时交付设计或代码草稿，不能填写虚构的样本量、系数、引文或已经完成的检验。代码执行前核对用户文件、软件版本与官方接口，只报告实际运行结果。

## 来源与按需参考

本入口是社会学适配版，基于 [Wentor AI 原版](https://github.com/wentorai/research-plugins/blob/bf44b3cd617fa94c8a1b254c5d1987142ca3d631/skills/analysis/wrangling/missing-data-handling/SKILL.md) 整理，原版按 MIT 许可保留。需要原始示例或更多方法背景时读取 [上游快照](references/upstream.md) 的相关章节。快照保留了尚未逐段修复的简化规则与示例；本入口的修订是使用条件，不应直接复制快照代码作为经过验证的分析。
