# AMD AI Developer Program Register

> **AMD 官方 AI 开发者计划全自动入职与凭据获取工具**  
> 遵循“开箱即用，极简交付”原则，零复杂配置，一键下号并提取可用 API Key。

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/playwright-stealth-orange.svg)](https://playwright.dev/)
[![Powered By](https://img.shields.io/badge/Powered%20By-RegisterHub-purple.svg)](https://github.com/waw666waw666/RegisterHub)

---

## 框架母港与生态互链 (Ecosystem Backlink)

> **项目背景与互相引流说明**：  
> 本独立工程由 **[RegisterHub](https://github.com/waw666waw666/RegisterHub)** 开源注册自动化主框架一键解耦派生。  
> 
> 如果你需要探索**更多站点的自动化支持**（如 Deepgram、100MilionSeek、AMD、Coarena 等）、**三通道公网临时邮箱轮换**、**账号资产全生命周期审计**、或通过**脚手架一键生成新站点适配器**，欢迎前往并 Star 我们的主框架仓库：  
> 
> **主框架项目传送门**：**[https://github.com/waw666waw666/RegisterHub](https://github.com/waw666waw666/RegisterHub)**

---

## 项目简介

针对 AMD 官方 AI 开发者计划 (https://www.amd.com/en/registration/ai-dev-program-sign-up-form.html) 打造的工业级合规入职工具。具备 OneTrust 模态弹窗深度穿透、Akamai 传感器遥测自洽与表单自动装配能力。

### 核心优势与技术特征

- **顶级科技大厂官方计划**：AMD 官方 AI 算力开发者计划正规通道，合法合规
- **Akamai 遥测环境自洽**：针对企业级反爬自适应调整交互节律与鼠标动力学
- **OneTrust 弹窗穿透**：智能识别并清除阻断视窗的 Cookie 同意层与隐私横幅
- **企业开发者画像合成**：内置逼真的开发者身份、公司与应用场景生成器

---

## 极速上手

### 1. 环境准备与依赖安装

确保你的系统已安装 **Python ≥ 3.10**：

```bash
# 1. 克隆本项目
git clone https://github.com/waw666waw666/amd-register.git
cd amd-register

# 2. 安装核心依赖
pip install -r requirements.txt

# 3. 安装 Playwright 浏览器驱动内核
playwright install chromium
```

### 2. 运行配置与核心实操说明

项目根目录提供开箱即用的 `config.example.json`。可复制为 `config.json` 进行配置：

```json
{
  "email": null,
  "browser": {
    "headless": false,
    "slow_mo": 50,
    "timeout": 35000,
    "channel": "chrome",
    "proxy": "http://127.0.0.1:7897"
  },
  "output_dir": "./results"
}
```

### 核心必读：邮箱配置与验证码接收 (Email & OTP Guide)

1. **自备个人/工作邮箱配置**：
   - AMD 提交开发者入职表单后，会向注册邮箱发送一封包含 **6 位数字验证码** 的官方邮件；
   - 请在 `config.json` 中填入你的真实邮箱：
     ```json
     {
       "email": "your_work_email@outlook.com",
       "browser": {
         "headless": false
       }
     }
     ```
2. **终端交互式验码**：
   - 脚本会自动清理 OneTrust 隐私遮罩并填入全套合规开发者资料；
   - 提交表单后，控制台会停下并提示：
     ```text
     [?] 请在上方查收 AMD 官方邮件，并输入 6 位验证码: 
     ```
   - 打开邮箱查收验证码，在控制台输入 6 位数字回车，脚本即可完成入职并保存凭据至 `results/accounts.txt`。

### 3. 一键启动下号

在 Windows 终端中直接双击 **`run.bat`** 交互菜单，或在命令行运行：

```bash
# 默认生成 1 个账号凭据
python main.py

# 批量生成指定数量账号（如 5 个）
python main.py -n 5

# 无头静默模式运行
python main.py --headless -n 1
```

执行完毕后，所有生成的账号凭据将原子持久化落盘至 **`results/accounts.txt`**：
```text
邮箱----密码----有效API_Key----时间戳
```

---

## 体系化生态矩阵

本工程为 RegisterHub 家族核心实战矩阵之一：

| 独立开源项目 | 核心特色与福利 | 源码直达 |
| :--- | :--- | :--- |
| **RegisterHub** | 通用自动化注册母港与脚手架引擎 | [GitHub](https://github.com/waw666waw666/RegisterHub) |
| **Deepgram Register** | 官方 $200 免费额度 + 谷歌人机穿透 + 纯协议提 Key | [GitHub](https://github.com/waw666waw666/deepgram-register) |
| **100MilionSeek Register** | 每天免费 1 亿 Token 算力 + 免收信秒出 Key + 母号裂变 | [GitHub](https://github.com/waw666waw666/100milionseek-register) |
| **AMD AI Dev Register** | AMD 官方大厂计划 + Akamai 遥测 + OneTrust 穿透 | [GitHub](https://github.com/waw666waw666/amd-register) |
| **Coarena Register** | 谷歌登录后 100% 协议提 Key 与每日额度审计 | [GitHub](https://github.com/waw666waw666/coarena-register) |

---

## 免责声明 (Disclaimer)

本项目仅供软件工程自动化、浏览器驾驶协议与网络可用性技术交流与合法测试使用。使用者必须严格遵守目标平台服务条款与当地法律法规，严禁将本项目用于未经授权的大规模滥用或非法用途。作者不对任何因使用本项目造成的损失承担法律责任。详见 [DISCLAIMER.zh.md](DISCLAIMER.zh.md)。
