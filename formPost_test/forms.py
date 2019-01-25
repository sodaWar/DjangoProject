# coding:utf-8
from django import forms

class UserInfo(forms.Form):
    # 相当于<input type="text">
    user = forms.CharField(label="username", max_length=30,error_messages={'required':'用户名不能为空'})
    password = forms.CharField(label="password", max_length=30,error_messages={'required':'密码不能为空'})
    email = forms.EmailField(label="email", max_length=30,required=False)                        # required=Flase表示email可以为空
    mobile = forms.CharField(label="phone-number", max_length=30,error_messages={'required':'手机号不能为空'})

