# __私有成员变量和私有成员方法（只可以内部使用）

# class Phone:
#     __current_voltage = 0.1
#
#     def __keep_single_core(self):
#         print("单核运行")
#
#     def call_by_5G(self):
#         if self.__current_voltage >= 1:
#             print("开启5G通话")
#         else:
#             self.__keep_single_core()
#             print("电量不足，开启失败")
#
#
# phone = Phone()
# phone.call_by_5G()


# 练习
class Phone:
    __is_5G_enable = False

    def __check_5G(self):
        if self.__is_5G_enable:
            print("5G开启")
        else:
            print("5G关闭，开启4G")

    def call_by_5G(self):
        self.__check_5G()
        print("正在通话")


phone = Phone()
phone.call_by_5G()
