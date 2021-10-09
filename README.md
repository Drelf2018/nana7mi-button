# 鲨鱼按钮

## 贡献

请fork这个项目进行修改，修改完成后，在这个项目中发起一个Pull Request。

### 添加音声

**描述**: 所有语音元文件都存储在[src/voices.json 中](https://github.com/Drelf2018/nanami-button/blob/main/src/voices.json)。要添加或修改这些声音，您需要相应地修改此文件。

语音始终为 mp3 格式并存储在[public/voices 中](https://github.com/Drelf2018/nanami-button/blob/main/public/voices)。对应的网址是`voices/`。

对于新的语音，请使用 MP3GainGUI 等软件进行音量标准化。目前体积标准化值为 80。

由于本网站使用了强大的缓存策略，除了`index.html`，文件的文件名相同，即使修改，将**永远不会**被客户端刷新。因此，新语音的文件名，无论是新的还是修改过的，都**必须**与任何以前的文件名不同。

如果是修改语音，修改后删除原文件。

## 本地开发环境

本站使用 Vue + jQuery + Bootstrap 3 开发。

要部署本地开发环境，请先安装最新版本的 Node。然后按照以下步骤操作：

1. 克隆代码。
2. 转到代码目录并运行`npm install`.
3. 运行`npm run serve`。在代码修改过程中，这个本地开发服务器可以立即反映修改的结果。
4. 要编译用于部署的文件，请运行`npm run build`，这将生成`dist`目录。本站完全静态，可以直接部署整个`dist`目录。

> 要将您的代码贡献给这个项目，您不必在本地编译。在开发服务器中测试通过并推送到Github后，可以直接向这个项目请求一个Pull Request。

## 许可

项目: MIT


## 特别感谢

本项目基于 [aqua-button](https://github.com/zyzsdy/aqua-button).

本项目基于 [Meamea button](https://github.com/zyzsdy/meamea-button).

本项目基于 [Miki BUTTON](https://github.com/xuziang111/miki-button-src).

### 致Fork了本代码库的各位按钮站站长

不必在左下角标识“Powered By MeowSound Idols”，这不是版权标记的一部分。

Aqua Button和Meamea Button由MeowSound Idols托管并运营，因此加入了上述标识。

本项目中新增了 `file2json.py` 用于将新增的音频自动生成对应的 voices.json 配置文件

本项目中新增了 `modifyVoice.py` 用于规范化新增的音频音量

