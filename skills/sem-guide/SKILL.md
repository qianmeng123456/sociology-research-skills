---
name: sem-guide
description: 设计和评估 EFA/CFA、潜变量结构方程及测量不变性，区分测量与结构推断。
metadata:
  version: 0.1.0
  upstream_commit: bf44b3cd617fa94c8a1b254c5d1987142ca3d631
  adaptation: sociology-reviewed-entrypoint
---

# 测量模型与 SEM

先建立可识别且有理论依据的测量模型，再考虑结构路径。

## 工作方式

1. 说明反映性或形成性测量、潜变量含义、尺度设定、模型识别和样本依据。
2. 依据题项尺度、分布和缺失选择估计方法；有序题项在 lavaan 中明确 ordered 及适用估计器，检查当前版本对缺失和复杂设计的支持。
3. EFA 结合理论和数据探索；CFA 验证预设结构，说明是否使用独立样本、留出样本或同样本探索。
4. 检查收敛、异常方差、负荷、残差及多个拟合指标；修改指数只能提供待理论评估的线索。
5. 组间比较先评估适当的测量不变性；报告不变性层级、部分不变性的依据和均值比较限制。

## 交付

测量与结构模型语法、估计理由、诊断、参数和区间、模型修改记录。

## 方法修订与适用边界

不按固定 CFI/RMSEA 或 α 门槛宣告效度成立；不以同一数据反复删题后称为独立确认。横截面 SEM 的箭头或间接效应不能单独证明因果机制。

保留原始数据和处理记录；缺少数据时交付设计或代码草稿，不能填写虚构的样本量、系数、引文或已经完成的检验。代码执行前核对用户文件、软件版本与官方接口，只报告实际运行结果。

## 来源与按需参考

本入口是社会学适配版，基于 [Wentor AI 原版](https://github.com/wentorai/research-plugins/blob/bf44b3cd617fa94c8a1b254c5d1987142ca3d631/skills/analysis/statistics/sem-guide/SKILL.md) 整理，原版按 MIT 许可保留。需要原始示例或更多方法背景时读取 [上游快照](references/upstream.md) 的相关章节。快照保留了尚未逐段修复的简化规则与示例；本入口的修订是使用条件，不应直接复制快照代码作为经过验证的分析。

核对依据：

- [lavaan：有序数据](https://lavaan.ugent.be/tutorial/cat.html)
