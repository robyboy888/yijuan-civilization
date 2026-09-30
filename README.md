# 一卷 · 文明长卷系列

给出一个题目，让 Codex 自主研究、写作并制作文明史长卷视频，同时保留全部中间成果。

**示例：**《一卷道路：从兽径，到卫星轨道》

默认输出 180 秒、1920×1080、30fps 的青绿长卷，采用中文纪录片旁白、2.5D 分层动画、配乐、环境音和中文字幕。可以指定其他时长、比例和风格。

## 安装到 Codex

将仓库克隆到 Codex 的用户技能目录。若配置了 `CODEX_HOME`，请使用该目录下的 `skills`；否则默认是 `~/.codex/skills`。

### Windows PowerShell

```powershell
$skillHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
git clone https://github.com/robyboy888/yijuan-civilization.git (Join-Path $skillHome 'skills/yijuan-civilization')
```

### macOS / Linux

```bash
git clone https://github.com/robyboy888/yijuan-civilization.git "${CODEX_HOME:-$HOME/.codex}/skills/yijuan-civilization"
```

安装后，在新会话中调用：

```text
使用 $yijuan-civilization 制作《一卷道路：从兽径，到卫星轨道》。
```

也可以指定范围：

```text
使用 $yijuan-civilization 制作《一卷光明：从篝火，到激光》，时长150秒。
```

```text
使用 $yijuan-civilization，为《一卷记忆：从壁画，到数字世界》只完成研究、长篇母文案和分镜。
```

## 每集保留什么

|阶段|成果|
|---|---|
|研究|英文一手资料、直达来源、年代与论断对应表、不确定性说明|
|文字|3000–5000字母文案 MD/TXT、实际配音稿、完整分镜|
|画面|风格设定、概念长卷、最终提示词、场景图和独立图层|
|声音|原始配音、对齐数据、音乐/音效来源、混音|
|工程|可修改动画工程、素材清单、工具版本、复现命令|
|交付|高清母版、分享版、SRT、封面、实际成片验收记录|
|传播|长卷预告文案、X精简版、视频号文案|

详细文件约定见 [delivery.md](references/delivery.md)。

## 研究原则

每集重新搜索并打开资料正文核验。UNESCO、The Metropolitan Museum of Art、World Bank、Nature 是可选来源，按主题扩展至考古研究、博物馆、CERN、NASA、ESA、原始论文和技术档案。

区分文学意象与可验证史实，避免把“第一簇火”“岩壁刻痕”等叙事起点写成已知的唯一发明事件。来源机构不代表参与制作或为作品背书。

## 系列题目

- 《一卷人类：从第一簇火，到空间站》
- 《一卷道路：从兽径，到卫星轨道》
- 《一卷文字：从岩壁刻痕，到云端数据》
- 《一卷光明：从篝火，到激光》
- 《一卷远方：从步行，到深空探测》
- 《一卷城市：从村落，到超级都市》
- 《一卷机器：从石器，到人工智能》
- 《一卷记忆：从壁画，到数字世界》

各集叙事重点见 [series.md](references/series.md)。列表是选题参考，不会自动批量开拍。

## 运行条件

这是 Codex 工作流技能，不是独立的视频生成程序。完整制作需要所在环境提供联网检索、图像生成、中文 TTS、动画渲染及 FFmpeg/ffprobe。默认优先使用可用的 imagegen 和 HyperFrames；执行时检测工具与权限，服务费用按所用服务计算。仓库不包含这些工具、账号凭据或成片素材。

交付检查脚本使用 Python 3.9+ 标准库：

```bash
python scripts/audit_package.py /path/to/episode
```

它检查 `project.json` 中的必备文件、空文件和越界路径；不代替史实核查、视频解码或人工视听验收。详见 [制作与验收](references/production.md)。

生成结果默认保存在本地。发布到 X、视频号或其他平台需要单独指令。
