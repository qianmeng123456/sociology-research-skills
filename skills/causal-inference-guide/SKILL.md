---
name: causal-inference-guide
description: 为观察性社会研究评估 DiD、IV、RDD 或合成控制的识别条件，并设计诊断与敏感性分析。
metadata:
  version: 0.1.0
  upstream_commit: bf44b3cd617fa94c8a1b254c5d1987142ca3d631
  adaptation: sociology-reviewed-entrypoint
---

# 因果研究设计

先界定反事实、目标效应、干预时序和选择机制，再选择估计方法。

## 工作方式

1. 明确 ATE/ATT/LATE 或局部效应、处理单位、目标人群、时间零点、干扰与处理定义。
2. 用设计说明或因果图识别混杂、碰撞变量和处理后变量，避免无差别加入控制。
3. DiD 区分两组两期与分期处理；存在异质效应时评估分组时期 ATT 等方法，记录比较组、无预期及平行趋势假设。
4. IV 论证相关性、外生性、排除和适用时的单调性；RDD 检查阈值规则、操控、带宽和局部支持；合成控制评估供体污染与处理前拟合。
5. 按分配与误差相关结构选聚类层级，考虑少集群问题；报告效应区间、安慰剂、设计诊断和假设敏感性。

## 交付

识别论证、威胁及诊断计划、估计代码、可支持的因果陈述边界。

## 方法修订与适用边界

前趋势 p>0.05 不证明平行趋势。分期处理不默认使用普通 TWFE。上游 DiD/RDD/IV 代码是简化演示，存在聚类、首阶段控制与带宽问题；实际估计应使用核对过的实现。F>10 和过度识别检验通过不证明工具有效；RDD 不默认以运行变量标准差设带宽。

保留原始数据和处理记录；缺少数据时交付设计或代码草稿，不能填写虚构的样本量、系数、引文或已经完成的检验。代码执行前核对用户文件、软件版本与官方接口，只报告实际运行结果。

## 来源与按需参考

本入口是社会学适配版，基于 [Wentor AI 原版](https://github.com/wentorai/research-plugins/blob/bf44b3cd617fa94c8a1b254c5d1987142ca3d631/skills/analysis/econometrics/causal-inference-guide/SKILL.md) 整理，原版按 MIT 许可保留。需要原始示例或更多方法背景时读取 [上游快照](references/upstream.md) 的相关章节。快照保留了尚未逐段修复的简化规则与示例；本入口的修订是使用条件，不应直接复制快照代码作为经过验证的分析。

核对依据：

- [Jonathan Roth：DiD 研究与工具](https://www.jonathandroth.com/did-resources/)
