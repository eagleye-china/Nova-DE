import datetime
import os
from string import Template

# ==============================================================================
# 🌟 配置区：你可以把默认值写在这里，按回车就会使用默认值
# ==============================================================================
DEFAULT_GITHUB_USER = "eagleye-china"
DEFAULT_REAL_NAME = "单保录"
DEFAULT_DESC_EN = "A stunning, GPU-accelerated desktop application for PySide6."
DEFAULT_DESC_ZH = "基于 PySide6 和 QML 打造的炫酷桌面级应用框架。"
DEFAULT_DEPS = '["PySide6>=6.6", "openai>=1.0", "markdown>=3.5"]'


def ask(prompt, default):
    """交互式提问，带有默认值"""
    res = input(f"{prompt} [{default}]: ").strip()
    return res if res else default


def create_project_files():
    print("🔥 欢迎使用 Nova-Forge 终极项目锻造炉 (企业级全家桶版)\n")

    # 1. 收集信息与全局变量
    project_name = ask("📦 项目名 (PyPI包名, 如 nova-chat)", "my-awesome-project")
    repo_name = ask("📁 GitHub仓库名 (如 Nova-Agent)", project_name)
    github_user = ask("👤 GitHub用户名", DEFAULT_GITHUB_USER)
    real_name = ask("✍️ 你的真实姓名 (用于 LICENSE 版权)", DEFAULT_REAL_NAME)
    desc_en = ask("🇬🇧 英文描述 (简短)", DEFAULT_DESC_EN)
    desc_zh = ask("🇨🇳 中文描述 (简短)", DEFAULT_DESC_ZH)

    # 全局模版变量
    year = datetime.datetime.now().year
    module_name = project_name.replace('-', '_')

    # 防止 Markdown 截断的终极杀招
    CB = "`" * 3

    # 2. 生成 pyproject.toml
    pyproject_tmpl = """# ==========================================================
# 🚀 $PROJECT_NAME 企业级打包配置
# ==========================================================
[build-system]
requires = ["setuptools>=68.2", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "$PROJECT_NAME"
version = "0.1.0"
description = "$DESC_EN"
readme = "README.md"
requires-python = ">=3.10"
license = "MIT"
authors = [{ name = "$GITHUB_USER", email = "zdt168@sina.cn" }]
dependencies = $DEPS

[project.urls]
Homepage = "https://github.com/$GITHUB_USER/$REPO_NAME"
Repository = "https://github.com/$GITHUB_USER/$REPO_NAME"
Issues = "https://github.com/$GITHUB_USER/$REPO_NAME/issues"

[tool.setuptools.packages.find]
where = ["src"]

# ✅ 关键：资源文件打包配置
[tool.setuptools.package-data]
"$MODULE_NAME" = [
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
ignore = ["N802", "E501"]

[tool.mypy]
python_version = "3.10"
strict = true
ignore_missing_imports = true
"""
    with open("pyproject.toml", "w", encoding="utf-8") as f:
        f.write(Template(pyproject_tmpl).substitute(
            PROJECT_NAME=project_name, DESC_EN=desc_en,
            GITHUB_USER=github_user, REPO_NAME=repo_name,
            DEPS=DEFAULT_DEPS, MODULE_NAME=module_name
        ))
    print("✅ 已生成: pyproject.toml")

    # 3. 生成 LICENSE (动态年份)
    license_tmpl = """MIT License

Copyright (c) $YEAR $REAL_NAME ($GITHUB_USER)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
    with open("LICENSE", "w", encoding="utf-8") as f:
        f.write(Template(license_tmpl).substitute(
            YEAR=year, REAL_NAME=real_name, GITHUB_USER=github_user
        ))
    print("✅ 已生成: LICENSE (动态年份)")

    # 4. 生成 README.md (英文)
    readme_en_tmpl = f"""# $PROJECT_NAME 🌟

> **$DESC_EN**

