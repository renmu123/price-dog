# 简介

这是一个监控价格的软件，主要是骏河屋，日亚，animate等，目前实现了玛莎哆啦代理的骏河屋

# TODO

- [ ] 骏河屋
- [ ] animate
- [ ] 日亚
- [ ] 机器人插件
- [ ] WEB-UI
- [ ] 定时任务

# 安装

```commandline
poetry install
poetry shell
python index.py
```

找到`.env.sample`文件重命名为 `.env`，并填写相关配置

```


# 配置含义
```

# 启用MasadoraSuruga解析器必备参数

MASADORA_SURUGA_COOKIE=""

# 发送右键必备参数
```
# 启用MasadoraSuruga解析器必备参数
MASADORA_SURUGA_COOKIE=""

# 发送邮件必备参数
SMTP_SERVER="smtp.qq.com"
SMTP_PORT=465
SMTP_USER=""
SMTP_PASSWORD=""
```
