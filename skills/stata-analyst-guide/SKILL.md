---
name: stata-analyst-guide
description: 在用户选择 Stata 时组织社会研究 do-file、描述统计、模型估计与论文输出。
metadata:
  version: 0.1.0
  upstream_commit: bf44b3cd617fa94c8a1b254c5d1987142ca3d631
  adaptation: sociology-reviewed-entrypoint
---

# Stata 社会研究分析

适配已安装的 Stata 版本和实际数据结构。

## 工作方式

1. 检查 Stata 可用性、许可、版本、数据字典和研究设计；无运行环境时明确交付未执行的 do-file。
2. 设置项目相对路径、日志、随机种子和软件版本，保留只读原始数据。
3. 核对缺失码、权重、分层、PSU 和面板 ID，先完成描述与范围诊断。
4. 按目标选择 svy、回归、面板或测量方法，报告正确的权重和方差处理；外部 ado 依赖写出来源。
5. 从保存的模型生成图表和解释，核对样本数、基准组、系数量纲及区间。

## 交付

可复跑 do-file、依赖说明、实际运行日志或明确未运行状态、图表与结果解释。

## 方法修订与适用边界

不能把展示 do-file 当成已运行 Stata。软件命令成功不验证研究识别；不要根据显著性自动选择或删改变量。

保留原始数据和处理记录；缺少数据时交付设计或代码草稿，不能填写虚构的样本量、系数、引文或已经完成的检验。代码执行前核对用户文件、软件版本与官方接口，只报告实际运行结果。

## 来源与按需参考

本入口是社会学适配版，基于 [Wentor AI 原版](https://github.com/wentorai/research-plugins/blob/bf44b3cd617fa94c8a1b254c5d1987142ca3d631/skills/analysis/econometrics/stata-analyst-guide/SKILL.md) 整理，原版按 MIT 许可保留。需要原始示例或更多方法背景时读取 [上游快照](references/upstream.md) 的相关章节。快照保留了尚未逐段修复的简化规则与示例；本入口的修订是使用条件，不应直接复制快照代码作为经过验证的分析。
