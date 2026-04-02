# word-zotero

### Word + Zotero 引文修复

**[English](README.en.md)** | **中文**

`word-zotero` 处理的是 Word 稿件里真正麻烦的那一层：Zotero 引文还是不是活字段，参考文献还能不能安全刷新，live 源稿怎么稳妥地导出成静态投稿稿。

它适合这几类情况：
- Zotero 提示现有引文不是活动引文
- bibliography 损坏、重复，或者一刷新就报错
- 需要把稿件分成两份：
  - 一份继续用 Zotero 改
  - 一份提交投稿系统
- 需要确认某个期刊是否应该提交静态稿而不是带 field code 的源稿

## 核心原则

1. 不要把普通文本伪装成 Zotero citation。
2. 先分清楚目标文件是 `live source` 还是 `static submission`。
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

## 处理顺序

```text
live 还是 static？
        ↓
检查 docx 包结构
        ↓
确认 Zotero 条目和样式
        ↓
在 Word 里 refresh
        ↓
导出静态稿
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

## 相关 Skills

| Skill | 用途 |
|-------|------|
| `doc` | DOCX 结构化编辑与版式检查 |
| `academic-editing` | 正文润色与内容一致性修订 |
| `bioinfo-autopilot` | 数据与证据链核对 |

## License

MIT License
