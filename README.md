# 社会学研究 Skills

通用社会学研究工具集 v0.1：20 个经方法适配的 Wentor 基础技能，加上 7 个社会学专用技能。优先打磨问卷设计，默认中文说明，保持 Stata、R、Python 中立。

这是可调用的研究指导与工作流程，不是自动获得数据、统计软件许可或已经通过实证验证的科研系统。

## 先用什么

- 从整个研究问题开始：`$sociology-research-workflow`。
- 设计/检查问卷：`$sociological-survey-design`。
- 理论和研究假设：`$sociological-theory-analysis`。
- 质性访谈与编码：`$qualitative-interview-coding`。
- 文本构念测量：`$computational-text-analysis-for-social-science`。
- 抽样、权重和推广：`$sociological-sampling-design`。
- 研究整理和证据核对：`$sociological-reproducible-reporting`。

例如：`请用 $sociological-survey-design，围绕社区互助与归属感设计问卷。先给完整初稿，标明假设、自编题、编码、跳题及预测试方案，再和我修改。`

完整技能路由见 [工作流入口](skills/sociology-research-workflow/SKILL.md)。核心问卷设计见 [SKILL.md](skills/sociological-survey-design/SKILL.md)，可讨论的 [中文示例](examples/survey-demo/设计说明.md) 展示实际输出与尚待解决的问题。

## 项目与安装

从 GitHub 获取整套技能：

```bash
git clone https://github.com/qianmeng123456/sociology-research-skills.git
cd sociology-research-skills
python scripts/install_local.py
python scripts/install_local.py --apply
```

私有仓库需要相应 GitHub 访问权限。安装只需要 Python 标准库；修改并重新构建基础入口时才需要 PyYAML。本机安装回执由安装脚本生成，不纳入 GitHub 仓库。

`skills/` 是共同维护的安装版本；`vendor/wentorai/` 保存固定版本上游文件；`sources/` 保存来源、许可、选择路径及构建记录。运行时入口已重写方法决策，原版作为按需参考 `references/upstream.md` 保留。原版示例并非全部经过运行验证，安装入口指出具体适用限制。

`python scripts/install_local.py` 只预览；`python scripts/install_local.py --apply` 安装到用户的 `.agents/skills`。已存在且不同的文件会停止，不覆盖用户的其他技能。后续从项目更新使用 `--apply --update-managed`，仅替换安装回执确认仍未被用户修改的本项目文件；含文件删除的更新需要另行处理。复制后逐文件比较 SHA-256，回执见 `validation/installation.json`。

安装后技能可在下一轮使用。如果当前任务的技能清单尚未刷新，可明确给出技能路径；文件安装验证不等于已观测到应用自动触发，实际发现状态需在下一轮确认。[官方技能文档](https://learn.chatgpt.com/docs/build-skills)

## 本地验证

`python -m unittest discover -s tests -v` 检查问卷路径、缺失计分和安装冲突保护。

`python skills/sociological-survey-design/scripts/check_questionnaire.py examples/survey-demo/questionnaire.json` 检查简化 JSON 问卷的结构与编码。

`python scripts/validate_bundle.py --validator <skill-creator目录>/scripts/quick_validate.py --installed` 检查27个入口、内部链接、原版哈希与实际安装文件。验证报告保存在 `validation/`。构建基础入口需要 Python 与 PyYAML：`python scripts/build_foundation.py`；该命令从本地固定快照生成，不自动升级上游。

这些检查不证明构念效度、因果识别、真实样本代表性或 Stata/R 示例已执行。当前版本是可使用并继续共同迭代的工具集初版，用户研究上的实际验证尚未完成。

## 来源与协作

原始对话用于选择方向，具体来源重新核查。基础来源：[wentorai/research-plugins](https://github.com/wentorai/research-plugins)，固定 commit `bf44b3cd617fa94c8a1b254c5d1987142ca3d631`。聚合目录：[Auto-Research-Skills](https://github.com/brycewang-stanford/Auto-Research-Skills)。上游原文保留 Wentor AI MIT 许可，不代表所有外链资源或量表自动取得同一许可。

参阅 [设计决策](DESIGN.md) 了解名称替换、方法修订和接下来的共同打磨。后续应以真实使用发现的问题改进，避免为了数量无限增加技能。
