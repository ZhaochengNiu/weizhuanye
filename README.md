# 微专业招生宣传页与二维码

本目录包含一个可直接上传到学院网站的静态招生宣传页：

- `micro-major-admissions.html`：招生宣传网页
- `generate_qr.py`：根据正式发布后的网页链接生成二维码 SVG

## 使用方式

1. 打开 `micro-major-admissions.html`，将学院名称、微专业名称、报名时间、报名入口、咨询方式等内容替换为本年度真实招生信息。
2. 将 `micro-major-admissions.html` 上传到学院网站，获得正式访问链接。
3. 生成二维码：

```bash
python3 -m pip install --target ./.deps qrcode
PYTHONPATH=./.deps python3 generate_qr.py "https://zhaochengniu.github.io/weizhuanye/"
```

生成的 `admissions-qr.svg` 可粘贴到学校统一的微专业招生宣传材料中。
