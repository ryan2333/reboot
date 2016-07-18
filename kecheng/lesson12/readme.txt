1. 本周课程：
    dialog监控数据，没有定时刷新
    a.怎么控制
        定时器JS
        setInterval(function, millisecond)  //每隔millisecond执行一次function
        setTimeout(function, millisecond) //隔millisecond执行一次function,，只执行一次
2. 如果发现cpu 内存>x，发送邮件
3. url =>给浏览器用的
    给agent/其它组件 => 认证

4. psutils
5. highcharts
    select code, sum(cnt) from webaccess group by code;

6.爬虫
    requests
        发起请求, 获取结果
        
    pyquery
        解析HTML请求

    步骤：
        拼写url, request发起请求
        PyQuery(text)
        find('.class')
        一层一层 标签or class查找
        找到标签后：
        attr  attrib.get('attrname')
        value .value
        text, .text


浏览器===》程序的处理流程

1. 发起请求
    a. 浏览器中输入url
    b. 提交表单
    c. a href=""
    d. js ajax/jquery.post load get 
    e. curl/requests













作业：
1. 如何在url中获取参数值
    delete /tests/1/2
2. 根据accesslog统计状态code分布图
3. 服务器CPU,内存使用率仪表盘 
    ajax ++>url  获取值，更新页面，不刷新整个页面
4. 机房的增删改查