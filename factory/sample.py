class A:
    pass


if __name__ == "__main__":
    a = A()
    b = A()
    print(id(a) == id(b))
    print(a, b)


from django import forms


class PersonForm(forms.Form):
    name = forms.CharField(max_length=100)
    birth_date = forms.DateField(required=False)
