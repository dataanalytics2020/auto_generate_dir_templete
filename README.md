# create-project-structure.py

このファイルは、プロジェクトのディレクトリ構造を自動的に作成するPythonスクリプトです。以下の機能を提供します。

## 機能

1. 指定されたパスにディレクトリを作成します。
2. 必要なサブディレクトリ（`src`、`logs`）を作成します。
3. プロジェクトに必要なファイル（`main.py`、`config.py`、`utils.py`、`automation.log`、`.env`、`.gitignore`、`requirements.txt`、`README.md`）を作成します。

## 使用方法

1. スクリプトを実行するには、Pythonがインストールされている必要があります。
2. コマンドラインからスクリプトを実行し、プロジェクトのベースパスを引数として渡します。引数が指定されない場合、デフォルトのパス `attendance_automation` が使用されます。

### コマンド例

```python create_project.py```
```Enter project name: my_awesome_project```
