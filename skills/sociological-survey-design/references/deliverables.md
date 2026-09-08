# 问卷交付结构

按用户格式输出。未指定时使用 Markdown 问卷、CSV 编码表及 JSON/文字跳题规则即可；不因设计任务强制安装统计软件。

## 研究者简报

写研究问题、估计/描述目标、人群、覆盖与排除、模式、核心概念、预期用途、资料状态和设计假设。预计时长只能标为待预测试估计。

## 操作化记录字段

`rq_id, concept, definition, dimension, indicator, item_id, variable, analytical_role, source_status, source_locator, limitation`

所有题目应有用途；一个题目可支持多个问题。不强制所有人口学协变量都具备潜变量结构。

## 编码记录字段

`item_id, variable, wording, type, options, valid_values_or_range, eligible_if, missing_codes, missing_reason, reverse, scale_id, scoring_rule, next_rule, source_status, version`

事实与行为题通常逐项报告；非单维或未经验证的指标不自动合分。保留合法零值与“不适用”的区别。缺失码与有效数值不能重叠；平台将所有缺失导出为空时保留独立原因字段。

## 受访者版

包含简短说明、目标受访者可理解的自愿参与与跳过方式、真实的数据使用说明、筛选、分组题目和结束语。研究机构、联系人、伦理批件、匿名性及保存期限只有确认后才填真实值；未确认时标为发布前待定，不能假造机构身份。

## 偏误审查与验证

每项实质修改说明改变的含义或可比性。附认知访谈探查、设备与路由测试、样本规划和测量证据方案。末尾列真正阻碍正式调查的待定事项，而非把所有编辑细节变成审批项。
