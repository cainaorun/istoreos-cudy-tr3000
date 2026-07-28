<h1 align="center">iStoreOS for Cudy TR3000</h1>

<p align="center">
  <strong>基于 PadavanOnly ImmortalWrt 源码</strong><br>
  专为 Cudy TR3000 (512MB) 编译的 iStoreOS 固件
</p>

<p align="center">
  <img src="https://img.shields.io/badge/平台-mediatek%2Ffilogic-blue" alt="Platform">
  <img src="https://img.shields.io/badge/闪存-512MB-brightgreen" alt="Flash">
  <img src="https://img.shields.io/badge/内存-512MB-brightgreen" alt="RAM">
  <img src="https://img.shields.io/github/downloads/cainaorun/istoreos-cudy-tr3000/total" alt="Downloads">
</p>

---

## ✨ 特性

| 组件 | 说明 |
|------|------|
| **iStore 应用商店** | 内置完整 iStore 商店，可一键安装各种插件 |
| **Argon 主题** | 最美观的 LuCI 主题，支持深色/浅色模式 |
| **EasePi 面板** | iStoreOS 专属管理面板及资源文件 |
| **全套驱动** | TUN/MD-RAID/Ext4/ExFAT/NTFS/USB3 全包含 |
| **内核模块全开** | 1066+ 个 kmod 包，覆盖所有常用硬件 |

## 📥 下载固件

👉 [**Releases 页面**](https://github.com/cainaorun/istoreos-cudy-tr3000/releases)

下载 `sysupgrade.bin` 文件，通过 LuCI 或 `sysupgrade` 命令刷入。

> ⚠️ 仅适用于 **Cudy TR3000 512MB** 版本

## 🔧 编译说明

### 手动触发编译
1. 进入 [Actions](https://github.com/cainaorun/istoreos-cudy-tr3000/actions) 页面
2. 点击左侧 **Build iStoreOS**
3. 点击 **Run workflow** → **Run workflow**
4. 等待编译完成（约 1-2 小时）

### 自动编译
每天 14:00 (北京时间) 自动检查上游源码更新，有新提交时自动编译发布。

## 📦 固件内容

基于 [padavanonly/immortalwrt-mt798x-6.6](https://github.com/padavanonly/immortalwrt-mt798x-6.6) 源码编译，额外集成：

- `luci-app-store` — iStore 应用商店
- `luci-theme-argon` — Argon 主题
- `luci-app-argon-config` — Argon 主题配置
- `istoreos-files` — iStoreOS 系统配置、EasePi 面板资源
- `kmod-tun` — ZeroTier/Tailscale 等 VPN 工具支持
- `kmod-md-*` — 软 RAID 支持
- `kmod-fs-*` — Ext4/ExFAT/VFAT/NTFS 文件系统支持
- `kmod-usb-*` — USB 3.0/UAS 存储支持

## 📜 刷机方式

### 通过 LuCI 网页升级
1. 进入 **系统 → 备份/升级**
2. 选择 `sysupgrade.bin` 文件
3. 勾选 **保留配置** 或 **不保留配置**
4. 点击 **刷写固件**

### 通过命令行升级
```bash
sysupgrade -n /tmp/sysupgrade.bin
```

## 🤝 鸣谢

- [PadavanOnly](https://github.com/padavanonly) — ImmortalWrt MT798x 源码
- [iStoreOS](https://github.com/istoreos) — iStore 应用商店
- [jerrykuku](https://github.com/jerrykuku) — Argon 主题
- [asrtroh-netizen](https://github.com/asrtroh-netizen/immortalwrt-mt7981-cudy-tr3000) — 参考配置

## 📄 许可证

[GPL-2.0](LICENSE)
