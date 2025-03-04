from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while(1==1):
    print("Chương trình quản lý sinh viên")
    print("************************MENU************************")
    print("***  1. Nhập thông tin sinh viên                 ***")
    print("***  2. Cập nhật thông tin sinh viên bởi ID      ***")   
    print("***  3. Xóa sinh viên bởi ID                     ***")
    print("***  4. Tìm kiếm sinh viên theo tên              ***")
    print("***  5. Sắp xếp sinh viên theo điểm trung bình   ***")   
    print("***  6. Sắp xếp sinh viên theo tên chuyên ngành  ***")
    print("***  7. Hiển thị danh sách sinh viên             ***")
    print("***  0. Thoát khỏi chương trình                  ***")
    print("****************************************************")
    
    key = int(input("Nhập lựa chọn của bạn: "))
    if (key == 1):
        print("\n1. Nhập thông tin sinh viên")
        qlsv.nhapSinhVien()
        print("\nNhập thông tin sinh viên thành công!")
    elif (key == 2):
        if qlsv.soLuongSinhVien() > 0:
            print("\n2. Cập nhật thông tin sinh viên bởi ID")
            print("\n Nhập ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sách sinh viên rỗng!")
    elif (key == 3):
        if qlsv.soLuongSinhVien() > 0:
            print("\n3. Xóa sinh viên bởi ID")
            print("\n Nhập ID: ")
            ID = int(input())
            if qlsv.deleteByID(ID):
                print("\n Sinh viên có ID:", ID, "đã được xóa!")
            else:
                print("\n Không tìm thấy sinh viên có ID:", ID)
        else:
            print("\nDanh sách sinh viên rỗng!")
    elif (key == 4):
        if qlsv.soLuongSinhVien() > 0:
            print("\n4. Tìm kiếm sinh viên theo tên")
            print("\n Nhập tên cần tìm: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sách sinh viên rỗng!")
    elif (key == 5):
        if qlsv.soLuongSinhVien() > 0:
            print("\n5. Sắp xếp sinh viên theo điểm trung bình")
            qlsv.sortByDiem()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên rỗng!")
    elif (key == 6):
        if qlsv.soLuongSinhVien() > 0:
            print("\n6. Sắp xếp sinh viên theo tên tên. ")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên rỗng!")
    elif (key == 7):
        if qlsv.soLuongSinhVien() > 0:
            print("\n7. Hiển thị danh sách sinh viên")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên rỗng!")
            
    elif (key == 0):
        print("\nThoát khỏi chương trình!")
        break
    else:
        print("\nLựa chọn không hợp lệ!")