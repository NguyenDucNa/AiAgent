from enum import Enum

class ProductType(Enum):
    A = "MISA Mimosa Online"
    B = "MISA Bamboo Online"
    C = "AMIS Kế toán Doanh nghiệp"
    D = "Bộ giải pháp tài chính kế toán doanh nghiệp"
    E = "MISA Quản lý tài sản"
    F = "MISA SME 2023"
    G = "MISA eShop"
    H = "Thuế điện tử MISA mTax"
    I = "MISA eSign – Chữ ký số USB Token cho Doanh nghiệp"
    J = "Bộ giải pháp quản trị nguồn nhân lực"
    K = "AMIS Mua hàng"
    L = "AMIS Tuyển dụng"
    M = "AMIS Mục tiêu"
    N = "AMIS Đánh giá"
    O = "AMIS Thuế TNCN"
    P = "AMIS Bảo hiểm xã hội"
    Q = "AMIS Tiền lương"
    R = "AMIS Chấm công"
    S = "AMIS Thông tin nhân sự"
    T = "AMIS aiMarketing"
    U = "AMIS Khuyến mại"
    V = "AMIS Bán hàng"
    W = "MISA eSign – Chữ ký số từ xa cho cá nhân"
    X = "meInvoice Doanh nghiệp - Phát hành hóa đơn"
    Y = "meInvoice Doanh nghiệp - Xử lý hóa đơn"
    Z = "meInvoice Hộ kinh doanh - Xử lý hóa đơn"

    A1 = "MISA eSign – Chữ ký số từ xa cho hộ kinh doanh"
    B1 = "meInvoice Hộ Kinh doanh - Phát hành hóa đơn"
    C1 = "Văn phòng số"
    D1 = "MISA eSign – Chữ ký số từ xa cho doanh nghiệp"
    E1 = "AMIS Quản lý tài sản"
    F1 = "Quản lý phòng họp"
    G1 = "AMIS Văn thư"
    H1 = "Mạng xã hội doanh nghiệp"
    I1 = "Ghi chép và lưu trữ tài liệu"
    J1 = "Nền tảng ký tài liệu số"
    K1 = "AMIS Quy trình"
    L1 = "AMIS Kế toán Hộ kinh doanh"
    M1 = "Phần mềm quản lý nhà hàng CUKCUK"
    N1 = "MISA eSign - Chữ ký số USB Token cho Hộ kinh doanh"
    O1 = "Quản lý công việc"
    P1 = "AMIS Bảo hiểm xã hội Hộ kinh doanh"
    Q1 = "AILearning"


class MEI_ENTERPRISE_PKG(Enum):
    A = "MEIXD-50.000"
    B = "MEIXD-100.000"
    C = "MEIXD-300.000"
    D = "MEIXD-500.000"
    E = "MEIXD-1.000.000"
    F = "MEIXD-3.000.000"

    G = "MEIR-20.000"
    H = "MEIR-50.000"
    I = "MEIR-200.000"
    J = "MEIR-300.000"
    K = "MEIR-500.000"
    
    L = "MEIMTT-200.000"
    M ="MEIMTT-500.000"
    N = "MEIMTT-1.000.000"

    O ="MEIR-300"
    P = "MEIR-500"
    Q = "MEIR-1.000"
    R = "MEIR-2.000"
    S = "MEIR-5.000"
    T = "MEIR-10.000"
    U = "MEIR-100.000"

    V = "MEIVE-10.000"
    W = "MEIVE-100.000"
    X = "MEIVE-200.000"
    Y = "MEIVE-500.000"

    Z = "MEIMTT-300"
    A1 = "MEIMTT-500"
    B1 = "MEIMTT-1000"
    C1 = "MEIMTT-2000"
    D1 = "MEIMTT-5000"
    E1 = "MEIMTT-10.000"
    F1 = "MEIMTT-20000"
    G1 = "MEIMTT-50000"
    H1 = "MEIMTT-100.000"

    I1 = "MEIVE-20.000"
    J1 = "MEIVE-50.000"
    K1 = "MEIVE-100.000.000"

class MEI_HOUSEHOLD_PKG(Enum):
    A = "MEIMTT-200.000"
    B = "MEIMTT-500.000"
    C = "MEIMTT-1.000.000"

    D = "MEIHVE-10.000"
    E = "MEIHVE-20.000"
    F = "MEIHVE-50.000"
    G = "MEIHVE-100.000"
    H = "MEIHVE-200.000"
    I = "MEIHVE-500.000"
    J = "MEIHVE-1.000.000"

    K = "MEIH-300"
    L = "MEIH-500"
    M = "MEIH-1.000"
    N = "MEIH-2.000"
    O = "MEIH-5.000"
    P = "MEIH-10.000"

    Q = "MEIHMTT-300"
    R = "MEIHMTT-500"
    S = "MEIHMTT-1.000"
    T = "MEIHMTT-2.000"
    U = "MEIHMTT-5.000"
    V = "MEIHMTT-10.000"
    W = "MEIHMTT-20.000"
    X = "MEIHMTT-50.000"
    Y = "MEIHMTT-100.000"



