<template>
  <div id="app">
        <Modal></Modal>
        <nav class="navbar navbar-default navbar-fixed-top">
            <div class="container-fluid" id="top-header">
                <div class="navbar-header">
                    <!-- <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-navbar-collapse" aria-expanded="false">
                        <span class="sr-only">{{ $t("action.toggleNavbar") }}</span>
                    </button> -->
                    <a class="navbar-brand" href="/"><div>{{ $t("info.title") }}</div></a>
                </div>
                <div class="brand1">
                    <a href="https://space.bilibili.com/434334701/" target="_blank"><img src="resources/bilibili.svg" title="七海Nana7mi" alt="七海Nana7mi" height="18"/></a>
                </div>
                <div class="brand1">
                    鲨歌：
                    <a href="https://www.bilibili.com/video/BV1DK4y1g7zE/" target="_blank">无垠梦海</a>
                </div>
                <div class="brand1">
                    <a href="https://www.bilibili.com/video/BV1vJ411B7ng/" target="_blank">偶像宣言</a>
                </div>
                <!-- <div class="collapse navbar-collapse" id="bs-navbar-collapse">
                    <ul class="nav navbar-nav">
                        <li><a href="https://space.bilibili.com/434334701/" target="_blank"><img src="resources/bilibili.svg" height="18"/></a></li>
                    </ul>
                    <ul class="nav navbar-nav navbar-right">
                        <li class="dropdown">
                            <a href="javascript:;" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{$t("lang." + currentLang)}} <span class="caret"></span></a>
                            <ul class="dropdown-menu">
                                <li><a href="javascript:;" @click="chlang('zh-CN')">{{$t("lang.zh-CN")}}</a></li>
                                <li><a href="javascript:;" @click="chlang('en-US')">{{$t("lang.en-US")}}</a></li>
                                <li><a href="javascript:;" @click="chlang('ja-JP')">{{$t("lang.ja-JP")}}</a></li>
                            </ul>
                        </li>
                    </ul>
                </div> -->
            </div>
        </nav>
        <div class="container-fluid main-content">
            <HomePage></HomePage>
            <div class="fixed-left" >
                <img src="resources/mi.png">
            </div>  
            <div class="fixed-right" >
                <img src="resources/小人.gif">
            </div>
        </div>
        <footer class="footer">
                <div>
                    <div>{{$t("info.audioStaff")}}</div>
                    <div>友情链接:
                    <a href="https://www.supermikimiki.com/" target="_blank">弥按钮</a> &nbsp;
                    <a href="https://tieba.baidu.com/f?kw=%E4%B8%83%E6%B5%B7nana7mi" target="_blank">海吧</a> &nbsp;
                    </div>
                    <div>音频投稿: b站 <a href="https://space.bilibili.com/188888131" target="_blank">@脆鲨12138</a> 只有时间点也行</div>
                </div>
                <div>
                    <div class="text-right"><a href="https://github.com/xuziang111/miki-button-src" target="_blank">原项目</a></div>
                    <div class="text-right">本项目<a href="https://github.com/Drelf2018/nanami-button" target="_blank">{{$t("info.toGithub")}}</a></div>
                    <div class="text-right">{{$t("info.notOfficial")}}</div>
                </div>
                <!-- <div>Zyzsdy 2019-2020 <span style="color: rgba(0, 0, 0, 0.1)">Powered By Meowsound Idols</span></div> -->
        </footer>
  </div>
</template>

