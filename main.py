
import time

import sys

while True:

    def xac_nhan_tinh(text):
        print(text)

    xac_nhan_tinh("Tính diện tích hình gì?")
    xac_nhan_tinh("1. Hình tam giác")
    xac_nhan_tinh("2. Hình bình hành")
    xac_nhan_tinh("3. Hình vuông")
    xac_nhan_tinh("4. Hình chữ nhật")
    xac_nhan_tinh("5. Hình thang")
    xac_nhan_tinh("Sử dụng 1, 2, 3, 4, hoặc là 5!")

    xac_nhan_lai = input()

    xac_nhan_laiint = int(xac_nhan_lai)
    if xac_nhan_laiint == 1:
        chieuCao_hinhTamGiac = input("Nhập chiều cao: ")
        chieuCao_hinhTamGiacint = int(chieuCao_hinhTamGiac)
        do_dai_dayHinhTamgiac = input("Nhập độ dài đáy: ")
        do_dai_dayHinhTamgiacint = int(do_dai_dayHinhTamgiac)
        dien_tich_tam_giac = do_dai_dayHinhTamgiacint * chieuCao_hinhTamGiacint / 2
        print("Diện tích hình tam giác đó là :" + str(dien_tich_tam_giac))
    elif xac_nhan_laiint == 2:
        chieuCao_hinhBinhHanh = input("Nhập chiều cao :")
        chieuCao_hinhBinhHanhint = int(chieuCao_hinhBinhHanh)
        do_dai_dayHinhBinhHanh = input("Nhập độ dài đáy: ")
        do_dai_dayHinhBinhHanhint = int(do_dai_dayHinhBinhHanh)
        dien_tich_binh_hanh = do_dai_dayHinhBinhHanhint * chieuCao_hinhBinhHanhint
        print("Diện tích hình bình hành đó là: " + str(dien_tich_binh_hanh))
    elif xac_nhan_laiint == 3:
        canh = input("Nhập cạnh : ")
        canhint = int(canh)
        s_hinh_vuong = canhint**2
        print("Diện tích hình vuông đó là: " + str(s_hinh_vuong))
    elif xac_nhan_laiint == 4:
        chieu_dai = input("Nhập chiều dài : ")
        chieu_dai_int = int(chieu_dai)
        chieurong = input("Nhập chiều rộng: ")
        chieurong_int = int(chieurong)
        dien_tich_hinh_chu_nhat = chieu_dai_int * chieurong_int
        if chieurong_int > chieu_dai_int:
            print("Chiều rộng không thể lớn hơn chiều dài.")
        else:
            print("Diện tích hình chữ nhật đó là: " + str(dien_tich_hinh_chu_nhat))
    elif xac_nhan_laiint == 5:
        chieuCao_hinhThang = input("Nhập chiều cao :")
        chieuCao_hinhThang_int = int(chieuCao_hinhThang)
        do_dai_dayHinhThang_thu_nhat = input("Nhập độ dài đáy thứ nhất: ")
        do_dai_dayHinhThang_thu_nhat_int = int(do_dai_dayHinhThang_thu_nhat)
        do_dai_dayHinhThang_thu_hai = input("Nhập độ dài đáy thứ hai: ")
        do_dai_dayHinhThang_thu_hai_int = int(do_dai_dayHinhThang_thu_hai)
        dien_tich_hinh_thang = chieuCao_hinhThang_int * (
            do_dai_dayHinhThang_thu_nhat_int +
            do_dai_dayHinhThang_thu_hai_int / 2)
        print("Diện tích hình tam giác đó là: " + str(dien_tich_hinh_thang))
    else:
        print("Hả?")
    choi_lai = input("Bạn có muốn tính tiếp không?\n1. Có!\n2. Không!\n(C) là có, (K) là không\n")
    if choi_lai == "C" and "(C)" and "1" and "Có!" and "Có":
        pass
    else:
        sys.exit()

input()

# ------------------------------End------------------------------#
