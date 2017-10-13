
find_index_01.py   find index.html files 
                   params: [input: root dir, output: indexlist.csv]


Access Key,Secret Key
AKIAIA5J4XZKVECVY5YA,A6x486ftL9v5Dhgwdepkyu5nx3qj8mSie+CfYf6i


wboxes-20

//rex
http://www.rexegg.com/regex-disambiguation.html#lookaround
https://stackoverflow.com/questions/40602714/python-regular-expression-to-get-text-between-two-strings

//wagtail tutorial
https://github.com/springload/awesome-wagtail
https://blog.michaelyin.info/wagtail-tutorials/
https://snipcart.com/blog/django-ecommerce-tutorial-wagtail-cms

//python
methods
https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods

//django
https://simpleisbetterthancomplex.com/2015/12/07/working-with-django-view-decorators.html

//
就是这么弄的。服务器在墙外，ssh -d 在本机弄个socks5代理，浏览器使用
switchproxy连本机localhost的socks5代理

这种墙看到的数据只是SSH，难以封禁。

第一可能是你的SSH服务器不支持转发，需要开AllowTcpForwarding。

可能是你的SSH客户端有问题，别用putty之类，装个linux用openssh就行了。

还有记得浏览器上用远程DNS
用google的xxnet，这个对一点计算机不懂的难度有点高，但我设置好了，一直用这个
，最近也不行了

用日本筑波大学的SoftEther，效果不太好，最近还是不行

最后用Psiphon和3proxy搭档，看youtube大概能720左右，另外google的dns被土共搞死
了，所以保险点的方式是查看以太网，用自己网络提供商的dns地址，麻烦的是端口总
是在变。这对有些浏览器，例如chrome是个麻烦，因为它必须要有插件才能vpn，火狐
和win10自带的没问题。勉强不成问题了。但还有个麻烦，就是迟早要自个检测和换一
个config文件的ip，这对我爸这种电脑盲来说是不可能的任务。

总结起来，目前发现最好的办法是，用google的服务，xxnet，把ipv4换成ipv6，能傻
瓜化的让不知道电脑的人也能绕过土共的网络长城。