<style lang="scss">
@import "../node_modules/bootstrap/dist/css/bootstrap.css";
body{
    //background: linear-gradient(45deg, #bee4e4, #a6d8da);    //让背景的渐变带有倾斜
    //background-size:30px 30px;   //每一块小组成部分固定宽度和高度
    background: repeating-linear-gradient(-45deg, #bee4e4, #a6d8da 60px); 
    // background-color:#bee4e4;
}
.cate-header{
    color:#fff;
}
#top-header{
    display:flex;
}
.fixed-left{
    position: fixed;
    z-index: -1;
    top:10px;
    right:0;
}
.fixed-right{
    position: fixed;
    z-index: -1;
    top:60vh;
    //bottom:20;
    left:0;
}
.fixed-right img{
    height:30vh;
}
.fixed-left img{
    // position: absolute;
    // z-index: -1;
    // top:0;
    // right:0px;
    // width:50%;
    height:100vh;
}
.img-left{
    position: fixed;
    z-index: -1;
    top:0;
    right:-100px;
}
.img-center2{
    position: fixed;
    z-index: -1;
    
    top:0;
    right:-300px;
}
.img-center2 img{
    width:100%;
}
.img-center{
    display:flex;
    justify-content: center;
    padding:10px 0 10px 0;
}
.brand1{
    padding:0 5px 0 5px;
    display:flex;
    justify-content: center;
    align-items: center;
}
html{
    height:100%;
}
body{
    padding-top: 70px;
    height:100%;
}
#app{
    min-height:100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.main-content{
    // min-height: 100vh;
}
.footer {
    width: 100%;
    background-color: #ebebeb;
        display:flex;
    padding: 10px;
    color: #666;
    justify-content:space-between;
    align-items: center;
}
// .footer-content {
//     display:flex;
//     padding-top: 10px;
//     color: #666;
//     justify-content:space-between;
//     align-items: center;
// }
.text-right{
    text-align: right;
}
</style>
<script type="text/javascript" src="'./util/snowfall.js'"></script>
<script>
import Vue from 'vue'
import Component from 'vue-class-component'
import Modal from './components/modal.vue'
import HomePage from './components/home.vue'
import $ from 'jquery'
//import fetchpost from './util/fetchpost'