PRODUCTS= [
  {
    "AppCode": "MISAIVAN",
    "AppName": "AMIS Bảo hiểm xã hội Hộ kinh doanh",
    "ProductID": 691,
    "MarketName": "Hộ kinh doanh",
    "ListPackageProduct": [
      {
        "ItemPrice": 80000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 người dùng",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10 người dùng",
        "ProductID": 691,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 240000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"AMIS BHXH\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"AMIS BHXH\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "AMIS BHXH",
        "ModuleName": None,
        "DisplayName": "Phần mềm AMIS BHXH",
        "ProductID": 691,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "AILearning",
    "AppName": "AILearning",
    "ProductID": 690,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 1200000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Value\": 5, \"DataType\": \"number\", \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Dung lượng\", \"Value\": \"1\", \"DataType\": \"string\", \"ResourceID\": 101, \"ResourceCode\": \"DBCapacity\", \"ResourceName\": \"Dung lượng\"}]",
        "ItemName": "Mua thêm 5 người dùng",
        "ModuleName": None,
        "DisplayName": "Mua thêm 5 người dùng",
        "ProductID": 690,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2400000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Dung lượng\", \"Value\": \"5\", \"DataType\": \"string\", \"ResourceID\": 101, \"ResourceCode\": \"DBCapacity\", \"ResourceName\": \"Dung lượng\"}]",
        "ItemName": "Mua thêm 5 GB dung lượng lưu trữ",
        "ModuleName": None,
        "DisplayName": "Mua thêm 5 GB dung lượng lưu trữ",
        "ProductID": 690,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None  
      },
      {
        "ItemPrice": 7950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Đào tạo phần mềm 1 kèm 1 trực tuyến",
        "ModuleName": None,
        "DisplayName": "Đào tạo phần mềm 1 kèm 1 trực tuyến",
        "ProductID": 690,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 11950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Đào tạo phần mềm 1 kèm 1 trực tiếp",
        "ModuleName": None,
        "DisplayName": "Đào tạo phần mềm 1 kèm 1 trực tiếp",
        "ProductID": 690,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 20000000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Tư vấn triển khai phần mềm",
        "ModuleName": None,
        "DisplayName": "Tư vấn triển khai phần mềm",
        "ProductID": 690,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 0.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Tên gói\", \"Value\": \"AILearning\", \"DataType\": \"string\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Mã gói\", \"Value\": \"AILearning\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Thời hạn theo ngày\", \"Value\": 30, \"DataType\": \"number\", \"ResourceID\": 23, \"ResourceCode\": \"DurationByDay\", \"ResourceName\": \"Thời hạn theo ngày\"}]",
        "ItemName": "Gói dùng thử",
        "ModuleName": None,
        "DisplayName": "Gói dùng thử 30 ngày AILearning",
        "ProductID": 690,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7200000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Tên gói\", \"Value\": \"AILearning\", \"DataType\": \"string\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Mã gói\", \"Value\": \"AILearning\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Người dùng\", \"Value\": 30, \"DataType\": \"number\", \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Dung lượng\", \"Value\": \"6\", \"DataType\": \"string\", \"ResourceID\": 101, \"ResourceCode\": \"DBCapacity\", \"ResourceName\": \"Dung lượng\"}, {\"Name\": \"Thời hạn theo năm\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "AILearning",
        "ModuleName": None,
        "DisplayName": "AILearning",
        "ProductID": 690,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "MMO",
    "AppName": "MISA Mimosa Online",
    "ProductID": 687,
    "MarketName": "Hành chính sự nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 6000000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}, {\"Name\": \"Số lượng người dùng\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 83, \"ResourceCode\": \"NumberOfUser\", \"ResourceName\": \"Số lượng người dùng\"}, {\"Name\": \"Mã gói Suman\", \"Value\": \"MMO\", \"DataType\": \"string\", \"ResourceID\": 94, \"ResourceCode\": \"SumanPackCode\", \"ResourceName\": \"Mã gói Suman\"}, {\"Name\": \"Địa chỉ truy cập\", \"Value\": \"mimosaapp.misa.vn\", \"DataType\": \"string\", \"ResourceID\": 98, \"ResourceCode\": \"ApplicationURL\", \"ResourceName\": \"Địa chỉ truy cập\"}]",
        "ItemName": "Gói phần mềm kế toán ",
        "ModuleName": None,
        "DisplayName": "Gói phần mềm kế toán HCSN",
        "ProductID": 687,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "BBO",
    "AppName": "MISA Bamboo Online",
    "ProductID": 686,
    "MarketName": "Hành chính sự nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 6000000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}, {\"Name\": \"Mã gói Suman\", \"Value\": \"BBO\", \"DataType\": \"string\", \"ResourceID\": 94, \"ResourceCode\": \"SumanPackCode\", \"ResourceName\": \"Mã gói Suman\"}, {\"Name\": \"Địa chỉ truy cập\", \"Value\": \"bambooapp.misa.vn\", \"DataType\": \"string\", \"ResourceID\": 98, \"ResourceCode\": \"ApplicationURL\", \"ResourceName\": \"Địa chỉ truy cập\"}]",
        "ItemName": "Gói phần mềm kế toán xã/phường",
        "ModuleName": None,
        "DisplayName": "Gói phần mềm kế toán xã/phường",
        "ProductID": 686,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "Accounting",
    "AppName": "AMIS Kế toán Doanh nghiệp",
    "ProductID": 404,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 11950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Gói đào tạo phần mềm 1 kèm 1 trực tiếp",
        "ModuleName": None,
        "DisplayName": "Gói đào tạo phần mềm",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 20000000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Tư vấn triển khai phần mềm",
        "ModuleName": None,
        "DisplayName": "Tư vấn triển khai phần mềm",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Gói đào tạo phần mềm 1 kèm 1 trực tuyến",
        "ModuleName": None,
        "DisplayName": "Gói đào tạo phần mềm",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2450000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 01 người dùng gói Starter",
        "ModuleName": None,
        "DisplayName": "Mua thêm 01 người dùng gói Starter",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Chi nhánh\", \"Unit\": \"chi nhánh\", \"Value\": 1, \"ResourceID\": 43, \"ResourceCode\": \"Branch\", \"ResourceName\": \"Chi nhánh\"}]",
        "ItemName": "Mua thêm chi nhánh gói Starter",
        "ModuleName": None,
        "DisplayName": "Mua thêm chi nhánh gói Starter",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1350000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 01 người dùng gói Standard",
        "ModuleName": None,
        "DisplayName": "Mua thêm 01 người dùng gói Standard",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Chi nhánh\", \"Unit\": \"chi nhánh\", \"Value\": 1, \"ResourceID\": 43, \"ResourceCode\": \"Branch\", \"ResourceName\": \"Chi nhánh\"}]",
        "ItemName": "Mua thêm chi nhánh gói Standard",
        "ModuleName": None,
        "DisplayName": "Mua thêm chi nhánh gói Standard",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1750000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 01 người dùng gói Professional",
        "ModuleName": None,
        "DisplayName": "Mua thêm 01 người dùng gói Professional",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2450000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Chi nhánh\", \"Unit\": \"chi nhánh\", \"Value\": 1, \"ResourceID\": 43, \"ResourceCode\": \"Branch\", \"ResourceName\": \"Chi nhánh\"}]",
        "ItemName": "Mua thêm chi nhánh gói Professional",
        "ModuleName": None,
        "DisplayName": "Mua thêm chi nhánh gói Professional",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2150000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 01 người dùng gói Enterprise",
        "ModuleName": None,
        "DisplayName": "Mua thêm 01 người dùng gói Enterprise",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Chi nhánh\", \"Unit\": \"chi nhánh\", \"Value\": 1, \"ResourceID\": 43, \"ResourceCode\": \"Branch\", \"ResourceName\": \"Chi nhánh\"}]",
        "ItemName": "Mua thêm chi nhánh gói Enterprise",
        "ModuleName": None,
        "DisplayName": "Mua thêm chi nhánh gói Enterprise",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2250000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 01 người dùng gói Enterprise Plus",
        "ModuleName": None,
        "DisplayName": "Mua thêm 01 người dùng gói Enterprise Plus",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Chi nhánh\", \"Unit\": \"chi nhánh\", \"Value\": 1, \"ResourceID\": 43, \"ResourceCode\": \"Branch\", \"ResourceName\": \"Chi nhánh\"}]",
        "ItemName": "Mua thêm chi nhánh gói Enterprise Plus",
        "ModuleName": None,
        "DisplayName": "Mua thêm chi nhánh gói Enterprise Plus",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 330000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Value\": \"Starter\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}, {\"Name\": \"Là gói dịch vụ lưu trữ dữ liệu\", \"Value\": \"True\", \"DataType\": \"string\", \"ResourceID\": 91, \"ResourceCode\": \"IsDataStorage\", \"ResourceName\": \"Là gói dịch vụ lưu trữ dữ liệu\"}]",
        "ItemName": "Dịch vụ lưu trữ dữ liệu gói Starter",
        "ModuleName": None,
        "DisplayName": "Dịch vụ lưu trữ dữ liệu",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 440000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Value\": \"Standard\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}, {\"Name\": \"Là gói dịch vụ lưu trữ dữ liệu\", \"Value\": \"True\", \"DataType\": \"string\", \"ResourceID\": 91, \"ResourceCode\": \"IsDataStorage\", \"ResourceName\": \"Là gói dịch vụ lưu trữ dữ liệu\"}]",
        "ItemName": "Dịch vụ lưu trữ dữ liệu gói Standard",
        "ModuleName": None,
        "DisplayName": "Dịch vụ lưu trữ dữ liệu",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 550000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Value\": \"Professional\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}, {\"Name\": \"Là gói dịch vụ lưu trữ dữ liệu\", \"Value\": \"True\", \"DataType\": \"string\", \"ResourceID\": 91, \"ResourceCode\": \"IsDataStorage\", \"ResourceName\": \"Là gói dịch vụ lưu trữ dữ liệu\"}]",
        "ItemName": "Dịch vụ lưu trữ dữ liệu gói Professional",
        "ModuleName": None,
        "DisplayName": "Dịch vụ lưu trữ dữ liệu",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 660000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Value\": \"Enterprise\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}, {\"Name\": \"Là gói dịch vụ lưu trữ dữ liệu\", \"Value\": \"True\", \"DataType\": \"string\", \"ResourceID\": 91, \"ResourceCode\": \"IsDataStorage\", \"ResourceName\": \"Là gói dịch vụ lưu trữ dữ liệu\"}]",
        "ItemName": "Dịch vụ lưu trữ dữ liệu gói Enterprise",
        "ModuleName": None,
        "DisplayName": "Dịch vụ lưu trữ dữ liệu",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2200000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Value\": \"Enterprise Plus\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}, {\"Name\": \"Là gói dịch vụ lưu trữ dữ liệu\", \"Value\": \"True\", \"DataType\": \"string\", \"ResourceID\": 91, \"ResourceCode\": \"IsDataStorage\", \"ResourceName\": \"Là gói dịch vụ lưu trữ dữ liệu\"}]",
        "ItemName": "Dịch vụ lưu trữ dữ liệu gói Enterprise Plus",
        "ModuleName": None,
        "DisplayName": "Dịch vụ lưu trữ dữ liệu",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3000000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Dữ liệu\", \"Unit\": \"Dữ liệu/Năm\", \"Value\": \"1\", \"DataType\": \"string\", \"ResourceID\": 92, \"ResourceCode\": \"ResourceQuantity\", \"ResourceName\": \"Dữ liệu\"}]",
        "ItemName": "Mua thêm dữ liệu",
        "ModuleName": None,
        "DisplayName": "Mua thêm dữ liệu AMIS Kế Toán",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2450000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nghiệp vụ\", \"Unit\": None, \"Value\": 7, \"ResourceID\": 21, \"ResourceCode\": \"Business\", \"ResourceName\": \"Nghiệp vụ\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Starter\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Starter\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}, {\"Name\": \"Dữ liệu\", \"Value\": \"3\", \"DataType\": \"string\", \"ResourceID\": 92, \"ResourceCode\": \"ResourceQuantity\", \"ResourceName\": \"Dữ liệu\"}]",
        "ItemName": "Starter",
        "ModuleName": None,
        "DisplayName": "Starter",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 4050000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 3, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nghiệp vụ\", \"Unit\": None, \"Value\": 11, \"ResourceID\": 21, \"ResourceCode\": \"Business\", \"ResourceName\": \"Nghiệp vụ\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Standard\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Standard\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}, {\"Name\": \"Dữ liệu\", \"Value\": \"3\", \"DataType\": \"string\", \"ResourceID\": 92, \"ResourceCode\": \"ResourceQuantity\", \"ResourceName\": \"Dữ liệu\"}]",
        "ItemName": "Standard",
        "ModuleName": None,
        "DisplayName": "Standard",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 5250000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 3, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nghiệp vụ\", \"Unit\": None, \"Value\": 16, \"ResourceID\": 21, \"ResourceCode\": \"Business\", \"ResourceName\": \"Nghiệp vụ\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Professional\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Professional\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}, {\"Name\": \"Dữ liệu\", \"Value\": \"3\", \"DataType\": \"string\", \"ResourceID\": 92, \"ResourceCode\": \"ResourceQuantity\", \"ResourceName\": \"Dữ liệu\"}]",
        "ItemName": "Professional",
        "ModuleName": None,
        "DisplayName": "Professional",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 6450000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 3, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nghiệp vụ\", \"Unit\": None, \"Value\": 17, \"ResourceID\": 21, \"ResourceCode\": \"Business\", \"ResourceName\": \"Nghiệp vụ\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Enterprise\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Enterprise\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}, {\"Name\": \"Dữ liệu\", \"Value\": \"3\", \"DataType\": \"string\", \"ResourceID\": 92, \"ResourceCode\": \"ResourceQuantity\", \"ResourceName\": \"Dữ liệu\"}]",
        "ItemName": "Enterprise",
        "ModuleName": None,
        "DisplayName": "Enterprise",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 22500000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nghiệp vụ\", \"Unit\": None, \"Value\": 20, \"ResourceID\": 21, \"ResourceCode\": \"Business\", \"ResourceName\": \"Nghiệp vụ\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Enterprise Plus\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Enterprise Plus\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}, {\"Name\": \"Dữ liệu\", \"Value\": \"3\", \"DataType\": \"string\", \"ResourceID\": 92, \"ResourceCode\": \"ResourceQuantity\", \"ResourceName\": \"Dữ liệu\"}]",
        "ItemName": "Enterprise Plus",
        "ModuleName": None,
        "DisplayName": "Enterprise Plus",
        "ProductID": 404,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "ComboKT_DN",
    "AppName": "Bộ giải pháp tài chính kế toán doanh nghiệp",
    "ProductID": 406,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 11950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp Phần mềm Quản lý Tài chính kế toán doanh nghiệp - Gói đào tạo phần mềm 1 kèm 1 trực tiếp",
        "ModuleName": None,
        "DisplayName": "Gói đào tạo phần mềm",
        "ProductID": 406,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 20000000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp Phần mềm Quản lý Tài chính kế toán doanh nghiệp - Tư vấn triển khai phần mềm",
        "ModuleName": None,
        "DisplayName": "Tư vấn triển khai phần mềm",
        "ProductID": 406,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp Phần mềm Quản lý Tài chính kế toán doanh nghiệp - Gói đào tạo phần mềm 1 kèm 1 trực tuyến",
        "ModuleName": None,
        "DisplayName": "Gói đào tạo phần mềm",
        "ProductID": 406,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2450000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 01 người dùng gói Starter",
        "ModuleName": None,
        "DisplayName": "Mua thêm 01 người dùng",
        "ProductID": 406,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Chi nhánh\", \"Unit\": \"chi nhánh\", \"Value\": 1, \"ResourceID\": 43, \"ResourceCode\": \"Branch\", \"ResourceName\": \"Chi nhánh\"}]",
        "ItemName": "Mua thêm chi nhánh gói Starter",
        "ModuleName": None,
        "DisplayName": "Mua thêm chi nhánh",
        "ProductID": 406,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1350000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 01 người dùng gói Standard",
        "ModuleName": None,
        "DisplayName": "Mua thêm 01 người dùng",
        "ProductID": 406,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Chi nhánh\", \"Unit\": \"chi nhánh\", \"Value\": 1, \"ResourceID\": 43, \"ResourceCode\": \"Branch\", \"ResourceName\": \"Chi nhánh\"}]",
        "ItemName": "Mua thêm chi nhánh gói Standard",
        "ModuleName": None,
        "DisplayName": "Mua thêm chi nhánh",
        "ProductID": 406,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1750000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 01 người dùng gói Professional",
        "ModuleName": None,
        "DisplayName": "Mua thêm 01 người dùng",
        "ProductID": 406,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2450000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Chi nhánh\", \"Unit\": \"chi nhánh\", \"Value\": 1, \"ResourceID\": 43, \"ResourceCode\": \"Branch\", \"ResourceName\": \"Chi nhánh\"}]",
        "ItemName": "Mua thêm chi nhánh gói Professional",
        "ModuleName": None,
        "DisplayName": "Mua thêm chi nhánh",
        "ProductID": 406,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2150000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 01 người dùng gói Enterprise",
        "ModuleName": None,
        "DisplayName": "Mua thêm 01 người dùng",
        "ProductID": 406,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Chi nhánh\", \"Unit\": \"chi nhánh\", \"Value\": 1, \"ResourceID\": 43, \"ResourceCode\": \"Branch\", \"ResourceName\": \"Chi nhánh\"}]",
        "ItemName": "Mua thêm chi nhánh gói Enterprise",
        "ModuleName": None,
        "DisplayName": "Mua thêm chi nhánh",
        "ProductID": 406,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2250000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 01 người dùng gói Enterprise Plus",
        "ModuleName": None,
        "DisplayName": "Mua thêm 01 người dùng",
        "ProductID": 406,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Chi nhánh\", \"Unit\": \"chi nhánh\", \"Value\": 1, \"ResourceID\": 43, \"ResourceCode\": \"Branch\", \"ResourceName\": \"Chi nhánh\"}]",
        "ItemName": "Mua thêm chi nhánh gói Enterprise Plus",
        "ModuleName": None,
        "DisplayName": "Mua thêm chi nhánh",
        "ProductID": 406,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 450000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"300\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "Gói MEIR 300",
        "ModuleName": None,
        "DisplayName": "Gói MEIR 300",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 650000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"500\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "Gói MEIR 500",
        "ModuleName": None,
        "DisplayName": "Gói MEIR 500",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1050000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"1000\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "Gói MEIR 1.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIR 1.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3150000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"5000\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "Gói MEIR 5.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIR 5.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 5250000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"10000\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "Gói MEIR 10.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIR 10.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 30000000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"100000\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "Gói MEIR 100.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIR 100.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3500000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"10000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "Gói MEIVE 10.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIVE 10.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 5650000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"20000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "Gói MEIVE 20.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIVE 20.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 11650000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"50000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "Gói MEIVE 50.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIVE 50.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 19950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"100000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "Gói MEIVE 100.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIVE 100.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 33950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"200000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "Gói MEIVE 200.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIVE 200.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 74950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"500000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "Gói MEIVE 500.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIVE 500.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 250000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"300\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "Gói MEIMTT-300",
        "ModuleName": None,
        "DisplayName": "Gói MEIMTT-300",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 350000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"500\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "Gói MEIMTT-500",
        "ModuleName": None,
        "DisplayName": "Gói MEIMTT-500",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 550000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"1000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "Gói MEIMTT-1.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIMTT-1.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 850000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"2000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "Gói MEIMTT-2.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIMTT-2.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"5000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "Gói MEIMTT-5.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIMTT-5.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3050000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"10000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "Gói MEIMTT-10.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIMTT-10.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 5650000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"20000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "Gói MEIMTT-20.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIMTT-20.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 11650000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"50000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "Gói MEIMTT-50.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIMTT-50.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 19950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"100000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "Gói MEIMTT-100.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIMTT-100.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 129950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"1000000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "Gói MEIVE 1.000.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIVE 1.000.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 390000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 300, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "Gói MEIX-300",
        "ModuleName": None,
        "DisplayName": "Gói MEIX-300",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 690000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 1000, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "Gói MEIX-1.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIX-1.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1190000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 2000, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "Gói MEIX-2.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIX-2.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2490000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 5000, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "Gói MEIX-5.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIX-5.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 4490000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 10000, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "Gói MEIX-10.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIX-10.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1550000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"2000\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "Gói MEIR 2.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIR 2.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3000000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Dữ liệu\", \"Unit\": \"Dữ liệu/Năm\", \"Value\": \"1\", \"DataType\": \"string\", \"ResourceID\": 92, \"ResourceCode\": \"ResourceQuantity\", \"ResourceName\": \"Dữ liệu\"}]",
        "ItemName": "Mua thêm dữ liệu",
        "ModuleName": None,
        "DisplayName": "Mua thêm dữ liệu",
        "ProductID": 406,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7990000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Value\": 20000, \"DataType\": \"number\", \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "Gói MEIX-20.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIX-20.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 17490000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Value\": 50000, \"DataType\": \"number\", \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "Gói MEIX-50.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIX-50.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 30990000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Value\": 100000, \"DataType\": \"number\", \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "Gói MEIX-100.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIX-100.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 4000000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn bán lẻ xăng dầu\", \"Value\": \"50000\", \"DataType\": \"string\", \"ResourceID\": 89, \"ResourceCode\": \"NumberOfPetrol\", \"ResourceName\": \"Hóa đơn bán lẻ xăng dầu\"}]",
        "ItemName": "Gói MEIXD-50.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIXD-50.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7000000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn bán lẻ xăng dầu\", \"Value\": \"100000\", \"DataType\": \"string\", \"ResourceID\": 89, \"ResourceCode\": \"NumberOfPetrol\", \"ResourceName\": \"Hóa đơn bán lẻ xăng dầu\"}]",
        "ItemName": "Gói MEIXD-100.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIXD-100.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 18000000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn bán lẻ xăng dầu\", \"Value\": \"300000\", \"DataType\": \"string\", \"ResourceID\": 89, \"ResourceCode\": \"NumberOfPetrol\", \"ResourceName\": \"Hóa đơn bán lẻ xăng dầu\"}]",
        "ItemName": "Gói MEIXD-300.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIXD-300.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 27500000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn bán lẻ xăng dầu\", \"Value\": \"500000\", \"DataType\": \"string\", \"ResourceID\": 89, \"ResourceCode\": \"NumberOfPetrol\", \"ResourceName\": \"Hóa đơn bán lẻ xăng dầu\"}]",
        "ItemName": "Gói MEIXD-500.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIXD-500.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 50000000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn bán lẻ xăng dầu\", \"Value\": \"1000000\", \"DataType\": \"string\", \"ResourceID\": 89, \"ResourceCode\": \"NumberOfPetrol\", \"ResourceName\": \"Hóa đơn bán lẻ xăng dầu\"}]",
        "ItemName": "Gói MEIXD-1.000.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIXD-1.000.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 126000000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn bán lẻ xăng dầu\", \"Value\": \"3000000\", \"DataType\": \"string\", \"ResourceID\": 89, \"ResourceCode\": \"NumberOfPetrol\", \"ResourceName\": \"Hóa đơn bán lẻ xăng dầu\"}]",
        "ItemName": "Gói MEIXD-3.000.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIXD-3.000.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 9150000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": 20000, \"DataType\": \"number\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "Gói MEIR 20.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIR 20.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 19150000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Value\": 50000, \"DataType\": \"number\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "Gói MEIR 50.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIR 50.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 60000000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Value\": 200000, \"DataType\": \"number\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "Gói MEIR 200.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIR 200.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 84000000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Value\": 300000, \"DataType\": \"number\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "Gói MEIR 300.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIR 300.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 125000000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Value\": 500000, \"DataType\": \"number\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "Gói MEIR 500.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIR 500.000",
        "ProductID": 406,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2950000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp Phần mềm Quản lý Tài chính kế toán doanh nghiệp - Gói Starter năm đầu tiên",
        "ModuleName": None,
        "DisplayName": "Starter",
        "ProductID": 406,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 4550000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp Phần mềm Quản lý Tài chính kế toán doanh nghiệp - Gói Standard năm đầu tiên",
        "ModuleName": None,
        "DisplayName": "Standard",
        "ProductID": 406,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 5750000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp Phần mềm Quản lý Tài chính kế toán doanh nghiệp - Gói Professional năm đầu tiên",
        "ModuleName": None,
        "DisplayName": "Professional",
        "ProductID": 406,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 6950000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp Phần mềm Quản lý Tài chính kế toán doanh nghiệp - Gói Enterprise năm đầu tiên",
        "ModuleName": None,
        "DisplayName": "Enterprise",
        "ProductID": 406,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 23000000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp Phần mềm Quản lý Tài chính kế toán doanh nghiệp - Gói Enterprise Plus năm đầu tiên",
        "ModuleName": None,
        "DisplayName": "Enterprise Plus",
        "ProductID": 406,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "QLTS",
    "AppName": "MISA Quản lý tài sản",
    "ProductID": 682,
    "MarketName": "Hành chính sự nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 4000000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Dịch vụ đào tạo trực tuyến cho riêng từng đơn vị",
        "ModuleName": None,
        "DisplayName": "Phần mềm Quản lý tài sản MISA QLTS - Dịch vụ đào tạo trực tuyến cho riêng từng đơn vị",
        "ProductID": 682,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 4000000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Dịch vụ tập huấn tập trung cho các đơn vị",
        "ModuleName": None,
        "DisplayName": "Phần mềm Quản lý tài sản MISA QLTS - Dịch vụ tập huấn tập trung cho các đơn vị",
        "ProductID": 682,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 8000000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Dịch vụ đào tạo trực tiếp cho riêng từng đơn vị",
        "ModuleName": None,
        "DisplayName": "Phần mềm Quản lý tài sản MISA QLTS - Dịch vụ đào tạo trực tiếp cho riêng từng đơn vị",
        "ProductID": 682,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2000000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Dịch vụ tập huấn trực tuyến tập trung cho các đơn vị",
        "ModuleName": None,
        "DisplayName": "Phần mềm Quản lý tài sản MISA QLTS - Dịch vụ tập huấn trực tuyến tập trung cho các đơn vị",
        "ProductID": 682,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3000000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}, {\"Name\": \"Đơn vị trực thuộc\", \"Value\": \"1\", \"DataType\": \"string\", \"ResourceID\": 100, \"ResourceCode\": \"DependentUnit\", \"ResourceName\": \"Đơn vị trực thuộc\"}, {\"Name\": \"Mã gói Suman\", \"Value\": \"QLTS.ORG\", \"DataType\": \"string\", \"ResourceID\": 94, \"ResourceCode\": \"SumanPackCode\", \"ResourceName\": \"Mã gói Suman\"}]",
        "ItemName": "Gói dành cho đơn vị trực thuộc",
        "ModuleName": "Đơn vị trực thuộc",
        "DisplayName": "Gói Đơn vị trực thuộc - năm đầu tiên",
        "ProductID": 682,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 6000000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}, {\"Name\": \"Đơn vị chủ quản\", \"Value\": \"1\", \"DataType\": \"string\", \"ResourceID\": 99, \"ResourceCode\": \"ManagingUnit\", \"ResourceName\": \"Đơn vị chủ quản\"}, {\"Name\": \"Mã gói Suman\", \"Value\": \"QLTS.SUP\", \"DataType\": \"string\", \"ResourceID\": 94, \"ResourceCode\": \"SumanPackCode\", \"ResourceName\": \"Mã gói Suman\"}]",
        "ItemName": "Gói dành cho đơn vị chủ quản",
        "ModuleName": "Đơn vị chủ quản",
        "DisplayName": "Gói Đơn vị chủ quản - năm đầu tiên",
        "ProductID": 682,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "SME",
    "AppName": "MISA SME 2023",
    "ProductID": 679,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 1550000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Số lượng người dùng\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 83, \"ResourceCode\": \"NumberOfUser\", \"ResourceName\": \"Số lượng người dùng\"}]",
        "ItemName": "Phần mềm MISA SME bản trả phí định kỳ - Mua thêm 01 người dùng gói Standard",
        "ModuleName": None,
        "DisplayName": "Mua thêm 01 người dùng gói Standard",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Số lượng người dùng\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 83, \"ResourceCode\": \"NumberOfUser\", \"ResourceName\": \"Số lượng người dùng\"}]",
        "ItemName": "Phần mềm MISA SME bản trả phí định kỳ - Mua thêm 01 người dùng gói Professional",
        "ModuleName": None,
        "DisplayName": "Mua thêm 01 người dùng gói Professional",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2350000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Số lượng người dùng\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 83, \"ResourceCode\": \"NumberOfUser\", \"ResourceName\": \"Số lượng người dùng\"}]",
        "ItemName": "Phần mềm MISA SME bản trả phí định kỳ - Mua thêm 01 người dùng gói Enterprise",
        "ModuleName": None,
        "DisplayName": "Mua thêm 01 người dùng gói Enterprise",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2650000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Số lượng người dùng\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 83, \"ResourceCode\": \"NumberOfUser\", \"ResourceName\": \"Số lượng người dùng\"}]",
        "ItemName": "Phần mềm MISA SME bản trả phí 1 lần - Mua thêm 01 người dùng gói Standard",
        "ModuleName": None,
        "DisplayName": "Mua thêm 01 người dùng gói Standard",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3650000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Số lượng người dùng\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 83, \"ResourceCode\": \"NumberOfUser\", \"ResourceName\": \"Số lượng người dùng\"}]",
        "ItemName": "Phần mềm MISA SME bản trả phí 1 lần - Mua thêm 01 người dùng gói Professional",
        "ModuleName": None,
        "DisplayName": "Mua thêm 01 người dùng gói Professional",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 4650000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Số lượng người dùng\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 83, \"ResourceCode\": \"NumberOfUser\", \"ResourceName\": \"Số lượng người dùng\"}]",
        "ItemName": "Phần mềm MISA SME bản trả phí 1 lần - Mua thêm 1 người dùng gói Enterprise",
        "ModuleName": None,
        "DisplayName": "Mua thêm 01 người dùng gói Enterprise",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Phần mềm MISA SME bản trả phí định kỳ - Đào tạo phần mềm gói 1 kèm 1 trực tuyến",
        "ModuleName": None,
        "DisplayName": "Đào tạo phần mềm gói 1 kèm 1 trực tuyến",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 0.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Phần mềm MISA SME bản trả phí định kỳ - Đào tạo phần mềm gói tập trung trực tuyến",
        "ModuleName": None,
        "DisplayName": "Đào tạo phần mềm gói tập trung trực tuyến",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 20000000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Phần mềm MISA SME bản trả phí định kỳ - Tư vấn triển khai phần mềm",
        "ModuleName": None,
        "DisplayName": "Tư vấn triển khai phần mềm",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 11950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Phần mềm MISA SME bản trả phí định kỳ - Đào tạo phần mềm gói 1 kèm 1 trực tiếp",
        "ModuleName": None,
        "DisplayName": "Đào tạo phần mềm gói 1 kèm 1 trực tiếp",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 11950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Phần mềm MISA SME bản trả phí 1 lần - Đào tạo phần mềm gói 1 kèm 1 trực tiếp",
        "ModuleName": None,
        "DisplayName": "Đào tạo phần mềm gói 1 kèm 1 trực tiếp",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Phần mềm MISA SME bản trả phí 1 lần - Đào tạo phần mềm 1 kèm 1 trực tuyến",
        "ModuleName": None,
        "DisplayName": "Đào tạo phần mềm 1 kèm 1 trực tuyến",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 0.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Phần mềm MISA SME bản trả phí 1 lần - Đào tạo phần mềm tập trung trực tuyến",
        "ModuleName": None,
        "DisplayName": "Đào tạo phần mềm tập trung trực tuyến",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 20000000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Phần mềm MISA SME bản trả phí 1 lần - Tư vấn triển khai phần mềm",
        "ModuleName": None,
        "DisplayName": "Tư vấn triển khai phần mềm",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 4650000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Logo\", \"Value\": \"\", \"DataType\": \"string\", \"ResourceID\": 87, \"ResourceCode\": \"Logo\", \"ResourceName\": \"Logo\"}, {\"Name\": \"Loại giấy phép\", \"Value\": 3, \"DataType\": \"number\", \"ResourceID\": 86, \"ResourceCode\": \"LicenseType\", \"ResourceName\": \"Loại giấy phép\"}, {\"Name\": \"Mã gói\", \"Value\": \"Standard\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Value\": \"Standard\", \"DataType\": \"string\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Dòng sản phẩm\", \"Value\": \"SME2023\", \"DataType\": \"string\", \"ResourceID\": 85, \"ResourceCode\": \"ProductLine\", \"ResourceName\": \"Dòng sản phẩm\"}, {\"Name\": \"Số lượng người dùng\", \"Value\": 3, \"DataType\": \"number\", \"ResourceID\": 83, \"ResourceCode\": \"NumberOfUser\", \"ResourceName\": \"Số lượng người dùng\"}, {\"Name\": \"Mã gói (SME, CukCuk)\", \"Value\": \"SME.STD\", \"DataType\": \"string\", \"ResourceID\": 88, \"ResourceCode\": \"ProductPackCode\", \"ResourceName\": \"Mã gói (SME, CukCuk)\"}, {\"Name\": \"Thời hạn theo năm\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Standard",
        "ModuleName": "Trả phí định kỳ",
        "DisplayName": "Gói Standard",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Logo\", \"Value\": \"\", \"DataType\": \"string\", \"ResourceID\": 87, \"ResourceCode\": \"Logo\", \"ResourceName\": \"Logo\"}, {\"Name\": \"Loại giấy phép\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 86, \"ResourceCode\": \"LicenseType\", \"ResourceName\": \"Loại giấy phép\"}, {\"Name\": \"Mã gói\", \"Value\": \"Standard\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Value\": \"Standard\", \"DataType\": \"string\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Dòng sản phẩm\", \"Value\": \"SME2023\", \"DataType\": \"string\", \"ResourceID\": 85, \"ResourceCode\": \"ProductLine\", \"ResourceName\": \"Dòng sản phẩm\"}, {\"Name\": \"Số lượng người dùng\", \"Value\": 3, \"DataType\": \"number\", \"ResourceID\": 83, \"ResourceCode\": \"NumberOfUser\", \"ResourceName\": \"Số lượng người dùng\"}, {\"Name\": \"Mã gói (SME, CukCuk)\", \"Value\": \"SME.STD\", \"DataType\": \"string\", \"ResourceID\": 88, \"ResourceCode\": \"ProductPackCode\", \"ResourceName\": \"Mã gói (SME, CukCuk)\"}, {\"Name\": \"Thời hạn theo năm\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Standard",
        "ModuleName": "Trả phí 1 lần",
        "DisplayName": "Gói Standard",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 5850000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Logo\", \"Value\": \"\", \"DataType\": \"string\", \"ResourceID\": 87, \"ResourceCode\": \"Logo\", \"ResourceName\": \"Logo\"}, {\"Name\": \"Loại giấy phép\", \"Value\": 3, \"DataType\": \"number\", \"ResourceID\": 86, \"ResourceCode\": \"LicenseType\", \"ResourceName\": \"Loại giấy phép\"}, {\"Name\": \"Mã gói\", \"Value\": \"Professional\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Value\": \"Professional\", \"DataType\": \"string\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Dòng sản phẩm\", \"Value\": \"SME2023\", \"DataType\": \"string\", \"ResourceID\": 85, \"ResourceCode\": \"ProductLine\", \"ResourceName\": \"Dòng sản phẩm\"}, {\"Name\": \"Số lượng người dùng\", \"Value\": 3, \"DataType\": \"number\", \"ResourceID\": 83, \"ResourceCode\": \"NumberOfUser\", \"ResourceName\": \"Số lượng người dùng\"}, {\"Name\": \"Mã gói (SME, CukCuk)\", \"Value\": \"SME.PRO\", \"DataType\": \"string\", \"ResourceID\": 88, \"ResourceCode\": \"ProductPackCode\", \"ResourceName\": \"Mã gói (SME, CukCuk)\"}, {\"Name\": \"Thời hạn theo năm\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Professional",
        "ModuleName": "Trả phí định kỳ",
        "DisplayName": "Gói Professional",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 10950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Logo\", \"Value\": \"\", \"DataType\": \"string\", \"ResourceID\": 87, \"ResourceCode\": \"Logo\", \"ResourceName\": \"Logo\"}, {\"Name\": \"Loại giấy phép\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 86, \"ResourceCode\": \"LicenseType\", \"ResourceName\": \"Loại giấy phép\"}, {\"Name\": \"Mã gói\", \"Value\": \"Professional\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Value\": \"Professional\", \"DataType\": \"string\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Dòng sản phẩm\", \"Value\": \"SME2023\", \"DataType\": \"string\", \"ResourceID\": 85, \"ResourceCode\": \"ProductLine\", \"ResourceName\": \"Dòng sản phẩm\"}, {\"Name\": \"Số lượng người dùng\", \"Value\": 3, \"DataType\": \"number\", \"ResourceID\": 83, \"ResourceCode\": \"NumberOfUser\", \"ResourceName\": \"Số lượng người dùng\"}, {\"Name\": \"Mã gói (SME, CukCuk)\", \"Value\": \"SME.PRO\", \"DataType\": \"string\", \"ResourceID\": 88, \"ResourceCode\": \"ProductPackCode\", \"ResourceName\": \"Mã gói (SME, CukCuk)\"}, {\"Name\": \"Thời hạn theo năm\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Professional",
        "ModuleName": "Trả phí 1 lần",
        "DisplayName": "Gói Professional",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7050000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Logo\", \"Value\": \"\", \"DataType\": \"string\", \"ResourceID\": 87, \"ResourceCode\": \"Logo\", \"ResourceName\": \"Logo\"}, {\"Name\": \"Loại giấy phép\", \"Value\": 3, \"DataType\": \"number\", \"ResourceID\": 86, \"ResourceCode\": \"LicenseType\", \"ResourceName\": \"Loại giấy phép\"}, {\"Name\": \"Mã gói\", \"Value\": \"Enterprise\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Value\": \"Enterprise\", \"DataType\": \"string\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Dòng sản phẩm\", \"Value\": \"SME2023\", \"DataType\": \"string\", \"ResourceID\": 85, \"ResourceCode\": \"ProductLine\", \"ResourceName\": \"Dòng sản phẩm\"}, {\"Name\": \"Số lượng người dùng\", \"Value\": 3, \"DataType\": \"number\", \"ResourceID\": 83, \"ResourceCode\": \"NumberOfUser\", \"ResourceName\": \"Số lượng người dùng\"}, {\"Name\": \"Mã gói (SME, CukCuk)\", \"Value\": \"SME.ENT\", \"DataType\": \"string\", \"ResourceID\": 88, \"ResourceCode\": \"ProductPackCode\", \"ResourceName\": \"Mã gói (SME, CukCuk)\"}, {\"Name\": \"Thời hạn theo năm\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Enterprise",
        "ModuleName": "Trả phí định kỳ",
        "DisplayName": "Gói Enterprise",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 13950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Logo\", \"Value\": \"\", \"DataType\": \"string\", \"ResourceID\": 87, \"ResourceCode\": \"Logo\", \"ResourceName\": \"Logo\"}, {\"Name\": \"Loại giấy phép\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 86, \"ResourceCode\": \"LicenseType\", \"ResourceName\": \"Loại giấy phép\"}, {\"Name\": \"Mã gói\", \"Value\": \"Enterprise\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Value\": \"Enterprise\", \"DataType\": \"string\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Dòng sản phẩm\", \"Value\": \"SME2023\", \"DataType\": \"string\", \"ResourceID\": 85, \"ResourceCode\": \"ProductLine\", \"ResourceName\": \"Dòng sản phẩm\"}, {\"Name\": \"Số lượng người dùng\", \"Value\": 3, \"DataType\": \"number\", \"ResourceID\": 83, \"ResourceCode\": \"NumberOfUser\", \"ResourceName\": \"Số lượng người dùng\"}, {\"Name\": \"Mã gói (SME, CukCuk)\", \"Value\": \"SME.ENT\", \"DataType\": \"string\", \"ResourceID\": 88, \"ResourceCode\": \"ProductPackCode\", \"ResourceName\": \"Mã gói (SME, CukCuk)\"}, {\"Name\": \"Thời hạn theo năm\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Enterprise",
        "ModuleName": "Trả phí 1 lần",
        "DisplayName": "Gói Enterprise",
        "ProductID": 679,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "Mshopkeeper",
    "AppName": "MISA eShop",
    "ProductID": 678,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 199000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Value\": \"MSHO.STT\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Số lượng chi nhánh\", \"Value\": \"1\", \"DataType\": \"string\", \"ResourceID\": 93, \"ResourceCode\": \"NumberOfBranch\", \"ResourceName\": \"Số lượng chi nhánh\"}]",
        "ItemName": "Mua thêm chi nhánh gói Starter",
        "ModuleName": None,
        "DisplayName": "Mua thêm chi nhánh gói Starter",
        "ProductID": 678,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 299000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Value\": \"MSHO.STD\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Số lượng chi nhánh\", \"Value\": \"1\", \"DataType\": \"string\", \"ResourceID\": 93, \"ResourceCode\": \"NumberOfBranch\", \"ResourceName\": \"Số lượng chi nhánh\"}]",
        "ItemName": "Mua thêm chi nhánh gói Standard",
        "ModuleName": None,
        "DisplayName": "Mua thêm chi nhánh gói Standard",
        "ProductID": 678,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 299000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Value\": \"MSHO.PRO\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Số lượng chi nhánh\", \"Value\": \"1\", \"DataType\": \"string\", \"ResourceID\": 93, \"ResourceCode\": \"NumberOfBranch\", \"ResourceName\": \"Số lượng chi nhánh\"}]",
        "ItemName": "Mua thêm chi nhánh gói Professional",
        "ModuleName": None,
        "DisplayName": "Mua thêm chi nhánh gói Professional",
        "ProductID": 678,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 299000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Value\": \"MSHO.ENT\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Số lượng chi nhánh\", \"Value\": \"1\", \"DataType\": \"string\", \"ResourceID\": 93, \"ResourceCode\": \"NumberOfBranch\", \"ResourceName\": \"Số lượng chi nhánh\"}]",
        "ItemName": "Mua thêm chi nhánh gói Enterprise",
        "ModuleName": None,
        "DisplayName": "Mua thêm chi nhánh gói Enterprise",
        "ProductID": 678,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Đào tạo trực tuyến 1 kèm 1 phần mềm MISA eShop",
        "ModuleName": None,
        "DisplayName": "Đào tạo trực tuyến 1 kèm 1 phần mềm MISA eShop",
        "ProductID": 678,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 0.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Đào tạo trực tuyến tập trung phần mềm MISA eShop",
        "ModuleName": None,
        "DisplayName": "Đào tạo trực tuyến tập trung phần mềm MISA eShop",
        "ProductID": 678,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 11950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Tư vấn triển khai phần mềm MISA eShop",
        "ModuleName": None,
        "DisplayName": "Tư vấn triển khai phần mềm MISA eShop",
        "ProductID": 678,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 11950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Tư vấn triển khai phần mềm MISA Lomas cho khách hàng eShop",
        "ModuleName": None,
        "DisplayName": "Tư vấn triển khai phần mềm MISA Lomas cho khách hàng eShop",
        "ProductID": 678,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Đào tạo trực tuyến 1 kèm 1 phần mềm MISA Lomas trên MISA eShop",
        "ModuleName": None,
        "DisplayName": "Đào tạo trực tuyến 1 kèm 1 phần mềm MISA Lomas trên MISA eShop",
        "ProductID": 678,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 0.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Đào tạo trực tuyến tập trung phần mềm MISA Lomas trên MISA eShop",
        "ModuleName": None,
        "DisplayName": "Đào tạo trực tuyến tập trung phần mềm MISA Lomas trên MISA eShop",
        "ProductID": 678,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 0.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Value\": \"MSHO.TRL\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Value\": \"Trial\", \"DataType\": \"string\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo ngày\", \"Value\": 15, \"DataType\": \"number\", \"ResourceID\": 23, \"ResourceCode\": \"DurationByDay\", \"ResourceName\": \"Thời hạn theo ngày\"}, {\"Name\": \"Số lượng chi nhánh\", \"Value\": \"1\", \"DataType\": \"string\", \"ResourceID\": 93, \"ResourceCode\": \"NumberOfBranch\", \"ResourceName\": \"Số lượng chi nhánh\"}]",
        "ItemName": "Dùng thử",
        "ModuleName": None,
        "DisplayName": "Gói dùng thử 15 ngày eShop",
        "ProductID": 678,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 199000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Value\": \"MSHO.STT\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Value\": \"Starter\", \"DataType\": \"string\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo tháng\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 22, \"ResourceCode\": \"DurationByMonth\", \"ResourceName\": \"Thời hạn theo tháng\"}, {\"Name\": \"Số lượng chi nhánh\", \"Value\": \"1\", \"DataType\": \"string\", \"ResourceID\": 93, \"ResourceCode\": \"NumberOfBranch\", \"ResourceName\": \"Số lượng chi nhánh\"}]",
        "ItemName": "Starter",
        "ModuleName": None,
        "DisplayName": "Starter",
        "ProductID": 678,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 299000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Value\": \"MSHO.STD\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Value\": \"Standard\", \"DataType\": \"string\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo tháng\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 22, \"ResourceCode\": \"DurationByMonth\", \"ResourceName\": \"Thời hạn theo tháng\"}, {\"Name\": \"Số lượng chi nhánh\", \"Value\": \"1\", \"DataType\": \"string\", \"ResourceID\": 93, \"ResourceCode\": \"NumberOfBranch\", \"ResourceName\": \"Số lượng chi nhánh\"}]",
        "ItemName": "Standard",
        "ModuleName": None,
        "DisplayName": "Standard",
        "ProductID": 678,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 499000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Value\": \"MSHO.PRO\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Value\": \"Professional\", \"DataType\": \"string\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo tháng\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 22, \"ResourceCode\": \"DurationByMonth\", \"ResourceName\": \"Thời hạn theo tháng\"}, {\"Name\": \"Số lượng chi nhánh\", \"Value\": \"1\", \"DataType\": \"string\", \"ResourceID\": 93, \"ResourceCode\": \"NumberOfBranch\", \"ResourceName\": \"Số lượng chi nhánh\"}]",
        "ItemName": "Professional",
        "ModuleName": None,
        "DisplayName": "Professional",
        "ProductID": 678,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 599000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Value\": \"MSHO.ENT\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Value\": \"Enterprise\", \"DataType\": \"string\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo tháng\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 22, \"ResourceCode\": \"DurationByMonth\", \"ResourceName\": \"Thời hạn theo tháng\"}, {\"Name\": \"Số lượng chi nhánh\", \"Value\": \"1\", \"DataType\": \"string\", \"ResourceID\": 93, \"ResourceCode\": \"NumberOfBranch\", \"ResourceName\": \"Số lượng chi nhánh\"}]",
        "ItemName": "Enterprise",
        "ModuleName": None,
        "DisplayName": "Enterprise",
        "ProductID": 678,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 399000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo tháng\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 22, \"ResourceCode\": \"DurationByMonth\", \"ResourceName\": \"Thời hạn theo tháng\"}, {\"Name\": \"Mã gói\", \"Value\": \"LOMAS\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Là gói lomas\", \"Value\": \"True\", \"DataType\": \"string\", \"ResourceID\": 96, \"ResourceCode\": \"IsLomas\", \"ResourceName\": \"Là gói lomas\"}]",
        "ItemName": "MISA Lomas",
        "ModuleName": None,
        "DisplayName": "Mua thêm MISA Lomas",
        "ProductID": 678,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "mTax",
    "AppName": "Thuế điện tử MISA mTax",
    "ProductID": 505,
    "MarketName": "Cá nhân",
    "ListPackageProduct": [
      {
        "ItemPrice": 1045000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Value\": \"mTax\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Value\": \"mTax\", \"DataType\": \"string\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "1 năm",
        "ModuleName": None,
        "DisplayName": "Gói 1 năm",
        "ProductID": 505,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1870000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Value\": \"mTax\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Value\": \"mTax\", \"DataType\": \"string\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Value\": 2, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "2 năm ",
        "ModuleName": None,
        "DisplayName": "Gói 2 năm",
        "ProductID": 505,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2585000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Value\": \"mTax\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Value\": \"mTax\", \"DataType\": \"string\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Value\": 3, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "3 năm",
        "ModuleName": None,
        "DisplayName": "Gói 3 năm",
        "ProductID": 505,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3960000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Value\": \"mTax\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Value\": \"mTax\", \"DataType\": \"string\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Value\": 5, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "5 năm",
        "ModuleName": None,
        "DisplayName": "Gói 5 năm",
        "ProductID": 505,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "Combo_eSign_DN",
    "AppName": "MISA eSign – Chữ ký số USB Token cho Doanh nghiệp",
    "ProductID": 675,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 1049000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Dịch vụ chữ ký số MISA eSign cho Cá nhân trong Tổ chức gói mua mới 1 năm đã bao gồm USB Token",
        "ModuleName": "Cá nhân trong tổ chức",
        "DisplayName": "1 năm",
        "ProductID": 675,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1829000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Dịch vụ chữ ký số MISA eSign cho Tổ chức gói mua mới 1 năm lần đầu đã bao gồm USB Token",
        "ModuleName": "Tổ chức",
        "DisplayName": "1 năm",
        "ProductID": 675,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1449000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Dịch vụ chữ ký số MISA eSign cho Cá nhân trong Tổ chức gói mua mới 2 năm đã bao gồm USB Token",
        "ModuleName": "Cá nhân trong tổ chức",
        "DisplayName": "2 năm",
        "ProductID": 675,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2729000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Dịch vụ chữ ký số MISA eSign cho Tổ chức gói mua mới 2 năm lần đầu đã bao gồm USB Token",
        "ModuleName": "Tổ chức",
        "DisplayName": "2 năm",
        "ProductID": 675,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1749000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Dịch vụ chữ ký số MISA eSign cho Cá nhân trong Tổ chức gói mua mới 3 năm đã bao gồm USB Token",
        "ModuleName": "Cá nhân trong tổ chức",
        "DisplayName": "3 năm",
        "ProductID": 675,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3529000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Dịch vụ chữ ký số MISA eSign cho Tổ chức gói mua mới 3 năm lần đầu đã bao gồm USB Token",
        "ModuleName": "Tổ chức",
        "DisplayName": "3 năm",
        "ProductID": 675,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2049000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Dịch vụ chữ ký số MISA eSign cho Cá nhân trong Tổ chức gói mua mới 4 năm đã bao gồm USB Token",
        "ModuleName": "Cá nhân trong tổ chức",
        "DisplayName": "4 năm",
        "ProductID": 675,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2349000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Dịch vụ chữ ký số MISA eSign cho Cá nhân trong Tổ chức mua mới 5 năm đã bao gồm USB Token",
        "ModuleName": "Cá nhân trong tổ chức",
        "DisplayName": "5 năm",
        "ProductID": 675,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 4329000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Dịch vụ chữ ký số MISA eSign cho Tổ chức gói mua mới 4 năm đã bao gồm USB Token",
        "ModuleName": "Tổ chức",
        "DisplayName": "4 năm",
        "ProductID": 675,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 5029000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Dịch vụ chữ ký số MISA eSign cho Tổ chức gói mua mới 5 năm đã bao gồm USB Token",
        "ModuleName": "Tổ chức",
        "DisplayName": "5 năm",
        "ProductID": 675,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "HRMCombo",
    "AppName": "Bộ giải pháp quản trị nguồn nhân lực",
    "ProductID": 491,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 7950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm Quản trị nguồn nhân lực MISA AMIS HRM - Đào tạo 1 kèm 1 trực tuyến gói Standard",
        "ModuleName": None,
        "DisplayName": "Đào tạo gói Standard",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 11950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm Quản trị nguồn nhân lực MISA AMIS HRM - Đào tạo 1 kèm 1 trực tiếp gói Standard",
        "ModuleName": None,
        "DisplayName": "Đào tạo gói Standard",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 20000000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm Quản trị nguồn nhân lực MISA AMIS HRM - Tư vấn triển khai gói Standard",
        "ModuleName": None,
        "DisplayName": "Tư vấn triển khai gói Standard",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm Quản trị nguồn nhân lực MISA AMIS HRM - Đào tạo 1 kèm 1 trực tuyến gói Professional",
        "ModuleName": None,
        "DisplayName": "Đào tạo gói Professional",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 11950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm Quản trị nguồn nhân lực MISA AMIS HRM - Đào tạo 1 kèm 1 trực tiếp gói Professsional",
        "ModuleName": None,
        "DisplayName": "Đào tạo gói Professsional",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 20000000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm Quản trị nguồn nhân lực MISA AMIS HRM - Tư vấn triển khai gói Professional",
        "ModuleName": None,
        "DisplayName": "Tư vấn triển khai gói Professional",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1400000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 người dùng AMIS Thông tin nhân sự",
        "ModuleName": None,
        "DisplayName": "AMIS Thông tin nhân sự - Mua thêm 10 người dùng",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1700000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 người dùng AMIS Chấm công",
        "ModuleName": None,
        "DisplayName": "AMIS Chấm công - Mua thêm 10 người dùng",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1700000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 người dùng AMIS Tiền lương",
        "ModuleName": None,
        "DisplayName": "AMIS Tiền lương - Mua thêm 10 người dùng",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 80000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 người dùng AMIS Thuế TNCN",
        "ModuleName": None,
        "DisplayName": "AMIS Thuế TNCN - Mua thêm 10 người dùng",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 80000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 người dùng AMIS BHXH",
        "ModuleName": None,
        "DisplayName": "AMIS BHXH - Mua thêm 10 người dùng",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 320000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 hồ sơ nhân viên AMIS Thông tin nhân sự",
        "ModuleName": None,
        "DisplayName": "AMIS Thông tin nhân sự - Mua thêm 10 hồ sơ nhân viên",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 380000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 hồ sơ nhân viên AMIS Chấm công",
        "ModuleName": None,
        "DisplayName": "AMIS Chấm công - Mua thêm 10 hồ sơ nhân viên",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 380000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 hồ sơ nhân viên AMIS Tiền lương",
        "ModuleName": None,
        "DisplayName": "AMIS Tiền lương - Mua thêm 10 hồ sơ nhân viên",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1400000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 người dùng AMIS Mục tiêu",
        "ModuleName": None,
        "DisplayName": "AMIS Mục tiêu - Mua thêm 10 người dùng",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1400000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 người dùng AMIS Đánh giá",
        "ModuleName": None,
        "DisplayName": "AMIS Đánh giá - Mua thêm 10 người dùng",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1400000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 10 người dùng AMIS Mạng xã hội",
        "ModuleName": None,
        "DisplayName": "AMIS Mạng xã hội - Mua thêm 10 người dùng",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 12600000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm Quản trị nguồn nhân lực MISA AMIS HRM - Gói Standard năm đầu tiên",
        "ModuleName": None,
        "DisplayName": "Standard",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 18000000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm Quản trị nguồn nhân lực MISA AMIS HRM - Gói Professional năm đầu tiên",
        "ModuleName": None,
        "DisplayName": "Professional",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 4200000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 10 người dùng gói Standard",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10 người dùng gói Standard",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 6000000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 10 người dùng gói Professional",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10 người dùng gói Professional",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 756000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 hồ sơ nhân viên",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10 hồ sơ nhân viên",
        "ProductID": 491,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "APU",
    "AppName": "AMIS Mua hàng",
    "ProductID": 477,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 4450000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 01 người dùng",
        "ModuleName": None,
        "DisplayName": "Mua thêm 01 người dùng",
        "ProductID": 477,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 8900000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 2, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"AMIS Mua hàng\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"AMIS Mua hàng\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "AMIS Mua hàng",
        "ModuleName": None,
        "DisplayName": "Phần mềm AMIS Mua hàng",
        "ProductID": 477,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "Recruitment",
    "AppName": "AMIS Tuyển dụng",
    "ProductID": 457,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 5400000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 nhân viên gói Enterprise Plus",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10 nhân viên gói Enterprise Plus",
        "ProductID": 457,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 4500000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 5, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 5, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Starter\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Starter\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Starter",
        "ModuleName": None,
        "DisplayName": "Stater",
        "ProductID": 457,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 8400000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Standard\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Standard\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Standard",
        "ModuleName": None,
        "DisplayName": "Standard",
        "ProductID": 457,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 15600000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 20, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 20, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Professional\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Professional\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Professional",
        "ModuleName": None,
        "DisplayName": "Professional",
        "ProductID": 457,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 21600000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Enterprise\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Enterprise\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Enterprise",
        "ModuleName": None,
        "DisplayName": "Enterprise",
        "ProductID": 457,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 33000000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 50, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 50, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Enterprise Plus\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Enterprise Plus\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Enterprise Plus",
        "ModuleName": None,
        "DisplayName": "Enterprise Plus",
        "ProductID": 457,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "Goal",
    "AppName": "AMIS Mục tiêu",
    "ProductID": 456,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 2300000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 người dùng",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10 người dùng",
        "ProductID": 456,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 6900000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"AMIS Mục tiêu\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"AMIS Mục tiêu\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "AMIS Mục tiêu",
        "ModuleName": None,
        "DisplayName": "Phần mềm AMIS Mục tiêu",
        "ProductID": 456,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "Review",
    "AppName": "AMIS Đánh giá",
    "ProductID": 455,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 2300000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 người dùng",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10 người dùng",
        "ProductID": 455,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 6900000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"AMIS Đánh giá\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"AMIS Đánh giá\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "AMIS Đánh giá",
        "ModuleName": None,
        "DisplayName": "Phần mềm AMIS Đánh giá",
        "ProductID": 455,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "MinTax",
    "AppName": "AMIS Thuế TNCN",
    "ProductID": 454,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 80000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 người dùng",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10 người dùng",
        "ProductID": 454,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 240000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"AMIS Thuế TNCN\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"AMIS Thuế TNCN\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "AMIS Thuế TNCN",
        "ModuleName": None,
        "DisplayName": "Phần mềm AMIS Thuế TNCN",
        "ProductID": 454,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "MISAIVAN",
    "AppName": "AMIS Bảo hiểm xã hội",
    "ProductID": 453,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 80000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 người dùng",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10 người dùng",
        "ProductID": 453,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 240000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"AMIS BHXH\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"AMIS BHXH\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "AMIS BHXH",
        "ModuleName": None,
        "DisplayName": "Phần mềm AMIS BHXH",
        "ProductID": 453,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "Payroll",
    "AppName": "AMIS Tiền lương",
    "ProductID": 451,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 380000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 hồ sơ nhân viên",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10 hồ sơ nhân viên",
        "ProductID": 451,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1700000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 người dùng",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10 người dùng",
        "ProductID": 451,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 5100000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"AMIS Tiền lương\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"AMIS Tiền lương\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "AMIS Tiền lương",
        "ModuleName": None,
        "DisplayName": "Phần mềm AMIS Tiền lương",
        "ProductID": 451,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "Timesheet",
    "AppName": "AMIS Chấm công",
    "ProductID": 450,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 380000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 hồ sơ nhân viên",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10 hồ sơ nhân viên",
        "ProductID": 450,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1700000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 người dùng",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10 người dùng",
        "ProductID": 450,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 5100000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"AMIS Chấm công\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"AMIS Chấm công\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "AMIS Chấm công",
        "ModuleName": None,
        "DisplayName": "Phần mềm AMIS Chấm công",
        "ProductID": 450,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "EmployeesProfile",
    "AppName": "AMIS Thông tin nhân sự",
    "ProductID": 449,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 320000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 hồ sơ nhân viên",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10 hồ sơ nhân viên",
        "ProductID": 449,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Gói đào tạo phần mềm 1 kèm 1 trực tuyến",
        "ModuleName": None,
        "DisplayName": "Gói đào tạo phần mềm",
        "ProductID": 449,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 11950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Gói đào tạo phần mềm 1 kèm 1 trực tiếp",
        "ModuleName": None,
        "DisplayName": "Gói đào tạo phần mềm",
        "ProductID": 449,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 20000000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Tư vấn triển khai phần mềm",
        "ModuleName": None,
        "DisplayName": "Tư vấn triển khai phần mềm",
        "ProductID": 449,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1400000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}]",
        "ItemName": "Mua thêm 10 người dùng",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10 người dùng",
        "ProductID": 449,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 4200000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nhân viên\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 14, \"ResourceCode\": \"Employee\", \"ResourceName\": \"Nhân viên\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"AMIS Thông tin nhân sự\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"AMIS Thông tin nhân sự\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "AMIS Thông tin nhân sự",
        "ModuleName": None,
        "DisplayName": "Phần mềm AMIS Thông tin nhân sự",
        "ProductID": 449,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "aimkt",
    "AppName": "AMIS aiMarketing",
    "ProductID": 448,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 250000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Email gửi tự động\", \"Unit\": None, \"Value\": 10000, \"ResourceID\": 9, \"ResourceCode\": \"Email\", \"ResourceName\": \"Email gửi tự động\"}]",
        "ItemName": "Mua thêm 10.000 email quảng cáo",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10.000 email quảng cáo",
        "ProductID": 448,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2900000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"CTA\", \"Unit\": None, \"Value\": 0, \"ResourceID\": 7, \"ResourceCode\": \"Cta\", \"ResourceName\": \"CTA\"}, {\"Name\": \"Form\", \"Unit\": None, \"Value\": 0, \"ResourceID\": 20, \"ResourceCode\": \"Form\", \"ResourceName\": \"Form\"}, {\"Name\": \"Landing page xuất bản\", \"Unit\": None, \"Value\": 0, \"ResourceID\": 8, \"ResourceCode\": \"Page\", \"ResourceName\": \"Landing page xuất bản\"}, {\"Name\": \"Email gửi tự động\", \"Unit\": None, \"Value\": 60000, \"ResourceID\": 9, \"ResourceCode\": \"Email\", \"ResourceName\": \"Email gửi tự động\"}, {\"Name\": \"Liên hệ lưu trữ\", \"Unit\": None, \"Value\": 10000, \"ResourceID\": 11, \"ResourceCode\": \"Contact\", \"ResourceName\": \"Liên hệ lưu trữ\"}, {\"Name\": \"Kịch bản tự động\", \"Unit\": None, \"Value\": 0, \"ResourceID\": 15, \"ResourceCode\": \"Workflows\", \"ResourceName\": \"Kịch bản tự động\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Email Marketing\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Email Marketing\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Email Marketing",
        "ModuleName": None,
        "DisplayName": "Email Marketing",
        "ProductID": 448,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 8900000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"CTA\", \"Unit\": None, \"Value\": -1, \"ResourceID\": 7, \"ResourceCode\": \"Cta\", \"ResourceName\": \"CTA\"}, {\"Name\": \"Form\", \"Unit\": None, \"Value\": -1, \"ResourceID\": 20, \"ResourceCode\": \"Form\", \"ResourceName\": \"Form\"}, {\"Name\": \"Landing page xuất bản\", \"Unit\": None, \"Value\": 20, \"ResourceID\": 8, \"ResourceCode\": \"Page\", \"ResourceName\": \"Landing page xuất bản\"}, {\"Name\": \"Email gửi tự động\", \"Unit\": None, \"Value\": 60000, \"ResourceID\": 9, \"ResourceCode\": \"Email\", \"ResourceName\": \"Email gửi tự động\"}, {\"Name\": \"Liên hệ lưu trữ\", \"Unit\": None, \"Value\": 10000, \"ResourceID\": 11, \"ResourceCode\": \"Contact\", \"ResourceName\": \"Liên hệ lưu trữ\"}, {\"Name\": \"Kịch bản tự động\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 15, \"ResourceCode\": \"Workflows\", \"ResourceName\": \"Kịch bản tự động\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Starter\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Starter\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Starter",
        "ModuleName": None,
        "DisplayName": "Starter",
        "ProductID": 448,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 15900000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"CTA\", \"Unit\": None, \"Value\": -1, \"ResourceID\": 7, \"ResourceCode\": \"Cta\", \"ResourceName\": \"CTA\"}, {\"Name\": \"Form\", \"Unit\": None, \"Value\": -1, \"ResourceID\": 20, \"ResourceCode\": \"Form\", \"ResourceName\": \"Form\"}, {\"Name\": \"Landing page xuất bản\", \"Unit\": None, \"Value\": 50, \"ResourceID\": 8, \"ResourceCode\": \"Page\", \"ResourceName\": \"Landing page xuất bản\"}, {\"Name\": \"Email gửi tự động\", \"Unit\": None, \"Value\": 200000, \"ResourceID\": 9, \"ResourceCode\": \"Email\", \"ResourceName\": \"Email gửi tự động\"}, {\"Name\": \"Liên hệ lưu trữ\", \"Unit\": None, \"Value\": 30000, \"ResourceID\": 11, \"ResourceCode\": \"Contact\", \"ResourceName\": \"Liên hệ lưu trữ\"}, {\"Name\": \"Kịch bản tự động\", \"Unit\": None, \"Value\": 25, \"ResourceID\": 15, \"ResourceCode\": \"Workflows\", \"ResourceName\": \"Kịch bản tự động\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Standard\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Standard\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Standard",
        "ModuleName": None,
        "DisplayName": "Standard",
        "ProductID": 448,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 31900000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"CTA\", \"Unit\": None, \"Value\": -1, \"ResourceID\": 7, \"ResourceCode\": \"Cta\", \"ResourceName\": \"CTA\"}, {\"Name\": \"Form\", \"Unit\": None, \"Value\": -1, \"ResourceID\": 20, \"ResourceCode\": \"Form\", \"ResourceName\": \"Form\"}, {\"Name\": \"Landing page xuất bản\", \"Unit\": None, \"Value\": -1, \"ResourceID\": 8, \"ResourceCode\": \"Page\", \"ResourceName\": \"Landing page xuất bản\"}, {\"Name\": \"Email gửi tự động\", \"Unit\": None, \"Value\": 800000, \"ResourceID\": 9, \"ResourceCode\": \"Email\", \"ResourceName\": \"Email gửi tự động\"}, {\"Name\": \"Liên hệ lưu trữ\", \"Unit\": None, \"Value\": 80000, \"ResourceID\": 11, \"ResourceCode\": \"Contact\", \"ResourceName\": \"Liên hệ lưu trữ\"}, {\"Name\": \"Kịch bản tự động\", \"Unit\": None, \"Value\": -1, \"ResourceID\": 15, \"ResourceCode\": \"Workflows\", \"ResourceName\": \"Kịch bản tự động\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Professional\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Professional\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Professional",
        "ModuleName": None,
        "DisplayName": "Professional",
        "ProductID": 448,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 63900000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"CTA\", \"Unit\": None, \"Value\": -1, \"ResourceID\": 7, \"ResourceCode\": \"Cta\", \"ResourceName\": \"CTA\"}, {\"Name\": \"Form\", \"Unit\": None, \"Value\": -1, \"ResourceID\": 20, \"ResourceCode\": \"Form\", \"ResourceName\": \"Form\"}, {\"Name\": \"Landing page xuất bản\", \"Unit\": None, \"Value\": -1, \"ResourceID\": 8, \"ResourceCode\": \"Page\", \"ResourceName\": \"Landing page xuất bản\"}, {\"Name\": \"Email gửi tự động\", \"Unit\": None, \"Value\": 2000000, \"ResourceID\": 9, \"ResourceCode\": \"Email\", \"ResourceName\": \"Email gửi tự động\"}, {\"Name\": \"Liên hệ lưu trữ\", \"Unit\": None, \"Value\": 200000, \"ResourceID\": 11, \"ResourceCode\": \"Contact\", \"ResourceName\": \"Liên hệ lưu trữ\"}, {\"Name\": \"Kịch bản tự động\", \"Unit\": None, \"Value\": -1, \"ResourceID\": 15, \"ResourceCode\": \"Workflows\", \"ResourceName\": \"Kịch bản tự động\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Enterprise\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Enterprise\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Enterprise",
        "ModuleName": None,
        "DisplayName": "Enterprise",
        "ProductID": 448,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 0.0,
        "ItemType": 1,
        "ResourceInfor": None,
        "ItemName": "Ultimate",
        "ModuleName": None,
        "DisplayName": "Ultimate",
        "ProductID": 448,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "Promotion",
    "AppName": "AMIS Khuyến mại",
    "ProductID": 447,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 1200000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 5, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 05 người dùng",
        "ModuleName": None,
        "DisplayName": "Mua thêm 05 người dùng",
        "ProductID": 447,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2400000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"AMIS Khuyến mại\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"AMIS Khuyến mại\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "AMIS Khuyến mại",
        "ModuleName": None,
        "DisplayName": "Phần mềm AMIS Khuyến mại",
        "ProductID": 447,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "CRM",
    "AppName": "AMIS Bán hàng",
    "ProductID": 446,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 4800000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 5, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 05 người dùng gói Standard",
        "ModuleName": None,
        "DisplayName": "Mua thêm 05 người dùng gói Standard",
        "ProductID": 446,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 6000000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 5, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 05 người dùng gói Professional",
        "ModuleName": None,
        "DisplayName": "Mua thêm 05 người dùng gói Professional",
        "ProductID": 446,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7200000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 5, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 05 người dùng gói Enterprise",
        "ModuleName": None,
        "DisplayName": "Mua thêm 05 người dùng gói Enterprise",
        "ProductID": 446,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 9600000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"CRM2.Standard\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Standard\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Standard",
        "ModuleName": None,
        "DisplayName": "Standard",
        "ProductID": 446,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 12000000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"CRM2.Professional\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Professional\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Professional",
        "ModuleName": None,
        "DisplayName": "Professional",
        "ProductID": 446,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 14400000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"CRM2.Enterprise\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Enterprise\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Enterprise",
        "ModuleName": None,
        "DisplayName": "Enterprise",
        "ProductID": 446,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "RemoteSigning",
    "AppName": "MISA eSign – Chữ ký số từ xa cho cá nhân",
    "ProductID": 427,
    "MarketName": "Cá nhân",
    "ListPackageProduct": [
      {
        "ItemPrice": 550000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "1 năm",
        "ModuleName": "Cá nhân",
        "DisplayName": "1 năm",
        "ProductID": 427,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 2, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "2 năm",
        "ModuleName": "Cá nhân",
        "DisplayName": "2 năm",
        "ProductID": 427,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1250000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 3, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "3 năm",
        "ModuleName": "Cá nhân",
        "DisplayName": "3 năm",
        "ProductID": 427,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1550000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 4, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "4 năm",
        "ModuleName": "Cá nhân",
        "DisplayName": "4 năm",
        "ProductID": 427,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1850000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 5, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "5 năm",
        "ModuleName": "Cá nhân",
        "DisplayName": "5 năm",
        "ProductID": 427,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "Meinvoice.vn",
    "AppName": "meInvoice Doanh nghiệp - Phát hành hóa đơn",
    "ProductID": 426,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 450000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"300\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "MEIR-300",
        "ModuleName": "Hóa đơn điện tử",
        "DisplayName": "MEIR-300",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3050000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"10000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "MEIVE-10.000",
        "ModuleName": "Vé điện tử",
        "DisplayName": "MEIVE-10.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 250000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"300\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIMTT-300",
        "ModuleName": "Hóa đơn từ máy tính tiền",
        "DisplayName": "MEIMTT-300",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 650000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"500\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "MEIR-500",
        "ModuleName": "Hóa đơn điện tử",
        "DisplayName": "MEIR-500",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 350000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"500\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIMTT-500",
        "ModuleName": "Hóa đơn từ máy tính tiền",
        "DisplayName": "MEIMTT-500",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 5650000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"20000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "MEIVE-20.000",
        "ModuleName": "Vé điện tử",
        "DisplayName": "MEIVE-20.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 4000000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn bán lẻ xăng dầu\", \"Value\": \"50000\", \"DataType\": \"string\", \"ResourceID\": 89, \"ResourceCode\": \"NumberOfPetrol\", \"ResourceName\": \"Hóa đơn bán lẻ xăng dầu\"}]",
        "ItemName": "MEIXD-50.000",
        "ModuleName": "Hóa đơn bán lẻ xăng dầu",
        "DisplayName": "MEIXD-50.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1050000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"1000\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "MEIR-1.000",
        "ModuleName": "Hóa đơn điện tử",
        "DisplayName": "MEIR-1.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 550000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"1000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIMTT-1.000",
        "ModuleName": "Hóa đơn từ máy tính tiền",
        "DisplayName": "MEIMTT-1000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 11650000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"50000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "MEIVE-50.000",
        "ModuleName": "Vé điện tử",
        "DisplayName": "MEIVE-50.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7000000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn bán lẻ xăng dầu\", \"Value\": \"100000\", \"DataType\": \"string\", \"ResourceID\": 89, \"ResourceCode\": \"NumberOfPetrol\", \"ResourceName\": \"Hóa đơn bán lẻ xăng dầu\"}]",
        "ItemName": "MEIXD-100.000",
        "ModuleName": "Hóa đơn bán lẻ xăng dầu",
        "DisplayName": "MEIXD-100.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 19950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"100000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "MEIVE-100.000",
        "ModuleName": "Vé điện tử",
        "DisplayName": "MEIVE-100.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 850000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"2000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIMTT-2.000",
        "ModuleName": "Hóa đơn từ máy tính tiền",
        "DisplayName": "MEIMTT-2000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1550000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"2000\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "MEIR-2.000",
        "ModuleName": "Hóa đơn điện tử",
        "DisplayName": "MEIR-2.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 18000000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn bán lẻ xăng dầu\", \"Value\": \"300000\", \"DataType\": \"string\", \"ResourceID\": 89, \"ResourceCode\": \"NumberOfPetrol\", \"ResourceName\": \"Hóa đơn bán lẻ xăng dầu\"}]",
        "ItemName": "MEIXD-300.000",
        "ModuleName": "Hóa đơn bán lẻ xăng dầu",
        "DisplayName": "MEIXD-300.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3150000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"5000\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "MEIR-5.000",
        "ModuleName": "Hóa đơn điện tử",
        "DisplayName": "MEIR-5.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 33950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"200000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "MEIVE-200.000",
        "ModuleName": "Vé điện tử",
        "DisplayName": "MEIVE-200.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"5000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIMTT-5.000",
        "ModuleName": "Hóa đơn từ máy tính tiền",
        "DisplayName": "MEIMTT-5000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 27500000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn bán lẻ xăng dầu\", \"Value\": \"500000\", \"DataType\": \"string\", \"ResourceID\": 89, \"ResourceCode\": \"NumberOfPetrol\", \"ResourceName\": \"Hóa đơn bán lẻ xăng dầu\"}]",
        "ItemName": "MEIXD-500.000",
        "ModuleName": "Hóa đơn bán lẻ xăng dầu",
        "DisplayName": "MEIXD-500.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 5250000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"10000\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "MEIR-10.000",
        "ModuleName": "Hóa đơn điện tử",
        "DisplayName": "MEIR-10.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 74950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"500000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "MEIVE-500.000",
        "ModuleName": "Vé điện tử",
        "DisplayName": "MEIVE-500.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3050000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"10000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIMTT-10.000",
        "ModuleName": "Hóa đơn từ máy tính tiền",
        "DisplayName": "MEIMTT-10.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 50000000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn bán lẻ xăng dầu\", \"Value\": \"1000000\", \"DataType\": \"string\", \"ResourceID\": 89, \"ResourceCode\": \"NumberOfPetrol\", \"ResourceName\": \"Hóa đơn bán lẻ xăng dầu\"}]",
        "ItemName": "MEIXD-1.000.000",
        "ModuleName": "Hóa đơn bán lẻ xăng dầu",
        "DisplayName": "MEIXD-1.000.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 5650000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"20000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIMTT-20.000",
        "ModuleName": "Hóa đơn từ máy tính tiền",
        "DisplayName": "MEIMTT-20000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 129950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"1000000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "MEIVE-1.000.000",
        "ModuleName": "Vé điện tử",
        "DisplayName": "MEIVE-1.000.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 126000000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn bán lẻ xăng dầu\", \"Value\": \"3000000\", \"DataType\": \"string\", \"ResourceID\": 89, \"ResourceCode\": \"NumberOfPetrol\", \"ResourceName\": \"Hóa đơn bán lẻ xăng dầu\"}]",
        "ItemName": "MEIXD-3.000.000",
        "ModuleName": "Hóa đơn bán lẻ xăng dầu",
        "DisplayName": "MEIXD-3.000.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 9150000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": 20000, \"DataType\": \"number\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "MEIR-20.000",
        "ModuleName": "Hóa đơn điện tử",
        "DisplayName": "MEIR-20.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 11650000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"50000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIMTT-50.000",
        "ModuleName": "Hóa đơn từ máy tính tiền",
        "DisplayName": "MEIMTT-50000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 19950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Value\": 50000, \"DataType\": \"number\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "MEIR-50.000",
        "ModuleName": "Hóa đơn điện tử",
        "DisplayName": "MEIR-50.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 32000000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"100000\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "MEIR-100.000",
        "ModuleName": "Hóa đơn điện tử",
        "DisplayName": "MEIR-100.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 19950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"100000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIMTT-100.000",
        "ModuleName": "Hóa đơn từ máy tính tiền",
        "DisplayName": "MEIMTT-100.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 60000000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Value\": 200000, \"DataType\": \"number\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "MEIR-200.000",
        "ModuleName": "Hóa đơn điện tử",
        "DisplayName": "MEIR-200.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 33950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Value\": 200000, \"DataType\": \"number\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIMTT-200.000",
        "ModuleName": "Hóa đơn từ máy tính tiền",
        "DisplayName": "MEIMTT-200.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 84000000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Value\": 300000, \"DataType\": \"number\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "MEIR-300.000",
        "ModuleName": "Hóa đơn điện tử",
        "DisplayName": "MEIR-300.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 74950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Value\": 500000, \"DataType\": \"number\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIMTT-500.000",
        "ModuleName": "Hóa đơn từ máy tính tiền",
        "DisplayName": "MEIMTT-500.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 125000000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Value\": 500000, \"DataType\": \"number\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "MEIR-500.000",
        "ModuleName": "Hóa đơn điện tử",
        "DisplayName": "MEIR-500.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 129950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Value\": 1000000, \"DataType\": \"number\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIMTT-1.000.000",
        "ModuleName": "Hóa đơn từ máy tính tiền",
        "DisplayName": "MEIMTT-1.000.000",
        "ProductID": 426,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 0.0,
        "ItemType": 1,
        "ResourceInfor": None,
        "ItemName": "MEIR-10.000+",
        "ModuleName": "Hóa đơn điện tử",
        "DisplayName": "MEIR-10.000+",
        "ProductID": 426,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "MeInbot",
    "AppName": "meInvoice Doanh nghiệp - Xử lý hóa đơn",
    "ProductID": 425,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 0.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 50, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}, {\"Name\": \"Thời hạn theo ngày\", \"Unit\": None, \"Value\": 5, \"ResourceID\": 23, \"ResourceCode\": \"DurationByDay\", \"ResourceName\": \"Thời hạn theo ngày\"}]",
        "ItemName": "Gói dùng thử",
        "ModuleName": "Xử lý hóa đơn",
        "DisplayName": "Gói dùng thử",
        "ProductID": 425,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 390000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 300, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "MEIX-300",
        "ModuleName": "Xử lý hóa đơn",
        "DisplayName": "MEIX-300",
        "ProductID": 425,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 690000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 1000, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "MEIX-1.000",
        "ModuleName": "Xử lý hóa đơn",
        "DisplayName": "MEIX-1.000",
        "ProductID": 425,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1190000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 2000, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "MEIX-2.000",
        "ModuleName": "Xử lý hóa đơn",
        "DisplayName": "MEIX-2.000",
        "ProductID": 425,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2490000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 5000, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "MEIX-5.000",
        "ModuleName": "Xử lý hóa đơn",
        "DisplayName": "MEIX-5.000",
        "ProductID": 425,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 4490000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 10000, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "MEIX-10.000",
        "ModuleName": "Xử lý hóa đơn",
        "DisplayName": "MEIX-10.000",
        "ProductID": 425,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7990000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Value\": 20000, \"DataType\": \"number\", \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "MEIX-20.000",
        "ModuleName": "Xử lý hóa đơn",
        "DisplayName": "MEIX-20.000",
        "ProductID": 425,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 17490000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Value\": 50000, \"DataType\": \"number\", \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "MEIX-50.000",
        "ModuleName": "Xử lý hóa đơn",
        "DisplayName": "MEIX-50.000",
        "ProductID": 425,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 30990000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Value\": 100000, \"DataType\": \"number\", \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "MEIX-100.000",
        "ModuleName": "Xử lý hóa đơn",
        "DisplayName": "MEIX-100.000",
        "ProductID": 425,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 500000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"MEIV\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"MeInbot\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Dịch vụ phần mềm",
        "ModuleName": "Xử lý hóa đơn",
        "DisplayName": "Dịch vụ phần mềm",
        "ProductID": 425,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "MeInbot",
    "AppName": "meInvoice Hộ kinh doanh - Xử lý hóa đơn",
    "ProductID": 424,
    "MarketName": "Hộ kinh doanh",
    "ListPackageProduct": [
      {
        "ItemPrice": 0.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 50, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}, {\"Name\": \"Thời hạn theo ngày\", \"Unit\": None, \"Value\": 5, \"ResourceID\": 23, \"ResourceCode\": \"DurationByDay\", \"ResourceName\": \"Thời hạn theo ngày\"}]",
        "ItemName": "Gói dùng thử",
        "ModuleName": "Xử lý hóa đơn",
        "DisplayName": "Gói dùng thử",
        "ProductID": 424,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 390000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 300, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "MEIXH-300",
        "ModuleName": "Xử lý hóa đơn",
        "DisplayName": "MEIXH-300",
        "ProductID": 424,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 690000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 1000, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "MEIXH-1.000",
        "ModuleName": "Xử lý hóa đơn",
        "DisplayName": "MEIXH-1.000",
        "ProductID": 424,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1190000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 2000, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "MEIXH-2.000",
        "ModuleName": "Xử lý hóa đơn",
        "DisplayName": "MEIXH-2.000",
        "ProductID": 424,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2490000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 5000, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "MEIXH-5.000",
        "ModuleName": "Xử lý hóa đơn",
        "DisplayName": "MEIXH-5.000",
        "ProductID": 424,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 4490000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": \"10000\", \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "MEIXH-10.000",
        "ModuleName": "Xử lý hóa đơn",
        "DisplayName": "MEIXH-10.000",
        "ProductID": 424,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 500000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"MEIXH\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"MeInbot\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Dịch vụ phần mềm",
        "ModuleName": "Xử lý hóa đơn",
        "DisplayName": "Dịch vụ phần mềm",
        "ProductID": 424,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "RemoteSigning",
    "AppName": "MISA eSign – Chữ ký số từ xa cho hộ kinh doanh",
    "ProductID": 423,
    "MarketName": "Hộ kinh doanh",
    "ListPackageProduct": [
      {
        "ItemPrice": 550000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "1 năm",
        "ModuleName": "Hộ, cá nhân kinh doanh",
        "DisplayName": "1 năm",
        "ProductID": 423,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 2, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "2 năm",
        "ModuleName": "Hộ, cá nhân kinh doanh",
        "DisplayName": "2 năm",
        "ProductID": 423,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1250000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 3, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "3 năm",
        "ModuleName": "Hộ, cá nhân kinh doanh",
        "DisplayName": "3 năm",
        "ProductID": 423,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1550000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 4, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "4 năm",
        "ModuleName": "Hộ, cá nhân kinh doanh",
        "DisplayName": "4 năm",
        "ProductID": 423,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1850000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 5, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "5 năm",
        "ModuleName": "Hộ, cá nhân kinh doanh",
        "DisplayName": "5 năm",
        "ProductID": 423,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "Meinvoice.vn",
    "AppName": "meInvoice Hộ Kinh doanh - Phát hành hóa đơn",
    "ProductID": 422,
    "MarketName": "Hộ kinh doanh",
    "ListPackageProduct": [
      {
        "ItemPrice": 3050000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"10000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "MEIHVE-10.000",
        "ModuleName": "Vé điện tử",
        "DisplayName": "MEIHVE-10.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 450000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"300\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "MEIH-300",
        "ModuleName": "Hóa đơn điện tử",
        "DisplayName": "MEIH-300",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 5650000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"20000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "MEIHVE-20.000",
        "ModuleName": "Vé điện tử",
        "DisplayName": "MEIHVE-20.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 250000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"300\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIHMTT-300",
        "ModuleName": "Hóa đơn điện tử từ máy tính tiền",
        "DisplayName": "MEIHMTT-300",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 650000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"500\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "MEIH-500",
        "ModuleName": "Hóa đơn điện tử",
        "DisplayName": "MEIH-500",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 11650000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"50000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "MEIHVE-50.000",
        "ModuleName": "Vé điện tử",
        "DisplayName": "MEIHVE-50.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 350000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"500\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIHMTT-500",
        "ModuleName": "Hóa đơn điện tử từ máy tính tiền",
        "DisplayName": "MEIHMTT-500",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1050000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"1000\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "MEIH-1.000",
        "ModuleName": "Hóa đơn điện tử",
        "DisplayName": "MEIH-1.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 19950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"100000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "MEIHVE-100.000",
        "ModuleName": "Vé điện tử",
        "DisplayName": "MEIHVE-100.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 550000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"1000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIHMTT-1.000",
        "ModuleName": "Hóa đơn điện tử từ máy tính tiền",
        "DisplayName": "MEIHMTT-1.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1550000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"2000\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "MEIH-2.000",
        "ModuleName": "Hóa đơn điện tử",
        "DisplayName": "MEIH-2.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 33950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"200000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "MEIHVE-200.000",
        "ModuleName": "Vé điện tử",
        "DisplayName": "MEIHVE-200.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 850000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"2000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIHMTT-2.000",
        "ModuleName": "Hóa đơn điện tử từ máy tính tiền",
        "DisplayName": "MEIHMTT-2.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3150000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"5000\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "MEIH-5.000",
        "ModuleName": "Hóa đơn điện tử",
        "DisplayName": "MEIH-5.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 74950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"500000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "MEIHVE-500.000",
        "ModuleName": "Vé điện tử",
        "DisplayName": "MEIHVE-500.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"5000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIHMTT-5.000",
        "ModuleName": "Hóa đơn điện tử từ máy tính tiền",
        "DisplayName": "MEIHMTT-5.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 5250000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"10000\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "MEIH-10.000",
        "ModuleName": "Hóa đơn điện tử",
        "DisplayName": "MEIH-10.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 129950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"1000000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "MEIHVE-1.000.000",
        "ModuleName": "Vé điện tử",
        "DisplayName": "MEIHVE-1.000.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3050000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"10000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIHMTT-10.000",
        "ModuleName": "Hóa đơn điện tử từ máy tính tiền",
        "DisplayName": "MEIHMTT-10.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 5650000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"20000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIHMTT-20.000",
        "ModuleName": "Hóa đơn điện tử từ máy tính tiền",
        "DisplayName": "MEIHMTT-20.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 11650000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"50000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIHMTT-50.000",
        "ModuleName": "Hóa đơn điện tử từ máy tính tiền",
        "DisplayName": "MEIHMTT-50.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 19950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"100000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIHMTT-100.000",
        "ModuleName": "Hóa đơn điện tử từ máy tính tiền",
        "DisplayName": "MEIHMTT-100.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 33950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Value\": 200000, \"DataType\": \"number\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIHMTT-200.000",
        "ModuleName": "Hóa đơn điện tử từ máy tính tiền",
        "DisplayName": "MEIMTT-200.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 74950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Value\": 500000, \"DataType\": \"number\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIHMTT-500.000",
        "ModuleName": "Hóa đơn điện tử từ máy tính tiền",
        "DisplayName": "MEIMTT-500.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 129950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Value\": 1000000, \"DataType\": \"number\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "MEIHMTT-1.000.000",
        "ModuleName": "Hóa đơn điện tử từ máy tính tiền",
        "DisplayName": "MEIMTT-1.000.000",
        "ProductID": 422,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "ComboKT_HKD",
    "AppName": "Bộ giải pháp tài chính kế toán hộ kinh doanh",
    "ProductID": 420,
    "MarketName": "Hộ kinh doanh",
    "ListPackageProduct": [
      {
        "ItemPrice": 800000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 01 người dùng",
        "ModuleName": None,
        "DisplayName": "Mua thêm 01 người dùng",
        "ProductID": 420,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 450000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"300\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "Gói MEIH-300",
        "ModuleName": None,
        "DisplayName": "Gói MEIH-300",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 650000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"500\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "Gói MEIH-500",
        "ModuleName": None,
        "DisplayName": "Gói MEIH-500",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1050000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"1000\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "Gói MEIH-1.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIH-1.000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1550000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"2000\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "Gói MEIH-2.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIH-2.000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3150000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"5000\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "Gói MEIH-5.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIH-5.000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 5250000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử đầu ra\", \"Unit\": None, \"Value\": \"10000\", \"ResourceID\": 18, \"ResourceCode\": \"NumberOfInvoice\", \"ResourceName\": \"Hóa đơn điện tử đầu ra\"}]",
        "ItemName": "Gói MEIH-10.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIH-10.000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3500000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"10000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "Gói MEIHVE-10.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIHVE-10.000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 5650000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"20000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "Gói MEIHVE-20.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIHVE-20.000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 11650000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"50000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "Gói MEIHVE-50.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIHVE-50.000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 19950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"100000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "Gói MEIHVE-100.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIHVE-100.000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 33950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"200000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "Gói MEIHVE-200.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIHVE-200.000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 74950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"500000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "Gói MEIHVE-500.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIHVE-500.000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 129950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Vé điện tử\", \"Unit\": None, \"Value\": \"1000000\", \"ResourceID\": 17, \"ResourceCode\": \"NumberOfTicket\", \"ResourceName\": \"Vé điện tử\"}]",
        "ItemName": "Gói MEIHVE-1.000.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIHVE-1.000.000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 250000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"300\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "Gói MEIHMTT-300",
        "ModuleName": None,
        "DisplayName": "Gói MEIHMTT-300",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 350000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"500\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "Gói MEIHMTT-500",
        "ModuleName": None,
        "DisplayName": "Gói MEIHMTT-500",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 550000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"1000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "Gói MEIHMTT-1.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIHMTT-1.000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 850000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"2000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "Gói MEIHMTT-2.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIHMTT-2.000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"5000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "Gói MEIHMTT-5.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIHMTT-5.000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3050000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"10000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "Gói MEIHMTT-10.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIHMTT-10.000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 5650000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"20000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "Gói MEIHMTT-20.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIHMTT-20.000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 11650000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"50000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "Gói MEIHMTT-50.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIHMTT-50.000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 19950000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn điện tử từ máy tính tiền\", \"Unit\": None, \"Value\": \"100000\", \"ResourceID\": 19, \"ResourceCode\": \"NumberOfCashRegister\", \"ResourceName\": \"Hóa đơn điện tử từ máy tính tiền\"}]",
        "ItemName": "Gói MEIHMTT-100.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIHMTT-100.000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 390000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 300, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "Gói MEIXH 300",
        "ModuleName": None,
        "DisplayName": "Gói MEIXH 300",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 690000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 1000, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "Gói MEIXH 1.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIXH 1000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1190000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 2000, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "Gói MEIXH 2.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIXH 2000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2490000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": 5000, \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "Gói MEIXH 5.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIXH 5000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 4490000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Hóa đơn đầu vào\", \"Unit\": None, \"Value\": \"10000\", \"ResourceID\": 12, \"ResourceCode\": \"Capacity\", \"ResourceName\": \"Hóa đơn đầu vào\"}]",
        "ItemName": "Gói MEIXH-10.000",
        "ModuleName": None,
        "DisplayName": "Gói MEIXH-10.000",
        "ProductID": 420,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2400000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp Quản lý Tài chính kế toán Hộ kinh doanh - Gói Cơ bản năm đầu tiên",
        "ModuleName": "Combo_KT_HKD",
        "DisplayName": "Cơ bản",
        "ProductID": 420,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3200000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp Quản lý Tài chính kế toán Hộ kinh doanh - Gói Toàn diện năm đầu tiên",
        "ModuleName": "Combo_KT_HKD",
        "DisplayName": "Toàn diện",
        "ProductID": 420,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3800000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp Quản lý Tài chính kế toán Hộ kinh doanh - Gói Nâng cao năm đầu tiên",
        "ModuleName": "Combo_KT_HKD",
        "DisplayName": "Nâng cao",
        "ProductID": 420,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "VPS",
    "AppName": "Văn phòng số",
    "ProductID": 419,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 1056000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 10 người dùng - AMIS Ghi chép",
        "ModuleName": None,
        "DisplayName": "AMIS Ghi chép - Mua thêm 10 người dùng",
        "ProductID": 419,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 960000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 10 người dùng - AMIS Mạng xã hội",
        "ModuleName": None,
        "DisplayName": "AMIS Mạng xã hội - Mua thêm 10 người dùng",
        "ProductID": 419,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2000000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 01 người dùng - AMIS Tài sản",
        "ModuleName": None,
        "DisplayName": "AMIS Tài sản - Mua thêm 01 người dùng",
        "ProductID": 419,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1000000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 5, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 05 người dùng - AMIS Văn thư",
        "ModuleName": None,
        "DisplayName": "AMIS Văn thư - Mua thêm 05 người dùng",
        "ProductID": 419,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 408000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Phòng họp\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 16, \"ResourceCode\": \"BookingRoom\", \"ResourceName\": \"Phòng họp\"}]",
        "ItemName": "Mua thêm 01 phòng họp - AMIS Phòng họp",
        "ModuleName": None,
        "DisplayName": "AMIS Phòng họp - Mua thêm 01 phòng họp",
        "ProductID": 419,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Đào tạo 1 kèm 1 trực tuyến gói Standard",
        "ModuleName": None,
        "DisplayName": "Gói đào tạo 1-1 trực tuyến Standard",
        "ProductID": 419,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 11950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Đào tạo 1 kèm 1 trực tiếp gói Standard",
        "ModuleName": None,
        "DisplayName": "Gói đào tạo gói Standard",
        "ProductID": 419,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 20000000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Tư vấn, triển khai gói Standard",
        "ModuleName": None,
        "DisplayName": "Gói tư vấn, triển khai gói Standard",
        "ProductID": 419,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2880000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 10 người dùng gói Premium - AMIS Công việc",
        "ModuleName": None,
        "DisplayName": "AMIS Công việc - Mua thêm 10 người dùng",
        "ProductID": 419,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3600000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 10 người dùng gói Premium - AMIS Quy trình",
        "ModuleName": None,
        "DisplayName": "AMIS Quy trình - Mua thêm 10 người dùng",
        "ProductID": 419,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1100.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Tin nhắn SMS\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 6, \"ResourceCode\": \"SMS\", \"ResourceName\": \"Tin nhắn SMS\"}]",
        "ItemName": "Mua thêm tin nhắn SMS",
        "ModuleName": None,
        "DisplayName": "Mua thêm tin nhắn SMS",
        "ProductID": 419,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1560000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Tài liệu ký\", \"Unit\": None, \"Value\": 200, \"ResourceID\": 13, \"ResourceCode\": \"Document\", \"ResourceName\": \"Tài liệu ký\"}]",
        "ItemName": "WeS-200",
        "ModuleName": None,
        "DisplayName": "WeS-200",
        "ProductID": 419,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3640000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Tài liệu ký\", \"Unit\": None, \"Value\": 500, \"ResourceID\": 13, \"ResourceCode\": \"Document\", \"ResourceName\": \"Tài liệu ký\"}]",
        "ItemName": "WeS-500",
        "ModuleName": None,
        "DisplayName": "WeS-500",
        "ProductID": 419,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7160000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Tài liệu ký\", \"Unit\": None, \"Value\": 1000, \"ResourceID\": 13, \"ResourceCode\": \"Document\", \"ResourceName\": \"Tài liệu ký\"}]",
        "ItemName": "WeS-1.000",
        "ModuleName": None,
        "DisplayName": "WeS-1.000",
        "ProductID": 419,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 18840000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Tài liệu ký\", \"Unit\": None, \"Value\": 3000, \"ResourceID\": 13, \"ResourceCode\": \"Document\", \"ResourceName\": \"Tài liệu ký\"}]",
        "ItemName": "WeS-3.000",
        "ModuleName": None,
        "DisplayName": "WeS-3.000",
        "ProductID": 419,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 26040000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Tài liệu ký\", \"Unit\": None, \"Value\": 5000, \"ResourceID\": 13, \"ResourceCode\": \"Document\", \"ResourceName\": \"Tài liệu ký\"}]",
        "ItemName": "WeS-5.000",
        "ModuleName": None,
        "DisplayName": "WeS-5.000",
        "ProductID": 419,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 43640000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Tài liệu ký\", \"Unit\": None, \"Value\": \"10000\", \"ResourceID\": 13, \"ResourceCode\": \"Document\", \"ResourceName\": \"Tài liệu ký\"}]",
        "ItemName": "WeS-10.000",
        "ModuleName": None,
        "DisplayName": "WeS-10.000",
        "ProductID": 419,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 399200.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Lượt chứng thực B2B\", \"Unit\": \"lượt\", \"Value\": 100, \"ResourceID\": 44, \"ResourceCode\": \"EVerifyContractB2B\", \"ResourceName\": \"Lượt chứng thực B2B\"}]",
        "ItemName": "Gói chứng thực hợp đồng điện tử B2B100",
        "ModuleName": None,
        "DisplayName": "B2B - Gói 100 lượt chứng thực hợp đồng điện tử",
        "ProductID": 419,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 239200.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Lượt chứng thực B2C\", \"Unit\": \"lượt\", \"Value\": 100, \"ResourceID\": 45, \"ResourceCode\": \"EVerifyContractB2C\", \"ResourceName\": \"Lượt chứng thực B2C\"}]",
        "ItemName": "Gói chứng thực hợp đồng điện tử B2C100",
        "ModuleName": None,
        "DisplayName": "B2C - Gói 100 lượt chứng thực hợp đồng điện tử",
        "ProductID": 419,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 800000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Lượt ký xác thực bằng eKYC\", \"Unit\": \"lượt\", \"Value\": 300, \"ResourceID\": 56, \"ResourceCode\": \"EKYCContract\", \"ResourceName\": \"Lượt ký xác thực bằng eKYC\"}]",
        "ItemName": "Gói mua thêm 300 lượt xác thực người ký bằng eKYC",
        "ModuleName": None,
        "DisplayName": "Gói mua thêm 300 lượt xác thực người ký bằng eKYC",
        "ProductID": 419,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Đào tạo 1 kèm 1 trực tuyến gói Professional",
        "ModuleName": None,
        "DisplayName": "Gói đào tạo gói Professional",
        "ProductID": 419,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 11950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Đào tạo 1 kèm 1 trực tiếp gói Professional",
        "ModuleName": None,
        "DisplayName": "Gói đào tạo gói Professional",
        "ProductID": 419,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 20000000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Tư vấn, triển khai gói Professional",
        "ModuleName": None,
        "DisplayName": "Gói tư vấn, triển khai gói Professional",
        "ProductID": 419,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7950000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Đào tạo 1 kèm 1 trực tuyến gói Enterprise",
        "ModuleName": None,
        "DisplayName": "Gói đào tạo gói Enterprise",
        "ProductID": 419,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 20000000.0,
        "ItemType": 3,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Tư vấn, triển khai gói Enterprise",
        "ModuleName": None,
        "DisplayName": "Gói tư vấn, triển khai gói Enterprise",
        "ProductID": 419,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 0.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Gói Starter",
        "ModuleName": "VPS",
        "DisplayName": "Gói Starter",
        "ProductID": 419,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 18800000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Gói Standard năm đầu tiên",
        "ModuleName": "VPS",
        "DisplayName": "Gói Standard",
        "ProductID": 419,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 32112000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Gói Professional năm đầu tiên",
        "ModuleName": "VPS",
        "DisplayName": "Gói Professional",
        "ProductID": 419,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 39112000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Gói Enteprise năm đầu tiên",
        "ModuleName": "VPS",
        "DisplayName": "Gói Enterprise",
        "ProductID": 419,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "RemoteSigning",
    "AppName": "MISA eSign – Chữ ký số từ xa cho doanh nghiệp",
    "ProductID": 418,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 3900000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Value\": 1, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}, {\"Name\": \"Mã gói\", \"Value\": \"05\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}]",
        "ItemName": "1 năm",
        "ModuleName": "Tổ chức - Gói nâng cao",
        "DisplayName": "1 năm",
        "ProductID": 418,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 5900000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Value\": 2, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}, {\"Name\": \"Mã gói\", \"Value\": \"05\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}]",
        "ItemName": "2 năm",
        "ModuleName": "Tổ chức - Gói nâng cao",
        "DisplayName": "2 năm",
        "ProductID": 418,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7900000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Value\": 3, \"DataType\": \"number\", \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}, {\"Name\": \"Mã gói\", \"Value\": \"05\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}]",
        "ItemName": "3 năm",
        "ModuleName": "Tổ chức - Gói nâng cao",
        "DisplayName": "3 năm",
        "ProductID": 418,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1350000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "1 năm",
        "ModuleName": "Tổ chức - Gói cơ bản",
        "DisplayName": "1 năm",
        "ProductID": 418,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2250000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 2, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "2 năm",
        "ModuleName": "Tổ chức - Gói cơ bản",
        "DisplayName": "2 năm",
        "ProductID": 418,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3050000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 3, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "3 năm",
        "ModuleName": "Tổ chức - Gói cơ bản",
        "DisplayName": "3 năm",
        "ProductID": 418,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3850000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 4, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "4 năm",
        "ModuleName": "Tổ chức - Gói cơ bản",
        "DisplayName": "4 năm",
        "ProductID": 418,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 4550000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 5, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "5 năm",
        "ModuleName": "Tổ chức - Gói cơ bản",
        "DisplayName": "5 năm",
        "ProductID": 418,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 550000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "1 năm",
        "ModuleName": "Cá nhân trong Tổ chức",
        "DisplayName": "1 năm",
        "ProductID": 418,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 2, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "2 năm",
        "ModuleName": "Cá nhân trong Tổ chức",
        "DisplayName": "2 năm",
        "ProductID": 418,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1250000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 3, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "3 năm",
        "ModuleName": "Cá nhân trong Tổ chức",
        "DisplayName": "3 năm",
        "ProductID": 418,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1550000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 4, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "4 năm",
        "ModuleName": "Cá nhân trong Tổ chức",
        "DisplayName": "4 năm",
        "ProductID": 418,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1850000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 5, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "5 năm",
        "ModuleName": "Cá nhân trong Tổ chức",
        "DisplayName": "5 năm",
        "ProductID": 418,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "AMS",
    "AppName": "AMIS Quản lý tài sản",
    "ProductID": 417,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 3500000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 1 người dùng",
        "ModuleName": None,
        "DisplayName": "Mua thêm 1 người dùng",
        "ProductID": 417,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 7000000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 2, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"AMIS Tài sản\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"AMIS Tài sản\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "AMIS Tài sản",
        "ModuleName": None,
        "DisplayName": "AMIS Tài sản",
        "ProductID": 417,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "BookingRoom",
    "AppName": "Quản lý phòng họp",
    "ProductID": 416,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 700000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Phòng họp\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 16, \"ResourceCode\": \"BookingRoom\", \"ResourceName\": \"Phòng họp\"}]",
        "ItemName": "Mua thêm 1 phòng họp",
        "ModuleName": None,
        "DisplayName": "Mua thêm 1 phòng họp",
        "ProductID": 416,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3500000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Phòng họp\", \"Unit\": None, \"Value\": 5, \"ResourceID\": 16, \"ResourceCode\": \"BookingRoom\", \"ResourceName\": \"Phòng họp\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"AMIS Phòng họp\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"AMIS Phòng họp\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "AMIS Phòng họp",
        "ModuleName": None,
        "DisplayName": "AMIS Phòng họp",
        "ProductID": 416,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "Dispatch",
    "AppName": "AMIS Văn thư",
    "ProductID": 415,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 1500000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 5, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 05 người dùng",
        "ModuleName": None,
        "DisplayName": "Mua thêm 05 người dùng",
        "ProductID": 415,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3000000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"AMIS Văn thư\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"AMIS Văn thư\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "AMIS Văn thư",
        "ModuleName": None,
        "DisplayName": "AMIS Văn thư",
        "ProductID": 415,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "Newsfeed",
    "AppName": "Mạng xã hội doanh nghiệp",
    "ProductID": 414,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 1300000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 10 người dùng",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10 người dùng",
        "ProductID": 414,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 3900000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"AMIS Mạng xã hội\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"AMIS Mạng xã hội\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "AMIS Mạng xã hội",
        "ModuleName": None,
        "DisplayName": "AMIS Mạng xã hội",
        "ProductID": 414,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "Document",
    "AppName": "Ghi chép và lưu trữ tài liệu",
    "ProductID": 413,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 1500000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 10 người dùng",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10 người dùng",
        "ProductID": 413,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 4500000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"AMIS Ghi chép\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"AMIS Ghi chép\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "AMIS Ghi chép",
        "ModuleName": None,
        "DisplayName": "AMIS Ghi chép",
        "ProductID": 413,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "Wesign",
    "AppName": "Nền tảng ký tài liệu số",
    "ProductID": 411,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 1100.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Tin nhắn SMS\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 6, \"ResourceCode\": \"SMS\", \"ResourceName\": \"Tin nhắn SMS\"}]",
        "ItemName": "Mua thêm tin nhắn SMS",
        "ModuleName": None,
        "DisplayName": "Mua thêm tin nhắn SMS",
        "ProductID": 411,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 499000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Lượt chứng thực B2B\", \"Unit\": \"lượt\", \"Value\": 100, \"ResourceID\": 44, \"ResourceCode\": \"EVerifyContractB2B\", \"ResourceName\": \"Lượt chứng thực B2B\"}]",
        "ItemName": "Gói chứng thực hợp đồng điện tử B2B100",
        "ModuleName": None,
        "DisplayName": "Gói chứng thực hợp đồng điện tử B2B100",
        "ProductID": 411,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 299000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Lượt chứng thực B2C\", \"Unit\": \"lượt\", \"Value\": 100, \"ResourceID\": 45, \"ResourceCode\": \"EVerifyContractB2C\", \"ResourceName\": \"Lượt chứng thực B2C\"}]",
        "ItemName": "Gói chứng thực hợp đồng điện tử B2C100",
        "ModuleName": None,
        "DisplayName": "Gói chứng thực hợp đồng điện tử B2C100",
        "ProductID": 411,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1000000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Lượt ký xác thực bằng eKYC\", \"Unit\": \"lượt\", \"Value\": 300, \"ResourceID\": 56, \"ResourceCode\": \"EKYCContract\", \"ResourceName\": \"Lượt ký xác thực bằng eKYC\"}]",
        "ItemName": "Gói mua thêm 300 lượt xác thực người ký bằng eKYC",
        "ModuleName": None,
        "DisplayName": "Gói mua thêm 300 lượt xác thực người ký bằng eKYC",
        "ProductID": 411,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 0.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Tài liệu ký\", \"Unit\": None, \"Value\": 30, \"ResourceID\": 13, \"ResourceCode\": \"Document\", \"ResourceName\": \"Tài liệu ký\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Free\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Free\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Free",
        "ModuleName": None,
        "DisplayName": "Free",
        "ProductID": 411,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1000000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"WeSign\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"WeSign\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Dịch vụ phần mềm",
        "ModuleName": None,
        "DisplayName": "Dịch vụ phần mềm",
        "ProductID": 411,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Tài liệu ký\", \"Unit\": None, \"Value\": 200, \"ResourceID\": 13, \"ResourceCode\": \"Document\", \"ResourceName\": \"Tài liệu ký\"}]",
        "ItemName": "WeS-200",
        "ModuleName": None,
        "DisplayName": "WeS-200",
        "ProductID": 411,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 4550000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Tài liệu ký\", \"Unit\": None, \"Value\": 500, \"ResourceID\": 13, \"ResourceCode\": \"Document\", \"ResourceName\": \"Tài liệu ký\"}]",
        "ItemName": "WeS-500",
        "ModuleName": None,
        "DisplayName": "WeS-500",
        "ProductID": 411,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 8950000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Tài liệu ký\", \"Unit\": None, \"Value\": 1000, \"ResourceID\": 13, \"ResourceCode\": \"Document\", \"ResourceName\": \"Tài liệu ký\"}]",
        "ItemName": "WeS-1.000",
        "ModuleName": None,
        "DisplayName": "WeS-1.000",
        "ProductID": 411,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 23550000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Tài liệu ký\", \"Unit\": None, \"Value\": 3000, \"ResourceID\": 13, \"ResourceCode\": \"Document\", \"ResourceName\": \"Tài liệu ký\"}]",
        "ItemName": "WeS-3.000",
        "ModuleName": None,
        "DisplayName": "WeS-3.000",
        "ProductID": 411,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 32550000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Tài liệu ký\", \"Unit\": None, \"Value\": 5000, \"ResourceID\": 13, \"ResourceCode\": \"Document\", \"ResourceName\": \"Tài liệu ký\"}]",
        "ItemName": "WeS-5.000",
        "ModuleName": None,
        "DisplayName": "WeS-5.000",
        "ProductID": 411,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 54550000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Tài liệu ký\", \"Unit\": None, \"Value\": \"10000\", \"ResourceID\": 13, \"ResourceCode\": \"Document\", \"ResourceName\": \"Tài liệu ký\"}]",
        "ItemName": "WeS-10.000",
        "ModuleName": None,
        "DisplayName": "WeS-10.000",
        "ProductID": 411,
        "IsCapacityPackage": True,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "AMISProcess",
    "AppName": "AMIS Quy trình",
    "ProductID": 410,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 5200000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 10 người dùng gói Premium",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10 người dùng gói Premium",
        "ProductID": 410,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 0.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 5, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Free\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Free\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Free",
        "ModuleName": None,
        "DisplayName": "Free",
        "ProductID": 410,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 10400000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 20, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Premium\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Premium\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Premium",
        "ModuleName": None,
        "DisplayName": "Premium",
        "ProductID": 410,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "HKD",
    "AppName": "AMIS Kế toán Hộ kinh doanh",
    "ProductID": 405,
    "MarketName": "Hộ kinh doanh",
    "ListPackageProduct": [
      {
        "ItemPrice": 2400000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 3, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Nghiệp vụ\", \"Unit\": None, \"Value\": 7, \"ResourceID\": 21, \"ResourceCode\": \"Business\", \"ResourceName\": \"Nghiệp vụ\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Individual\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"AMIS Kế toán Hộ kinh doanh\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Phần mềm AMIS Kế toán dành cho hộ, cá nhân kinh doanh",
        "ModuleName": None,
        "DisplayName": "AMIS kế toán Hộ kinh doanh",
        "ProductID": 405,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 800000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 01 người dùng",
        "ModuleName": None,
        "DisplayName": "Mua thêm 01 người dùng",
        "ProductID": 405,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "CukCuk.vn",
    "AppName": "Phần mềm quản lý nhà hàng CUKCUK",
    "ProductID": 230,
    "MarketName": "Hộ kinh doanh",
    "ListPackageProduct": [
      {
        "ItemPrice": 0.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Thời hạn theo ngày\", \"Unit\": \"Gói\", \"Value\": 15, \"DataType\": \"number\", \"ResourceID\": 23, \"ResourceCode\": \"DurationByDay\", \"ResourceName\": \"Thời hạn theo ngày\"}, {\"Name\": \"Mã gói\", \"Value\": \"CUK.TRL\", \"DataType\": \"string\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Value\": \"Starter\", \"DataType\": \"string\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}]",
        "ItemName": "Gói dùng thử",
        "ModuleName": "Gói sản phẩm",
        "DisplayName": "Gói dùng thử 15 ngày CukCuk",
        "ProductID": 230,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 199000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"CUK.STD\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Standard\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo tháng\", \"Unit\": None, \"Value\": \"1\", \"ResourceID\": 22, \"ResourceCode\": \"DurationByMonth\", \"ResourceName\": \"Thời hạn theo tháng\"}]",
        "ItemName": "Standard",
        "ModuleName": "Gói sản phẩm",
        "DisplayName": "Standard",
        "ProductID": 230,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 299000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"CUK.PRO\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Professional\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo tháng\", \"Unit\": None, \"Value\": \"1\", \"ResourceID\": 22, \"ResourceCode\": \"DurationByMonth\", \"ResourceName\": \"Thời hạn theo tháng\"}]",
        "ItemName": "Professional",
        "ModuleName": "Gói sản phẩm",
        "DisplayName": "Professional",
        "ProductID": 230,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 499000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"CUK.ENT\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Enterprise\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo tháng\", \"Unit\": None, \"Value\": \"1\", \"ResourceID\": 22, \"ResourceCode\": \"DurationByMonth\", \"ResourceName\": \"Thời hạn theo tháng\"}]",
        "ItemName": "Enterprise",
        "ModuleName": "Gói sản phẩm",
        "DisplayName": "Enterprise",
        "ProductID": 230,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "Combo_eSign_HKD",
    "AppName": "MISA eSign - Chữ ký số USB Token cho Hộ kinh doanh",
    "ProductID": 184,
    "MarketName": "Hộ kinh doanh",
    "ListPackageProduct": [
      {
        "ItemPrice": 1049000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Dịch vụ chữ ký số MISA eSign cho Hộ, cá nhân kinh doanh gói mua mới 1 năm đã bao gồm USB Token",
        "ModuleName": "Hộ kinh doanh",
        "DisplayName": "1 năm",
        "ProductID": 184,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1449000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Dịch vụ chữ ký số MISA eSign cho Hộ, cá nhân kinh doanh gói mua mới 2 năm đã bao gồm USB Token",
        "ModuleName": "Hộ kinh doanh",
        "DisplayName": "2 năm",
        "ProductID": 184,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 1749000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Dịch vụ chữ ký số MISA eSign cho Hộ, cá nhân kinh doanh gói mua mới 3 năm đã bao gồm USB Token",
        "ModuleName": "Hộ kinh doanh",
        "DisplayName": "3 năm",
        "ProductID": 184,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2049000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Dịch vụ chữ ký số MISA eSign cho Hộ, cá nhân kinh doanh gói mua mới 4 năm đã bao gồm USB Token",
        "ModuleName": "Hộ kinh doanh",
        "DisplayName": "4 năm",
        "ProductID": 184,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 2349000.0,
        "ItemType": 1,
        "ResourceInfor": "[]",
        "ItemName": "Dịch vụ chữ ký số MISA eSign cho Hộ, cá nhân kinh doanh gói mua mới 5 năm đã bao gồm USB Token",
        "ModuleName": "Hộ kinh doanh",
        "DisplayName": "5 năm",
        "ProductID": 184,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  },
  {
    "AppCode": "Task",
    "AppName": "Quản lý công việc",
    "ProductID": 409,
    "MarketName": "Doanh nghiệp",
    "ListPackageProduct": [
      {
        "ItemPrice": 4300000.0,
        "ItemType": 2,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}]",
        "ItemName": "Mua thêm 10 người dùng gói Premium",
        "ModuleName": None,
        "DisplayName": "Mua thêm 10 người dùng gói Premium",
        "ProductID": 409,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 0.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 5, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Free\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Free\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 10, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Free",
        "ModuleName": None,
        "DisplayName": "Free",
        "ProductID": 409,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      },
      {
        "ItemPrice": 8600000.0,
        "ItemType": 1,
        "ResourceInfor": "[{\"Name\": \"Người dùng\", \"Unit\": None, \"Value\": 20, \"ResourceID\": 10, \"ResourceCode\": \"Account\", \"ResourceName\": \"Người dùng\"}, {\"Name\": \"Mã gói\", \"Unit\": None, \"Value\": \"Premium\", \"ResourceID\": 36, \"ResourceCode\": \"PackageCode\", \"ResourceName\": \"Mã gói\"}, {\"Name\": \"Tên gói\", \"Unit\": None, \"Value\": \"Premium\", \"ResourceID\": 37, \"ResourceCode\": \"PackageName\", \"ResourceName\": \"Tên gói\"}, {\"Name\": \"Thời hạn theo năm\", \"Unit\": None, \"Value\": 1, \"ResourceID\": 41, \"ResourceCode\": \"DurationByYear\", \"ResourceName\": \"Thời hạn theo năm\"}]",
        "ItemName": "Premium",
        "ModuleName": None,
        "DisplayName": "Premium",
        "ProductID": 409,
        "IsCapacityPackage": False,
        "PackageId": None,
        "MultiPackage": None
      }
    ]
  }
]

RESPONSE_CREATE_EXTEND_QUOTE= {
  "status_code": 200,
  "body": "[{\"AppCode\":\"eShop\",\"AppName\":\"Phần mềm quản lý bán hàng đa kênh MISA eShop\",\"ProductID\":693,\"MarketName\":\"Hộ kinh doanh\",\"ListPackageProduct\":[{\"ItemPrice\":3950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Đào tạo trực tuyến 1 kèm 1 phần mềm MISA eShop\",\"ModuleName\":null,\"DisplayName\":\"Đào tạo trực tuyến 1 kèm 1 phần mềm MISA eShop\",\"ProductID\":693,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Tư vấn triển khai phần mềm MISA eShop\",\"ModuleName\":null,\"DisplayName\":\"Tư vấn triển khai phần mềm MISA eShop\",\"ProductID\":693,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2388000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"e-Starter\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"e-Starter\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"e-Starter\",\"ModuleName\":\"Bán thương mại điện tử\",\"DisplayName\":\"e-Starter\",\"ProductID\":693,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2388000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"s-Standard\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"s-Standard\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"s-Standard\",\"ModuleName\":\"Bán tại cửa hàng\",\"DisplayName\":\"s-Standard\",\"ProductID\":693,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2388000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"Omi-Starter\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"Omi-Starter\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Omi-Starter\",\"ModuleName\":\"Bán đa kênh\",\"DisplayName\":\"Omi-Starter\",\"ProductID\":693,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3588000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"e-Standard\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"e-Standard\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"e-Standard\",\"ModuleName\":\"Bán thương mại điện tử\",\"DisplayName\":\"e-Standard\",\"ProductID\":693,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3588000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"s-Professional\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"s-Professional\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"s-Professional\",\"ModuleName\":\"Bán tại cửa hàng\",\"DisplayName\":\"s-Professional\",\"ProductID\":693,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3588000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"Omi-Standard\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"Omi-Standard\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Omi-Standard\",\"ModuleName\":\"Bán đa kênh\",\"DisplayName\":\"Omi-Standard\",\"ProductID\":693,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4788000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"e-Professional\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"e-Professional\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"e-Professional\",\"ModuleName\":\"Bán thương mại điện tử\",\"DisplayName\":\"e-Professional\",\"ProductID\":693,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4788000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"s-Enterprise\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"s-Enterprise\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"s-Enterprise\",\"ModuleName\":\"Bán tại cửa hàng\",\"DisplayName\":\"s-Enterprise\",\"ProductID\":693,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5988000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"Omi-Professional\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"Omi-Professional\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Omi-Professional\",\"ModuleName\":\"Bán đa kênh\",\"DisplayName\":\"Omi-Professional\",\"ProductID\":693,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5988000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"e-Enterprise\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"e-Enterprise\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"e-Enterprise\",\"ModuleName\":\"Bán thương mại điện tử\",\"DisplayName\":\"e-Enterprise\",\"ProductID\":693,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":8388000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"Omi-Enterprise\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"Omi-Enterprise\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Omi-Enterprise\",\"ModuleName\":\"Bán đa kênh\",\"DisplayName\":\"Omi-Enterprise\",\"ProductID\":693,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"ComboCukCuk\",\"AppName\":\"Bộ giải pháp quản lý nhà hàng\",\"ProductID\":692,\"MarketName\":\"Hộ kinh doanh\",\"ListPackageProduct\":[{\"ItemPrice\":3950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm quản lý nhà hàng và thiết bị - Gói Đào tạo phần mềm 1 kèm 1 trực tuyến\",\"ModuleName\":null,\"DisplayName\":\"Đào tạo phần mềm 1 kèm 1 trực tuyến\",\"ProductID\":692,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm quản lý nhà hàng và thiết bị - Gói Tư vấn triển khai phần mềm MISA CukCuk\",\"ModuleName\":null,\"DisplayName\":\"Tư vấn triển khai phần mềm MISA CukCuk\",\"ProductID\":692,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":199000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"CUK.STD\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Standard\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo tháng\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"1\\\", \\\"ResourceID\\\": 22, \\\"ResourceCode\\\": \\\"DurationByMonth\\\", \\\"ResourceName\\\": \\\"Thời hạn theo tháng\\\"}]\",\"ItemName\":\"Mua thêm năm phần mềm MISA CukCuk gói Standard\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm năm phần mềm MISA CukCuk gói Standard\",\"ProductID\":692,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":299000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"CUK.PRO\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Professional\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo tháng\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"1\\\", \\\"ResourceID\\\": 22, \\\"ResourceCode\\\": \\\"DurationByMonth\\\", \\\"ResourceName\\\": \\\"Thời hạn theo tháng\\\"}]\",\"ItemName\":\"Mua thêm năm phần mềm MISA CukCuk gói Professional\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm năm phần mềm MISA CukCuk gói Professional\",\"ProductID\":692,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":499000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"CUK.ENT\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Enterprise\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo tháng\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"1\\\", \\\"ResourceID\\\": 22, \\\"ResourceCode\\\": \\\"DurationByMonth\\\", \\\"ResourceName\\\": \\\"Thời hạn theo tháng\\\"}]\",\"ItemName\":\"Mua thêm năm phần mềm MISA CukCuk gói Enterprise\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm năm phần mềm MISA CukCuk gói Enterprise\",\"ProductID\":692,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":12452000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Máy POS Sunmi D3 Pro\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 103, \\\"ResourceCode\\\": \\\"SunmiPOS\\\", \\\"ResourceName\\\": \\\"Máy POS Sunmi D3 Pro\\\"}]\",\"ItemName\":\"Máy POS Sunmi D3 Pro\",\"ModuleName\":null,\"DisplayName\":\"Máy POS Sunmi D3 Pro\",\"ProductID\":692,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1150000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Máy in nhiệt\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 105, \\\"ResourceCode\\\": \\\"ThermalPrinter\\\", \\\"ResourceName\\\": \\\"Máy in nhiệt\\\"}]\",\"ItemName\":\"Máy in nhiệt model XP-Q805KL\",\"ModuleName\":null,\"DisplayName\":\"Máy in nhiệt model XP-Q805KL\",\"ProductID\":692,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":847000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Két đựng tiền\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 107, \\\"ResourceCode\\\": \\\"CashDrawer\\\", \\\"ResourceName\\\": \\\"Két đựng tiền\\\"}]\",\"ItemName\":\"Két đựng tiền AT-410\",\"ModuleName\":null,\"DisplayName\":\"Két đựng tiền AT-410\",\"ProductID\":692,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7020.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Giấy nhiệt\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 109, \\\"ResourceCode\\\": \\\"ThermalPaper\\\", \\\"ResourceName\\\": \\\"Giấy nhiệt\\\"}]\",\"ItemName\":\"Giấy nhiệt - Khổ 80x45mm (cho máy Q805KL)\",\"ModuleName\":null,\"DisplayName\":\"Giấy nhiệt - Khổ 80x45mm (cho máy Q805KL)\",\"ProductID\":692,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":39420.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Giấy decal nhiệt\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 108, \\\"ResourceCode\\\": \\\"ThermalDecalPaper\\\", \\\"ResourceName\\\": \\\"Giấy decal nhiệt\\\"}]\",\"ItemName\":\"Giấy decal nhiệt - Khổ 50x30x30m\",\"ModuleName\":null,\"DisplayName\":\"Giấy decal nhiệt - Khổ 50x30x30m\",\"ProductID\":692,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1150000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Máy in nhiệt\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 105, \\\"ResourceCode\\\": \\\"ThermalPrinter\\\", \\\"ResourceName\\\": \\\"Máy in nhiệt\\\"}]\",\"ItemName\":\"Máy in nhiệt model PD805KL\",\"ModuleName\":null,\"DisplayName\":\"Máy in nhiệt model PD805KL\",\"ProductID\":692,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1540000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Máy in nhiệt\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 105, \\\"ResourceCode\\\": \\\"ThermalPrinter\\\", \\\"ResourceName\\\": \\\"Máy in nhiệt\\\"}]\",\"ItemName\":\"Máy in nhiệt model PD304\",\"ModuleName\":null,\"DisplayName\":\"Máy in nhiệt model PD304\",\"ProductID\":692,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3850000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Máy tính bảng\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 110, \\\"ResourceCode\\\": \\\"Tablet\\\", \\\"ResourceName\\\": \\\"Máy tính bảng\\\"}]\",\"ItemName\":\"Máy tính bảng\",\"ModuleName\":null,\"DisplayName\":\"Máy tính bảng\",\"ProductID\":692,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3850000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Màn hình phụ máy POS D3 Pro\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 104, \\\"ResourceCode\\\": \\\"SecondaryMonitorPOS\\\", \\\"ResourceName\\\": \\\"Màn hình phụ máy POS D3 Pro\\\"}]\",\"ItemName\":\"Màn hình phụ máy POS D3 Pro\",\"ModuleName\":null,\"DisplayName\":\"Màn hình phụ máy POS D3 Pro\",\"ProductID\":692,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Combo 1: Table service starter\",\"ModuleName\":null,\"DisplayName\":\"Combo 1: Starter\",\"ProductID\":692,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":14200000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Combo 2: Standard\",\"ModuleName\":null,\"DisplayName\":\"Combo 2: Standard\",\"ProductID\":692,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":15400000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Combo 3: Professional\",\"ModuleName\":null,\"DisplayName\":\"Combo 3: Professional\",\"ProductID\":692,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":17800000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Combo 4: Enterprise\",\"ModuleName\":null,\"DisplayName\":\"Combo 4: Enterprise\",\"ProductID\":692,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"MISAIVAN\",\"AppName\":\"AMIS Bảo hiểm xã hội Hộ kinh doanh\",\"ProductID\":691,\"MarketName\":\"Hộ kinh doanh\",\"ListPackageProduct\":[{\"ItemPrice\":80000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10 người dùng\",\"ProductID\":691,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":240000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS BHXH\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS BHXH\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"AMIS BHXH\",\"ModuleName\":null,\"DisplayName\":\"Phần mềm AMIS BHXH\",\"ProductID\":691,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"AILearning\",\"AppName\":\"AILearning\",\"ProductID\":690,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":1200000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Value\\\": 5, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Dung lượng\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 101, \\\"ResourceCode\\\": \\\"DBCapacity\\\", \\\"ResourceName\\\": \\\"Dung lượng\\\"}]\",\"ItemName\":\"Mua thêm 5 người dùng\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 5 người dùng\",\"ProductID\":690,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2400000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Dung lượng\\\", \\\"Value\\\": \\\"5\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 101, \\\"ResourceCode\\\": \\\"DBCapacity\\\", \\\"ResourceName\\\": \\\"Dung lượng\\\"}]\",\"ItemName\":\"Mua thêm 5 GB dung lượng lưu trữ\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 5 GB dung lượng lưu trữ\",\"ProductID\":690,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Đào tạo phần mềm 1 kèm 1 trực tuyến\",\"ModuleName\":null,\"DisplayName\":\"Đào tạo phần mềm 1 kèm 1 trực tuyến\",\"ProductID\":690,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Đào tạo phần mềm 1 kèm 1 trực tiếp\",\"ModuleName\":null,\"DisplayName\":\"Đào tạo phần mềm 1 kèm 1 trực tiếp\",\"ProductID\":690,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":20000000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Tư vấn triển khai phần mềm\",\"ModuleName\":null,\"DisplayName\":\"Tư vấn triển khai phần mềm\",\"ProductID\":690,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7200000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"AILearning\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"AILearning\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Người dùng\\\", \\\"Value\\\": 30, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Dung lượng\\\", \\\"Value\\\": \\\"6\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 101, \\\"ResourceCode\\\": \\\"DBCapacity\\\", \\\"ResourceName\\\": \\\"Dung lượng\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"AILearning\",\"ModuleName\":null,\"DisplayName\":\"AILearning\",\"ProductID\":690,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"MMO\",\"AppName\":\"MISA Mimosa Online\",\"ProductID\":687,\"MarketName\":\"Hành chính sự nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":6000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Số lượng người dùng\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 83, \\\"ResourceCode\\\": \\\"NumberOfUser\\\", \\\"ResourceName\\\": \\\"Số lượng người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói Suman\\\", \\\"Value\\\": \\\"MMO\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 94, \\\"ResourceCode\\\": \\\"SumanPackCode\\\", \\\"ResourceName\\\": \\\"Mã gói Suman\\\"}, {\\\"Name\\\": \\\"Địa chỉ truy cập\\\", \\\"Value\\\": \\\"mimosaapp.misa.vn\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 98, \\\"ResourceCode\\\": \\\"ApplicationURL\\\", \\\"ResourceName\\\": \\\"Địa chỉ truy cập\\\"}]\",\"ItemName\":\"Gói phần mềm kế toán \",\"ModuleName\":null,\"DisplayName\":\"Gói phần mềm kế toán HCSN\",\"ProductID\":687,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"BBO\",\"AppName\":\"MISA Bamboo Online\",\"ProductID\":686,\"MarketName\":\"Hành chính sự nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":6000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Mã gói Suman\\\", \\\"Value\\\": \\\"BBO\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 94, \\\"ResourceCode\\\": \\\"SumanPackCode\\\", \\\"ResourceName\\\": \\\"Mã gói Suman\\\"}, {\\\"Name\\\": \\\"Địa chỉ truy cập\\\", \\\"Value\\\": \\\"bambooapp.misa.vn\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 98, \\\"ResourceCode\\\": \\\"ApplicationURL\\\", \\\"ResourceName\\\": \\\"Địa chỉ truy cập\\\"}]\",\"ItemName\":\"Gói phần mềm kế toán xã/phường\",\"ModuleName\":null,\"DisplayName\":\"Gói phần mềm kế toán xã/phường\",\"ProductID\":686,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"Accounting\",\"AppName\":\"AMIS Kế toán Doanh nghiệp\",\"ProductID\":404,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":11950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Gói đào tạo phần mềm 1 kèm 1 trực tiếp\",\"ModuleName\":null,\"DisplayName\":\"Gói đào tạo phần mềm\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":20000000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Tư vấn triển khai phần mềm\",\"ModuleName\":null,\"DisplayName\":\"Tư vấn triển khai phần mềm\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Gói đào tạo phần mềm 1 kèm 1 trực tuyến\",\"ModuleName\":null,\"DisplayName\":\"Gói đào tạo phần mềm\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2450000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 01 người dùng gói Starter\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 01 người dùng gói Starter\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Chi nhánh\\\", \\\"Unit\\\": \\\"chi nhánh\\\", \\\"Value\\\": 1, \\\"ResourceID\\\": 43, \\\"ResourceCode\\\": \\\"Branch\\\", \\\"ResourceName\\\": \\\"Chi nhánh\\\"}]\",\"ItemName\":\"Mua thêm chi nhánh gói Starter\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm chi nhánh gói Starter\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1350000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 01 người dùng gói Standard\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 01 người dùng gói Standard\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Chi nhánh\\\", \\\"Unit\\\": \\\"chi nhánh\\\", \\\"Value\\\": 1, \\\"ResourceID\\\": 43, \\\"ResourceCode\\\": \\\"Branch\\\", \\\"ResourceName\\\": \\\"Chi nhánh\\\"}]\",\"ItemName\":\"Mua thêm chi nhánh gói Standard\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm chi nhánh gói Standard\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1750000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 01 người dùng gói Professional\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 01 người dùng gói Professional\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2450000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Chi nhánh\\\", \\\"Unit\\\": \\\"chi nhánh\\\", \\\"Value\\\": 1, \\\"ResourceID\\\": 43, \\\"ResourceCode\\\": \\\"Branch\\\", \\\"ResourceName\\\": \\\"Chi nhánh\\\"}]\",\"ItemName\":\"Mua thêm chi nhánh gói Professional\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm chi nhánh gói Professional\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2150000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 01 người dùng gói Enterprise\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 01 người dùng gói Enterprise\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Chi nhánh\\\", \\\"Unit\\\": \\\"chi nhánh\\\", \\\"Value\\\": 1, \\\"ResourceID\\\": 43, \\\"ResourceCode\\\": \\\"Branch\\\", \\\"ResourceName\\\": \\\"Chi nhánh\\\"}]\",\"ItemName\":\"Mua thêm chi nhánh gói Enterprise\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm chi nhánh gói Enterprise\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2250000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 01 người dùng gói Enterprise Plus\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 01 người dùng gói Enterprise Plus\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Chi nhánh\\\", \\\"Unit\\\": \\\"chi nhánh\\\", \\\"Value\\\": 1, \\\"ResourceID\\\": 43, \\\"ResourceCode\\\": \\\"Branch\\\", \\\"ResourceName\\\": \\\"Chi nhánh\\\"}]\",\"ItemName\":\"Mua thêm chi nhánh gói Enterprise Plus\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm chi nhánh gói Enterprise Plus\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":330000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"Starter\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Là gói dịch vụ lưu trữ dữ liệu\\\", \\\"Value\\\": \\\"true\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 91, \\\"ResourceCode\\\": \\\"IsDataStorage\\\", \\\"ResourceName\\\": \\\"Là gói dịch vụ lưu trữ dữ liệu\\\"}]\",\"ItemName\":\"Dịch vụ lưu trữ dữ liệu gói Starter\",\"ModuleName\":null,\"DisplayName\":\"Dịch vụ lưu trữ dữ liệu\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":440000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"Standard\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Là gói dịch vụ lưu trữ dữ liệu\\\", \\\"Value\\\": \\\"true\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 91, \\\"ResourceCode\\\": \\\"IsDataStorage\\\", \\\"ResourceName\\\": \\\"Là gói dịch vụ lưu trữ dữ liệu\\\"}]\",\"ItemName\":\"Dịch vụ lưu trữ dữ liệu gói Standard\",\"ModuleName\":null,\"DisplayName\":\"Dịch vụ lưu trữ dữ liệu\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":550000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"Professional\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Là gói dịch vụ lưu trữ dữ liệu\\\", \\\"Value\\\": \\\"true\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 91, \\\"ResourceCode\\\": \\\"IsDataStorage\\\", \\\"ResourceName\\\": \\\"Là gói dịch vụ lưu trữ dữ liệu\\\"}]\",\"ItemName\":\"Dịch vụ lưu trữ dữ liệu gói Professional\",\"ModuleName\":null,\"DisplayName\":\"Dịch vụ lưu trữ dữ liệu\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":660000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"Enterprise\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Là gói dịch vụ lưu trữ dữ liệu\\\", \\\"Value\\\": \\\"true\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 91, \\\"ResourceCode\\\": \\\"IsDataStorage\\\", \\\"ResourceName\\\": \\\"Là gói dịch vụ lưu trữ dữ liệu\\\"}]\",\"ItemName\":\"Dịch vụ lưu trữ dữ liệu gói Enterprise\",\"ModuleName\":null,\"DisplayName\":\"Dịch vụ lưu trữ dữ liệu\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2200000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"Enterprise Plus\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Là gói dịch vụ lưu trữ dữ liệu\\\", \\\"Value\\\": \\\"true\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 91, \\\"ResourceCode\\\": \\\"IsDataStorage\\\", \\\"ResourceName\\\": \\\"Là gói dịch vụ lưu trữ dữ liệu\\\"}]\",\"ItemName\":\"Dịch vụ lưu trữ dữ liệu gói Enterprise Plus\",\"ModuleName\":null,\"DisplayName\":\"Dịch vụ lưu trữ dữ liệu\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3000000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Dữ liệu\\\", \\\"Unit\\\": \\\"Dữ liệu/Năm\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 92, \\\"ResourceCode\\\": \\\"ResourceQuantity\\\", \\\"ResourceName\\\": \\\"Dữ liệu\\\"}]\",\"ItemName\":\"Mua thêm dữ liệu\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm dữ liệu AMIS Kế Toán\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2450000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nghiệp vụ\\\", \\\"Unit\\\": null, \\\"Value\\\": 7, \\\"ResourceID\\\": 21, \\\"ResourceCode\\\": \\\"Business\\\", \\\"ResourceName\\\": \\\"Nghiệp vụ\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Starter\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Starter\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Dữ liệu\\\", \\\"Value\\\": \\\"3\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 92, \\\"ResourceCode\\\": \\\"ResourceQuantity\\\", \\\"ResourceName\\\": \\\"Dữ liệu\\\"}]\",\"ItemName\":\"Starter\",\"ModuleName\":null,\"DisplayName\":\"Starter\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4050000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 3, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nghiệp vụ\\\", \\\"Unit\\\": null, \\\"Value\\\": 11, \\\"ResourceID\\\": 21, \\\"ResourceCode\\\": \\\"Business\\\", \\\"ResourceName\\\": \\\"Nghiệp vụ\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Standard\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Standard\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Dữ liệu\\\", \\\"Value\\\": \\\"3\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 92, \\\"ResourceCode\\\": \\\"ResourceQuantity\\\", \\\"ResourceName\\\": \\\"Dữ liệu\\\"}]\",\"ItemName\":\"Standard\",\"ModuleName\":null,\"DisplayName\":\"Standard\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5250000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 3, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nghiệp vụ\\\", \\\"Unit\\\": null, \\\"Value\\\": 16, \\\"ResourceID\\\": 21, \\\"ResourceCode\\\": \\\"Business\\\", \\\"ResourceName\\\": \\\"Nghiệp vụ\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Professional\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Professional\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Dữ liệu\\\", \\\"Value\\\": \\\"3\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 92, \\\"ResourceCode\\\": \\\"ResourceQuantity\\\", \\\"ResourceName\\\": \\\"Dữ liệu\\\"}]\",\"ItemName\":\"Professional\",\"ModuleName\":null,\"DisplayName\":\"Professional\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":6450000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 3, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nghiệp vụ\\\", \\\"Unit\\\": null, \\\"Value\\\": 17, \\\"ResourceID\\\": 21, \\\"ResourceCode\\\": \\\"Business\\\", \\\"ResourceName\\\": \\\"Nghiệp vụ\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Enterprise\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Enterprise\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Dữ liệu\\\", \\\"Value\\\": \\\"3\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 92, \\\"ResourceCode\\\": \\\"ResourceQuantity\\\", \\\"ResourceName\\\": \\\"Dữ liệu\\\"}]\",\"ItemName\":\"Enterprise\",\"ModuleName\":null,\"DisplayName\":\"Enterprise\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":22500000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nghiệp vụ\\\", \\\"Unit\\\": null, \\\"Value\\\": 20, \\\"ResourceID\\\": 21, \\\"ResourceCode\\\": \\\"Business\\\", \\\"ResourceName\\\": \\\"Nghiệp vụ\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Enterprise Plus\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Enterprise Plus\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Dữ liệu\\\", \\\"Value\\\": \\\"3\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 92, \\\"ResourceCode\\\": \\\"ResourceQuantity\\\", \\\"ResourceName\\\": \\\"Dữ liệu\\\"}]\",\"ItemName\":\"Enterprise Plus\",\"ModuleName\":null,\"DisplayName\":\"Enterprise Plus\",\"ProductID\":404,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"ComboKT_DN\",\"AppName\":\"Bộ giải pháp tài chính kế toán doanh nghiệp\",\"ProductID\":406,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":11950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp Phần mềm Quản lý Tài chính kế toán doanh nghiệp - Gói đào tạo phần mềm 1 kèm 1 trực tiếp\",\"ModuleName\":null,\"DisplayName\":\"Gói đào tạo phần mềm\",\"ProductID\":406,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":20000000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp Phần mềm Quản lý Tài chính kế toán doanh nghiệp - Tư vấn triển khai phần mềm\",\"ModuleName\":null,\"DisplayName\":\"Tư vấn triển khai phần mềm\",\"ProductID\":406,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp Phần mềm Quản lý Tài chính kế toán doanh nghiệp - Gói đào tạo phần mềm 1 kèm 1 trực tuyến\",\"ModuleName\":null,\"DisplayName\":\"Gói đào tạo phần mềm\",\"ProductID\":406,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2450000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 01 người dùng gói Starter\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 01 người dùng\",\"ProductID\":406,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Chi nhánh\\\", \\\"Unit\\\": \\\"chi nhánh\\\", \\\"Value\\\": 1, \\\"ResourceID\\\": 43, \\\"ResourceCode\\\": \\\"Branch\\\", \\\"ResourceName\\\": \\\"Chi nhánh\\\"}]\",\"ItemName\":\"Mua thêm chi nhánh gói Starter\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm chi nhánh\",\"ProductID\":406,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1350000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 01 người dùng gói Standard\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 01 người dùng\",\"ProductID\":406,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Chi nhánh\\\", \\\"Unit\\\": \\\"chi nhánh\\\", \\\"Value\\\": 1, \\\"ResourceID\\\": 43, \\\"ResourceCode\\\": \\\"Branch\\\", \\\"ResourceName\\\": \\\"Chi nhánh\\\"}]\",\"ItemName\":\"Mua thêm chi nhánh gói Standard\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm chi nhánh\",\"ProductID\":406,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1750000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 01 người dùng gói Professional\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 01 người dùng\",\"ProductID\":406,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2450000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Chi nhánh\\\", \\\"Unit\\\": \\\"chi nhánh\\\", \\\"Value\\\": 1, \\\"ResourceID\\\": 43, \\\"ResourceCode\\\": \\\"Branch\\\", \\\"ResourceName\\\": \\\"Chi nhánh\\\"}]\",\"ItemName\":\"Mua thêm chi nhánh gói Professional\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm chi nhánh\",\"ProductID\":406,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2150000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 01 người dùng gói Enterprise\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 01 người dùng\",\"ProductID\":406,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Chi nhánh\\\", \\\"Unit\\\": \\\"chi nhánh\\\", \\\"Value\\\": 1, \\\"ResourceID\\\": 43, \\\"ResourceCode\\\": \\\"Branch\\\", \\\"ResourceName\\\": \\\"Chi nhánh\\\"}]\",\"ItemName\":\"Mua thêm chi nhánh gói Enterprise\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm chi nhánh\",\"ProductID\":406,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2250000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 01 người dùng gói Enterprise Plus\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 01 người dùng\",\"ProductID\":406,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Chi nhánh\\\", \\\"Unit\\\": \\\"chi nhánh\\\", \\\"Value\\\": 1, \\\"ResourceID\\\": 43, \\\"ResourceCode\\\": \\\"Branch\\\", \\\"ResourceName\\\": \\\"Chi nhánh\\\"}]\",\"ItemName\":\"Mua thêm chi nhánh gói Enterprise Plus\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm chi nhánh\",\"ProductID\":406,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":450000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"300\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Gói MEIR 300\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIR 300\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":650000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"500\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Gói MEIR 500\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIR 500\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1050000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"1000\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Gói MEIR 1.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIR 1.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3150000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"5000\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Gói MEIR 5.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIR 5.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5250000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"10000\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Gói MEIR 10.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIR 10.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":30000000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"100000\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Gói MEIR 100.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIR 100.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3500000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"10000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"Gói MEIVE 10.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIVE 10.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5650000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"20000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"Gói MEIVE 20.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIVE 20.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11650000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"50000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"Gói MEIVE 50.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIVE 50.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":19950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"100000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"Gói MEIVE 100.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIVE 100.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":33950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"200000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"Gói MEIVE 200.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIVE 200.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":74950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"500000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"Gói MEIVE 500.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIVE 500.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":250000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"300\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"Gói MEIMTT-300\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIMTT-300\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":350000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"500\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"Gói MEIMTT-500\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIMTT-500\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":550000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"1000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"Gói MEIMTT-1.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIMTT-1.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":850000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"2000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"Gói MEIMTT-2.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIMTT-2.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"5000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"Gói MEIMTT-5.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIMTT-5.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3050000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"10000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"Gói MEIMTT-10.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIMTT-10.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5650000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"20000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"Gói MEIMTT-20.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIMTT-20.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11650000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"50000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"Gói MEIMTT-50.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIMTT-50.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":19950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"100000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"Gói MEIMTT-100.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIMTT-100.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":129950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"1000000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"Gói MEIVE 1.000.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIVE 1.000.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":390000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 300, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"Gói MEIX-300\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIX-300\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":690000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 1000, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"Gói MEIX-1.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIX-1.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1190000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 2000, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"Gói MEIX-2.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIX-2.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2490000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 5000, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"Gói MEIX-5.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIX-5.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4490000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 10000, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"Gói MEIX-10.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIX-10.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1550000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"2000\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Gói MEIR 2.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIR 2.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3000000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Dữ liệu\\\", \\\"Unit\\\": \\\"Dữ liệu/Năm\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 92, \\\"ResourceCode\\\": \\\"ResourceQuantity\\\", \\\"ResourceName\\\": \\\"Dữ liệu\\\"}]\",\"ItemName\":\"Mua thêm dữ liệu\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm dữ liệu\",\"ProductID\":406,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7990000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Value\\\": 20000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"Gói MEIX-20.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIX-20.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":17490000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Value\\\": 50000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"Gói MEIX-50.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIX-50.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":30990000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Value\\\": 100000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"Gói MEIX-100.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIX-100.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4000000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\", \\\"Value\\\": \\\"50000\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 89, \\\"ResourceCode\\\": \\\"NumberOfPetrol\\\", \\\"ResourceName\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\"}]\",\"ItemName\":\"Gói MEIXD-50.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIXD-50.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7000000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\", \\\"Value\\\": \\\"100000\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 89, \\\"ResourceCode\\\": \\\"NumberOfPetrol\\\", \\\"ResourceName\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\"}]\",\"ItemName\":\"Gói MEIXD-100.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIXD-100.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":18000000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\", \\\"Value\\\": \\\"300000\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 89, \\\"ResourceCode\\\": \\\"NumberOfPetrol\\\", \\\"ResourceName\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\"}]\",\"ItemName\":\"Gói MEIXD-300.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIXD-300.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":27500000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\", \\\"Value\\\": \\\"500000\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 89, \\\"ResourceCode\\\": \\\"NumberOfPetrol\\\", \\\"ResourceName\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\"}]\",\"ItemName\":\"Gói MEIXD-500.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIXD-500.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":50000000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\", \\\"Value\\\": \\\"1000000\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 89, \\\"ResourceCode\\\": \\\"NumberOfPetrol\\\", \\\"ResourceName\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\"}]\",\"ItemName\":\"Gói MEIXD-1.000.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIXD-1.000.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":126000000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\", \\\"Value\\\": \\\"3000000\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 89, \\\"ResourceCode\\\": \\\"NumberOfPetrol\\\", \\\"ResourceName\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\"}]\",\"ItemName\":\"Gói MEIXD-3.000.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIXD-3.000.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":9150000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": 20000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Gói MEIR 20.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIR 20.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":19150000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Value\\\": 50000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Gói MEIR 50.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIR 50.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":60000000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Value\\\": 200000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Gói MEIR 200.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIR 200.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":84000000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Value\\\": 300000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Gói MEIR 300.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIR 300.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":125000000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Value\\\": 500000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Gói MEIR 500.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIR 500.000\",\"ProductID\":406,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": 100, \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}, {\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 100, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}, {\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nghiệp vụ\\\", \\\"Unit\\\": null, \\\"Value\\\": 7, \\\"ResourceID\\\": 21, \\\"ResourceCode\\\": \\\"Business\\\", \\\"ResourceName\\\": \\\"Nghiệp vụ\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Starter\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Starter\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Dữ liệu\\\", \\\"Value\\\": \\\"3\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 92, \\\"ResourceCode\\\": \\\"ResourceQuantity\\\", \\\"ResourceName\\\": \\\"Dữ liệu\\\"}]\",\"ItemName\":\"Bộ giải pháp Phần mềm Quản lý Tài chính kế toán doanh nghiệp - Gói Starter năm đầu tiên\",\"ModuleName\":null,\"DisplayName\":\"Starter\",\"ProductID\":406,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4550000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": 100, \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}, {\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 100, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}, {\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 3, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nghiệp vụ\\\", \\\"Unit\\\": null, \\\"Value\\\": 11, \\\"ResourceID\\\": 21, \\\"ResourceCode\\\": \\\"Business\\\", \\\"ResourceName\\\": \\\"Nghiệp vụ\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Standard\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Standard\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Dữ liệu\\\", \\\"Value\\\": \\\"3\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 92, \\\"ResourceCode\\\": \\\"ResourceQuantity\\\", \\\"ResourceName\\\": \\\"Dữ liệu\\\"}]\",\"ItemName\":\"Bộ giải pháp Phần mềm Quản lý Tài chính kế toán doanh nghiệp - Gói Standard năm đầu tiên\",\"ModuleName\":null,\"DisplayName\":\"Standard\",\"ProductID\":406,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5750000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": 100, \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}, {\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 100, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}, {\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 3, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nghiệp vụ\\\", \\\"Unit\\\": null, \\\"Value\\\": 16, \\\"ResourceID\\\": 21, \\\"ResourceCode\\\": \\\"Business\\\", \\\"ResourceName\\\": \\\"Nghiệp vụ\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Professional\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Professional\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Dữ liệu\\\", \\\"Value\\\": \\\"3\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 92, \\\"ResourceCode\\\": \\\"ResourceQuantity\\\", \\\"ResourceName\\\": \\\"Dữ liệu\\\"}]\",\"ItemName\":\"Bộ giải pháp Phần mềm Quản lý Tài chính kế toán doanh nghiệp - Gói Professional năm đầu tiên\",\"ModuleName\":null,\"DisplayName\":\"Professional\",\"ProductID\":406,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":6950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": 100, \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}, {\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 100, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}, {\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 3, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nghiệp vụ\\\", \\\"Unit\\\": null, \\\"Value\\\": 17, \\\"ResourceID\\\": 21, \\\"ResourceCode\\\": \\\"Business\\\", \\\"ResourceName\\\": \\\"Nghiệp vụ\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Enterprise\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Enterprise\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Dữ liệu\\\", \\\"Value\\\": \\\"3\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 92, \\\"ResourceCode\\\": \\\"ResourceQuantity\\\", \\\"ResourceName\\\": \\\"Dữ liệu\\\"}]\",\"ItemName\":\"Bộ giải pháp Phần mềm Quản lý Tài chính kế toán doanh nghiệp - Gói Enterprise năm đầu tiên\",\"ModuleName\":null,\"DisplayName\":\"Enterprise\",\"ProductID\":406,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":23000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": 100, \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}, {\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 100, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}, {\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nghiệp vụ\\\", \\\"Unit\\\": null, \\\"Value\\\": 20, \\\"ResourceID\\\": 21, \\\"ResourceCode\\\": \\\"Business\\\", \\\"ResourceName\\\": \\\"Nghiệp vụ\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Enterprise Plus\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Enterprise Plus\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Dữ liệu\\\", \\\"Value\\\": \\\"3\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 92, \\\"ResourceCode\\\": \\\"ResourceQuantity\\\", \\\"ResourceName\\\": \\\"Dữ liệu\\\"}]\",\"ItemName\":\"Bộ giải pháp Phần mềm Quản lý Tài chính kế toán doanh nghiệp - Gói Enterprise Plus năm đầu tiên\",\"ModuleName\":null,\"DisplayName\":\"Enterprise Plus\",\"ProductID\":406,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"QLTS\",\"AppName\":\"MISA Quản lý tài sản\",\"ProductID\":682,\"MarketName\":\"Hành chính sự nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":4000000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Dịch vụ đào tạo trực tuyến cho riêng từng đơn vị\",\"ModuleName\":null,\"DisplayName\":\"Phần mềm Quản lý tài sản MISA QLTS - Dịch vụ đào tạo trực tuyến cho riêng từng đơn vị\",\"ProductID\":682,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4000000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Dịch vụ tập huấn tập trung cho các đơn vị\",\"ModuleName\":null,\"DisplayName\":\"Phần mềm Quản lý tài sản MISA QLTS - Dịch vụ tập huấn tập trung cho các đơn vị\",\"ProductID\":682,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":8000000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Dịch vụ đào tạo trực tiếp cho riêng từng đơn vị\",\"ModuleName\":null,\"DisplayName\":\"Phần mềm Quản lý tài sản MISA QLTS - Dịch vụ đào tạo trực tiếp cho riêng từng đơn vị\",\"ProductID\":682,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2000000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Dịch vụ tập huấn trực tuyến tập trung cho các đơn vị\",\"ModuleName\":null,\"DisplayName\":\"Phần mềm Quản lý tài sản MISA QLTS - Dịch vụ tập huấn trực tuyến tập trung cho các đơn vị\",\"ProductID\":682,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Đơn vị trực thuộc\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 100, \\\"ResourceCode\\\": \\\"DependentUnit\\\", \\\"ResourceName\\\": \\\"Đơn vị trực thuộc\\\"}, {\\\"Name\\\": \\\"Mã gói Suman\\\", \\\"Value\\\": \\\"QLTS.ORG\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 94, \\\"ResourceCode\\\": \\\"SumanPackCode\\\", \\\"ResourceName\\\": \\\"Mã gói Suman\\\"}]\",\"ItemName\":\"Gói dành cho đơn vị trực thuộc\",\"ModuleName\":\"Đơn vị trực thuộc\",\"DisplayName\":\"Gói Đơn vị trực thuộc - năm đầu tiên\",\"ProductID\":682,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":6000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Đơn vị chủ quản\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 99, \\\"ResourceCode\\\": \\\"ManagingUnit\\\", \\\"ResourceName\\\": \\\"Đơn vị chủ quản\\\"}, {\\\"Name\\\": \\\"Mã gói Suman\\\", \\\"Value\\\": \\\"QLTS.SUP\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 94, \\\"ResourceCode\\\": \\\"SumanPackCode\\\", \\\"ResourceName\\\": \\\"Mã gói Suman\\\"}]\",\"ItemName\":\"Gói dành cho đơn vị chủ quản\",\"ModuleName\":\"Đơn vị chủ quản\",\"DisplayName\":\"Gói Đơn vị chủ quản - năm đầu tiên\",\"ProductID\":682,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"SME\",\"AppName\":\"MISA SME 2023\",\"ProductID\":679,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":1550000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Số lượng người dùng\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 83, \\\"ResourceCode\\\": \\\"NumberOfUser\\\", \\\"ResourceName\\\": \\\"Số lượng người dùng\\\"}]\",\"ItemName\":\"Phần mềm MISA SME bản trả phí định kỳ - Mua thêm 01 người dùng gói Standard\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 01 người dùng gói Standard\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Số lượng người dùng\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 83, \\\"ResourceCode\\\": \\\"NumberOfUser\\\", \\\"ResourceName\\\": \\\"Số lượng người dùng\\\"}]\",\"ItemName\":\"Phần mềm MISA SME bản trả phí định kỳ - Mua thêm 01 người dùng gói Professional\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 01 người dùng gói Professional\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2350000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Số lượng người dùng\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 83, \\\"ResourceCode\\\": \\\"NumberOfUser\\\", \\\"ResourceName\\\": \\\"Số lượng người dùng\\\"}]\",\"ItemName\":\"Phần mềm MISA SME bản trả phí định kỳ - Mua thêm 01 người dùng gói Enterprise\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 01 người dùng gói Enterprise\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2650000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Số lượng người dùng\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 83, \\\"ResourceCode\\\": \\\"NumberOfUser\\\", \\\"ResourceName\\\": \\\"Số lượng người dùng\\\"}]\",\"ItemName\":\"Phần mềm MISA SME bản trả phí 1 lần - Mua thêm 01 người dùng gói Standard\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 01 người dùng gói Standard\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3650000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Số lượng người dùng\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 83, \\\"ResourceCode\\\": \\\"NumberOfUser\\\", \\\"ResourceName\\\": \\\"Số lượng người dùng\\\"}]\",\"ItemName\":\"Phần mềm MISA SME bản trả phí 1 lần - Mua thêm 01 người dùng gói Professional\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 01 người dùng gói Professional\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4650000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Số lượng người dùng\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 83, \\\"ResourceCode\\\": \\\"NumberOfUser\\\", \\\"ResourceName\\\": \\\"Số lượng người dùng\\\"}]\",\"ItemName\":\"Phần mềm MISA SME bản trả phí 1 lần - Mua thêm 1 người dùng gói Enterprise\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 01 người dùng gói Enterprise\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Phần mềm MISA SME bản trả phí định kỳ - Đào tạo phần mềm gói 1 kèm 1 trực tuyến\",\"ModuleName\":null,\"DisplayName\":\"Đào tạo phần mềm gói 1 kèm 1 trực tuyến\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":0.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Phần mềm MISA SME bản trả phí định kỳ - Đào tạo phần mềm gói tập trung trực tuyến\",\"ModuleName\":null,\"DisplayName\":\"Đào tạo phần mềm gói tập trung trực tuyến\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":20000000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Phần mềm MISA SME bản trả phí định kỳ - Tư vấn triển khai phần mềm\",\"ModuleName\":null,\"DisplayName\":\"Tư vấn triển khai phần mềm\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Phần mềm MISA SME bản trả phí định kỳ - Đào tạo phần mềm gói 1 kèm 1 trực tiếp\",\"ModuleName\":null,\"DisplayName\":\"Đào tạo phần mềm gói 1 kèm 1 trực tiếp\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Phần mềm MISA SME bản trả phí 1 lần - Đào tạo phần mềm gói 1 kèm 1 trực tiếp\",\"ModuleName\":null,\"DisplayName\":\"Đào tạo phần mềm gói 1 kèm 1 trực tiếp\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Phần mềm MISA SME bản trả phí 1 lần - Đào tạo phần mềm 1 kèm 1 trực tuyến\",\"ModuleName\":null,\"DisplayName\":\"Đào tạo phần mềm 1 kèm 1 trực tuyến\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":0.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Phần mềm MISA SME bản trả phí 1 lần - Đào tạo phần mềm tập trung trực tuyến\",\"ModuleName\":null,\"DisplayName\":\"Đào tạo phần mềm tập trung trực tuyến\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":20000000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Phần mềm MISA SME bản trả phí 1 lần - Tư vấn triển khai phần mềm\",\"ModuleName\":null,\"DisplayName\":\"Tư vấn triển khai phần mềm\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4650000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Logo\\\", \\\"Value\\\": \\\"\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 87, \\\"ResourceCode\\\": \\\"Logo\\\", \\\"ResourceName\\\": \\\"Logo\\\"}, {\\\"Name\\\": \\\"Loại giấy phép\\\", \\\"Value\\\": 3, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 86, \\\"ResourceCode\\\": \\\"LicenseType\\\", \\\"ResourceName\\\": \\\"Loại giấy phép\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"Standard\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"Standard\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Dòng sản phẩm\\\", \\\"Value\\\": \\\"SME2023\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 85, \\\"ResourceCode\\\": \\\"ProductLine\\\", \\\"ResourceName\\\": \\\"Dòng sản phẩm\\\"}, {\\\"Name\\\": \\\"Số lượng người dùng\\\", \\\"Value\\\": 3, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 83, \\\"ResourceCode\\\": \\\"NumberOfUser\\\", \\\"ResourceName\\\": \\\"Số lượng người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói (SME, CukCuk)\\\", \\\"Value\\\": \\\"SME.STD\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 88, \\\"ResourceCode\\\": \\\"ProductPackCode\\\", \\\"ResourceName\\\": \\\"Mã gói (SME, CukCuk)\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Standard\",\"ModuleName\":\"Trả phí định kỳ\",\"DisplayName\":\"Gói Standard\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Logo\\\", \\\"Value\\\": \\\"\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 87, \\\"ResourceCode\\\": \\\"Logo\\\", \\\"ResourceName\\\": \\\"Logo\\\"}, {\\\"Name\\\": \\\"Loại giấy phép\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 86, \\\"ResourceCode\\\": \\\"LicenseType\\\", \\\"ResourceName\\\": \\\"Loại giấy phép\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"Standard\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"Standard\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Dòng sản phẩm\\\", \\\"Value\\\": \\\"SME2023\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 85, \\\"ResourceCode\\\": \\\"ProductLine\\\", \\\"ResourceName\\\": \\\"Dòng sản phẩm\\\"}, {\\\"Name\\\": \\\"Số lượng người dùng\\\", \\\"Value\\\": 3, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 83, \\\"ResourceCode\\\": \\\"NumberOfUser\\\", \\\"ResourceName\\\": \\\"Số lượng người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói (SME, CukCuk)\\\", \\\"Value\\\": \\\"SME.STD\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 88, \\\"ResourceCode\\\": \\\"ProductPackCode\\\", \\\"ResourceName\\\": \\\"Mã gói (SME, CukCuk)\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Standard\",\"ModuleName\":\"Trả phí 1 lần\",\"DisplayName\":\"Gói Standard\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5850000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Logo\\\", \\\"Value\\\": \\\"\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 87, \\\"ResourceCode\\\": \\\"Logo\\\", \\\"ResourceName\\\": \\\"Logo\\\"}, {\\\"Name\\\": \\\"Loại giấy phép\\\", \\\"Value\\\": 3, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 86, \\\"ResourceCode\\\": \\\"LicenseType\\\", \\\"ResourceName\\\": \\\"Loại giấy phép\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"Professional\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"Professional\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Dòng sản phẩm\\\", \\\"Value\\\": \\\"SME2023\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 85, \\\"ResourceCode\\\": \\\"ProductLine\\\", \\\"ResourceName\\\": \\\"Dòng sản phẩm\\\"}, {\\\"Name\\\": \\\"Số lượng người dùng\\\", \\\"Value\\\": 3, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 83, \\\"ResourceCode\\\": \\\"NumberOfUser\\\", \\\"ResourceName\\\": \\\"Số lượng người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói (SME, CukCuk)\\\", \\\"Value\\\": \\\"SME.PRO\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 88, \\\"ResourceCode\\\": \\\"ProductPackCode\\\", \\\"ResourceName\\\": \\\"Mã gói (SME, CukCuk)\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Professional\",\"ModuleName\":\"Trả phí định kỳ\",\"DisplayName\":\"Gói Professional\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":10950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Logo\\\", \\\"Value\\\": \\\"\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 87, \\\"ResourceCode\\\": \\\"Logo\\\", \\\"ResourceName\\\": \\\"Logo\\\"}, {\\\"Name\\\": \\\"Loại giấy phép\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 86, \\\"ResourceCode\\\": \\\"LicenseType\\\", \\\"ResourceName\\\": \\\"Loại giấy phép\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"Professional\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"Professional\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Dòng sản phẩm\\\", \\\"Value\\\": \\\"SME2023\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 85, \\\"ResourceCode\\\": \\\"ProductLine\\\", \\\"ResourceName\\\": \\\"Dòng sản phẩm\\\"}, {\\\"Name\\\": \\\"Số lượng người dùng\\\", \\\"Value\\\": 3, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 83, \\\"ResourceCode\\\": \\\"NumberOfUser\\\", \\\"ResourceName\\\": \\\"Số lượng người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói (SME, CukCuk)\\\", \\\"Value\\\": \\\"SME.PRO\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 88, \\\"ResourceCode\\\": \\\"ProductPackCode\\\", \\\"ResourceName\\\": \\\"Mã gói (SME, CukCuk)\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Professional\",\"ModuleName\":\"Trả phí 1 lần\",\"DisplayName\":\"Gói Professional\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7050000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Logo\\\", \\\"Value\\\": \\\"\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 87, \\\"ResourceCode\\\": \\\"Logo\\\", \\\"ResourceName\\\": \\\"Logo\\\"}, {\\\"Name\\\": \\\"Loại giấy phép\\\", \\\"Value\\\": 3, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 86, \\\"ResourceCode\\\": \\\"LicenseType\\\", \\\"ResourceName\\\": \\\"Loại giấy phép\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"Enterprise\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"Enterprise\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Dòng sản phẩm\\\", \\\"Value\\\": \\\"SME2023\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 85, \\\"ResourceCode\\\": \\\"ProductLine\\\", \\\"ResourceName\\\": \\\"Dòng sản phẩm\\\"}, {\\\"Name\\\": \\\"Số lượng người dùng\\\", \\\"Value\\\": 3, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 83, \\\"ResourceCode\\\": \\\"NumberOfUser\\\", \\\"ResourceName\\\": \\\"Số lượng người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói (SME, CukCuk)\\\", \\\"Value\\\": \\\"SME.ENT\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 88, \\\"ResourceCode\\\": \\\"ProductPackCode\\\", \\\"ResourceName\\\": \\\"Mã gói (SME, CukCuk)\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Enterprise\",\"ModuleName\":\"Trả phí định kỳ\",\"DisplayName\":\"Gói Enterprise\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":13950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Logo\\\", \\\"Value\\\": \\\"\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 87, \\\"ResourceCode\\\": \\\"Logo\\\", \\\"ResourceName\\\": \\\"Logo\\\"}, {\\\"Name\\\": \\\"Loại giấy phép\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 86, \\\"ResourceCode\\\": \\\"LicenseType\\\", \\\"ResourceName\\\": \\\"Loại giấy phép\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"Enterprise\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"Enterprise\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Dòng sản phẩm\\\", \\\"Value\\\": \\\"SME2023\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 85, \\\"ResourceCode\\\": \\\"ProductLine\\\", \\\"ResourceName\\\": \\\"Dòng sản phẩm\\\"}, {\\\"Name\\\": \\\"Số lượng người dùng\\\", \\\"Value\\\": 3, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 83, \\\"ResourceCode\\\": \\\"NumberOfUser\\\", \\\"ResourceName\\\": \\\"Số lượng người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói (SME, CukCuk)\\\", \\\"Value\\\": \\\"SME.ENT\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 88, \\\"ResourceCode\\\": \\\"ProductPackCode\\\", \\\"ResourceName\\\": \\\"Mã gói (SME, CukCuk)\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Enterprise\",\"ModuleName\":\"Trả phí 1 lần\",\"DisplayName\":\"Gói Enterprise\",\"ProductID\":679,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"Mshopkeeper\",\"AppName\":\"MISA eShop\",\"ProductID\":678,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":199000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"MSHO.STT\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Số lượng chi nhánh\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 93, \\\"ResourceCode\\\": \\\"NumberOfBranch\\\", \\\"ResourceName\\\": \\\"Số lượng chi nhánh\\\"}]\",\"ItemName\":\"Mua thêm chi nhánh gói Starter\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm chi nhánh gói Starter\",\"ProductID\":678,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":299000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"MSHO.STD\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Số lượng chi nhánh\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 93, \\\"ResourceCode\\\": \\\"NumberOfBranch\\\", \\\"ResourceName\\\": \\\"Số lượng chi nhánh\\\"}]\",\"ItemName\":\"Mua thêm chi nhánh gói Standard\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm chi nhánh gói Standard\",\"ProductID\":678,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":299000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"MSHO.PRO\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Số lượng chi nhánh\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 93, \\\"ResourceCode\\\": \\\"NumberOfBranch\\\", \\\"ResourceName\\\": \\\"Số lượng chi nhánh\\\"}]\",\"ItemName\":\"Mua thêm chi nhánh gói Professional\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm chi nhánh gói Professional\",\"ProductID\":678,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":299000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"MSHO.ENT\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Số lượng chi nhánh\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 93, \\\"ResourceCode\\\": \\\"NumberOfBranch\\\", \\\"ResourceName\\\": \\\"Số lượng chi nhánh\\\"}]\",\"ItemName\":\"Mua thêm chi nhánh gói Enterprise\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm chi nhánh gói Enterprise\",\"ProductID\":678,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Đào tạo trực tuyến 1 kèm 1 phần mềm MISA eShop\",\"ModuleName\":null,\"DisplayName\":\"Đào tạo trực tuyến 1 kèm 1 phần mềm MISA eShop\",\"ProductID\":678,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":0.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Đào tạo trực tuyến tập trung phần mềm MISA eShop\",\"ModuleName\":null,\"DisplayName\":\"Đào tạo trực tuyến tập trung phần mềm MISA eShop\",\"ProductID\":678,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Tư vấn triển khai phần mềm MISA eShop\",\"ModuleName\":null,\"DisplayName\":\"Tư vấn triển khai phần mềm MISA eShop\",\"ProductID\":678,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Tư vấn triển khai phần mềm MISA Lomas cho khách hàng eShop\",\"ModuleName\":null,\"DisplayName\":\"Tư vấn triển khai phần mềm MISA Lomas cho khách hàng eShop\",\"ProductID\":678,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Đào tạo trực tuyến 1 kèm 1 phần mềm MISA Lomas trên MISA eShop\",\"ModuleName\":null,\"DisplayName\":\"Đào tạo trực tuyến 1 kèm 1 phần mềm MISA Lomas trên MISA eShop\",\"ProductID\":678,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":0.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Đào tạo trực tuyến tập trung phần mềm MISA Lomas trên MISA eShop\",\"ModuleName\":null,\"DisplayName\":\"Đào tạo trực tuyến tập trung phần mềm MISA Lomas trên MISA eShop\",\"ProductID\":678,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":0.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"MSHO.TRL\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"Trial\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo ngày\\\", \\\"Value\\\": 15, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 23, \\\"ResourceCode\\\": \\\"DurationByDay\\\", \\\"ResourceName\\\": \\\"Thời hạn theo ngày\\\"}, {\\\"Name\\\": \\\"Số lượng chi nhánh\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 93, \\\"ResourceCode\\\": \\\"NumberOfBranch\\\", \\\"ResourceName\\\": \\\"Số lượng chi nhánh\\\"}]\",\"ItemName\":\"Dùng thử\",\"ModuleName\":null,\"DisplayName\":\"Gói dùng thử 15 ngày eShop\",\"ProductID\":678,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":199000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"MSHO.STT\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"Starter\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo tháng\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 22, \\\"ResourceCode\\\": \\\"DurationByMonth\\\", \\\"ResourceName\\\": \\\"Thời hạn theo tháng\\\"}, {\\\"Name\\\": \\\"Số lượng chi nhánh\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 93, \\\"ResourceCode\\\": \\\"NumberOfBranch\\\", \\\"ResourceName\\\": \\\"Số lượng chi nhánh\\\"}]\",\"ItemName\":\"Starter\",\"ModuleName\":null,\"DisplayName\":\"Starter\",\"ProductID\":678,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":299000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"MSHO.STD\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"Standard\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo tháng\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 22, \\\"ResourceCode\\\": \\\"DurationByMonth\\\", \\\"ResourceName\\\": \\\"Thời hạn theo tháng\\\"}, {\\\"Name\\\": \\\"Số lượng chi nhánh\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 93, \\\"ResourceCode\\\": \\\"NumberOfBranch\\\", \\\"ResourceName\\\": \\\"Số lượng chi nhánh\\\"}]\",\"ItemName\":\"Standard\",\"ModuleName\":null,\"DisplayName\":\"Standard\",\"ProductID\":678,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":499000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"MSHO.PRO\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"Professional\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo tháng\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 22, \\\"ResourceCode\\\": \\\"DurationByMonth\\\", \\\"ResourceName\\\": \\\"Thời hạn theo tháng\\\"}, {\\\"Name\\\": \\\"Số lượng chi nhánh\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 93, \\\"ResourceCode\\\": \\\"NumberOfBranch\\\", \\\"ResourceName\\\": \\\"Số lượng chi nhánh\\\"}]\",\"ItemName\":\"Professional\",\"ModuleName\":null,\"DisplayName\":\"Professional\",\"ProductID\":678,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":599000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"MSHO.ENT\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"Enterprise\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo tháng\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 22, \\\"ResourceCode\\\": \\\"DurationByMonth\\\", \\\"ResourceName\\\": \\\"Thời hạn theo tháng\\\"}, {\\\"Name\\\": \\\"Số lượng chi nhánh\\\", \\\"Value\\\": \\\"1\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 93, \\\"ResourceCode\\\": \\\"NumberOfBranch\\\", \\\"ResourceName\\\": \\\"Số lượng chi nhánh\\\"}]\",\"ItemName\":\"Enterprise\",\"ModuleName\":null,\"DisplayName\":\"Enterprise\",\"ProductID\":678,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":399000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo tháng\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 22, \\\"ResourceCode\\\": \\\"DurationByMonth\\\", \\\"ResourceName\\\": \\\"Thời hạn theo tháng\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"LOMAS\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Là gói lomas\\\", \\\"Value\\\": \\\"true\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 96, \\\"ResourceCode\\\": \\\"IsLomas\\\", \\\"ResourceName\\\": \\\"Là gói lomas\\\"}]\",\"ItemName\":\"MISA Lomas\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm MISA Lomas\",\"ProductID\":678,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"mTax\",\"AppName\":\"Thuế điện tử MISA mTax\",\"ProductID\":505,\"MarketName\":\"Cá nhân\",\"ListPackageProduct\":[{\"ItemPrice\":1045000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"mTax\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"mTax\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"1 năm\",\"ModuleName\":null,\"DisplayName\":\"Gói 1 năm\",\"ProductID\":505,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1870000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"mTax\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"mTax\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 2, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"2 năm \",\"ModuleName\":null,\"DisplayName\":\"Gói 2 năm\",\"ProductID\":505,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2585000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"mTax\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"mTax\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 3, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"3 năm\",\"ModuleName\":null,\"DisplayName\":\"Gói 3 năm\",\"ProductID\":505,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3960000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"mTax\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"mTax\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 5, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"5 năm\",\"ModuleName\":null,\"DisplayName\":\"Gói 5 năm\",\"ProductID\":505,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"Combo_eSign_DN\",\"AppName\":\"MISA eSign – Chữ ký số USB Token cho Doanh nghiệp\",\"ProductID\":675,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":1049000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Dịch vụ chữ ký số MISA eSign cho Cá nhân trong Tổ chức gói mua mới 1 năm đã bao gồm USB Token\",\"ModuleName\":\"Cá nhân trong tổ chức\",\"DisplayName\":\"1 năm\",\"ProductID\":675,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1829000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Dịch vụ chữ ký số MISA eSign cho Tổ chức gói mua mới 1 năm lần đầu đã bao gồm USB Token\",\"ModuleName\":\"Tổ chức\",\"DisplayName\":\"1 năm\",\"ProductID\":675,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1449000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Dịch vụ chữ ký số MISA eSign cho Cá nhân trong Tổ chức gói mua mới 2 năm đã bao gồm USB Token\",\"ModuleName\":\"Cá nhân trong tổ chức\",\"DisplayName\":\"2 năm\",\"ProductID\":675,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2729000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Dịch vụ chữ ký số MISA eSign cho Tổ chức gói mua mới 2 năm lần đầu đã bao gồm USB Token\",\"ModuleName\":\"Tổ chức\",\"DisplayName\":\"2 năm\",\"ProductID\":675,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1749000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Dịch vụ chữ ký số MISA eSign cho Cá nhân trong Tổ chức gói mua mới 3 năm đã bao gồm USB Token\",\"ModuleName\":\"Cá nhân trong tổ chức\",\"DisplayName\":\"3 năm\",\"ProductID\":675,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3529000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Dịch vụ chữ ký số MISA eSign cho Tổ chức gói mua mới 3 năm lần đầu đã bao gồm USB Token\",\"ModuleName\":\"Tổ chức\",\"DisplayName\":\"3 năm\",\"ProductID\":675,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2049000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Dịch vụ chữ ký số MISA eSign cho Cá nhân trong Tổ chức gói mua mới 4 năm đã bao gồm USB Token\",\"ModuleName\":\"Cá nhân trong tổ chức\",\"DisplayName\":\"4 năm\",\"ProductID\":675,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2349000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Dịch vụ chữ ký số MISA eSign cho Cá nhân trong Tổ chức mua mới 5 năm đã bao gồm USB Token\",\"ModuleName\":\"Cá nhân trong tổ chức\",\"DisplayName\":\"5 năm\",\"ProductID\":675,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4329000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Dịch vụ chữ ký số MISA eSign cho Tổ chức gói mua mới 4 năm đã bao gồm USB Token\",\"ModuleName\":\"Tổ chức\",\"DisplayName\":\"4 năm\",\"ProductID\":675,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5029000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Dịch vụ chữ ký số MISA eSign cho Tổ chức gói mua mới 5 năm đã bao gồm USB Token\",\"ModuleName\":\"Tổ chức\",\"DisplayName\":\"5 năm\",\"ProductID\":675,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"HRMCombo\",\"AppName\":\"Bộ giải pháp quản trị nguồn nhân lực\",\"ProductID\":491,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":7950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm Quản trị nguồn nhân lực MISA AMIS HRM - Đào tạo 1 kèm 1 trực tuyến gói Standard\",\"ModuleName\":null,\"DisplayName\":\"Đào tạo gói Standard\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm Quản trị nguồn nhân lực MISA AMIS HRM - Đào tạo 1 kèm 1 trực tiếp gói Standard\",\"ModuleName\":null,\"DisplayName\":\"Đào tạo gói Standard\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":20000000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm Quản trị nguồn nhân lực MISA AMIS HRM - Tư vấn triển khai gói Standard\",\"ModuleName\":null,\"DisplayName\":\"Tư vấn triển khai gói Standard\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm Quản trị nguồn nhân lực MISA AMIS HRM - Đào tạo 1 kèm 1 trực tuyến gói Professional\",\"ModuleName\":null,\"DisplayName\":\"Đào tạo gói Professional\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm Quản trị nguồn nhân lực MISA AMIS HRM - Đào tạo 1 kèm 1 trực tiếp gói Professsional\",\"ModuleName\":null,\"DisplayName\":\"Đào tạo gói Professsional\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":20000000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm Quản trị nguồn nhân lực MISA AMIS HRM - Tư vấn triển khai gói Professional\",\"ModuleName\":null,\"DisplayName\":\"Tư vấn triển khai gói Professional\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1400000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng AMIS Thông tin nhân sự\",\"ModuleName\":null,\"DisplayName\":\"AMIS Thông tin nhân sự - Mua thêm 10 người dùng\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1700000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng AMIS Chấm công\",\"ModuleName\":null,\"DisplayName\":\"AMIS Chấm công - Mua thêm 10 người dùng\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1700000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng AMIS Tiền lương\",\"ModuleName\":null,\"DisplayName\":\"AMIS Tiền lương - Mua thêm 10 người dùng\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":80000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng AMIS Thuế TNCN\",\"ModuleName\":null,\"DisplayName\":\"AMIS Thuế TNCN - Mua thêm 10 người dùng\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":80000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng AMIS BHXH\",\"ModuleName\":null,\"DisplayName\":\"AMIS BHXH - Mua thêm 10 người dùng\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":320000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 hồ sơ nhân viên AMIS Thông tin nhân sự\",\"ModuleName\":null,\"DisplayName\":\"AMIS Thông tin nhân sự - Mua thêm 10 hồ sơ nhân viên\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":380000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 hồ sơ nhân viên AMIS Chấm công\",\"ModuleName\":null,\"DisplayName\":\"AMIS Chấm công - Mua thêm 10 hồ sơ nhân viên\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":380000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 hồ sơ nhân viên AMIS Tiền lương\",\"ModuleName\":null,\"DisplayName\":\"AMIS Tiền lương - Mua thêm 10 hồ sơ nhân viên\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1400000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng AMIS Mục tiêu\",\"ModuleName\":null,\"DisplayName\":\"AMIS Mục tiêu - Mua thêm 10 người dùng\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1400000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng AMIS Đánh giá\",\"ModuleName\":null,\"DisplayName\":\"AMIS Đánh giá - Mua thêm 10 người dùng\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1400000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng AMIS Mạng xã hội\",\"ModuleName\":null,\"DisplayName\":\"AMIS Mạng xã hội - Mua thêm 10 người dùng\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":12600000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm Quản trị nguồn nhân lực MISA AMIS HRM - Gói Standard năm đầu tiên\",\"ModuleName\":null,\"DisplayName\":\"Standard\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":18000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm Quản trị nguồn nhân lực MISA AMIS HRM - Gói Professional năm đầu tiên\",\"ModuleName\":null,\"DisplayName\":\"Professional\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4200000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng gói Standard\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10 người dùng gói Standard\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":6000000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng gói Professional\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10 người dùng gói Professional\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":756000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 hồ sơ nhân viên\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10 hồ sơ nhân viên\",\"ProductID\":491,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"APU\",\"AppName\":\"AMIS Mua hàng\",\"ProductID\":477,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":4450000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 01 người dùng\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 01 người dùng\",\"ProductID\":477,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":8900000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 2, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Mua hàng\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Mua hàng\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"AMIS Mua hàng\",\"ModuleName\":null,\"DisplayName\":\"Phần mềm AMIS Mua hàng\",\"ProductID\":477,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"Recruitment\",\"AppName\":\"AMIS Tuyển dụng\",\"ProductID\":457,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":5400000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 nhân viên gói Enterprise Plus\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10 nhân viên gói Enterprise Plus\",\"ProductID\":457,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4500000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 5, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 5, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Starter\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Starter\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Starter\",\"ModuleName\":null,\"DisplayName\":\"Stater\",\"ProductID\":457,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":8400000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Standard\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Standard\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Standard\",\"ModuleName\":null,\"DisplayName\":\"Standard\",\"ProductID\":457,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":15600000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 20, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 20, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Professional\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Professional\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Professional\",\"ModuleName\":null,\"DisplayName\":\"Professional\",\"ProductID\":457,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":21600000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Enterprise\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Enterprise\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Enterprise\",\"ModuleName\":null,\"DisplayName\":\"Enterprise\",\"ProductID\":457,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":33000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 50, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 50, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Enterprise Plus\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Enterprise Plus\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Enterprise Plus\",\"ModuleName\":null,\"DisplayName\":\"Enterprise Plus\",\"ProductID\":457,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"Goal\",\"AppName\":\"AMIS Mục tiêu\",\"ProductID\":456,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":2300000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10 người dùng\",\"ProductID\":456,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":6900000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Mục tiêu\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Mục tiêu\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"AMIS Mục tiêu\",\"ModuleName\":null,\"DisplayName\":\"Phần mềm AMIS Mục tiêu\",\"ProductID\":456,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"Review\",\"AppName\":\"AMIS Đánh giá\",\"ProductID\":455,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":2300000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10 người dùng\",\"ProductID\":455,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":6900000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Đánh giá\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Đánh giá\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"AMIS Đánh giá\",\"ModuleName\":null,\"DisplayName\":\"Phần mềm AMIS Đánh giá\",\"ProductID\":455,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"MinTax\",\"AppName\":\"AMIS Thuế TNCN\",\"ProductID\":454,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":80000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10 người dùng\",\"ProductID\":454,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":240000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Thuế TNCN\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Thuế TNCN\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"AMIS Thuế TNCN\",\"ModuleName\":null,\"DisplayName\":\"Phần mềm AMIS Thuế TNCN\",\"ProductID\":454,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"MISAIVAN\",\"AppName\":\"AMIS Bảo hiểm xã hội\",\"ProductID\":453,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":80000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10 người dùng\",\"ProductID\":453,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":240000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS BHXH\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS BHXH\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"AMIS BHXH\",\"ModuleName\":null,\"DisplayName\":\"Phần mềm AMIS BHXH\",\"ProductID\":453,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"Payroll\",\"AppName\":\"AMIS Tiền lương\",\"ProductID\":451,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":380000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 hồ sơ nhân viên\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10 hồ sơ nhân viên\",\"ProductID\":451,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1700000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10 người dùng\",\"ProductID\":451,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5100000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Tiền lương\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Tiền lương\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"AMIS Tiền lương\",\"ModuleName\":null,\"DisplayName\":\"Phần mềm AMIS Tiền lương\",\"ProductID\":451,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"Timesheet\",\"AppName\":\"AMIS Chấm công\",\"ProductID\":450,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":380000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 hồ sơ nhân viên\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10 hồ sơ nhân viên\",\"ProductID\":450,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1700000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10 người dùng\",\"ProductID\":450,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5100000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Chấm công\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Chấm công\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"AMIS Chấm công\",\"ModuleName\":null,\"DisplayName\":\"Phần mềm AMIS Chấm công\",\"ProductID\":450,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"EmployeesProfile\",\"AppName\":\"AMIS Thông tin nhân sự\",\"ProductID\":449,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":320000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 hồ sơ nhân viên\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10 hồ sơ nhân viên\",\"ProductID\":449,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Gói đào tạo phần mềm 1 kèm 1 trực tuyến\",\"ModuleName\":null,\"DisplayName\":\"Gói đào tạo phần mềm\",\"ProductID\":449,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Gói đào tạo phần mềm 1 kèm 1 trực tiếp\",\"ModuleName\":null,\"DisplayName\":\"Gói đào tạo phần mềm\",\"ProductID\":449,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":20000000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Tư vấn triển khai phần mềm\",\"ModuleName\":null,\"DisplayName\":\"Tư vấn triển khai phần mềm\",\"ProductID\":449,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1400000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10 người dùng\",\"ProductID\":449,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4200000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nhân viên\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 14, \\\"ResourceCode\\\": \\\"Employee\\\", \\\"ResourceName\\\": \\\"Nhân viên\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Thông tin nhân sự\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Thông tin nhân sự\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"AMIS Thông tin nhân sự\",\"ModuleName\":null,\"DisplayName\":\"Phần mềm AMIS Thông tin nhân sự\",\"ProductID\":449,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"aimkt\",\"AppName\":\"AMIS aiMarketing\",\"ProductID\":448,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":250000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Email gửi tự động\\\", \\\"Unit\\\": null, \\\"Value\\\": 10000, \\\"ResourceID\\\": 9, \\\"ResourceCode\\\": \\\"Email\\\", \\\"ResourceName\\\": \\\"Email gửi tự động\\\"}]\",\"ItemName\":\"Mua thêm 10.000 email quảng cáo\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10.000 email quảng cáo\",\"ProductID\":448,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2900000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"CTA\\\", \\\"Unit\\\": null, \\\"Value\\\": 0, \\\"ResourceID\\\": 7, \\\"ResourceCode\\\": \\\"Cta\\\", \\\"ResourceName\\\": \\\"CTA\\\"}, {\\\"Name\\\": \\\"Form\\\", \\\"Unit\\\": null, \\\"Value\\\": 0, \\\"ResourceID\\\": 20, \\\"ResourceCode\\\": \\\"Form\\\", \\\"ResourceName\\\": \\\"Form\\\"}, {\\\"Name\\\": \\\"Landing page xuất bản\\\", \\\"Unit\\\": null, \\\"Value\\\": 0, \\\"ResourceID\\\": 8, \\\"ResourceCode\\\": \\\"Page\\\", \\\"ResourceName\\\": \\\"Landing page xuất bản\\\"}, {\\\"Name\\\": \\\"Email gửi tự động\\\", \\\"Unit\\\": null, \\\"Value\\\": 60000, \\\"ResourceID\\\": 9, \\\"ResourceCode\\\": \\\"Email\\\", \\\"ResourceName\\\": \\\"Email gửi tự động\\\"}, {\\\"Name\\\": \\\"Liên hệ lưu trữ\\\", \\\"Unit\\\": null, \\\"Value\\\": 10000, \\\"ResourceID\\\": 11, \\\"ResourceCode\\\": \\\"Contact\\\", \\\"ResourceName\\\": \\\"Liên hệ lưu trữ\\\"}, {\\\"Name\\\": \\\"Kịch bản tự động\\\", \\\"Unit\\\": null, \\\"Value\\\": 0, \\\"ResourceID\\\": 15, \\\"ResourceCode\\\": \\\"Workflows\\\", \\\"ResourceName\\\": \\\"Kịch bản tự động\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Email Marketing\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Email Marketing\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Email Marketing\",\"ModuleName\":null,\"DisplayName\":\"Email Marketing\",\"ProductID\":448,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":8900000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"CTA\\\", \\\"Unit\\\": null, \\\"Value\\\": -1, \\\"ResourceID\\\": 7, \\\"ResourceCode\\\": \\\"Cta\\\", \\\"ResourceName\\\": \\\"CTA\\\"}, {\\\"Name\\\": \\\"Form\\\", \\\"Unit\\\": null, \\\"Value\\\": -1, \\\"ResourceID\\\": 20, \\\"ResourceCode\\\": \\\"Form\\\", \\\"ResourceName\\\": \\\"Form\\\"}, {\\\"Name\\\": \\\"Landing page xuất bản\\\", \\\"Unit\\\": null, \\\"Value\\\": 20, \\\"ResourceID\\\": 8, \\\"ResourceCode\\\": \\\"Page\\\", \\\"ResourceName\\\": \\\"Landing page xuất bản\\\"}, {\\\"Name\\\": \\\"Email gửi tự động\\\", \\\"Unit\\\": null, \\\"Value\\\": 60000, \\\"ResourceID\\\": 9, \\\"ResourceCode\\\": \\\"Email\\\", \\\"ResourceName\\\": \\\"Email gửi tự động\\\"}, {\\\"Name\\\": \\\"Liên hệ lưu trữ\\\", \\\"Unit\\\": null, \\\"Value\\\": 10000, \\\"ResourceID\\\": 11, \\\"ResourceCode\\\": \\\"Contact\\\", \\\"ResourceName\\\": \\\"Liên hệ lưu trữ\\\"}, {\\\"Name\\\": \\\"Kịch bản tự động\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 15, \\\"ResourceCode\\\": \\\"Workflows\\\", \\\"ResourceName\\\": \\\"Kịch bản tự động\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Starter\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Starter\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Starter\",\"ModuleName\":null,\"DisplayName\":\"Starter\",\"ProductID\":448,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":15900000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"CTA\\\", \\\"Unit\\\": null, \\\"Value\\\": -1, \\\"ResourceID\\\": 7, \\\"ResourceCode\\\": \\\"Cta\\\", \\\"ResourceName\\\": \\\"CTA\\\"}, {\\\"Name\\\": \\\"Form\\\", \\\"Unit\\\": null, \\\"Value\\\": -1, \\\"ResourceID\\\": 20, \\\"ResourceCode\\\": \\\"Form\\\", \\\"ResourceName\\\": \\\"Form\\\"}, {\\\"Name\\\": \\\"Landing page xuất bản\\\", \\\"Unit\\\": null, \\\"Value\\\": 50, \\\"ResourceID\\\": 8, \\\"ResourceCode\\\": \\\"Page\\\", \\\"ResourceName\\\": \\\"Landing page xuất bản\\\"}, {\\\"Name\\\": \\\"Email gửi tự động\\\", \\\"Unit\\\": null, \\\"Value\\\": 200000, \\\"ResourceID\\\": 9, \\\"ResourceCode\\\": \\\"Email\\\", \\\"ResourceName\\\": \\\"Email gửi tự động\\\"}, {\\\"Name\\\": \\\"Liên hệ lưu trữ\\\", \\\"Unit\\\": null, \\\"Value\\\": 30000, \\\"ResourceID\\\": 11, \\\"ResourceCode\\\": \\\"Contact\\\", \\\"ResourceName\\\": \\\"Liên hệ lưu trữ\\\"}, {\\\"Name\\\": \\\"Kịch bản tự động\\\", \\\"Unit\\\": null, \\\"Value\\\": 25, \\\"ResourceID\\\": 15, \\\"ResourceCode\\\": \\\"Workflows\\\", \\\"ResourceName\\\": \\\"Kịch bản tự động\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Standard\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Standard\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Standard\",\"ModuleName\":null,\"DisplayName\":\"Standard\",\"ProductID\":448,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":31900000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"CTA\\\", \\\"Unit\\\": null, \\\"Value\\\": -1, \\\"ResourceID\\\": 7, \\\"ResourceCode\\\": \\\"Cta\\\", \\\"ResourceName\\\": \\\"CTA\\\"}, {\\\"Name\\\": \\\"Form\\\", \\\"Unit\\\": null, \\\"Value\\\": -1, \\\"ResourceID\\\": 20, \\\"ResourceCode\\\": \\\"Form\\\", \\\"ResourceName\\\": \\\"Form\\\"}, {\\\"Name\\\": \\\"Landing page xuất bản\\\", \\\"Unit\\\": null, \\\"Value\\\": -1, \\\"ResourceID\\\": 8, \\\"ResourceCode\\\": \\\"Page\\\", \\\"ResourceName\\\": \\\"Landing page xuất bản\\\"}, {\\\"Name\\\": \\\"Email gửi tự động\\\", \\\"Unit\\\": null, \\\"Value\\\": 800000, \\\"ResourceID\\\": 9, \\\"ResourceCode\\\": \\\"Email\\\", \\\"ResourceName\\\": \\\"Email gửi tự động\\\"}, {\\\"Name\\\": \\\"Liên hệ lưu trữ\\\", \\\"Unit\\\": null, \\\"Value\\\": 80000, \\\"ResourceID\\\": 11, \\\"ResourceCode\\\": \\\"Contact\\\", \\\"ResourceName\\\": \\\"Liên hệ lưu trữ\\\"}, {\\\"Name\\\": \\\"Kịch bản tự động\\\", \\\"Unit\\\": null, \\\"Value\\\": -1, \\\"ResourceID\\\": 15, \\\"ResourceCode\\\": \\\"Workflows\\\", \\\"ResourceName\\\": \\\"Kịch bản tự động\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Professional\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Professional\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Professional\",\"ModuleName\":null,\"DisplayName\":\"Professional\",\"ProductID\":448,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":63900000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"CTA\\\", \\\"Unit\\\": null, \\\"Value\\\": -1, \\\"ResourceID\\\": 7, \\\"ResourceCode\\\": \\\"Cta\\\", \\\"ResourceName\\\": \\\"CTA\\\"}, {\\\"Name\\\": \\\"Form\\\", \\\"Unit\\\": null, \\\"Value\\\": -1, \\\"ResourceID\\\": 20, \\\"ResourceCode\\\": \\\"Form\\\", \\\"ResourceName\\\": \\\"Form\\\"}, {\\\"Name\\\": \\\"Landing page xuất bản\\\", \\\"Unit\\\": null, \\\"Value\\\": -1, \\\"ResourceID\\\": 8, \\\"ResourceCode\\\": \\\"Page\\\", \\\"ResourceName\\\": \\\"Landing page xuất bản\\\"}, {\\\"Name\\\": \\\"Email gửi tự động\\\", \\\"Unit\\\": null, \\\"Value\\\": 2000000, \\\"ResourceID\\\": 9, \\\"ResourceCode\\\": \\\"Email\\\", \\\"ResourceName\\\": \\\"Email gửi tự động\\\"}, {\\\"Name\\\": \\\"Liên hệ lưu trữ\\\", \\\"Unit\\\": null, \\\"Value\\\": 200000, \\\"ResourceID\\\": 11, \\\"ResourceCode\\\": \\\"Contact\\\", \\\"ResourceName\\\": \\\"Liên hệ lưu trữ\\\"}, {\\\"Name\\\": \\\"Kịch bản tự động\\\", \\\"Unit\\\": null, \\\"Value\\\": -1, \\\"ResourceID\\\": 15, \\\"ResourceCode\\\": \\\"Workflows\\\", \\\"ResourceName\\\": \\\"Kịch bản tự động\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Enterprise\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Enterprise\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Enterprise\",\"ModuleName\":null,\"DisplayName\":\"Enterprise\",\"ProductID\":448,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":0.0000,\"ItemType\":1,\"ResourceInfor\":null,\"ItemName\":\"Ultimate\",\"ModuleName\":null,\"DisplayName\":\"Ultimate\",\"ProductID\":448,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"Promotion\",\"AppName\":\"AMIS Khuyến mại\",\"ProductID\":447,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":1200000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 5, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 05 người dùng\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 05 người dùng\",\"ProductID\":447,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2400000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Khuyến mại\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Khuyến mại\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"AMIS Khuyến mại\",\"ModuleName\":null,\"DisplayName\":\"Phần mềm AMIS Khuyến mại\",\"ProductID\":447,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"CRM\",\"AppName\":\"AMIS Bán hàng\",\"ProductID\":446,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":4800000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 5, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 05 người dùng gói Standard\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 05 người dùng gói Standard\",\"ProductID\":446,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":6000000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 5, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 05 người dùng gói Professional\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 05 người dùng gói Professional\",\"ProductID\":446,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7200000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 5, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 05 người dùng gói Enterprise\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 05 người dùng gói Enterprise\",\"ProductID\":446,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":9600000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"CRM2.Standard\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Standard\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Standard\",\"ModuleName\":null,\"DisplayName\":\"Standard\",\"ProductID\":446,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":12000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"CRM2.Professional\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Professional\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Professional\",\"ModuleName\":null,\"DisplayName\":\"Professional\",\"ProductID\":446,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":14400000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"CRM2.Enterprise\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Enterprise\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Enterprise\",\"ModuleName\":null,\"DisplayName\":\"Enterprise\",\"ProductID\":446,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"RemoteSigning\",\"AppName\":\"MISA eSign – Chữ ký số từ xa cho cá nhân\",\"ProductID\":427,\"MarketName\":\"Cá nhân\",\"ListPackageProduct\":[{\"ItemPrice\":550000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"1 năm\",\"ModuleName\":\"Cá nhân\",\"DisplayName\":\"1 năm\",\"ProductID\":427,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 2, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"2 năm\",\"ModuleName\":\"Cá nhân\",\"DisplayName\":\"2 năm\",\"ProductID\":427,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1250000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 3, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"3 năm\",\"ModuleName\":\"Cá nhân\",\"DisplayName\":\"3 năm\",\"ProductID\":427,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1550000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 4, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"4 năm\",\"ModuleName\":\"Cá nhân\",\"DisplayName\":\"4 năm\",\"ProductID\":427,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1850000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 5, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"5 năm\",\"ModuleName\":\"Cá nhân\",\"DisplayName\":\"5 năm\",\"ProductID\":427,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"Meinvoice.vn\",\"AppName\":\"meInvoice Doanh nghiệp - Phát hành hóa đơn\",\"ProductID\":426,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":129950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"1000000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"MEIVE-1.000.000\",\"ModuleName\":\"Vé điện tử\",\"DisplayName\":\"MEIVE-1.000.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":126000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\", \\\"Value\\\": \\\"3000000\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 89, \\\"ResourceCode\\\": \\\"NumberOfPetrol\\\", \\\"ResourceName\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\"}]\",\"ItemName\":\"MEIXD-3.000.000\",\"ModuleName\":\"Hóa đơn bán lẻ xăng dầu\",\"DisplayName\":\"MEIXD-3.000.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":125000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Value\\\": 500000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"MEIR-500.000\",\"ModuleName\":\"Hóa đơn điện tử\",\"DisplayName\":\"MEIR-500.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":129950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Value\\\": 1000000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIMTT-1.000.000\",\"ModuleName\":\"Hóa đơn từ máy tính tiền\",\"DisplayName\":\"MEIMTT-1.000.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":74950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"500000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"MEIVE-500.000\",\"ModuleName\":\"Vé điện tử\",\"DisplayName\":\"MEIVE-500.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":50000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\", \\\"Value\\\": \\\"1000000\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 89, \\\"ResourceCode\\\": \\\"NumberOfPetrol\\\", \\\"ResourceName\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\"}]\",\"ItemName\":\"MEIXD-1.000.000\",\"ModuleName\":\"Hóa đơn bán lẻ xăng dầu\",\"DisplayName\":\"MEIXD-1.000.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":84000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Value\\\": 300000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"MEIR-300.000\",\"ModuleName\":\"Hóa đơn điện tử\",\"DisplayName\":\"MEIR-300.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":74950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Value\\\": 500000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIMTT-500.000\",\"ModuleName\":\"Hóa đơn từ máy tính tiền\",\"DisplayName\":\"MEIMTT-500.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":33950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"200000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"MEIVE-200.000\",\"ModuleName\":\"Vé điện tử\",\"DisplayName\":\"MEIVE-200.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":27500000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\", \\\"Value\\\": \\\"500000\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 89, \\\"ResourceCode\\\": \\\"NumberOfPetrol\\\", \\\"ResourceName\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\"}]\",\"ItemName\":\"MEIXD-500.000\",\"ModuleName\":\"Hóa đơn bán lẻ xăng dầu\",\"DisplayName\":\"MEIXD-500.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":60000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Value\\\": 200000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"MEIR-200.000\",\"ModuleName\":\"Hóa đơn điện tử\",\"DisplayName\":\"MEIR-200.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":33950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Value\\\": 200000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIMTT-200.000\",\"ModuleName\":\"Hóa đơn từ máy tính tiền\",\"DisplayName\":\"MEIMTT-200.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":32000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"100000\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"MEIR-100.000\",\"ModuleName\":\"Hóa đơn điện tử\",\"DisplayName\":\"MEIR-100.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":19950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"100000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"MEIVE-100.000\",\"ModuleName\":\"Vé điện tử\",\"DisplayName\":\"MEIVE-100.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":19950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"100000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIMTT-100.000\",\"ModuleName\":\"Hóa đơn từ máy tính tiền\",\"DisplayName\":\"MEIMTT-100.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1550000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"2000\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"MEIR-2.000\",\"ModuleName\":\"Hóa đơn điện tử\",\"DisplayName\":\"MEIR-2.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":18000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\", \\\"Value\\\": \\\"300000\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 89, \\\"ResourceCode\\\": \\\"NumberOfPetrol\\\", \\\"ResourceName\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\"}]\",\"ItemName\":\"MEIXD-300.000\",\"ModuleName\":\"Hóa đơn bán lẻ xăng dầu\",\"DisplayName\":\"MEIXD-300.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11650000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"50000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIMTT-50.000\",\"ModuleName\":\"Hóa đơn từ máy tính tiền\",\"DisplayName\":\"MEIMTT-50000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5650000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"20000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"MEIVE-20.000\",\"ModuleName\":\"Vé điện tử\",\"DisplayName\":\"MEIVE-20.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\", \\\"Value\\\": \\\"100000\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 89, \\\"ResourceCode\\\": \\\"NumberOfPetrol\\\", \\\"ResourceName\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\"}]\",\"ItemName\":\"MEIXD-100.000\",\"ModuleName\":\"Hóa đơn bán lẻ xăng dầu\",\"DisplayName\":\"MEIXD-100.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":19950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Value\\\": 50000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"MEIR-50.000\",\"ModuleName\":\"Hóa đơn điện tử\",\"DisplayName\":\"MEIR-50.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5650000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"20000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIMTT-20.000\",\"ModuleName\":\"Hóa đơn từ máy tính tiền\",\"DisplayName\":\"MEIMTT-20000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11650000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"50000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"MEIVE-50.000\",\"ModuleName\":\"Vé điện tử\",\"DisplayName\":\"MEIVE-50.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\", \\\"Value\\\": \\\"50000\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 89, \\\"ResourceCode\\\": \\\"NumberOfPetrol\\\", \\\"ResourceName\\\": \\\"Hóa đơn bán lẻ xăng dầu\\\"}]\",\"ItemName\":\"MEIXD-50.000\",\"ModuleName\":\"Hóa đơn bán lẻ xăng dầu\",\"DisplayName\":\"MEIXD-50.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":9150000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": 20000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"MEIR-20.000\",\"ModuleName\":\"Hóa đơn điện tử\",\"DisplayName\":\"MEIR-20.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3050000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"10000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"MEIVE-10.000\",\"ModuleName\":\"Vé điện tử\",\"DisplayName\":\"MEIVE-10.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3050000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"10000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIMTT-10.000\",\"ModuleName\":\"Hóa đơn từ máy tính tiền\",\"DisplayName\":\"MEIMTT-10.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5250000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"10000\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"MEIR-10.000\",\"ModuleName\":\"Hóa đơn điện tử\",\"DisplayName\":\"MEIR-10.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"5000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIMTT-5.000\",\"ModuleName\":\"Hóa đơn từ máy tính tiền\",\"DisplayName\":\"MEIMTT-5000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1050000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"1000\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"MEIR-1.000\",\"ModuleName\":\"Hóa đơn điện tử\",\"DisplayName\":\"MEIR-1.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":850000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"2000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIMTT-2.000\",\"ModuleName\":\"Hóa đơn từ máy tính tiền\",\"DisplayName\":\"MEIMTT-2000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3150000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"5000\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"MEIR-5.000\",\"ModuleName\":\"Hóa đơn điện tử\",\"DisplayName\":\"MEIR-5.000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":550000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"1000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIMTT-1.000\",\"ModuleName\":\"Hóa đơn từ máy tính tiền\",\"DisplayName\":\"MEIMTT-1000\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":650000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"500\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"MEIR-500\",\"ModuleName\":\"Hóa đơn điện tử\",\"DisplayName\":\"MEIR-500\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":350000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"500\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIMTT-500\",\"ModuleName\":\"Hóa đơn từ máy tính tiền\",\"DisplayName\":\"MEIMTT-500\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":450000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"300\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"MEIR-300\",\"ModuleName\":\"Hóa đơn điện tử\",\"DisplayName\":\"MEIR-300\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":250000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"300\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIMTT-300\",\"ModuleName\":\"Hóa đơn từ máy tính tiền\",\"DisplayName\":\"MEIMTT-300\",\"ProductID\":426,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":0.0000,\"ItemType\":1,\"ResourceInfor\":null,\"ItemName\":\"MEIR-10.000+\",\"ModuleName\":\"Hóa đơn điện tử\",\"DisplayName\":\"MEIR-10.000+\",\"ProductID\":426,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"MeInbot\",\"AppName\":\"meInvoice Doanh nghiệp - Xử lý hóa đơn\",\"ProductID\":425,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":0.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 50, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}, {\\\"Name\\\": \\\"Thời hạn theo ngày\\\", \\\"Unit\\\": null, \\\"Value\\\": 5, \\\"ResourceID\\\": 23, \\\"ResourceCode\\\": \\\"DurationByDay\\\", \\\"ResourceName\\\": \\\"Thời hạn theo ngày\\\"}]\",\"ItemName\":\"Gói dùng thử\",\"ModuleName\":\"Xử lý hóa đơn\",\"DisplayName\":\"Gói dùng thử\",\"ProductID\":425,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":30990000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Value\\\": 100000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"MEIX-100.000\",\"ModuleName\":\"Xử lý hóa đơn\",\"DisplayName\":\"MEIX-100.000\",\"ProductID\":425,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":17490000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Value\\\": 50000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"MEIX-50.000\",\"ModuleName\":\"Xử lý hóa đơn\",\"DisplayName\":\"MEIX-50.000\",\"ProductID\":425,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7990000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Value\\\": 20000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"MEIX-20.000\",\"ModuleName\":\"Xử lý hóa đơn\",\"DisplayName\":\"MEIX-20.000\",\"ProductID\":425,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4490000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 10000, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"MEIX-10.000\",\"ModuleName\":\"Xử lý hóa đơn\",\"DisplayName\":\"MEIX-10.000\",\"ProductID\":425,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2490000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 5000, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"MEIX-5.000\",\"ModuleName\":\"Xử lý hóa đơn\",\"DisplayName\":\"MEIX-5.000\",\"ProductID\":425,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1190000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 2000, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"MEIX-2.000\",\"ModuleName\":\"Xử lý hóa đơn\",\"DisplayName\":\"MEIX-2.000\",\"ProductID\":425,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":690000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 1000, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"MEIX-1.000\",\"ModuleName\":\"Xử lý hóa đơn\",\"DisplayName\":\"MEIX-1.000\",\"ProductID\":425,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":390000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 300, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"MEIX-300\",\"ModuleName\":\"Xử lý hóa đơn\",\"DisplayName\":\"MEIX-300\",\"ProductID\":425,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":500000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"MEIV\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"MeInbot\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Dịch vụ phần mềm\",\"ModuleName\":\"Xử lý hóa đơn\",\"DisplayName\":\"Dịch vụ phần mềm\",\"ProductID\":425,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"MeInbot\",\"AppName\":\"meInvoice Hộ kinh doanh - Xử lý hóa đơn\",\"ProductID\":424,\"MarketName\":\"Hộ kinh doanh\",\"ListPackageProduct\":[{\"ItemPrice\":0.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 50, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}, {\\\"Name\\\": \\\"Thời hạn theo ngày\\\", \\\"Unit\\\": null, \\\"Value\\\": 5, \\\"ResourceID\\\": 23, \\\"ResourceCode\\\": \\\"DurationByDay\\\", \\\"ResourceName\\\": \\\"Thời hạn theo ngày\\\"}]\",\"ItemName\":\"Gói dùng thử\",\"ModuleName\":\"Xử lý hóa đơn\",\"DisplayName\":\"Gói dùng thử\",\"ProductID\":424,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4490000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"10000\\\", \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"MEIXH-10.000\",\"ModuleName\":\"Xử lý hóa đơn\",\"DisplayName\":\"MEIXH-10.000\",\"ProductID\":424,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2490000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 5000, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"MEIXH-5.000\",\"ModuleName\":\"Xử lý hóa đơn\",\"DisplayName\":\"MEIXH-5.000\",\"ProductID\":424,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1190000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 2000, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"MEIXH-2.000\",\"ModuleName\":\"Xử lý hóa đơn\",\"DisplayName\":\"MEIXH-2.000\",\"ProductID\":424,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":690000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 1000, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"MEIXH-1.000\",\"ModuleName\":\"Xử lý hóa đơn\",\"DisplayName\":\"MEIXH-1.000\",\"ProductID\":424,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":390000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 300, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"MEIXH-300\",\"ModuleName\":\"Xử lý hóa đơn\",\"DisplayName\":\"MEIXH-300\",\"ProductID\":424,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":500000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"MEIXH\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"MeInbot\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Dịch vụ phần mềm\",\"ModuleName\":\"Xử lý hóa đơn\",\"DisplayName\":\"Dịch vụ phần mềm\",\"ProductID\":424,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"RemoteSigning\",\"AppName\":\"MISA eSign – Chữ ký số từ xa cho hộ kinh doanh\",\"ProductID\":423,\"MarketName\":\"Hộ kinh doanh\",\"ListPackageProduct\":[{\"ItemPrice\":550000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"04\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}]\",\"ItemName\":\"1 năm\",\"ModuleName\":\"Hộ, cá nhân kinh doanh\",\"DisplayName\":\"1 năm\",\"ProductID\":423,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 2, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"2 năm\",\"ModuleName\":\"Hộ, cá nhân kinh doanh\",\"DisplayName\":\"2 năm\",\"ProductID\":423,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1250000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 3, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"3 năm\",\"ModuleName\":\"Hộ, cá nhân kinh doanh\",\"DisplayName\":\"3 năm\",\"ProductID\":423,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1550000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 4, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"4 năm\",\"ModuleName\":\"Hộ, cá nhân kinh doanh\",\"DisplayName\":\"4 năm\",\"ProductID\":423,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1850000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 5, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"5 năm\",\"ModuleName\":\"Hộ, cá nhân kinh doanh\",\"DisplayName\":\"5 năm\",\"ProductID\":423,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"Meinvoice.vn\",\"AppName\":\"meInvoice Hộ Kinh doanh - Phát hành hóa đơn\",\"ProductID\":422,\"MarketName\":\"Hộ kinh doanh\",\"ListPackageProduct\":[{\"ItemPrice\":129950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"1000000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"MEIHVE-1.000.000\",\"ModuleName\":\"Vé điện tử\",\"DisplayName\":\"MEIHVE-1.000.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":19950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"100000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIHMTT-100.000\",\"ModuleName\":\"Hóa đơn điện tử từ máy tính tiền\",\"DisplayName\":\"MEIHMTT-100.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5250000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"10000\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"MEIH-10.000\",\"ModuleName\":\"Hóa đơn điện tử\",\"DisplayName\":\"MEIH-10.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":74950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"500000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"MEIHVE-500.000\",\"ModuleName\":\"Vé điện tử\",\"DisplayName\":\"MEIHVE-500.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11650000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"50000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIHMTT-50.000\",\"ModuleName\":\"Hóa đơn điện tử từ máy tính tiền\",\"DisplayName\":\"MEIHMTT-50.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3150000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"5000\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"MEIH-5.000\",\"ModuleName\":\"Hóa đơn điện tử\",\"DisplayName\":\"MEIH-5.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":33950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"200000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"MEIHVE-200.000\",\"ModuleName\":\"Vé điện tử\",\"DisplayName\":\"MEIHVE-200.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5650000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"20000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIHMTT-20.000\",\"ModuleName\":\"Hóa đơn điện tử từ máy tính tiền\",\"DisplayName\":\"MEIHMTT-20.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1550000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"2000\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"MEIH-2.000\",\"ModuleName\":\"Hóa đơn điện tử\",\"DisplayName\":\"MEIH-2.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":19950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"100000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"MEIHVE-100.000\",\"ModuleName\":\"Vé điện tử\",\"DisplayName\":\"MEIHVE-100.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3050000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"10000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIHMTT-10.000\",\"ModuleName\":\"Hóa đơn điện tử từ máy tính tiền\",\"DisplayName\":\"MEIHMTT-10.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1050000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"1000\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"MEIH-1.000\",\"ModuleName\":\"Hóa đơn điện tử\",\"DisplayName\":\"MEIH-1.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11650000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"50000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"MEIHVE-50.000\",\"ModuleName\":\"Vé điện tử\",\"DisplayName\":\"MEIHVE-50.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"5000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIHMTT-5.000\",\"ModuleName\":\"Hóa đơn điện tử từ máy tính tiền\",\"DisplayName\":\"MEIHMTT-5.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":650000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"500\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"MEIH-500\",\"ModuleName\":\"Hóa đơn điện tử\",\"DisplayName\":\"MEIH-500\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5650000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"20000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"MEIHVE-20.000\",\"ModuleName\":\"Vé điện tử\",\"DisplayName\":\"MEIHVE-20.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":850000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"2000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIHMTT-2.000\",\"ModuleName\":\"Hóa đơn điện tử từ máy tính tiền\",\"DisplayName\":\"MEIHMTT-2.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":450000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"300\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"MEIH-300\",\"ModuleName\":\"Hóa đơn điện tử\",\"DisplayName\":\"MEIH-300\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3050000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"10000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"MEIHVE-10.000\",\"ModuleName\":\"Vé điện tử\",\"DisplayName\":\"MEIHVE-10.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":550000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"1000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIHMTT-1.000\",\"ModuleName\":\"Hóa đơn điện tử từ máy tính tiền\",\"DisplayName\":\"MEIHMTT-1.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":350000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"500\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIHMTT-500\",\"ModuleName\":\"Hóa đơn điện tử từ máy tính tiền\",\"DisplayName\":\"MEIHMTT-500\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":250000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"300\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIHMTT-300\",\"ModuleName\":\"Hóa đơn điện tử từ máy tính tiền\",\"DisplayName\":\"MEIHMTT-300\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":33950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Value\\\": 200000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIHMTT-200.000\",\"ModuleName\":\"Hóa đơn điện tử từ máy tính tiền\",\"DisplayName\":\"MEIMTT-200.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":74950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Value\\\": 500000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIHMTT-500.000\",\"ModuleName\":\"Hóa đơn điện tử từ máy tính tiền\",\"DisplayName\":\"MEIMTT-500.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":129950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Value\\\": 1000000, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"MEIHMTT-1.000.000\",\"ModuleName\":\"Hóa đơn điện tử từ máy tính tiền\",\"DisplayName\":\"MEIMTT-1.000.000\",\"ProductID\":422,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"ComboKT_HKD\",\"AppName\":\"Bộ giải pháp tài chính kế toán hộ kinh doanh\",\"ProductID\":420,\"MarketName\":\"Hộ kinh doanh\",\"ListPackageProduct\":[{\"ItemPrice\":800000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 01 người dùng\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 01 người dùng\",\"ProductID\":420,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":450000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"300\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Gói MEIH-300\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIH-300\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":650000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"500\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Gói MEIH-500\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIH-500\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1050000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"1000\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Gói MEIH-1.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIH-1.000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1550000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"2000\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Gói MEIH-2.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIH-2.000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3150000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"5000\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Gói MEIH-5.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIH-5.000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5250000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"10000\\\", \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Gói MEIH-10.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIH-10.000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3500000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"10000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"Gói MEIHVE-10.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIHVE-10.000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5650000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"20000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"Gói MEIHVE-20.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIHVE-20.000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11650000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"50000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"Gói MEIHVE-50.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIHVE-50.000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":19950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"100000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"Gói MEIHVE-100.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIHVE-100.000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":33950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"200000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"Gói MEIHVE-200.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIHVE-200.000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":74950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"500000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"Gói MEIHVE-500.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIHVE-500.000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":129950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Vé điện tử\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"1000000\\\", \\\"ResourceID\\\": 17, \\\"ResourceCode\\\": \\\"NumberOfTicket\\\", \\\"ResourceName\\\": \\\"Vé điện tử\\\"}]\",\"ItemName\":\"Gói MEIHVE-1.000.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIHVE-1.000.000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":250000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"300\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"Gói MEIHMTT-300\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIHMTT-300\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":350000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"500\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"Gói MEIHMTT-500\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIHMTT-500\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":550000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"1000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"Gói MEIHMTT-1.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIHMTT-1.000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":850000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"2000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"Gói MEIHMTT-2.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIHMTT-2.000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"5000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"Gói MEIHMTT-5.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIHMTT-5.000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3050000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"10000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"Gói MEIHMTT-10.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIHMTT-10.000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5650000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"20000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"Gói MEIHMTT-20.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIHMTT-20.000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11650000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"50000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"Gói MEIHMTT-50.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIHMTT-50.000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":19950000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"100000\\\", \\\"ResourceID\\\": 19, \\\"ResourceCode\\\": \\\"NumberOfCashRegister\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử từ máy tính tiền\\\"}]\",\"ItemName\":\"Gói MEIHMTT-100.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIHMTT-100.000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":390000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 300, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"Gói MEIXH 300\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIXH 300\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":690000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 1000, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"Gói MEIXH 1.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIXH 1000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1190000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 2000, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"Gói MEIXH 2.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIXH 2000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2490000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 5000, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"Gói MEIXH 5.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIXH 5000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4490000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"10000\\\", \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"Gói MEIXH-10.000\",\"ModuleName\":null,\"DisplayName\":\"Gói MEIXH-10.000\",\"ProductID\":420,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2400000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 3, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nghiệp vụ\\\", \\\"Unit\\\": null, \\\"Value\\\": 7, \\\"ResourceID\\\": 21, \\\"ResourceCode\\\": \\\"Business\\\", \\\"ResourceName\\\": \\\"Nghiệp vụ\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Individual\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Kế toán Hộ kinh doanh\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": 100, \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Bộ giải pháp Quản lý Tài chính kế toán Hộ kinh doanh - Gói Cơ bản năm đầu tiên\",\"ModuleName\":\"Combo_KT_HKD\",\"DisplayName\":\"Cơ bản\",\"ProductID\":420,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3200000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 3, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nghiệp vụ\\\", \\\"Unit\\\": null, \\\"Value\\\": 7, \\\"ResourceID\\\": 21, \\\"ResourceCode\\\": \\\"Business\\\", \\\"ResourceName\\\": \\\"Nghiệp vụ\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Individual\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Kế toán Hộ kinh doanh\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": 300, \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}]\",\"ItemName\":\"Bộ giải pháp Quản lý Tài chính kế toán Hộ kinh doanh - Gói Toàn diện năm đầu tiên\",\"ModuleName\":\"Combo_KT_HKD\",\"DisplayName\":\"Toàn diện\",\"ProductID\":420,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3800000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 3, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nghiệp vụ\\\", \\\"Unit\\\": null, \\\"Value\\\": 7, \\\"ResourceID\\\": 21, \\\"ResourceCode\\\": \\\"Business\\\", \\\"ResourceName\\\": \\\"Nghiệp vụ\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Individual\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Kế toán Hộ kinh doanh\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Hóa đơn điện tử đầu ra\\\", \\\"Unit\\\": null, \\\"Value\\\": 300, \\\"ResourceID\\\": 18, \\\"ResourceCode\\\": \\\"NumberOfInvoice\\\", \\\"ResourceName\\\": \\\"Hóa đơn điện tử đầu ra\\\"}, {\\\"Name\\\": \\\"Hóa đơn đầu vào\\\", \\\"Unit\\\": null, \\\"Value\\\": 300, \\\"ResourceID\\\": 12, \\\"ResourceCode\\\": \\\"Capacity\\\", \\\"ResourceName\\\": \\\"Hóa đơn đầu vào\\\"}]\",\"ItemName\":\"Bộ giải pháp Quản lý Tài chính kế toán Hộ kinh doanh - Gói Nâng cao năm đầu tiên\",\"ModuleName\":\"Combo_KT_HKD\",\"DisplayName\":\"Nâng cao\",\"ProductID\":420,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"VPS\",\"AppName\":\"Văn phòng số\",\"ProductID\":419,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":1056000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng - AMIS Ghi chép\",\"ModuleName\":null,\"DisplayName\":\"AMIS Ghi chép - Mua thêm 10 người dùng\",\"ProductID\":419,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":960000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng - AMIS Mạng xã hội\",\"ModuleName\":null,\"DisplayName\":\"AMIS Mạng xã hội - Mua thêm 10 người dùng\",\"ProductID\":419,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2000000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 01 người dùng - AMIS Tài sản\",\"ModuleName\":null,\"DisplayName\":\"AMIS Tài sản - Mua thêm 01 người dùng\",\"ProductID\":419,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1000000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 5, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 05 người dùng - AMIS Văn thư\",\"ModuleName\":null,\"DisplayName\":\"AMIS Văn thư - Mua thêm 05 người dùng\",\"ProductID\":419,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":408000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Phòng họp\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 16, \\\"ResourceCode\\\": \\\"BookingRoom\\\", \\\"ResourceName\\\": \\\"Phòng họp\\\"}]\",\"ItemName\":\"Mua thêm 01 phòng họp - AMIS Phòng họp\",\"ModuleName\":null,\"DisplayName\":\"AMIS Phòng họp - Mua thêm 01 phòng họp\",\"ProductID\":419,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Đào tạo 1 kèm 1 trực tuyến gói Standard\",\"ModuleName\":null,\"DisplayName\":\"Gói đào tạo 1-1 trực tuyến Standard\",\"ProductID\":419,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Đào tạo 1 kèm 1 trực tiếp gói Standard\",\"ModuleName\":null,\"DisplayName\":\"Gói đào tạo gói Standard\",\"ProductID\":419,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":20000000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Tư vấn, triển khai gói Standard\",\"ModuleName\":null,\"DisplayName\":\"Gói tư vấn, triển khai gói Standard\",\"ProductID\":419,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2880000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng gói Premium - AMIS Công việc\",\"ModuleName\":null,\"DisplayName\":\"AMIS Công việc - Mua thêm 10 người dùng\",\"ProductID\":419,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3600000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng gói Premium - AMIS Quy trình\",\"ModuleName\":null,\"DisplayName\":\"AMIS Quy trình - Mua thêm 10 người dùng\",\"ProductID\":419,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1100.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Tin nhắn SMS\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 6, \\\"ResourceCode\\\": \\\"SMS\\\", \\\"ResourceName\\\": \\\"Tin nhắn SMS\\\"}]\",\"ItemName\":\"Mua thêm tin nhắn SMS\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm tin nhắn SMS\",\"ProductID\":419,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1560000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Tài liệu ký\\\", \\\"Unit\\\": null, \\\"Value\\\": 200, \\\"ResourceID\\\": 13, \\\"ResourceCode\\\": \\\"Document\\\", \\\"ResourceName\\\": \\\"Tài liệu ký\\\"}]\",\"ItemName\":\"WeS-200\",\"ModuleName\":null,\"DisplayName\":\"WeS-200\",\"ProductID\":419,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3640000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Tài liệu ký\\\", \\\"Unit\\\": null, \\\"Value\\\": 500, \\\"ResourceID\\\": 13, \\\"ResourceCode\\\": \\\"Document\\\", \\\"ResourceName\\\": \\\"Tài liệu ký\\\"}]\",\"ItemName\":\"WeS-500\",\"ModuleName\":null,\"DisplayName\":\"WeS-500\",\"ProductID\":419,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7160000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Tài liệu ký\\\", \\\"Unit\\\": null, \\\"Value\\\": 1000, \\\"ResourceID\\\": 13, \\\"ResourceCode\\\": \\\"Document\\\", \\\"ResourceName\\\": \\\"Tài liệu ký\\\"}]\",\"ItemName\":\"WeS-1.000\",\"ModuleName\":null,\"DisplayName\":\"WeS-1.000\",\"ProductID\":419,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":18840000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Tài liệu ký\\\", \\\"Unit\\\": null, \\\"Value\\\": 3000, \\\"ResourceID\\\": 13, \\\"ResourceCode\\\": \\\"Document\\\", \\\"ResourceName\\\": \\\"Tài liệu ký\\\"}]\",\"ItemName\":\"WeS-3.000\",\"ModuleName\":null,\"DisplayName\":\"WeS-3.000\",\"ProductID\":419,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":26040000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Tài liệu ký\\\", \\\"Unit\\\": null, \\\"Value\\\": 5000, \\\"ResourceID\\\": 13, \\\"ResourceCode\\\": \\\"Document\\\", \\\"ResourceName\\\": \\\"Tài liệu ký\\\"}]\",\"ItemName\":\"WeS-5.000\",\"ModuleName\":null,\"DisplayName\":\"WeS-5.000\",\"ProductID\":419,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":43640000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Tài liệu ký\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"10000\\\", \\\"ResourceID\\\": 13, \\\"ResourceCode\\\": \\\"Document\\\", \\\"ResourceName\\\": \\\"Tài liệu ký\\\"}]\",\"ItemName\":\"WeS-10.000\",\"ModuleName\":null,\"DisplayName\":\"WeS-10.000\",\"ProductID\":419,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":399200.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Lượt chứng thực B2B\\\", \\\"Unit\\\": \\\"lượt\\\", \\\"Value\\\": 100, \\\"ResourceID\\\": 44, \\\"ResourceCode\\\": \\\"EVerifyContractB2B\\\", \\\"ResourceName\\\": \\\"Lượt chứng thực B2B\\\"}]\",\"ItemName\":\"Gói chứng thực hợp đồng điện tử B2B100\",\"ModuleName\":null,\"DisplayName\":\"B2B - Gói 100 lượt chứng thực hợp đồng điện tử\",\"ProductID\":419,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":239200.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Lượt chứng thực B2C\\\", \\\"Unit\\\": \\\"lượt\\\", \\\"Value\\\": 100, \\\"ResourceID\\\": 45, \\\"ResourceCode\\\": \\\"EVerifyContractB2C\\\", \\\"ResourceName\\\": \\\"Lượt chứng thực B2C\\\"}]\",\"ItemName\":\"Gói chứng thực hợp đồng điện tử B2C100\",\"ModuleName\":null,\"DisplayName\":\"B2C - Gói 100 lượt chứng thực hợp đồng điện tử\",\"ProductID\":419,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":800000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Lượt ký xác thực bằng eKYC\\\", \\\"Unit\\\": \\\"lượt\\\", \\\"Value\\\": 300, \\\"ResourceID\\\": 56, \\\"ResourceCode\\\": \\\"EKYCContract\\\", \\\"ResourceName\\\": \\\"Lượt ký xác thực bằng eKYC\\\"}]\",\"ItemName\":\"Gói mua thêm 300 lượt xác thực người ký bằng eKYC\",\"ModuleName\":null,\"DisplayName\":\"Gói mua thêm 300 lượt xác thực người ký bằng eKYC\",\"ProductID\":419,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Đào tạo 1 kèm 1 trực tuyến gói Professional\",\"ModuleName\":null,\"DisplayName\":\"Gói đào tạo gói Professional\",\"ProductID\":419,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":11950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Đào tạo 1 kèm 1 trực tiếp gói Professional\",\"ModuleName\":null,\"DisplayName\":\"Gói đào tạo gói Professional\",\"ProductID\":419,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":20000000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Tư vấn, triển khai gói Professional\",\"ModuleName\":null,\"DisplayName\":\"Gói tư vấn, triển khai gói Professional\",\"ProductID\":419,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7950000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Đào tạo 1 kèm 1 trực tuyến gói Enterprise\",\"ModuleName\":null,\"DisplayName\":\"Gói đào tạo gói Enterprise\",\"ProductID\":419,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":20000000.0000,\"ItemType\":3,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Tư vấn, triển khai gói Enterprise\",\"ModuleName\":null,\"DisplayName\":\"Gói tư vấn, triển khai gói Enterprise\",\"ProductID\":419,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":0.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Gói Starter\",\"ModuleName\":\"VPS\",\"DisplayName\":\"Gói Starter\",\"ProductID\":419,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":18800000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Gói Standard năm đầu tiên\",\"ModuleName\":\"VPS\",\"DisplayName\":\"Gói Standard\",\"ProductID\":419,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":32112000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Gói Professional năm đầu tiên\",\"ModuleName\":\"VPS\",\"DisplayName\":\"Gói Professional\",\"ProductID\":419,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":39112000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Bộ giải pháp phần mềm MISA AMIS Văn phòng số - Gói Enteprise năm đầu tiên\",\"ModuleName\":\"VPS\",\"DisplayName\":\"Gói Enterprise\",\"ProductID\":419,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"RemoteSigning\",\"AppName\":\"MISA eSign – Chữ ký số từ xa cho doanh nghiệp\",\"ProductID\":418,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":3900000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"05\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}]\",\"ItemName\":\"1 năm\",\"ModuleName\":\"Tổ chức - Gói nâng cao\",\"DisplayName\":\"1 năm\",\"ProductID\":418,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":5900000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 2, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"05\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}]\",\"ItemName\":\"2 năm\",\"ModuleName\":\"Tổ chức - Gói nâng cao\",\"DisplayName\":\"2 năm\",\"ProductID\":418,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7900000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 3, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"05\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}]\",\"ItemName\":\"3 năm\",\"ModuleName\":\"Tổ chức - Gói nâng cao\",\"DisplayName\":\"3 năm\",\"ProductID\":418,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1350000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"1 năm\",\"ModuleName\":\"Tổ chức - Gói cơ bản\",\"DisplayName\":\"1 năm\",\"ProductID\":418,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2250000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 2, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"2 năm\",\"ModuleName\":\"Tổ chức - Gói cơ bản\",\"DisplayName\":\"2 năm\",\"ProductID\":418,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3050000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 3, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"3 năm\",\"ModuleName\":\"Tổ chức - Gói cơ bản\",\"DisplayName\":\"3 năm\",\"ProductID\":418,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3850000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 4, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"4 năm\",\"ModuleName\":\"Tổ chức - Gói cơ bản\",\"DisplayName\":\"4 năm\",\"ProductID\":418,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4550000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 5, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"5 năm\",\"ModuleName\":\"Tổ chức - Gói cơ bản\",\"DisplayName\":\"5 năm\",\"ProductID\":418,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":550000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"1 năm\",\"ModuleName\":\"Cá nhân trong Tổ chức\",\"DisplayName\":\"1 năm\",\"ProductID\":418,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 2, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"2 năm\",\"ModuleName\":\"Cá nhân trong Tổ chức\",\"DisplayName\":\"2 năm\",\"ProductID\":418,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1250000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 3, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"3 năm\",\"ModuleName\":\"Cá nhân trong Tổ chức\",\"DisplayName\":\"3 năm\",\"ProductID\":418,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1550000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 4, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"4 năm\",\"ModuleName\":\"Cá nhân trong Tổ chức\",\"DisplayName\":\"4 năm\",\"ProductID\":418,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1850000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 5, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"5 năm\",\"ModuleName\":\"Cá nhân trong Tổ chức\",\"DisplayName\":\"5 năm\",\"ProductID\":418,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"AMS\",\"AppName\":\"AMIS Quản lý tài sản\",\"ProductID\":417,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":3500000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 1 người dùng\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 1 người dùng\",\"ProductID\":417,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":7000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 2, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Tài sản\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Tài sản\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"AMIS Tài sản\",\"ModuleName\":null,\"DisplayName\":\"AMIS Tài sản\",\"ProductID\":417,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"BookingRoom\",\"AppName\":\"Quản lý phòng họp\",\"ProductID\":416,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":700000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Phòng họp\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 16, \\\"ResourceCode\\\": \\\"BookingRoom\\\", \\\"ResourceName\\\": \\\"Phòng họp\\\"}]\",\"ItemName\":\"Mua thêm 1 phòng họp\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 1 phòng họp\",\"ProductID\":416,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3500000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Phòng họp\\\", \\\"Unit\\\": null, \\\"Value\\\": 5, \\\"ResourceID\\\": 16, \\\"ResourceCode\\\": \\\"BookingRoom\\\", \\\"ResourceName\\\": \\\"Phòng họp\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Phòng họp\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Phòng họp\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"AMIS Phòng họp\",\"ModuleName\":null,\"DisplayName\":\"AMIS Phòng họp\",\"ProductID\":416,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"Dispatch\",\"AppName\":\"AMIS Văn thư\",\"ProductID\":415,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":1500000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 5, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 05 người dùng\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 05 người dùng\",\"ProductID\":415,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Văn thư\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Văn thư\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"AMIS Văn thư\",\"ModuleName\":null,\"DisplayName\":\"AMIS Văn thư\",\"ProductID\":415,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"Newsfeed\",\"AppName\":\"Mạng xã hội doanh nghiệp\",\"ProductID\":414,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":1300000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10 người dùng\",\"ProductID\":414,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":3900000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Mạng xã hội\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Mạng xã hội\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"AMIS Mạng xã hội\",\"ModuleName\":null,\"DisplayName\":\"AMIS Mạng xã hội\",\"ProductID\":414,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"Document\",\"AppName\":\"Ghi chép và lưu trữ tài liệu\",\"ProductID\":413,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":1500000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10 người dùng\",\"ProductID\":413,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4500000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Ghi chép\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Ghi chép\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"AMIS Ghi chép\",\"ModuleName\":null,\"DisplayName\":\"AMIS Ghi chép\",\"ProductID\":413,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"Wesign\",\"AppName\":\"Nền tảng ký tài liệu số\",\"ProductID\":411,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":1100.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Tin nhắn SMS\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 6, \\\"ResourceCode\\\": \\\"SMS\\\", \\\"ResourceName\\\": \\\"Tin nhắn SMS\\\"}]\",\"ItemName\":\"Mua thêm tin nhắn SMS\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm tin nhắn SMS\",\"ProductID\":411,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":499000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Lượt chứng thực B2B\\\", \\\"Unit\\\": \\\"lượt\\\", \\\"Value\\\": 100, \\\"ResourceID\\\": 44, \\\"ResourceCode\\\": \\\"EVerifyContractB2B\\\", \\\"ResourceName\\\": \\\"Lượt chứng thực B2B\\\"}]\",\"ItemName\":\"Gói chứng thực hợp đồng điện tử B2B100\",\"ModuleName\":null,\"DisplayName\":\"Gói chứng thực hợp đồng điện tử B2B100\",\"ProductID\":411,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":299000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Lượt chứng thực B2C\\\", \\\"Unit\\\": \\\"lượt\\\", \\\"Value\\\": 100, \\\"ResourceID\\\": 45, \\\"ResourceCode\\\": \\\"EVerifyContractB2C\\\", \\\"ResourceName\\\": \\\"Lượt chứng thực B2C\\\"}]\",\"ItemName\":\"Gói chứng thực hợp đồng điện tử B2C100\",\"ModuleName\":null,\"DisplayName\":\"Gói chứng thực hợp đồng điện tử B2C100\",\"ProductID\":411,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1000000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Lượt ký xác thực bằng eKYC\\\", \\\"Unit\\\": \\\"lượt\\\", \\\"Value\\\": 300, \\\"ResourceID\\\": 56, \\\"ResourceCode\\\": \\\"EKYCContract\\\", \\\"ResourceName\\\": \\\"Lượt ký xác thực bằng eKYC\\\"}]\",\"ItemName\":\"Gói mua thêm 300 lượt xác thực người ký bằng eKYC\",\"ModuleName\":null,\"DisplayName\":\"Gói mua thêm 300 lượt xác thực người ký bằng eKYC\",\"ProductID\":411,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":0.0,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Tài liệu ký\\\", \\\"Unit\\\": null, \\\"Value\\\": 30, \\\"ResourceID\\\": 13, \\\"ResourceCode\\\": \\\"Document\\\", \\\"ResourceName\\\": \\\"Tài liệu ký\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Free\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Free\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Free\",\"ModuleName\":null,\"DisplayName\":\"Free\",\"ProductID\":411,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1000000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"WeSign\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"WeSign\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Dịch vụ phần mềm\",\"ModuleName\":null,\"DisplayName\":\"Dịch vụ phần mềm\",\"ProductID\":411,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Tài liệu ký\\\", \\\"Unit\\\": null, \\\"Value\\\": 200, \\\"ResourceID\\\": 13, \\\"ResourceCode\\\": \\\"Document\\\", \\\"ResourceName\\\": \\\"Tài liệu ký\\\"}]\",\"ItemName\":\"WeS-200\",\"ModuleName\":null,\"DisplayName\":\"WeS-200\",\"ProductID\":411,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":4550000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Tài liệu ký\\\", \\\"Unit\\\": null, \\\"Value\\\": 500, \\\"ResourceID\\\": 13, \\\"ResourceCode\\\": \\\"Document\\\", \\\"ResourceName\\\": \\\"Tài liệu ký\\\"}]\",\"ItemName\":\"WeS-500\",\"ModuleName\":null,\"DisplayName\":\"WeS-500\",\"ProductID\":411,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":8950000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Tài liệu ký\\\", \\\"Unit\\\": null, \\\"Value\\\": 1000, \\\"ResourceID\\\": 13, \\\"ResourceCode\\\": \\\"Document\\\", \\\"ResourceName\\\": \\\"Tài liệu ký\\\"}]\",\"ItemName\":\"WeS-1.000\",\"ModuleName\":null,\"DisplayName\":\"WeS-1.000\",\"ProductID\":411,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":23550000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Tài liệu ký\\\", \\\"Unit\\\": null, \\\"Value\\\": 3000, \\\"ResourceID\\\": 13, \\\"ResourceCode\\\": \\\"Document\\\", \\\"ResourceName\\\": \\\"Tài liệu ký\\\"}]\",\"ItemName\":\"WeS-3.000\",\"ModuleName\":null,\"DisplayName\":\"WeS-3.000\",\"ProductID\":411,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":32550000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Tài liệu ký\\\", \\\"Unit\\\": null, \\\"Value\\\": 5000, \\\"ResourceID\\\": 13, \\\"ResourceCode\\\": \\\"Document\\\", \\\"ResourceName\\\": \\\"Tài liệu ký\\\"}]\",\"ItemName\":\"WeS-5.000\",\"ModuleName\":null,\"DisplayName\":\"WeS-5.000\",\"ProductID\":411,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":54550000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Tài liệu ký\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"10000\\\", \\\"ResourceID\\\": 13, \\\"ResourceCode\\\": \\\"Document\\\", \\\"ResourceName\\\": \\\"Tài liệu ký\\\"}]\",\"ItemName\":\"WeS-10.000\",\"ModuleName\":null,\"DisplayName\":\"WeS-10.000\",\"ProductID\":411,\"IsCapacityPackage\":true,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"AMISProcess\",\"AppName\":\"AMIS Quy trình\",\"ProductID\":410,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":5200000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng gói Premium\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10 người dùng gói Premium\",\"ProductID\":410,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":0.0,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 5, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Free\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Free\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Free\",\"ModuleName\":null,\"DisplayName\":\"Free\",\"ProductID\":410,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":10400000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 20, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Premium\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Premium\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Premium\",\"ModuleName\":null,\"DisplayName\":\"Premium\",\"ProductID\":410,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"HKD\",\"AppName\":\"AMIS Kế toán Hộ kinh doanh\",\"ProductID\":405,\"MarketName\":\"Hộ kinh doanh\",\"ListPackageProduct\":[{\"ItemPrice\":2400000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 3, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Nghiệp vụ\\\", \\\"Unit\\\": null, \\\"Value\\\": 7, \\\"ResourceID\\\": 21, \\\"ResourceCode\\\": \\\"Business\\\", \\\"ResourceName\\\": \\\"Nghiệp vụ\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Individual\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"AMIS Kế toán Hộ kinh doanh\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Phần mềm AMIS Kế toán dành cho hộ, cá nhân kinh doanh\",\"ModuleName\":null,\"DisplayName\":\"AMIS kế toán Hộ kinh doanh\",\"ProductID\":405,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":800000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 01 người dùng\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 01 người dùng\",\"ProductID\":405,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":330000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"Individual\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Value\\\": 1, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}, {\\\"Name\\\": \\\"Là gói dịch vụ lưu trữ dữ liệu\\\", \\\"Value\\\": \\\"true\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 91, \\\"ResourceCode\\\": \\\"IsDataStorage\\\", \\\"ResourceName\\\": \\\"Là gói dịch vụ lưu trữ dữ liệu\\\"}]\",\"ItemName\":\"Dịch vụ lưu trữ dữ liệu\",\"ModuleName\":null,\"DisplayName\":\"Dịch vụ lưu trữ dữ liệu\",\"ProductID\":405,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"CukCuk.vn\",\"AppName\":\"Phần mềm quản lý nhà hàng CUKCUK\",\"ProductID\":230,\"MarketName\":\"Hộ kinh doanh\",\"ListPackageProduct\":[{\"ItemPrice\":0.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Thời hạn theo ngày\\\", \\\"Unit\\\": \\\"Gói\\\", \\\"Value\\\": 15, \\\"DataType\\\": \\\"number\\\", \\\"ResourceID\\\": 23, \\\"ResourceCode\\\": \\\"DurationByDay\\\", \\\"ResourceName\\\": \\\"Thời hạn theo ngày\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Value\\\": \\\"CUK.TRL\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Value\\\": \\\"Starter\\\", \\\"DataType\\\": \\\"string\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}]\",\"ItemName\":\"Gói dùng thử\",\"ModuleName\":\"Gói sản phẩm\",\"DisplayName\":\"Gói dùng thử 15 ngày CukCuk\",\"ProductID\":230,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":199000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"CUK.STD\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Standard\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo tháng\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"1\\\", \\\"ResourceID\\\": 22, \\\"ResourceCode\\\": \\\"DurationByMonth\\\", \\\"ResourceName\\\": \\\"Thời hạn theo tháng\\\"}]\",\"ItemName\":\"Standard\",\"ModuleName\":\"Gói sản phẩm\",\"DisplayName\":\"Standard\",\"ProductID\":230,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":299000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"CUK.PRO\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Professional\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo tháng\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"1\\\", \\\"ResourceID\\\": 22, \\\"ResourceCode\\\": \\\"DurationByMonth\\\", \\\"ResourceName\\\": \\\"Thời hạn theo tháng\\\"}]\",\"ItemName\":\"Professional\",\"ModuleName\":\"Gói sản phẩm\",\"DisplayName\":\"Professional\",\"ProductID\":230,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":499000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"CUK.ENT\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Enterprise\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo tháng\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"1\\\", \\\"ResourceID\\\": 22, \\\"ResourceCode\\\": \\\"DurationByMonth\\\", \\\"ResourceName\\\": \\\"Thời hạn theo tháng\\\"}]\",\"ItemName\":\"Enterprise\",\"ModuleName\":\"Gói sản phẩm\",\"DisplayName\":\"Enterprise\",\"ProductID\":230,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"Combo_eSign_HKD\",\"AppName\":\"MISA eSign - Chữ ký số USB Token cho Hộ kinh doanh\",\"ProductID\":184,\"MarketName\":\"Hộ kinh doanh\",\"ListPackageProduct\":[{\"ItemPrice\":1049000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Dịch vụ chữ ký số MISA eSign cho Hộ, cá nhân kinh doanh gói mua mới 1 năm đã bao gồm USB Token\",\"ModuleName\":\"Hộ kinh doanh\",\"DisplayName\":\"1 năm\",\"ProductID\":184,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1449000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Dịch vụ chữ ký số MISA eSign cho Hộ, cá nhân kinh doanh gói mua mới 2 năm đã bao gồm USB Token\",\"ModuleName\":\"Hộ kinh doanh\",\"DisplayName\":\"2 năm\",\"ProductID\":184,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":1749000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Dịch vụ chữ ký số MISA eSign cho Hộ, cá nhân kinh doanh gói mua mới 3 năm đã bao gồm USB Token\",\"ModuleName\":\"Hộ kinh doanh\",\"DisplayName\":\"3 năm\",\"ProductID\":184,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2049000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Dịch vụ chữ ký số MISA eSign cho Hộ, cá nhân kinh doanh gói mua mới 4 năm đã bao gồm USB Token\",\"ModuleName\":\"Hộ kinh doanh\",\"DisplayName\":\"4 năm\",\"ProductID\":184,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":2349000.0000,\"ItemType\":1,\"ResourceInfor\":\"[]\",\"ItemName\":\"Dịch vụ chữ ký số MISA eSign cho Hộ, cá nhân kinh doanh gói mua mới 5 năm đã bao gồm USB Token\",\"ModuleName\":\"Hộ kinh doanh\",\"DisplayName\":\"5 năm\",\"ProductID\":184,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]},{\"AppCode\":\"Task\",\"AppName\":\"Quản lý công việc\",\"ProductID\":409,\"MarketName\":\"Doanh nghiệp\",\"ListPackageProduct\":[{\"ItemPrice\":4300000.0000,\"ItemType\":2,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}]\",\"ItemName\":\"Mua thêm 10 người dùng gói Premium\",\"ModuleName\":null,\"DisplayName\":\"Mua thêm 10 người dùng gói Premium\",\"ProductID\":409,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":0.0,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 5, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Free\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Free\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 10, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Free\",\"ModuleName\":null,\"DisplayName\":\"Free\",\"ProductID\":409,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null},{\"ItemPrice\":8600000.0000,\"ItemType\":1,\"ResourceInfor\":\"[{\\\"Name\\\": \\\"Người dùng\\\", \\\"Unit\\\": null, \\\"Value\\\": 20, \\\"ResourceID\\\": 10, \\\"ResourceCode\\\": \\\"Account\\\", \\\"ResourceName\\\": \\\"Người dùng\\\"}, {\\\"Name\\\": \\\"Mã gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Premium\\\", \\\"ResourceID\\\": 36, \\\"ResourceCode\\\": \\\"PackageCode\\\", \\\"ResourceName\\\": \\\"Mã gói\\\"}, {\\\"Name\\\": \\\"Tên gói\\\", \\\"Unit\\\": null, \\\"Value\\\": \\\"Premium\\\", \\\"ResourceID\\\": 37, \\\"ResourceCode\\\": \\\"PackageName\\\", \\\"ResourceName\\\": \\\"Tên gói\\\"}, {\\\"Name\\\": \\\"Thời hạn theo năm\\\", \\\"Unit\\\": null, \\\"Value\\\": 1, \\\"ResourceID\\\": 41, \\\"ResourceCode\\\": \\\"DurationByYear\\\", \\\"ResourceName\\\": \\\"Thời hạn theo năm\\\"}]\",\"ItemName\":\"Premium\",\"ModuleName\":null,\"DisplayName\":\"Premium\",\"ProductID\":409,\"IsCapacityPackage\":false,\"PackageId\":null,\"MultiPackage\":null}]}]",
  "headers": {
    "server": "nginx/1.23.1",
    "date": "Tue, 29 Apr 2025 08:26:17 GMT",
    "content-type": "application/json; charset=utf-8",
    "content-length": "249578",
    "connection": "keep-alive",
    "vary": "Accept-Encoding"
  },
  "files": []
}