<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/zzkluck/ArknightsCharVis">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Arknights-Character-Status-Visualization</h3>

  <p align="center">
    明日方舟干员数据可视化
    <br />
    <a href="https://github.com/zzkluck/ArknightsCharVis"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/zzkluck/ArknightsCharVis">View Demo</a>
    ·
    <a href="https://github.com/zzkluck/ArknightsCharVis/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/zzkluck/ArknightsCharVis/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![ArkVis Demo][product-demo]

我是一名明日方舟玩家，一直以来我尝试将明日方舟的干员数据，以攻防为横纵轴画在一张散点图上：
* [​[数据贴]明日方舟干员大赏(19.11.03)](https://ngabbs.com/read.php?tid=18959001)
* [​[数据氵]自由囚犯版本，干员数据一图流(20.12.17)](https://ngabbs.com/read.php?tid=24687178)
* [​[数据氵]彩虹六号版本，干员数据一图流(21.03.10)](https://ngabbs.com/read.php?tid=25857739)
* [​[数据氵]二周年版本，干员数据一图流发布(21.05.13)](https://ngabbs.com/read.php?tid=26739638)
* [[数据氵]异嘉鸿雪版本，干员数据一图流(22.08.31)](https://ngabbs.com/read.php?tid=33304109)

期间也是尝试了各式各样的技术，但总感觉不太尽如人意。终于，在明日方舟开服五周年之际，最近新学了`manim`，感觉是找到了各方面都比较靠谱的解决方案。与之前的版本相比，突出的好处是可以直接把干员头像怼上去了，真是可喜可贺。

干脆开个项目好了。

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
* [manim](https://www.manim.community/)
* [ArknightsGameData](https://github.com/Kengxxiao/ArknightsGameData)
* [ArknightsGameResource](https://github.com/yuanyan3060/ArknightsGameResource)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

如果你只是需要[图图](images/tutu.png)，~~你只需要到images目录下去找就好了~~，理论上我准备根据版本发在`releases`里，但我还没开始做。

如果你准备看看代码，一起研究下这个图图是怎么画出来的，或者做二次开发，那么需要准备如下环境。

### Prerequisites

本项目的绘图功能强烈地依赖于`manim`，我建议使用`conda`安装，不算创建环境的相关命令，一切顺利的话只要一行：
```bash
conda install -c conda-forge manim
```
如果你的安装过程进行的不太顺利，或者不想使用`conda`，请查阅[manim官方文档](https://www.manim.community/)。大体上就是你得亲手安装`ffmpeg`以及linux下那些`libxxx`。

<!-- USAGE EXAMPLES -->
## Usage
通过如下命令启动`manim`渲染，脚本会自动从[ArknightsGameData](https://github.com/Kengxxiao/ArknightsGameData)和[ArknightsGameResource](https://github.com/yuanyan3060/ArknightsGameResource)中下载所需数据，并保存于`assets`文件夹。
```bash
manim -qk scene.py ArkVis
```
渲染结果于`media/images/scene`中找到。
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] 借助`manim`完成基本的散点图绘制功能
- [x] 自动从其他开源项目下载数据
- [ ] 解决数据点之间的重合覆盖问题
- [ ] 尝试敌人数据的绘制

See the [open issues](https://github.com/zzkluck/ArknightsCharVis/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@zzkluck](https://blog.zzkluck.tech) - zzkluck@qq.com

Project Link: [https://github.com/zzkluck/ArknightsCharVis](https://github.com/zzkluck/ArknightsCharVis)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/zzkluck/ArknightsCharVis/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/zzkluck/ArknightsCharVis/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/zzkluck/ArknightsCharVis/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/zzkluck/ArknightsCharVis/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/zzkluck/ArknightsCharVis/blob/master/LICENSE.txt
[product-demo]: images/demo.png
