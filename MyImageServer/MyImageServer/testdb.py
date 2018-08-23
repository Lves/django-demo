# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from TestModel.models import Test
 
# 数据库操作
def testdb(request):
    # test1 = Test(name='lvesli')
    # test1.save()
    # return HttpResponse("<p>数据添加成功！</p>")
    response1 = ""
    list = Test.objects.all()
      # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")
