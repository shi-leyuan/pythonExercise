# 继承
class Phone11:
    IMEI = None
    productor = "深圳"

    def call_by_4G(self):
        print("4G通话")


class Phone15(Phone11):
    face = "666"
    productor = "郑州"  # 进行复写

    def call_by_5G(self):
        print("5G通话")

    print(f"父类的厂商为:Phone11.productor")



phone = Phone15()
print(phone.IMEI)
print(phone.productor)
print(phone.face)
phone.call_by_4G()
phone.call_by_5G()
print("--------------------------------")
print(f"父类的厂商为:Phone11.productor")
