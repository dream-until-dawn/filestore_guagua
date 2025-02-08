# filestore_guagua

### 介绍

一个自用的 python 数据到本地保存及其读取的库

### 使用

```python
python -m build # 打包
pip install --upgrade twine setuptools wheel packaging # 安装 twine、setuptools、 wheel 和packaging
```
#### 测试线
```python
python -m twine upload --repository testpypi dist/* # 上传包到 pypi-test
pip install --index-url https://test.pypi.org/simple/ --no-deps filestore_guagua # 安装包
```
#### 正式线
```python
python -m twine upload dist/* # 上传包到 pypi
pip install --upgrade filestore_guagua # 安装包
```
