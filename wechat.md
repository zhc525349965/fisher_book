---
title: 朋友圈 Wechat
---

# <H2Icon/> 朋友圈 Wechat

> 用来展示图片，规则同微信朋友圈。

## 图片展示

### 1 单图

组件将所传图片等比压缩，长边压缩/拉伸至`360rpx`。
> 朋友圈组件只包含图片部分，其他部分展示代码为展示用。

示例代码

![单图](http://imglf3.nosdn0.126.net/img/YXcvYzgxMzh2bmQyVVBmd3dSVFFBUVVCeEY1ekR1WFZJQW1lMTdwZ1J5NlAzdEpaVlpmcnhBPT0.jpeg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg)

```wxml
<view>
    <view class="wechat">
        <l-avatar class="avatar" size='80' shape="square" src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574067618442&di=b8474bcfaea4c13487e6aac9c3f66c84&imgtype=0&src=http%3A%2F%2Fimg14.360buyimg.com%2Fn1%2Fjfs%2Ft21772%2F172%2F702988837%2F107053%2F5e0f9964%2F5b1619e2N9a2189a8.jpg" />
        <view class="right">
            <view class="name">Lin-UI-27315</view>
            <view class='content'>一张横屏图片的展示，宽为360rpx。</view>
            <l-wechat urls='{{urls1_1}}'></l-wechat>
        </view>
    </view>
    <view class="line"></view>
</view>
<view>
    <view class="wechat">
        <l-avatar class="avatar" size='80' shape="square" src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574067618442&di=b8474bcfaea4c13487e6aac9c3f66c84&imgtype=0&src=http%3A%2F%2Fimg14.360buyimg.com%2Fn1%2Fjfs%2Ft21772%2F172%2F702988837%2F107053%2F5e0f9964%2F5b1619e2N9a2189a8.jpg" />
        <view class="right">
            <view class="name">Lin-UI-27315</view>
            <view class='content'>一张竖屏图片的展示，高为360rpx。</view>
            <l-wechat urls='{{urls1_2}}'></l-wechat>
        </view>
    </view>
    <view class="line"></view>
</view>
```

```js
  data: {
    urls1_1: ['http://img2.imgtn.bdimg.com/it/u=1944156091,814818697&fm=26&gp=0.jpg'],
    urls1_2: ['https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1575390421137&di=3ba6f1c3b893af11a8cf7a32455d011c&imgtype=0&src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2Fee327b05d345a246d773b4b73df51c408f11112615d8e-5luZ3f_fw658'],
  },
```

```wxss
.wechat {
    display: flex;
    flex-direction: row;
}

.avatar {
    margin-left: 20rpx;
}

.right {
    margin-left: 20rpx;
}

.name {
    color: rgb(91, 108, 160);
    font-weight: 450;
}

.content {
    margin-top: 7rpx;
    margin-right: 10rpx;
    color: black;
    font-weight: 445;
    margin-bottom: 15rpx;
}

.line {
    height: 1px;
    border-top: solid Silver 1px;
    margin-bottom: 40rpx;
    margin-top: 30rpx;
}
```

### 2 多图

多图展示时，组件自动按照朋友圈样式进行布局。

图片展示为边长`158rpx`的正方形图片。

示例代码

![多图模式](http://imglf5.nosdn0.126.net/img/YXcvYzgxMzh2bmQyVVBmd3dSVFFBVHpTOXNLdHl1Uy9MdGJVZVBXTjBDZ3g3a295UFUwcTFBPT0.jpeg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg)

```wxml
<view>
    <view class="wechat">
        <l-avatar class="avatar" size='80' shape="square" src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574067618442&di=b8474bcfaea4c13487e6aac9c3f66c84&imgtype=0&src=http%3A%2F%2Fimg14.360buyimg.com%2Fn1%2Fjfs%2Ft21772%2F172%2F702988837%2F107053%2F5e0f9964%2F5b1619e2N9a2189a8.jpg" />
        <view class="right">
            <view class="name">Lin-UI-27315</view>
            <view class='content'>多张图片展示，显示为边长158rpx的正方形。</view>
            <l-wechat urls='{{urls2}}'></l-wechat>
        </view>
    </view>
    <view class="line"></view>
</view>
<view>
    <view class="wechat">
        <l-avatar class="avatar" size='80' shape="square" src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574067618442&di=b8474bcfaea4c13487e6aac9c3f66c84&imgtype=0&src=http%3A%2F%2Fimg14.360buyimg.com%2Fn1%2Fjfs%2Ft21772%2F172%2F702988837%2F107053%2F5e0f9964%2F5b1619e2N9a2189a8.jpg" />
        <view class="right">
            <view class="name">Lin-UI-27315</view>
            <view class='content'>多张图片展示，自动按照朋友圈显示规则排序。</view>
            <l-wechat urls='{{urls5}}'></l-wechat>
        </view>
    </view>
    <view class="line"></view>
</view>
```

```js
  data: {
    urls2:['http://img2.imgtn.bdimg.com/it/u=1944156091,814818697&fm=26&gp=0.jpg','http://pic1.win4000.com/wallpaper/2/596470aa0a9d3.jpg'],
    urls5:['http://img2.imgtn.bdimg.com/it/u=1944156091,814818697&fm=26&gp=0.jpg','http://pic1.win4000.com/wallpaper/2/596470aa0a9d3.jpg','http://pic1.win4000.com/wallpaper/2018-02-02/5a741b536cf04.jpg','http://image.naic.org.cn/uploadfile/2017/1011/1507715213116632.jpg','http://e0.ifengimg.com/10/2019/0421/9FB69F78D3D83925878EF2CFFEFA435E3F0F5DED_size144_w1080_h608.jpeg']
  },
```

```wxss
    wxss文件同上
```

## 图片列表 urls  

urls接收一个数组，数组内元素可以有两种格式。

- 数组元素为字符串

```js
['图片1.jpg','图片2.jpg','图片3.jpg']
```

- 数组元素为对象，对象包含url。

```js
[{url:'1.jpg',
  key: 'key1'},
  {url:'2.jpg',
  key:'key2',
  value:2}]
```
  
两种格式根据实际情况自行选择。在组件事件中返回的detail内容会根据所传的urls形式返回。

## 预览 preview

组件图片支持预览，默认状态为打开，可以通过设置`preview`属性为`false`关闭预览。


## 图片尺寸

### 单图 single-size

单张图片时，组件将所传图片等比压缩，长边压缩/拉伸至`360rpx`。通过设置`single-size`可以更改长边大小，单位`rpx`。

### 多图 multiple-size

多张图片时，图片展示为边长`158rpx`的正方形图片。通过设置`multiple-size`可以更改图片边长，单位`rpx`

## 图像间隔 gap-row gap-column

> 此设置仅在多图展示时生效

通过设置`gap-row`和`gap-column`属性来更改多图时，图片的水平间隔和竖直间隔，默认值为`10rpx`;

## 裁剪模式

### 单图 single-mode
属性`single-mode`可以更改单图展示时图片的裁剪模式，默认值`aspectFit`。

### 多图 multiple-mode 
属性`multiple-mode`可以更改多图展示时图片的裁剪模式，默认值`aspectFill`。

### 示例代码

![裁剪模式](http://imglf6.nosdn0.126.net/img/YXcvYzgxMzh2bmQyVVBmd3dSVFFBZlJqcmpTR2lFemo2YUlQWTMwTnNZWS9WWE5vNFQ5cFdRPT0.jpeg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg)

```wxml
<view>
    <view class="wechat">
        <l-avatar class="avatar" size='80' shape="square" src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574067618442&di=b8474bcfaea4c13487e6aac9c3f66c84&imgtype=0&src=http%3A%2F%2Fimg14.360buyimg.com%2Fn1%2Fjfs%2Ft21772%2F172%2F702988837%2F107053%2F5e0f9964%2F5b1619e2N9a2189a8.jpg" />
        <view class="right">
            <view class="name">Lin-UI-27315</view>
            <view class='content'>通过single-mode可以更改单图时图片裁剪、缩放的模式。示例为center模式。</view>
            <l-wechat urls='{{urls1_1}}' single-mode='center'></l-wechat>
        </view>
    </view>
    <view class="line"></view>
</view>
<view>
    <view class="wechat">
        <l-avatar class="avatar" size='80' shape="square" src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574067618442&di=b8474bcfaea4c13487e6aac9c3f66c84&imgtype=0&src=http%3A%2F%2Fimg14.360buyimg.com%2Fn1%2Fjfs%2Ft21772%2F172%2F702988837%2F107053%2F5e0f9964%2F5b1619e2N9a2189a8.jpg" />
        <view class="right">
            <view class="name">Lin-UI-27315</view>
            <view class='content'>通过multiple-mode可以更改多图时图片裁剪、缩放的模式。示例为scaleToFill模式。</view>
            <l-wechat urls='{{urls4}}' multiple-mode='scaleToFill'></l-wechat>
        </view>
    </view>
    <view class="line"></view>
</view>
```

```js
  data: {
    urls1_1: ['http://img2.imgtn.bdimg.com/it/u=1944156091,814818697&fm=26&gp=0.jpg'],
    urls4: ['http://img2.imgtn.bdimg.com/it/u=1944156091,814818697&fm=26&gp=0.jpg', 'http://pic1.win4000.com/wallpaper/2/596470aa0a9d3.jpg', 'http://pic1.win4000.com/wallpaper/2018-02-02/5a741b536cf04.jpg', 'http://image.naic.org.cn/uploadfile/2017/1011/1507715213116632.jpg', ],
  },
```

```wxss
    wxss文件同上
```

## 属性（Wechat Attributes）

| 参数   | 说明 | 类型 | 可选值 | 默认值 |  
|:----|:----|:----|:----|:----|
| urls	| 图片地址，详细说明见属性urls说明	| Array | - | [] |
| preview	| 图片可预览  | Boolean| `true`,`false` | `true` |
| single-size | 单图时，图片长边的长度，单位rpx | Number | - | 360 |
| multiple-size	| 多图时，图片边长，单位rpx |	Number | - | 158 |
| gap-row	| 多图时，图片水平间隔 | Number |	- | 10 |
| gap-column	| 多图时，图片垂直间隔 | Number |	- | 10 |
| single-mode	| 单图时，图片缩放裁剪的模式 |	String	| 见[小程序image组件](https://developers.weixin.qq.com/miniprogram/dev/component/image.html) |`aspectFit`|
| multiple-mode	| 多图时，图片缩放裁剪的模式 |	String	| 见[小程序image组件](https://developers.weixin.qq.com/miniprogram/dev/component/image.html) |`aspectFill`|


## 外部样式类（Wechat ExternalClasses）
| 外部样式类名 | 说明 | 备注 |
| :--------- | :----------------- | :----- |
| l-class | 覆盖组件整体样式的外部样式类 | - |
| l-single-image-class | 覆盖组件单图时图片样式的外部样式类 |- |
| l-multi-image-class  |覆盖组件多图时图片样式的外部样式类 |- |


## 组件事件（Wechat Events）

| 事件名称   | 说明   | 返回值   | 备注   | 
|:----|:----|:----|:----|
| bind:lintap  | 点击图片时触发   | event.detail = {current:[ 当前点击项的信息 ], all: [ 当前所有项信息 ], index: 点击项的下标}  |urls格式与传入的urls格式保持一致  | 

<RightMenu />