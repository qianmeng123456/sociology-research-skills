# 简化问卷 JSON

仅支持单选 `single`、整数 `integer`、文本 `text`，单条向前路径及按精确答案跳转。不支持多选、随机化、配额、复合条件、循环题和跨题动态逻辑；不能代替问卷平台测试。

顶层包含 `start`、`questions` 和可选 `scales`。问题字段：`id`、`variable`、`wording`、`type`、`missing`（代码到原因）及 `next`（答案到目标，`*` 为默认，`END` 为结束）。单选有 `options`（仅有效代码），整数有 `min/max`。代码在 JSON 对象中用字符串；数值响应传整数，文本传字符串。

量表有 `id/items/min/max/method/min_answered/reverse`，仅支持数值编码的单选题。`method` 是 mean 或 sum；未作答或缺失码不计分，少于 min_answered 返回 None。反向公式适用于上下界不为1的量尺；保留缺失码。反向列表可为空，不建议为使用脚本强行增加反向题。

运行：`python <skill-dir>/scripts/check_questionnaire.py <questionnaire.json>`。

校验覆盖 ID/变量重名、选项缺失码冲突、非法目的题号、未覆盖分支、不可达节点、环和合成分配置。它不理解“是否应该看到该题”的实质资格条件，不能检查中文措辞、因果识别或构念效度。评分函数也不负责资格判定；调用方先按问卷路径处理输入。
