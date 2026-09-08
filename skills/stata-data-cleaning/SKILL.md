---
name: stata-data-cleaning
description: 用 Stata 完成研究数据检查、缺失编码、合并、变形和可追溯清洗。
metadata:
  version: 0.1.0
  upstream_commit: bf44b3cd617fa94c8a1b254c5d1987142ca3d631
  adaptation: sociology-reviewed-entrypoint
---

# Stata 数据整理

让每一步整理有可检查的输入输出和损失计数。

## 工作方式

1. 保留 raw，读取变量标签、编码本和导入设置，检查中文编码及日期。
2. 用 isid 或 duplicates 检查键，不以任意保留第一行解决具有实质差异的重复记录。
3. 合并前核对键与基数，合并后检查 _merge 的各类计数和未匹配原因，避免无依据 m:m。
4. 在筛选范围前显式排除 Stata 数值缺失；将拒答、跳题和不知道映射为区分的扩展缺失或配套原因字段。
5. reshape 前后检查唯一键、行数与值一致性；用 assert 写真实不变量，输出清洗日志和数据字典。

## 交付

清洗 do-file、合并与样本流转日志、派生数据及编码表。

## 方法修订与适用边界

Stata 数值缺失大于普通数值，age>60 会包含缺失，需显式限制。异常值不自动删除；不可为通过 isid 随意去重。

保留原始数据和处理记录；缺少数据时交付设计或代码草稿，不能填写虚构的样本量、系数、引文或已经完成的检验。代码执行前核对用户文件、软件版本与官方接口，只报告实际运行结果。

## 来源与按需参考

本入口是社会学适配版，基于 [Wentor AI 原版](https://github.com/wentorai/research-plugins/blob/bf44b3cd617fa94c8a1b254c5d1987142ca3d631/skills/analysis/wrangling/stata-data-cleaning/SKILL.md) 整理，原版按 MIT 许可保留。需要原始示例或更多方法背景时读取 [上游快照](references/upstream.md) 的相关章节。快照保留了尚未逐段修复的简化规则与示例；本入口的修订是使用条件，不应直接复制快照代码作为经过验证的分析。
