# in the name of God
# Seyyed Mahdi HassanPour
# SeyyedMahdiHP@gmail.com
"""
this a sandbox python project
"""


def func():
    """
    this is a doc string
    :return:
    """
    pass


def complexfunc(real=0.0, imag=0.0):
    """Form a complex Number
        :keyword args:
            :param real: the real part(default0.0)
            :param imag: the imaginary part(default0.0)
    :return:
    """
    pass
print("this is complex func doc string:\r\n", complexfunc.__doc__, "\r\n")
print(func.__name__, func.__doc__);print("multiple statement on one line,with semicolon; delimiter")
print("this is 1th line "
      "this 2nd line\r\n"
      "this is 3rd line\r\n"
      "this is 4th line ,...\r\n"
      "of a multiple line statement")
s1 = """ this is a very
    long string using \""" \""" """

s2 = ("this is a very"
      "long string using (\" \")")
s3 = "this is a "\
    "very long string using \\"
print(s1, s2, s3)