@Component({
    components:{
        Modal,
        HomePage
    }
})
class App extends Vue {
    get currentLang(){
        return this.$i18n.locale;
    }
    data(){
        return {
            xxx:'container-fluid img-left'
        }
    }
    created(){
        // eslint-disable-next-line 
        console.log("                             ;&@@@@@@|`\n                           !&&&&&&&&&&&%'\n                         `|$$%$%%%$$$$$$$:\n                         !$$$$$%%$$$$&&&&%`\n                        '%$$$%%$$$;;%$$$&$'\n                        :$$$!`'|$!` .!%$&$'\n                        ;&$%!%%!!'.:|||$$%'\n                        ;&$%'        .!$&|.\n                        `|$&%'      .!&&$;\n                         `!&&&$;. .;$&&$!\n                          .:|&$|:'';$@@$'\n                          .!&@|'````!@&&|`\n                       ;&$$$&$:`|&!.;&@@&$&|.\n                      ;&$%$&$$!'!|':%&&&&$&&|`\n                     !&$$$&$$%!!$$!;|$&&&&&$&!.  \n                    !&$%&@&$&%!!!!;!%&&&&@@&$&|`  \n                 `|$$%&@@&&&%!!!!!!%&&@@&&&&&&%`  \n                '%$$%$|:%@&&$|!||!!%&&%%|`;&&&&&:    \n               ;&&$%%' `%&@@$||!|!!$@&&@|. '$@&&&!    \n              !&&$$!   `%&@&%||||!!$@&&&|.   !@@&&%` \n              ;$$$&@|. '$&&&$%$$%%%$@&&&&: :$&&&&&!   \n               `%&$$$&&&&&&$|!!||||$&&&@&$&$$$&&!   \n           .. :!..!$&||@&&&$%%%|%%$$&&&@%|&&$$!   \n       .`     :|'   '|&&$$&%|%|!|%%$&&&&&!!$:   \n     .`       '%$&&;`|&$$&$|!||!|||%$$&&@|.`'   \n    ``        '||%|;|&&$$&%|||!!!||%&&&&&$:.;|'   \n   ``         ;||%$&&&$$$$%!|!!!!||%&&&$&&@@@&%:``..  \n   `.        '|%%%$&&&$$&$|!|!!!|||%$&&&&&&%%%||;:!'`.  \n  .'...   . '!%%%:!&$$$&&$|!||!!||||$&&&&&&&$$%%!:||;'  \n  `'``.....'|$$%;'|$%||||!!!||!!|||||||%%%$$$%%%%|%$%'  \n  .'``````;$&&$$$$&%%|!||!!!|!!!||||||||%%$$&$%%$%:  \n   .::';|$&@@@@&&&$|||!||!!||!!!!|||||||%%%$$&$%|!`  \n       ;$&@@@@@@&$|||!!!!!!||!!!!|||||||%%%%$$$&$||;.  \n          .!%%|!|||||!!!!!!||!!!!||||||||%%%%$$%%%;  \n                :|||!!!!!!!||!!!!||!|||||%%%%%!`    \n                :|||!!|!!!!|!!!!!||!|||||%%|%%!.  \n               '|||!!||!!!!|!!!!!||!!|||||%|%%%:    \n              .;|||!!||!!!!!!!!!!||!!|||||%%|%%|'  \n              '|%||!|||!!!!|!!!!!||!!|||||%%|%%$!. \n             .!%%||||%|!!!||!!!!!||!|||||||%|%%$$:  \n             `|%%||||%|||||||||||||||||%|||%%%%$!. \n                :|||%%|||||%|||||%%|||||%||%%;`    \n                     ';!!!!|%|!!;;||!!!;;:'`     \n                    .'''':'           `::'''.    \n                    `:''''`           .:''''`    \n                    .`''''`           .'''`..    \n                    .    .             .     .  \n                    .    .             .     .  \n                    .    .             .     .    \n                    .    .             .     .  \n                     .   .              .    .     \n                    :'  .'.             ::  .;'  \n                    ;$$$&%`             :$$$&%'  \n                    :$$$&|.             '$&&&%`  \n                     !&&&;               ;&&&!   \n                     :$&&;               :$&&;   \n                     .|&&;               '$&&:   \n                     .|@@|.              '$@@;   \n                     '$@@@;              !@@@|.  \n                     `|&&&;             '%&&&%`  \n                     :$$$$%'           :$$$$&!   \n                     :;.  ``          .`  `|$'   \n                      .....            `...`.     \n /早知道女孩子也会被 /女人配不上我 /弥希miki是没有未来的 /咳嗽X /伸懒腰X /mahiru主人 /人不能X狗 至少不该/黄色废料/你只希望我们有肉体关系是吗/喝水/miki是这个世界的中心/民风淳朴/八木直言要/打嗝N/咳嗽XX/咳嗽XXX")
        // console.log("10/12饿啊 结果miki真的就从头到尾没变过 920后也没变过 真的是太扭曲了")
        // console.log("观众不要试图去改变演员想法，特别还是虚拟的（")
        //早知道女孩子也会被 女人配不上我 弥希miki是没有未来的 咳嗽X 伸懒腰X mahiru主人
        this.$i18n.locale = localStorage.getItem("lang") || this.$i18n.locale;
    }
    mounted(){
        if(document.body.clientWidth<768){
            this.xxx = 'container-fluid img-center2'
        }
        // snowFall.snow(document.body, {minSize: 10, maxSize:32});
        // $(document).snowfall();
        Date.now||(Date.now=function(){return(new Date).getTime()}),function(){"use strict";for(var t=["webkit","moz"],e=0;e<t.length&&!window.requestAnimationFrame;++e){var i=t[e];window.requestAnimationFrame=window[i+"RequestAnimationFrame"],window.cancelAnimationFrame=window[i+"CancelAnimationFrame"]||window[i+"CancelRequestAnimationFrame"]}if(/iP(ad|hone|od).*OS 6/.test(window.navigator.userAgent)||!window.requestAnimationFrame||!window.cancelAnimationFrame){var s=0;window.requestAnimationFrame=function(t){var e=Date.now(),i=Math.max(s+16,e);return setTimeout(function(){t(s=i)},i-e)},window.cancelAnimationFrame=clearTimeout}}(),function(t){t.snowfall=function(e,i){function s(s,n,a,o){this.x=s,this.y=n,this.size=a,this.speed=o,this.step=0,this.stepSize=h(1,10)/100,i.collection&&(this.target=m[h(0,m.length-1)]);var r=null;i.image?(r=document.createElement("img"),r.src=i.image):(r=document.createElement("div"),t(r).css({background:i.flakeColor})),t(r).attr({"class":"snowfall-flakes"}).css({width:this.size,height:this.size,position:i.flakePosition,top:this.y,left:this.x,fontSize:0,zIndex:i.flakeIndex}),t(e).get(0).tagName===t(document).get(0).tagName?(t("body").append(t(r)),e=t("body")):t(e).append(t(r)),this.element=r,this.update=function(){if(this.y+=this.speed,this.y>l-(this.size+6)&&this.reset(),this.element.style.top=this.y+"px",this.element.style.left=this.x+"px",this.step+=this.stepSize,this.x+=y===!1?Math.cos(this.step):y+Math.cos(this.step),i.collection&&this.x>this.target.x&&this.x<this.target.width+this.target.x&&this.y>this.target.y&&this.y<this.target.height+this.target.y){var t=this.target.element.getContext("2d"),e=this.x-this.target.x,s=this.y-this.target.y,n=this.target.colData;if(void 0!==n[parseInt(e)][parseInt(s+this.speed+this.size)]||s+this.speed+this.size>this.target.height)if(s+this.speed+this.size>this.target.height){for(;s+this.speed+this.size>this.target.height&&this.speed>0;)this.speed*=.5;t.fillStyle="#fff",void 0==n[parseInt(e)][parseInt(s+this.speed+this.size)]?(n[parseInt(e)][parseInt(s+this.speed+this.size)]=1,t.fillRect(e,s+this.speed+this.size,this.size,this.size)):(n[parseInt(e)][parseInt(s+this.speed)]=1,t.fillRect(e,s+this.speed,this.size,this.size)),this.reset()}else this.speed=1,this.stepSize=0,parseInt(e)+1<this.target.width&&void 0==n[parseInt(e)+1][parseInt(s)+1]?this.x++:parseInt(e)-1>0&&void 0==n[parseInt(e)-1][parseInt(s)+1]?this.x--:(t.fillStyle="#fff",t.fillRect(e,s,this.size,this.size),n[parseInt(e)][parseInt(s)]=1,this.reset())}(this.x+this.size>d-c||this.x<c)&&this.reset()},this.reset=function(){this.y=0,this.x=h(c,d-c),this.stepSize=h(1,10)/100,this.size=h(100*i.minSize,100*i.maxSize)/100,this.element.style.width=this.size+"px",this.element.style.height=this.size+"px",this.speed=h(i.minSpeed,i.maxSpeed)}}function n(){for(r=0;r<a.length;r+=1)a[r].update();f=requestAnimationFrame(function(){n()})}var a=[],o={flakeCount:35,flakeColor:"#ffffff",flakePosition:"absolute",flakeIndex:999999,minSize:1,maxSize:2,minSpeed:1,maxSpeed:5,round:!1,shadow:!1,collection:!1,collectionHeight:40,deviceorientation:!1},i=t.extend(o,i),h=function(t,e){return Math.round(t+Math.random()*(e-t))};t(e).data("snowfall",this);var r=0,l=t(e).height(),d=t(e).width(),c=0,f=0;if(i.collection!==!1){var p=document.createElement("canvas");if(p.getContext&&p.getContext("2d"))for(var m=[],w=t(i.collection),g=i.collectionHeight,r=0;r<w.length;r++){var u=w[r].getBoundingClientRect(),x=t("<canvas/>",{"class":"snowfall-canvas"}),z=[];if(u.top-g>0){t("body").append(x),x.css({position:i.flakePosition,left:u.left+"px",top:u.top-g+"px"}).prop({width:u.width,height:g});for(var v=0;v<u.width;v++)z[v]=[];m.push({element:x.get(0),x:u.left,y:u.top-g,width:u.width,height:g,colData:z})}}else i.collection=!1}for(t(e).get(0).tagName===t(document).get(0).tagName&&(c=25),t(window).bind("resize",function(){l=t(e)[0].clientHeight,d=t(e)[0].offsetWidth}),r=0;r<i.flakeCount;r+=1)a.push(new s(h(c,d-c),h(0,l),h(100*i.minSize,100*i.maxSize)/100,h(i.minSpeed,i.maxSpeed)));i.round&&t(".snowfall-flakes").css({"-moz-border-radius":i.maxSize,"-webkit-border-radius":i.maxSize,"border-radius":i.maxSize}),i.shadow&&t(".snowfall-flakes").css({"-moz-box-shadow":"1px 1px 1px #555","-webkit-box-shadow":"1px 1px 1px #555","box-shadow":"1px 1px 1px #555"});var y=!1;i.deviceorientation&&t(window).bind("deviceorientation",function(t){y=.1*t.originalEvent.gamma}),n(),this.clear=function(){t(".snowfall-canvas").remove(),t(e).children(".snowfall-flakes").remove(),cancelAnimationFrame(f)}},t.fn.snowfall=function(e){return"object"==typeof e||void 0==e?this.each(function(){new t.snowfall(this,e)}):"string"==typeof e?this.each(function(){var e=t(this).data("snowfall");e&&e.clear()}):void 0}}(jQuery);
    // 下雪
// $("#app").snowfall({flakeCount : 200, maxSpeed : 10, maxSize : 5})
        
    }
    chlang(v){
        this.$i18n.locale = v;
        localStorage.setItem("lang", v);
    }
}

export default App;
</script>