**English** | [简体中文](https://github.com/$GITHUB_USER/$REPO_NAME/blob/main/README_zh.md)

[![PyPI version](https://img.shields.io/pypi/v/$PROJECT_NAME?color=blue)](https://pypi.org/project/$PROJECT_NAME/)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://pypi.org/project/$PROJECT_NAME/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/$GITHUB_USER/$REPO_NAME/blob/main/LICENSE)

## 🤔 Why $PROJECT_NAME?

- 🚀 **Blazing Fast**: Built with pure PySide6 and QML, zero heavy WebViews.
- 🎨 **Stunning UI**: Native dark mode, smooth animations, and pixel-perfect layout.
- 🧠 **AI Ready**: Out-of-the-box support for OpenAI and DeepSeek protocols.

## 📦 Installation

{CB}bash
pip install $PROJECT_NAME
{CB}

## 🚀 Quick Start (Magic in 10 Lines)

{CB}python
import sys
from PySide6.QtWidgets import QApplication
# from $MODULE_NAME import AppWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sys.exit(app.exec())
{CB}

## 📸 Screenshots

*(Add your GIFs here - a moving GIF is worth 1000 lines of code.)*

## 📜 License

MIT License. See [LICENSE](https://github.com/$GITHUB_USER/$REPO_NAME/blob/main/LICENSE) for details.
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(Template(readme_en_tmpl).substitute(
            PROJECT_NAME=project_name, DESC_EN=desc_en, GITHUB_USER=github_user,
            REPO_NAME=repo_name, MODULE_NAME=module_name
        ))
    print("✅ 已生成: README.md")

    # 5. 生成 README_zh.md (中文)
    readme_zh_tmpl = f"""# $PROJECT_NAME 🌟

> **$DESC_ZH**

[English](https://github.com/$GITHUB_USER/$REPO_NAME/blob/main/README.md) | **简体中文**

[![PyPI version](https://img.shields.io/pypi/v/$PROJECT_NAME?color=blue)](https://pypi.org/project/$PROJECT_NAME/)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://pypi.org/project/$PROJECT_NAME/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/$GITHUB_USER/$REPO_NAME/blob/main/LICENSE)

## 🤔 为什么选择 $PROJECT_NAME？

- 🚀 **极致性能**：基于原生 PySide6 和 QML，拒绝笨重的 WebView。
- 🎨 **顶级颜值**：原生暗黑模式，丝滑动画，像素级布局。
- 🧠 **AI 原生**：开箱即用的 OpenAI / DeepSeek 协议支持。

## 📦 安装

{CB}bash
pip install $PROJECT_NAME
{CB}

## 🚀 快速开始（10 行代码的魔法）

{CB}python
import sys
from PySide6.QtWidgets import QApplication
# from $MODULE_NAME import AppWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sys.exit(app.exec())
{CB}

## 📸 效果预览

*(在此处放入你的 15 秒动图 GIF)*

## 📜 开源协议

MIT License，允许商用和二次修改。
"""
    with open("README_zh.md", "w", encoding="utf-8") as f:
        f.write(Template(readme_zh_tmpl).substitute(
            PROJECT_NAME=project_name, DESC_ZH=desc_zh, GITHUB_USER=github_user,
            REPO_NAME=repo_name, MODULE_NAME=module_name
        ))
    print("✅ 已生成: README_zh.md")

    # 6. 生成 .gitignore
    if not os.path.exists(".gitignore"):
        with open(".gitignore", "w", encoding="utf-8") as f:
            f.write(
                "# Python\n__pycache__/\n*.py[cod]\nbuild/\ndist/\n*.egg-info/\n\n# IDE\n.idea/\n.vscode/\n.DS_Store\n\n# Environments\n.env\n.venv\nvenv/\n")
        print("✅ 已生成: .gitignore")

    # 7. 生成 project_structure.txt
    structure_content = f"""{project_name}/
├── src/
│   └── {module_name}/
│       ├── __init__.py
│       ├── core/
│       │   └── __init__.py
│       └── ui/
│           ├── __init__.py
│           └── main_window.py
├── examples/
│   └── basic_demo.py
├── LICENSE
├── README.md
├── README_zh.md
├── .gitignore
└── pyproject.toml
"""
    with open("project_structure.txt", "w", encoding="utf-8") as f:
        f.write(structure_content)
    print("✅ 已生成: project_structure.txt")

    # 8. 生成 init_git.py (一键推 GitHub)
    init_git_content = f"""import subprocess
import sys
import os
import re
from pathlib import Path

GITHUB_USER = "{github_user}"

def run(cmd, ignore_error=False):
    print(f"👉 正在执行: {{' '.join(cmd)}}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0 and not ignore_error:
        print(f"❌ 错误: {{result.stderr}}")
    return result

def main():
    repo_name = Path.cwd().name
    version = "0.1.0"
    toml_path = Path.cwd() / "pyproject.toml"
    if toml_path.exists():
        content = toml_path.read_text(encoding="utf-8")
        v_match = re.search(r'version\\s*=\\s*["\\']([^"\\']+)["\\']', content)
        if v_match: version = v_match.group(1)

    remote_url = f"git@github.com:{{GITHUB_USER}}/{{repo_name}}.git"
    tag_name = f"v{{version}}"

    if not os.path.exists(".git"):
        run(["git", "init"])
        run(["git", "branch", "-M", "main"])
        run(["git", "config", "core.autocrlf", "false"])
        run(["git", "add", "."])
        run(["git", "commit", "-m", f"feat: initial release v{{version}}"])

    remotes = subprocess.run(["git", "remote"], capture_output=True, text=True).stdout
    if "origin" not in remotes:
        run(["git", "remote", "add", "origin", remote_url])

    run(["git", "push", "-f", "-u", "origin", "main"])

    tags = subprocess.run(["git", "tag"], capture_output=True, text=True).stdout
    if tag_name not in tags.split():
        run(["git", "tag", tag_name])
    run(["git", "push", "origin", tag_name])
    print(f"🚀 已推送到 GitHub 并触发 {{tag_name}} 发布！")

if __name__ == "__main__":
    main()
"""
    with open("init_git.py", "w", encoding="utf-8") as f:
        f.write(init_git_content)
    print("✅ 已生成: init_git.py (一键推 GitHub)")

    # 9. 生成 build_prod.bat (一键推 PyPI)
    build_bat_content = f"""@echo off
chcp 65001 >nul
echo =========================================
echo       {project_name} 打包与发布
echo =========================================
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build
if exist src\\*.egg-info rmdir /s /q src\\*.egg-info
python -m build
python -m twine check dist/*
python -m twine upload dist/*
pause
"""
    with open("build_prod.bat", "w", encoding="utf-8") as f:
        f.write(build_bat_content)
    print("✅ 已生成: build_prod.bat (一键发版 PyPI)")

    print("\n🎉 终极全家桶生成完毕！你现在拥有：")
    print("   1. 完整的配置文件与文档")
    print("   2. LICENSE 协议 (已自动填入当前年份)")
    print("   3. 目录结构规范")
    print("   4. 一键推 GitHub (init_git.py)")
    print("   5. 一键推 PyPI (build_prod.bat)")
    print("👉 下一步：直接写你的核心代码，然后双击运行发版脚本！")


if __name__ == "__main__":
    create_project_files()
