'''
javascript
定义变量
var name='yhzhao'
var age=22
var sex=true,hobby=[]
var scores={'math': 80, 'english': 90}
console.log(name)

boolean: true, false
string: ''
int :10 20
dict: {}

增删改查:
var dict1 = {'a':1, 'b':2, 'c':3}
dict1['d'] =4;
dict1['a'] = 7;
for (var k in dict1){
    console.log(dict1[k])
}

list: []
添加元素:
list.push()   //追加一个元素到数组
list.pop()    //从末尾删除一个元素,并返回删除的元素

遍历:
var a = ['a', 'b', 'c', 'd']
for (i=0; i<a.length; i++) {
    console.log(a[i]);
}

None: null

四则运算
and && : 两个都为True结果为True
or || : 两个都为False结果才为False
not !: 取反

条件表达式
> < = != >= <=

获取用户输入信息
s = prompt('please enter you name:')

if(s == 'yhzhao'){
    alert('ok')
} else if(s == 'woniu){
    alert('woniu')
}

else{
    alert('false')
}

var s = 40;
if(s >= 80){
    alert('优秀')
} else if (s >= '70') {
    alert('良好')
} else if(s>=60){
    alert('及格')
} else {
    alert('不及格')
}

#查看变量类型
typeof()

#类型转换:
parseInt()
parsefloat()


while循环
var user = prompt('Enter you name:')
while (user != 'kk'){
    alert('error')
    user = prompt('Enter you name:')
}
alert('ok')

do...while循环:
do{
    var user = prompt("Enter you name:");
    if (user != 'kk') {
        alert('error')
    } else {
        alert('ok')
    }
}while (user != 'kk')

for循环:

for (i=0; i<10; i++) {
    console.log(i);
}

函数:

function add(x, y) {
    return x + y
}
var x = parseInt(prompt('Enter the first number:'));
var y = parseInt(prompt('Enter the second nuber:'));
console.log(add(x, y));
alert(x+' + '+y+' = '+add(x,y));


#JS点击事件调用函数
<input type="text" id="num1" value="10">
<input type="text" id="num2" value="11">
<button onclick="add()">相加</button>
<div id="result"></div>
<script type="text/javascript">

    function add() {
        var num1 = document.getElementById('num1').value,
            num2 = document.getElementById('num2').value;
        var result = parseInt(num1) + parseInt(num2);
        document.getElementById('result').innerHTML = result;
    }

#jQuery

<script type="text/javascript" src="../static/jquery-2.2.4.min.js"></script>
<script type="text/javascript">
    jQuery(document).ready(function(){
        //页面加载完成后执行这个函数
        //获取标签元素
        /**
        tag ==> jQuery('tag')
         id ==>jQuery('#id')
         class ==> jQuery('.class')

        **/
        alert('loading finish');
    })

jQuery绑定事件

<input type="text" id="num1" value="10">
<input type="text" id="num2" value="11">
<button onclick="add()">相加</button>
<button id="btn2">相加2</button>
<input id="content">
<div id="result"></div>
<script type="text/javascript" src="../static/jquery-2.2.4.min.js"></script>
<script type="text/javascript">
    jQuery(document).ready(function(){
        //页面加载完成后执行这个函数
        //获取标签元素
        /**
        tag ==> jQuery('tag')
         id ==>jQuery('#id')
         class ==> jQuery('.class')

        **/
        jQuery('#btn2').bind('click',function () {  //为ID btn2绑定事件
            var num1 = jQuery('#num1').val();  //获取第一个数值,如果括号中有数字则设置值
            var num2 = jQuery('#num2').val();  //获取第二个数值,如果括号中有数字则设置值
            var rt = parseInt(num1) + parseInt(num2)  //数值相加
            jQuery('#content').val(rt)  //返回值  赋值
            jQuery('#result').html('结果为: '+rt)  //返回到页面值  赋值
        });
    });
    或者:
    jQuery('#btn2').click(function () {
                    var num1 = jQuery('#num1').val();  //获取第一个数值,如果括号中有数字则设置值
                    var num2 = jQuery('#num2').val();  //获取第二个数值,如果括号中有数字则设置值
                    var rt = parseInt(num1) + parseInt(num2)  //数值相加
                    jQuery('#content').val(rt)  //返回值  赋给Value属性值
                    jQuery('#result').html('结果为: '+rt)  //返回到页面值  赋值<div><xxxx/div>
                });

    function add() {
                var num1 = document.getElementById('num1').value,
                    num2 = document.getElementById('num2').value;
                var result = parseInt(num1) + parseInt(num2);
                document.getElementById('result').innerHTML = result;
            }
</script>

window.location.reload()
window.location.replace('/users')
confirm('确定删除吗?')
作业:
用户信息添加
用户信息修改
dialog
ajax
'''