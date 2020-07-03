# -*- coding: utf-8 -*-

# @Time : 2020/7/3 10:04 
# @Author : dzzhyk
# @File : csv_spliter.py 
# @Software: PyCharm


import csv
import json


class Detail():

    def __init__(self,
            crawled ,
            spider ,
            href ,
            title ,
            mileage ,
            emission ,
            gearbox ,
            transfers ,
            region ,
            manufacturer ,
            level ,
            engine ,
            gearbox_d ,
            struction ,
            LWH ,
            wheelbase ,
            luggage ,
            curb_weight ,
            displacement ,
            intake_form ,
            cylinders ,
            horsepower ,
            torque ,
            fuel ,
            fuel_label ,
            fuel_supply ,
            drive_method ,
            assistance ,
            front_suspension,
            back_suspension ,
            front_brake ,
            back_brake ,
            driving_brake ,
            front_tire ,
            back_tire ,
            front_airbag ,
            side_airbag ,
            head_airbag ,
            tire_pressure ,
            locking ,
            child_seat ,
            keyless ,
            abs ,
            esp ,
            sunroof ,
            skylight ,
            suction_door ,
            induction_trunk ,
            induction_wiper ,
            back_wiper ,
            windows ,
            mirror_elec ,
            mirror_heat ,
            steering_wheel ,
            cruise ,
            air_cond ,
            air_control ,
            gps ,
            radar ,
            image ,
            leather ,
            seat_heat
    ):
        self.crawled =                             crawled
        self.spider =                              spider
        self.href =                            href
        self.title =                            title
        self.mileage =                            mileage
        self.emission =                            emission
        self.gearbox =                            gearbox
        self.transfers =                            transfers
        self.region =                            region
        self.manufacturer =                            manufacturer
        self.level =                            level
        self.engine =                            engine
        self.gearbox_d =                            gearbox_d
        self.struction =                      struction
        self.LWH =                            LWH
        self.wheelbase =                            wheelbase
        self.luggage =                            luggage
        self.curb_weight =                            curb_weight
        self.displacement =                            displacement
        self.intake_form =                            intake_form
        self.cylinders =                            cylinders
        self.horsepower =                            horsepower
        self.torque =                            torque
        self.fuel =                            fuel
        self.fuel_label =                            fuel_label
        self.fuel_supply =                            fuel_supply
        self.drive_method =                            drive_method
        self.assistance =                            assistance
        self.front_suspension =                            front_suspension
        self.back_suspension =                         back_suspension
        self.front_brake =                         front_brake
        self.back_brake =                         back_brake
        self.driving_brake =                         driving_brake
        self.front_tire =                         front_tire
        self.back_tire =                         back_tire
        self.front_airbag =                         front_airbag
        self.side_airbag =                         side_airbag
        self.head_airbag =                         head_airbag
        self.tire_pressure =                         tire_pressure
        self.locking =                         locking
        self.child_seat =                         child_seat
        self.keyless =                         keyless
        self.abs =                         abs
        self.esp =                         esp
        self.sunroof =                         sunroof
        self.skylight =                         skylight
        self.suction_door =                         suction_door
        self.induction_trunk =                         induction_trunk
        self.induction_wiper =                         induction_wiper
        self.back_wiper =                         back_wiper
        self.windows =                         windows
        self.mirror_elec =                         mirror_elec
        self.mirror_heat =                         mirror_heat
        self.steering_wheel =                         steering_wheel
        self.cruise =                         cruise
        self.air_cond =                         air_cond
        self.air_control =                         air_control
        self.gps =                         gps
        self.radar =                         radar
        self.image =                         image
        self.leather =                         leather
        self.seat_heat =                         seat_heat



# 分割csv到标准json格式
def ssplit(filename, save_to):

    col1 =  0
    col2 =  1
    col3 =  2
    col4 =  3
    col5 =  4
    col6 =  5
    col7 =  6
    col8 =  7
    col9 =  8
    col10 = 9
    col11 = 10
    col12 = 11
    col13 = 12
    col14 = 13
    col15 = 14
    col16 = 15

    cnt = 0

    fout = open(save_to, "w", encoding='utf-8')

    with open("../detail_test.csv", "r", encoding='utf-8') as fin:
        reader = csv.reader(fin)
        result = list(reader)
        i = 0
        while True:
            if i*6 >= len(result):
                break
            line1 = i * 6
            line2 = i*6 + 1
            line3 = i*6 + 2
            line4 = i*6 + 3
            line5 = i*6 + 4
            line6 = i*6 + 5
            temp = Detail(
                crawled =           result[line1][col1],
                spider =            "car_spider",
                href =              result[line1][col4],
                title =             result[line1][col2],
                mileage =           result[line1][col3],
                emission =          result[line2][col16],
                gearbox =           result[line1][col5],
                transfers =         result[line1][col6],
                region =            result[line1][col7],

                manufacturer =      result[line1][col8],
                level =             result[line1][col9],
                engine =            result[line1][col10],
                gearbox_d =         result[line1][col11],
                struction =         result[line1][col12],
                LWH =               result[line1][col13],
                wheelbase =         result[line1][col14],
                luggage =           result[line1][col15],
                curb_weight =       result[line1][col16],

                displacement =      result[line2][col8],
                intake_form =       result[line2][col9],
                cylinders =         result[line2][col10],
                horsepower =        result[line2][col11],
                torque =            result[line2][col12],
                fuel =              result[line2][col13],
                fuel_label =        result[line2][col14],
                fuel_supply =       result[line2][col15],

                drive_method =      result[line3][col8],
                assistance =        result[line3][col9],
                front_suspension =  result[line3][col10],
                back_suspension =   result[line3][col11],
                front_brake =       result[line3][col12],
                back_brake =        result[line3][col13],
                driving_brake =     result[line3][col14],
                front_tire =        result[line3][col15],
                back_tire =         result[line3][col16],

                front_airbag =      result[line4][col8],
                side_airbag =       result[line4][col9],
                head_airbag =       result[line4][col10],
                tire_pressure =     result[line4][col11],
                locking =           result[line4][col12],
                child_seat =        result[line4][col13],
                keyless =           result[line4][col14],
                abs =               result[line4][col15],
                esp =               result[line4][col16],

                sunroof =           result[line5][col8],
                skylight =          result[line5][col9],
                suction_door =      result[line5][col10],
                induction_trunk =   result[line5][col11],
                induction_wiper =   result[line5][col12],
                back_wiper =        result[line5][col13],
                windows =           result[line5][col14],
                mirror_elec =       result[line5][col15],
                mirror_heat =       result[line5][col16],

                steering_wheel =    result[line6][col8],
                cruise =            result[line6][col9],
                air_cond =          result[line6][col10],
                air_control =       result[line6][col11],
                gps =               result[line6][col12],
                radar =             result[line6][col13],
                image =             result[line6][col14],
                leather =           result[line6][col15],
                seat_heat =         result[line6][col16]
            )
            content = json.dumps(temp.__dict__, ensure_ascii=False)
            fout.write(content + "\n")
            cnt += 1
            i += 1
        fin.close()
    fout.close()
    print("Done! " + str(cnt) + " 条记录")
    return cnt


if __name__ == '__main__':
    cnt = ssplit("../detail_test.csv", "../data/guazi/getted/guazi_detail")

