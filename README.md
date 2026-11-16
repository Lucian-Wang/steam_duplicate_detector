# Steam账号去重检测工具

本项目是一个用于检测并去除Steam账号列表中重复账号的桌面小工具。适用于需要批量管理、去重Steam账号的场景，提升账号整理效率。

## 功能简介

- 支持批量粘贴账号列表（每行一个账号）
- 按去掉首尾空格后的整行文字精确去重，跳过空行，保留首次出现的顺序
- 明确提示所有重复账号内容
- 去重结果可直接复制和使用
- 简洁易用的中文界面

## 使用方法

1. 克隆或下载本项目代码：

   ```bash
   git clone https://github.com/Lucian-Wang/steam_duplicate_detector.git
   cd steam_duplicate_detector
   ```

2. 运行环境：  
   需安装Python 3，推荐 3.7 及以上版本，自带标准库无需额外依赖。

3. 启动方法：

   ```bash
   python steam_duplicate_detector.py
   ```

4. 按照界面提示操作：

   - 将需要去重的账号列表粘贴到输入框（每行一个账号）
   - 点击“检测去重”按钮
   - 查看去重结果与重复账号提示

## 界面预览

- 输入区标题：“请输入账号列表，每行一个：”
- 检测按钮：“检测去重”
- 输出区标题：“去重后账号列表：”
- 检测结果弹窗会显示“检测到以下重复账号”或“未检测到重复账号”

## 适用场景

- Steam账号批量管理与整理
- 批量导入导出账号时防止重复
- 账号贩卖、租赁等行业批量去重需求

## 开发与贡献

欢迎提交 Issue 或 PR 进行功能完善和Bug修复。

1. Fork 本仓库
2. 新建分支进行开发
3. 提交 Pull Request

## 版权信息

© [Lucian](https://lucian.wang/)

---

如有问题与建议，欢迎通过GitHub Issue与作者联系。

## 维护与反馈

维护者：[Lucian](https://lucian.wang/) · 邮箱：im@lucian.wang · [问题反馈](https://github.com/Lucian-Wang/steam_duplicate_detector/issues)
