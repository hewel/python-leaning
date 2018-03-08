h = float(input('请输入你的身高：'))
w = float(input('请输入你的体重：'))
bmi = w/h/h
status = '结果未知'
if bmi < 0:
    pass
elif bmi < 18.5:
    status = '过轻'
elif bmi < 25:
    status = '正常'
elif bmi < 28:
    status = '过重'
elif bmi < 32:
    status = '肥胖'
else:
    status = '严重肥胖'
print('BMI指数： %.1f \n 状态：%s' %(bmi, status))
