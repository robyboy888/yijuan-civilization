# 交付约定

每集单独目录。续做旧项目时保留现有文件，补齐缺项；不要为了统一命名破坏旧链接。

|路径|必备内容|
|---|---|
|`project.json`|完整题名、短名、时长、分辨率、fps、状态、deliverables 映射|
|`00-文字全文-纪录片母文案.md`|完整长文、用途说明、来源索引|
|`00-文字全文-纪录片母文案.txt`|纯正文|
|`01-完整脚本与分镜.md`|时间轴、精确旁白、场景、运动、转场、来源ID|
|`02-史料依据与边界.md`|来源表、论断对应、日期及不确定性|
|`03-概念图说明与提示词.md`|概念图说明、分场最终提示词、图层要求|
|`04-成片交付说明.md`|实际规格、文件导航、验收、限制、复现命令|
|`05-文明长卷预告文案.md`|长预告、X版、视频号版、封面简介|
|`design.md`|系列风格与本集构图/声音设计|
|`assets/`|概念图、正式场景、独立图层（可在 film/assets 下，通过映射指定）|
|`film/`|可编辑工程、最终 narration.txt、配音原文件、边界数据、混音、字幕、生成清单、验收日志、实际成片抽帧|
|`封面.png`|单独可使用封面，与最终标题一致|
|`短标题-时长秒-1080p.mp4`|高清母版|
|`短标题-时长秒-1080p-分享版.mp4`|分享版，按实际比例调整文件标签|
|`短标题.srt`|外置字幕|

`project.json` 示例结构（路径都相对本集目录，替换示例数据）：

```json
{
  "title": "一卷道路：从兽径，到卫星轨道",
  "short_title": "一卷道路",
  "duration_seconds": 180,
  "width": 1920,
  "height": 1080,
  "fps": 30,
  "status": "in_progress",
  "deliverables": {
    "mother_md": "00-文字全文-纪录片母文案.md",
    "mother_txt": "00-文字全文-纪录片母文案.txt",
    "storyboard": "01-完整脚本与分镜.md",
    "research": "02-史料依据与边界.md",
    "prompts": "03-概念图说明与提示词.md",
    "delivery": "04-成片交付说明.md",
    "copy": "05-文明长卷预告文案.md",
    "design": "design.md",
    "concept": "assets/长卷概念图.png",
    "cover": "封面.png",
    "master": "一卷道路-180秒-1080p.mp4",
    "share": "一卷道路-180秒-1080p-分享版.mp4",
    "srt": "一卷道路.srt",
    "narration": "film/narration.txt",
    "composition": "film/index.html",
    "manifest": "film/production-manifest.json",
    "voice": "film/assets/narration.wav",
    "voice_alignment": "film/audio-timing.json",
    "mix": "film/assets/audio-master.wav",
    "verification": "film/verification.json",
    "share_verification": "film/share-verification.json",
    "snapshots": "film/snapshots"
  }
}
```

状态只有完成实际验收后才改为 `complete`。生成清单逐项记录全部素材及配音分段，验收记录覆盖母版和分享版。项目里的文件路径必须真实有效。

默认保留全部中间成果，不在渲染结束后清理原音频、边界数据、提示词、素材、工程或日志。交付回复优先展示视频与母文案、预告文案链接，再简要列出规格及限制，不必把每个素材路径都塞进聊天。
