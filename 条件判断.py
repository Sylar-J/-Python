#小明身高1.75，体重80.5kg。
#请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
xmsg = input('小明身高为：')
xmtz = input('小明体重为：')
xmsg = float(xmsg)
xmtz = float(xmtz)
BMI = xmtz / xmsg ** 2
if BMI > 32:
    print('严重肥胖')
elif BMI > 28:
    print('肥胖')
elif BMI > 25:
    print('过重')
elif BMI > 18.5:
    print('正常')
else :
    print('过轻')
print('小明的BMI：', BMI)


    

   

    

    

    
