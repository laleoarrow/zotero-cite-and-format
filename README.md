# zotero-cite-and-format

### Zotero 引文与格式

`zotero-cite-and-format` 是一个 **Word-facing manuscript skill**。它处理的不是“找文献”本身，而是 **Word 手稿里的 Zotero 活字段、参考文献、期刊格式、导出策略和最终 QA**。

它的核心目标只有一个：**把手稿保持为可继续用 Zotero 编辑、能按期刊要求导出、且在 Word 里稳定工作的规范稿件。**

## 它负责什么

- 修复或核对 Zotero live fields
- 刷新或重建 bibliography
- 区分 `Zotero 可编辑稿` 与 `投稿静态稿`
- 根据 review / research 手稿类型路由不同格式规则
- 在标题页、摘要、表格、图注、补充材料、符号和 Word run-level 细节上做期刊向格式控制
- 在 repeated corruption、unreadable content、导出后 ref1 丢失等场景下执行 package-level QA

## 它不负责什么

- Zotero library 搜索、导入、全文获取、API 查询
- 普通正文润色或综述语言重写
- 与 Zotero 无关的纯 DOCX 排版

这些分别应交给：
- `zotero:Zotero`
- `academic-editing`
- `doc`

## 核心约束

- 规范源稿永远是 `name_zotero.docx`
- `name.docx` 只在期刊/投稿系统要求或用户明确要求时才创建
- 用户可见的 manuscript DOCX 最多保留两份
- 完成后删除临时文件、throwaway 变体和 recovery 副本
- 绝不伪造 Zotero citation
- 绝不 unlink 规范源稿
- 绝不把 `ADDIN ZOTERO_ITEM` 计数当作完整验证

## 处理顺序

1. 先分清任务类型：
   `Library / Citation Discovery`、`Live Field / Bibliography`、`Review Manuscript Formatting`、`Research Manuscript Formatting`、`Package Final Gate`
2. 先修好或确认 `name_zotero.docx`
3. 再做 Word-facing formatting
4. 确有需要时才导出 static copy
5. 最后做 package QA，并清理临时文件

## 重灾区

最常见的误判不是“明显报错”，而是：

- field 数量看起来对，但 refresh 不工作
- bibliography 看起来在，实际上 ref 1 丢了
- Word 能打开一次，但反复 reopen 会触发 unreadable-content / recovery
- 标题页、摘要、表格、脚注符号、斜体 `P`、上标等 run-level 格式在局部修文后 silently drift

这个 skill 的设计重点，就是让这些问题先被路由出来，再去读对应 `references/`，而不是在 `SKILL.md` 里堆满细则。

## references/ 分工

- `word-zotero-workflow.md`
  live-field repair、bibliography rebuild、refresh failure、static export
- `manuscript-formatting.md`
  title page、abstract、prose block、table、legend、supplement、spacing
- `review-manuscripts.md`
  narrative review、perspective、primer、review-style section
- `research-manuscripts.md`
  cohort、omics、MR、trial、methods-driven paper
- `pre-submission-final-gate.md`
  final / submit / 投稿前 / repeated package failure
- `official-sources.md`
  期刊 policy 或 Zotero 行为的官方依据
- `sci-formatting.md`
  斜体、上标、科学符号、run-level hygiene
- `validation-cases.md`
  真实失败案例与回归检查
- `failure-modes.md`
  正常流程解释不了的异常故障

## 为什么现在的 SKILL.md 变短了

旧版本的问题不是规则不够，而是：

- 把“文件产物策略”写成了主叙事
- 同一件事在 `Overview / Default target / Deliverable rule / Quick Reference / Output Contract` 里反复说
- `SKILL.md` 自己承担了太多本应由 `references/` 承担的细节

新版本保留全部关键要求，但把 `SKILL.md` 压缩成：

- scope
- core contract
- hard rules
- division of labor
- route first
- final gate
- report back

这使它更像一个触发器和调度器，而不是一本混合说明书。

## 安装

### CC Switch

```bash
git clone https://github.com/laleoarrow/zotero-cite-and-format.git ~/agents/zotero-cite-and-format
mkdir -p ~/.cc-switch/skills
ln -s ~/agents/zotero-cite-and-format/skills/zotero-cite-and-format ~/.cc-switch/skills/zotero-cite-and-format
```

### Claude Code

```bash
git clone https://github.com/laleoarrow/zotero-cite-and-format.git ~/agents/zotero-cite-and-format
ln -s ~/agents/zotero-cite-and-format/skills/zotero-cite-and-format ~/.claude/skills/zotero-cite-and-format
```

### Codex CLI

```bash
git clone https://github.com/laleoarrow/zotero-cite-and-format.git ~/agents/zotero-cite-and-format
ln -s ~/agents/zotero-cite-and-format/skills/zotero-cite-and-format ~/.codex/skills/zotero-cite-and-format
```

## License

MIT License
