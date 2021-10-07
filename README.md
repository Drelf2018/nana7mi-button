# Miki button

## Contributing

Please fork this project for modification, and after completing the modification, initiate a Pull Request in this project.

### 添加音声

**Description**: All voice meta information is stored in [src/voices.json](src/voices.json). To add or modify these voices, you need to modify this file accordingly.

Voice is always in mp3 format and stored in [public/voices](public/voices). The corresponding URL is `voices/`.

For new voice, please use software such as MP3GainGUI for volume standardization. Currently the volume standardized value is 80.

Because this site uses a strong cache strategy, except for `index.html`, files with the same filename, even if modified, will **NEVER** be refreshed by the client. Therefore, the filename of the newly voice, whatever it is new or modified, **MUST** be different from any previous filename.

If you are modifying voice, delete the original file after modification.

## 本地开发环境

This site is developed using Vue + jQuery + Bootstrap 3.

To deploy a local development environment, first install the latest version of Node. Then follow these steps:

1. Clone the code.

2. Go to the code directory and run `npm install`.

3. Run `npm run serve`. During the code modification process, this local development server can immediately reflect the results of the modification.

4. To compile the files for deployment, run `npm run build`, which will generate the `dist` directory. This site is completely static, you can directly deploy the entire `dist` directory.

> To contribute your code to this project, you don't have to compile locally. After passing the test in the development server and pushing it to Github, you can directly require a Pull Request to this project.

## LICENCE

Program: MIT


## Special Thanks

本项目基于 [aqua-button](https://github.com/zyzsdy/aqua-button).

本项目基于 [Meamea button](https://github.com/zyzsdy/meamea-button).

### 致Fork了本代码库的各位按钮站站长

不必在左下角标识“Powered By MeowSound Idols”，这不是版权标记的一部分。

Aqua Button和Meamea Button由MeowSound Idols托管并运营，因此加入了上述标识。



