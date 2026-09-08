---
name: text-mining-guide
description: 对研究语料执行分词、检索、主题或分类基线；社会构念测量使用 computational-text-analysis-for-social-science。
metadata:
  version: 0.1.0
  upstream_commit: bf44b3cd617fa94c8a1b254c5d1987142ca3d631
  adaptation: sociology-reviewed-entrypoint
---

# 文本挖掘基础

从语料结构和语言特征选择可验证的文本处理方法。

## 工作方式

1. 确认文档、作者、时间、平台、语言和采集覆盖，检查重复与授权使用范围。
2. 依任务比较保留与移除标点、数字、否定词、表情的影响；中文不默认按空格分词。
3. 先建立可解释的词典或 TF-IDF 基线，再按任务选择主题模型、嵌入或监督模型。
4. 依据作者、来源或时间分割数据；在训练集内拟合词表和预处理，保留独立验证数据。
5. 检查分类别错误、否定、反讽、群体和时间漂移，记录数据及模型版本。

## 交付

语料说明、处理脚本、基线、验证指标及错误分析。

## 方法修订与适用边界

词频、情感词典、主题标签或余弦相似度不是构念效度本身；上游英文清洗和示范情感词表不能直接移植到中文社会学结论。

保留原始数据和处理记录；缺少数据时交付设计或代码草稿，不能填写虚构的样本量、系数、引文或已经完成的检验。代码执行前核对用户文件、软件版本与官方接口，只报告实际运行结果。

## 来源与按需参考

本入口是社会学适配版，基于 [Wentor AI 原版](https://github.com/wentorai/research-plugins/blob/bf44b3cd617fa94c8a1b254c5d1987142ca3d631/skills/analysis/wrangling/text-mining-guide/SKILL.md) 整理，原版按 MIT 许可保留。需要原始示例或更多方法背景时读取 [上游快照](references/upstream.md) 的相关章节。快照保留了尚未逐段修复的简化规则与示例；本入口的修订是使用条件，不应直接复制快照代码作为经过验证的分析。
