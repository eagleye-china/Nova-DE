import os

# ==============================================================================
# 🌟 配置区：你可以把默认值写在这里，按回车就会使用默认值
# ==============================================================================
DEFAULT_GITHUB_USER = "eagleye-china"
DEFAULT_DESC_EN = "A stunning, GPU-accelerated desktop application for PySide6."
DEFAULT_DESC_ZH = "基于 PySide6 和 QML 打造的炫酷桌面级应用框架。"
DEFAULT_DEPS = '["PySide6>=6.6", "openai>=1.0", "markdown>=3.5"]'


def ask(prompt, default):
    """交互式提问，带有默认值"""
    res = input(f"{prompt} [{default}]: ").strip()
    return res if res else default


def create_project_files():
    print("🚀 欢迎使用 Nova 系列项目脚手架生成器 (企业级配置版)\n")

    # 1. 收集信息
    project_name = ask("📦 项目名 (PyPI包名, 如 nova-chat)", "my-awesome-project")
    repo_name = ask("📁 GitHub仓库名 (如 Nova-Agent)", project_name)
    github_user = ask("👤 GitHub用户名", DEFAULT_GITHUB_USER)
    desc_en = ask("🇬🇧 英文描述 (简短)", DEFAULT_DESC_EN)
    desc_zh = ask("🇨🇳 中文描述 (简短)", DEFAULT_DESC_ZH)

    # 2. 生成 pyproject.toml
    pyproject_content = f"""# ==========================================================
# 🚀 {project_name} 企业级打包配置
# ==========================================================
[build-system]
requires = ["setuptools>=68.2", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{project_name}"
version = "0.1.0"
description = "{desc_en}"
readme = "README.md"
requires-python = ">=3.10"
license = "MIT"
authors = [{{ name = "{github_user}", email = "zdt168@sina.cn" }}]
dependencies = {DEFAULT_DEPS}

[project.urls]
Homepage = "https://github.com/{github_user}/{repo_name}"
Repository = "https://github.com/{github_user}/{repo_name}"
Issues = "https://github.com/{github_user}/{repo_name}/issues"

[tool.setuptools.packages.find]
where = ["src"]

# ✅ 关键：资源文件打包配置 (根据你的项目名自动生成)
[tool.setuptools.package-data]
"{project_name.replace('-', '_')}" = [
    "ui/*.qml",
    "qml/*.qml",
    "resources/*"
]

# ================= 🛡️ 代码质量与规范约束 =================
[tool.ruff]
line-length = 100
target-version = "py310"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W", "UP", "B", "C4", "SIM"]
# 忽略 Qt 命名规范(N802) 和 长行限制(E501)
ignore = ["N802", "E501"]

[tool.mypy]
python_version = "3.10"
strict = true
ignore_missing_imports = true
"""
    with open("pyproject.toml", "w", encoding="utf-8") as f:
        f.write(pyproject_content)
    print("✅ 已生成: pyproject.toml (包含 Ruff/Mypy 企业级配置)")

    # 3. 生成 README.md (英文) - 使用 replace 完美避开 f-string 大括号与反引号冲突
    readme_en = """# {{PROJECT_NAME}} 🌟

> **{{DESC_EN}}**

**English** | [简体中文](https://github.com/{{GITHUB_USER}}/{{REPO_NAME}}/blob/main/README_zh.md)

[![PyPI version](https://img.shields.io/badge/pypi-coming_soon-orange)](https://pypi.org/project/{{PROJECT_NAME}}/)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://pypi.org/project/{{PROJECT_NAME}}/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/{{GITHUB_USER}}/{{REPO_NAME}}/blob/main/LICENSE)

## 🤔 Why {{PROJECT_NAME}}?

- 🚀 **Blazing Fast**: Built with pure PySide6 and QML, zero heavy WebViews.
- 🎨 **Stunning UI**: Native dark mode, smooth animations, and pixel-perfect layout.
- 🧠 **AI Ready**: Out-of-the-box support for OpenAI and DeepSeek protocols.

## 📦 Installation

```bash
pip install {{PROJECT_NAME}}
```

## 🚀 Quick Start (Magic in 10 Lines)

```python
import sys
from PySide6.QtWidgets import QApplication
# Import your amazing component here
# from {{MODULE_NAME}} import AppWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # window = AppWindow()
    # window.show()
    sys.exit(app.exec())
```

## 📸 Screenshots

*(Add your GIFs here - a moving GIF is worth 1000 lines of code.)*

## 📜 License

MIT License. See [LICENSE](https://github.com/{{GITHUB_USER}}/{{REPO_NAME}}/blob/main/LICENSE) for details.
"""

    readme_en = readme_en.replace("{{PROJECT_NAME}}", project_name)
    readme_en = readme_en.replace("{{DESC_EN}}", desc_en)
    readme_en = readme_en.replace("{{GITHUB_USER}}", github_user)
    readme_en = readme_en.replace("{{REPO_NAME}}", repo_name)
    readme_en = readme_en.replace("{{MODULE_NAME}}", project_name.replace('-', '_'))

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_en)
    print("✅ 已生成: README.md (英文门面)")

    # 4. 生成 README_zh.md (中文)
    readme_zh = """# {{PROJECT_NAME}} 🌟

> **{{DESC_ZH}}**

[English](https://github.com/{{GITHUB_USER}}/{{REPO_NAME}}/blob/main/README.md) | **简体中文**

[![PyPI version](https://img.shields.io/badge/pypi-coming_soon-orange)](https://pypi.org/project/{{PROJECT_NAME}}/)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://pypi.org/project/{{PROJECT_NAME}}/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/{{GITHUB_USER}}/{{REPO_NAME}}/blob/main/LICENSE)

## 🤔 为什么选择 {{PROJECT_NAME}}？

- 🚀 **极致性能**：基于原生 PySide6 和 QML，拒绝笨重的 WebView。
- 🎨 **顶级颜值**：原生暗黑模式，丝滑动画，像素级布局。
- 🧠 **AI 原生**：开箱即用的 OpenAI / DeepSeek 协议支持。

## 📦 安装

```bash
pip install {{PROJECT_NAME}}
```

## 🚀 快速开始（10 行代码的魔法）

```python
import sys
from PySide6.QtWidgets import QApplication
# 在这里导入你的惊艳组件
# from {{MODULE_NAME}} import AppWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # window = AppWindow()
    # window.show()
    sys.exit(app.exec())
```

## 📸 效果预览

*(在此处放入你的 15 秒动图 GIF，杀伤力巨大)*

## 📜 开源协议

MIT License，允许商用和二次修改。详情见 [LICENSE](https://github.com/{{GITHUB_USER}}/{{REPO_NAME}}/blob/main/LICENSE)。
"""

    readme_zh = readme_zh.replace("{{PROJECT_NAME}}", project_name)
    readme_zh = readme_zh.replace("{{DESC_ZH}}", desc_zh)
    readme_zh = readme_zh.replace("{{GITHUB_USER}}", github_user)
    readme_zh = readme_zh.replace("{{REPO_NAME}}", repo_name)
    readme_zh = readme_zh.replace("{{MODULE_NAME}}", project_name.replace('-', '_'))

    with open("README_zh.md", "w", encoding="utf-8") as f:
        f.write(readme_zh)
    print("✅ 已生成: README_zh.md (中文门面)")

    # 5. 生成基础 .gitignore
    if not os.path.exists(".gitignore"):
        gitignore_content = """# Python
__pycache__/
*.py[cod]
build/
dist/
*.egg-info/

# IDE
.idea/
.vscode/
.DS_Store

# Environments
.env
.venv
venv/
"""
        with open(".gitignore", "w", encoding="utf-8") as f:
            f.write(gitignore_content)
        print("✅ 已生成: .gitignore")

    print("\n🎉 项目基础设施生成完毕！")
    print("👉 接下来的标准动作：")
    print("   1. 创建 src 目录及代码文件")
    print("   2. 运行 python init_git.py 自动推送代码并打标签发版")
    print("   3. 配置 PyPI 的 Trusted Publishing 体验全自动发版")


if __name__ == "__main__":
    create_project_files()
