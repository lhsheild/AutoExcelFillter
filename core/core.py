from core import checkpoint

def start():
    print('开始程序...')

    while True:
        point_info = input('请输入监测点信息，不同信息以空格隔开。（如：NPJ47-99 9.33 1000 黄、浑浊、臭 或：NPJ47-99 9.33 1000 黄、浑浊、臭 淡黄、浑浊、微臭）：')
        point_info_list = point_info.split(' ')

        if len(point_info_list) == 4:
            point_name = point_info_list[0]
            point_time = float(point_info_list[1])
            point_water = int(point_info_list[2])
            point_status = point_info_list[3]

            check_point = checkpoint.CheckPoint(point_name, point_time, point_water, point_status)
            check_point.get_flow_excel()

        elif len(point_info_list) > 4:
            #TODO
            pass


    # TODO, UI
    # app = QApplication(sys.argv)
    #
    # main_window = core.window.MainWindow()
    # main_window.setFixedSize(1280, 720)
    # main_window.setWindowFlags(Qt.WindowMinimizeButtonHint)
    # main_window.move((app.desktop().screen().width() - main_window.width()) / 2,
    #                  (app.desktop().screen().height() - main_window.height()) / 2)
    # main_window.show()
    #
    # sys.exit(app.exec_())