---
title: 朋友圈 Wechat
---

# <H2Icon/> 朋友圈 Wechat

> 用来展示图片，规则同微信朋友圈。

## 图片展示

Wechat组件有单图展示和多图展示两种情景。两种情景下图片的设置互不影响。

### 1 单图展示

当url数组长度为1时，为单图展示。组件将所传图片等比压缩，长边压缩/拉伸至360rpx(默认值)，缩放模式为`aspectFit`(默认值)。
`single-image-long-side`属性可以更改长边长度,通过`mode-single`属性更改单图展示时，图片的缩放模式。
可以通过设置外部样式类`l-single-image-class`覆盖单图展示下图片的样式。
> 朋友圈组件只包含图片部分，其他部分展示代码为展示用。

示例代码

![单图模式](http://imglf3.nosdn0.126.net/img/YXcvYzgxMzh2bmNvZTljZFIxN2xRMEhTREVPZEU0OE1DdXZNbFg0TVUxYjNBVlhwWXY2YjJRPT0.jpeg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg)

```wxml
<view class='circle'>
    <view class="wechat">
        <l-avatar class="avatar" size='80' shape="square" src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574067618442&di=b8474bcfaea4c13487e6aac9c3f66c84&imgtype=0&src=http%3A%2F%2Fimg14.360buyimg.com%2Fn1%2Fjfs%2Ft21772%2F172%2F702988837%2F107053%2F5e0f9964%2F5b1619e2N9a2189a8.jpg" />
        <view class="right">
            <view class="name">Lin-UI-27315</view>
            <view class='content'>这是一条高仿的朋友圈，只有1张图片</view>
            <l-wechat l-class="image" urls='{{urls1_1}}' l-one-image-class='image-class'></l-wechat>
        </view>
    </view>
    <view class="line"></view>
</view>
<view class='circle'>
    <view class="wechat">
        <l-avatar class="avatar" size='80' shape="square" src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574067618442&di=b8474bcfaea4c13487e6aac9c3f66c84&imgtype=0&src=http%3A%2F%2Fimg14.360buyimg.com%2Fn1%2Fjfs%2Ft21772%2F172%2F702988837%2F107053%2F5e0f9964%2F5b1619e2N9a2189a8.jpg" />
        <view class="right">
            <view class="name">Lin-UI-27315</view>
            <view class='content'>这是一条高仿的朋友圈，只有1张图片</view>
            <l-wechat l-class="image" urls='{{urls1_2}}' l-one-image-class='image-class'></l-wechat>
        </view>
    </view>
    <view class="line"></view>
</view>
```

```js
data: {
	urls1_1: ['http://i0.hdslb.com/bfs/article/b501b14e56fb373b34afcea2e5c398de39116bd2.jpg'],
	urls1_2: ['https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574071192918&di=82fae997a4b5434f2fd2b4ffadbf6a90&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fmobile%2F2017-11-21%2F5a13dcd54ac3b.png'],
}
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
}

.image {
    margin-top: 15rpx;
    margin-bottom: 30rpx;
}

.line {
    height: 1px;
    border-top: solid Silver 1px;
    margin-bottom: 40rpx;
}

```

### 2 多图展示

当url数组长度为大于1时，为多图展示。多图展示时，组件自动按照朋友圈样式进行布局。图片展示为边长`158rpx`的正方形缩略图,图片裁剪模式为`aspectFill`,图片之间间隔为`10rpx`。
属性`size`可以更改多图展示下每张图片的边长。属性`mode-multiple`可以更改多图展示下的图片裁剪模式。`gap-row`和`gap-column`分别设置多图展示时图片水平间距和竖直间距。
可以通过外部样式类`l-multi-image-class`覆盖多图展示时，图片的样式。

示例代码

![多图模式](http://imglf3.nosdn0.126.net/img/YXcvYzgxMzh2bmNvZTljZFIxN2xRMFcxMFl2L0thL0dkeUljdzNZVFFQckRHNElJaVVFRVFBPT0.jpeg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg)

```wxml
<l-wechat l-class="image" urls='{{urls2}}'></l-wechat>
<view class="line"></view>
<l-wechat l-class="image" urls='{{urls3}}'></l-wechat>
<view class="line"></view>
<l-wechat l-class="image" urls='{{urls9}}'></l-wechat>
```

```js
data: {
	urls2: ['http://i0.hdslb.com/bfs/article/b501b14e56fb373b34afcea2e5c398de39116bd2.jpg','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574071192918&di=82fae997a4b5434f2fd2b4ffadbf6a90&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fmobile%2F2017-11-21%2F5a13dcd54ac3b.png'],
	urls3: ['http://i0.hdslb.com/bfs/article/b501b14e56fb373b34afcea2e5c398de39116bd2.jpg', 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1573645417694&di=823f17fce7f9734316e850196d079e88&imgtype=0&src=http%3A%2F%2Fcdn.duitang.com%2Fuploads%2Fblog%2F201404%2F22%2F20140422142715_8GtUk.thumb.600_0.jpeg', 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1573645417694&di=f455bc4cf2b1ea0f42d25dd91ffe3625&imgtype=0&src=http%3A%2F%2Fpic4.zhimg.com%2Fv2-06273e88b28b75cc0cbe4cee51312cf7_b.jpg'],
	urls9: ['http://i0.hdslb.com/bfs/article/b501b14e56fb373b34afcea2e5c398de39116bd2.jpg', 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1573645417694&di=823f17fce7f9734316e850196d079e88&imgtype=0&src=http%3A%2F%2Fcdn.duitang.com%2Fuploads%2Fblog%2F201404%2F22%2F20140422142715_8GtUk.thumb.600_0.jpeg', 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1573645417694&di=f455bc4cf2b1ea0f42d25dd91ffe3625&imgtype=0&src=http%3A%2F%2Fpic4.zhimg.com%2Fv2-06273e88b28b75cc0cbe4cee51312cf7_b.jpg','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574095423863&di=665e0defb97634c13e971e8927d286f0&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fmobile%2F2019-04-28%2F5cc56e6811585.jpg','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574095423863&di=5a66908ed0515c1653c384e986604976&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fmobile%2F2019-06-05%2F5cf781125242e.jpg','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574095423863&di=9ae6074b6f502a61fb8bf98d0aec192e&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fmobile%2F2018-08-16%2F5b75314b062e6.jpg','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574095423863&di=f54813a8680af71f2f35f4688bd475ff&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fmobile%2F2018-09-13%2F5b99ccb60b6c8.jpg','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574095423862&di=2d0ddcec3f7c2e36d4ffb35a8d720e41&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fmobile%2F2018-07-13%2F5b48396e092fa.jpg','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574095423862&di=03038c8dd907520d075927e15124eb20&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fmobile%2F2018-01-18%2F5a60495640573.jpg']
}
```

```wxss
.line {
    height: 1px;
    border-top: solid Silver 1px;
    margin-bottom: 40rpx;
}

.image {
    margin-top: 15rpx;
    margin-bottom: 30rpx;
}
```

##  urls

urls属性接收两种形式的传值方式。

- url数组，格式为

```js
['图片1.jpg','图片2.jpg','图片3.jpg']
```

数组内元素为图片地址。

- url对象数组，对象中包含url即可，可以包含其他内容。格式为：

```js
[{url:'1.jpg',
  key: 'key1'},
  {url:'2.jpg',
  key:'key2',
  value:2}]
```
  
两种模式根据实际情况自行选择。在组件事件中返回的detail内容会根据所传的urls形式返回。


## 图片尺寸 size

### 单图展示
通过设置 `single-image-long-side`属性更改单图展示时，图片长边显示的长度。默认值为`360`，单位`rpx`。同时，支持通过外部样式类`l-single-image-class`修改单图展示时图片的样式。

### 多图展示

通过设置`size`属性来更改多图展示时，图片的边长。默认值为`158`，单位`rpx`。同时，支持通过外部样式类`l-multi-image-class`修改多图展示时的图片样式。

### 示例代码

![图片大小](http://imglf3.nosdn0.126.net/img/YXcvYzgxMzh2bmNvZTljZFIxN2xROXJ5RXdzOTMySkordDlFUDRkNXMyVVVnSHJYaTJwTzFRPT0.jpg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg)

```wxml
<l-wechat l-class="image" urls='{{urls2}}'></l-wechat>
<view class="line"></view>
<l-wechat l-class="image" urls='{{urls2}}' size='250'></l-wechat>
<view class="line"></view>
<l-wechat l-class="image" urls='{{urls2}}' l-multi-image-class='multi-image'></l-wechat>
```

```js
data: {
	urls2: [{
      key: 'key1',
      url: 'http://i0.hdslb.com/bfs/article/b501b14e56fb373b34afcea2e5c398de39116bd2.jpg',
      status: 1
    }, {
      key: 'key2',
      url: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574071192918&di=82fae997a4b5434f2fd2b4ffadbf6a90&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fmobile%2F2017-11-21%2F5a13dcd54ac3b.png',
      status: 2
    }],
}    
```

```wxss
.image {
    margin-top: 15rpx;
    margin-bottom: 30rpx;
}

.multi-image {
    border-radius: 50rpx;
}
```

## 图像间隔 gap-row gap-column

> 仅在多图展示时生效

通过设置`gap-row`和`gap-column`属性来更改多图模式下，图片的水平间隔和竖直间隔，默认值为`10`，单位为`rpx`;

### 示例代码

![图像间隔](http://imglf4.nosdn0.126.net/img/YXcvYzgxMzh2bmNvZTljZFIxN2xRK3VSTlFoK01oNUVsWTZETytvODRKUmxqd2pQZkpkZVd3PT0.jpg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg)

```wxml
<l-wechat l-class="image" urls='{{urls4}}'></l-wechat>
<view class="line"></view>
<l-wechat l-class="image" urls='{{urls4}}' gap-row='20' gap-column='20'></l-wechat>
```

```js
data:{
urls4: ['https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574095423863&di=9ae6074b6f502a61fb8bf98d0aec192e&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fmobile%2F2018-08-16%2F5b75314b062e6.jpg','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574095423863&di=f54813a8680af71f2f35f4688bd475ff&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fmobile%2F2018-09-13%2F5b99ccb60b6c8.jpg','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574095423862&di=2d0ddcec3f7c2e36d4ffb35a8d720e41&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fmobile%2F2018-07-13%2F5b48396e092fa.jpg','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574095423862&di=03038c8dd907520d075927e15124eb20&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fmobile%2F2018-01-18%2F5a60495640573.jpg'],
}
```

```wxss
.image {
    margin-top: 15rpx;
    margin-bottom: 30rpx;
}

.line {
    height: 1px;
    border-top: solid Silver 1px;
    margin-bottom: 40rpx;
}
```

## 裁剪模式

通过设置`mode-single`和`mode-multiple`属性来设置单图展示和多图展示时图片的裁剪模式。
`mode-single`默认值为`aspectFit`，`mode-multiple`默认值为`aspectFill`。

### 示例代码

![裁剪模式](http://imglf3.nosdn0.126.net/img/YXcvYzgxMzh2bmNvZTljZFIxN2xReXNWV21RamUzaU0vNnZpNURETUFsWldaWXF5RDBHWHZRPT0.jpg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg)

```wxml
<l-wechat l-class="image" urls='{{urls4}}'></l-wechat>
<view class="line"></view>
<l-wechat l-class="image" urls='{{urls4}}' mode-multiple='aspectFit'></l-wechat>
```

```js
data:{
urls4: ['https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574095423863&di=9ae6074b6f502a61fb8bf98d0aec192e&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fmobile%2F2018-08-16%2F5b75314b062e6.jpg','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574095423863&di=f54813a8680af71f2f35f4688bd475ff&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fmobile%2F2018-09-13%2F5b99ccb60b6c8.jpg','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574095423862&di=2d0ddcec3f7c2e36d4ffb35a8d720e41&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fmobile%2F2018-07-13%2F5b48396e092fa.jpg','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574095423862&di=03038c8dd907520d075927e15124eb20&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fmobile%2F2018-01-18%2F5a60495640573.jpg'],
}
```

```wxss
.image {
    margin-top: 15rpx;
    margin-bottom: 30rpx;
}

.line {
    height: 1px;
    border-top: solid Silver 1px;
    margin-bottom: 40rpx;
}
```

## 预览 preview

组件默认支持图片预览，可以通过设置属性`preview`关闭预览模式。

## 属性（Wechat Attributes）

| 参数   | 说明 | 类型 | 可选值 | 默认值 |  
|:----|:----|:----|:----|:----|
| urls	| 图片的urls	| Array | - | - |
| preview	| 图片是否可预览  | Boolean| `true`,`false` | `true` |
| size	| 多图展示时的图片大小 |	String | - | 158 |
| gap-row	| 多图展示时图片横向间隔 | Number |	- | 10 |
| gap-column	| 多图展示时图片竖向间隔 | Number |	- | 10 |
| single-image-long-side | 单图展示时，长边的长度 | Number | - | 360 |
| mode-single	| 单图模式缩放裁剪模式 |	String	| 见[小程序image组件](https://developers.weixin.qq.com/miniprogram/dev/component/image.html) |`aspectFit`|
| mode-multiple	| 多图模式缩放裁剪模式 |	String	| 见[小程序image组件](https://developers.weixin.qq.com/miniprogram/dev/component/image.html) |`aspectFill`|


## 外部样式类（Wechat ExternalClasses）
| 外部样式类名 | 说明 | 备注 |
| :--------- | :----------------- | :----- |
| l-class | 覆盖组件整体的样式 | String |- |
| l-single-image-class | 覆盖组件单图展示时图片样式 |- |
|l-multi-image-class|覆盖组件多图展示时图片样式|- |


## 头像事件（Avatar Events）

| 事件名称   | 说明   | 返回值   | 备注   | 
|:----|:----|:----|:----|
| bind:lintap  | 点击图片时触发   | event.detail = {current:[ 当前点击项的url信息 ], all: [ 当前urls值 ], index: 点击项的下标}  |urls格式与传入的urls格式保持一致  | 

<RightMenu />