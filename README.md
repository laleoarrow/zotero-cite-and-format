# zotero-cite-and-format

### Zotero 引文与格式

`zotero-cite-and-format` 处理的是 Word 手稿里“引文完整性”和“期刊格式要求”同时成立的场景。Zotero 修复只是其中一部分，不是全部。它既处理 Zotero 引文是否还能刷新、参考文献是否还能安全重建，也处理面向目标期刊的 Word 格式细节，以及从已验证的 Zotero 源稿导出投稿静态稿。

默认不应该一上来就导出静态稿。先问两个问题：
- 目标期刊是什么？
- 这个期刊或投稿系统是否明确要求提交去掉 field codes 的静态手稿？

如果期刊还没定，或者暂时没有静态稿要求，就先只维护 `Zotero 可编辑稿`。

默认顺序应当是强制的：
1. 先修好或确认 `Zotero 可编辑稿`
2. 把这个 Zotero 版本当作唯一的规范源稿
3. 只有确实需要投稿静态稿时，才从这个源稿导出

它适合这几类情况：
- Zotero 识别不到这些引文，或者这些引文已经不能继续刷新/编辑
- bibliography 损坏、重复，或者一刷新就报错
- 需要按目标期刊要求调整 Word 手稿格式，但又不能把 Zotero 活字段或语义格式弄坏
- 需要把稿件分成两份：
  - 一份继续用 Zotero 改
  - 一份提交投稿系统
- 需要确认某个期刊是否应该提交静态稿而不是带 field code 的源稿

## 核心原则

1. 不要把普通文本伪装成 Zotero citation。
2. 先分清楚目标文件是 `Zotero 可编辑稿` 还是 `投稿静态稿`。
3. 任何会影响投稿行为的判断，先看官方来源：
   - Zotero 官方 KB
   - Zotero 官方 Word 集成实现
   - 目标期刊 author instructions

## 最容易踩的坑

最危险的不是报错，而是“看起来差不多”。

Zotero 的 bibliography 里，第 1 条参考文献有时和 bibliography field 的锚段在同一个段落里。静态导出时如果把这个段落按普通 field 去剥，就会出现三个典型问题：
- `ref 1` 丢失
- `References` 下面出现一大块空白
- 文献列表直接从 `2.` 开始

所以静态导出后一定要查：
- `ZOTERO_ITEM = 0`
- `ZOTERO_BIBL = 0`
- `References` 后面是不是立刻接 `1.`

## SCI 通用格式卫生

除非目标期刊另有明确要求，英文 SCI 的 Word 手稿应尽量把“有语义的格式”保留为真正的 Word 格式，而不是靠长得像的字符去伪装。

落到实操上，通常意味着：
- 科学计数法的指数用真正的上标格式
- 优先写成 `1.54 × 10` 加上标 `-3`，而不是直接粘成 `1.54 × 10⁻3`
- 该用斜体的内容就用真正斜体，不要用伪装字符
- 不要把 hyphen、minus、en dash、em dash 不分场景地混成一种符号
- 验证时看 Word 或渲染后的 PDF 页面，因为纯文本提取经常会把正确的上标压平成 `10-3`

## 怎么验证这个 skill 是能用的

这个 skill 现在是 `说明型 skill`，不是带现成脚本的自动化工具。所以“能不能运行”，看的不是单元测试，而是三件事：
- 会不会把问题先分成 `Zotero 可编辑稿` 和 `投稿静态稿`
- 会不会去查 Zotero 和期刊官方规则，而不是凭印象乱说
- 处理完以后，能不能把结果核到文档结构上

仓库里的 `references/` 就是为这个准备的：
- `references/official-sources.md`
  - 放官方依据，防止把 Word/Zotero 行为说错
- `references/validation-cases.md`
  - 放真实失败案例，检查这个 skill 有没有覆盖到关键坑

如果以后这个 skill 要升级成“真正可测试”的版本，再补 `scripts/` 更合适。那时候才值得加自动化测试。

## 处理顺序

```text
先把 Zotero 源稿弄好
        ↓
检查 docx 包结构
        ↓
确认 Zotero 条目和样式
        ↓
在 Word 里 refresh
        ↓
如确有需要，再从该源稿导出静态稿
        ↓
检查 ref 1、heading、field 数量
```

## 什么时候用，什么时候别用

适合：
- 修引文
- 修参考文献
- 导出投稿稿
- 查 Zotero/Word 文档结构问题

不适合：
- 单纯润色正文
- 单纯补 DOI
- 不涉及 Zotero 的普通 DOCX 排版
- 在目标期刊未定、也没有静态稿要求时，机械地先导出一份静态稿

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

安装时应始终指向 `skills/zotero-cite-and-format` 这个规范 skill 根目录，因为它包含 `SKILL.md` 和 `references/`。

## 相关 Skills

| Skill | 用途 |
|-------|------|
| `doc` | DOCX 结构化编辑与版式检查 |
| `academic-editing` | 正文润色与内容一致性修订 |
| `bioinfo-autopilot` | 数据与证据链核对 |

## License

MIT License
