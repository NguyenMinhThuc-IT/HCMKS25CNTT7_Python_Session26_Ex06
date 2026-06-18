from abc import ABC, abstractmethod

# ===================================================================
# 1. THIẾT KẾ CÁC LỚP ĐỐI TƯỢNG (CLASS DESIGN)
# ===================================================================

class Employee(ABC):
    """Lớp cha trừu tượng đại diện cho nhân viên nói chung."""
    
    def __init__(self, employee_id: str, name: str):
        self.employee_id = employee_id.strip().upper()
        self.name = name.strip()

    def display_info(self) -> None:
        """Hiển thị thông tin cơ bản của nhân viên."""
        # Trích xuất tên Class để xác định loại nhân viên động
        class_name = self.__class__.__name__
        emp_type = "Full-time" if class_name == "FullTimeEmployee" else \
                   "Part-time" if class_name == "PartTimeEmployee" else "Intern"
                   
        print(f"Mã NV: {self.employee_id:<5} | Họ tên: {self.name:<15} | Loại: {emp_type}")

    @abstractmethod
    def calculate_salary(self) -> float:
        """Phương thức trừu tượng tính lương, bắt buộc lớp con phải override."""
        pass


class FullTimeEmployee(Employee):
    """Nhân viên toàn thời gian."""
    
    def __init__(self, employee_id: str, name: str, base_salary: float, bonus: float):
        super().__init__(employee_id, name)
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self) -> float:
        """Lương = Lương cơ bản + Thưởng."""
        return self.base_salary + self.bonus


class PartTimeEmployee(Employee):
    """Nhân viên bán thời gian."""
    
    def __init__(self, employee_id: str, name: str, working_hours: float, hourly_rate: float):
        super().__init__(employee_id, name)
        self.working_hours = working_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self) -> float:
        """Lương = Số giờ làm * Lương theo giờ."""
        return self.working_hours * self.hourly_rate


class InternEmployee(Employee):
    """Thực tập sinh."""
    
    def __init__(self, employee_id: str, name: str, allowance: float):
        super().__init__(employee_id, name)
        self.allowance = allowance

    def calculate_salary(self) -> float:
        """Lương = Trợ cấp."""
        return self.allowance


# ===================================================================
# 2. ĐỊNH NGHĨA CÁC HÀM NGHIỆP VỤ CHO MENU (LOGIC FUNCTIONS)
# ===================================================================

def display_employees(employee_list: list[Employee]) -> None:
    """Chức năng 1: Duyệt danh sách và hiển thị thông tin cơ bản."""
    print("\n--- DANH SÁCH NHÂN VIÊN ---")
    if not employee_list:
        print("Hệ thống hiện chưa có nhân viên nào.")
        return
    for employee in employee_list:
        employee.display_info()


def display_salaries(employee_list: list[Employee]) -> None:
    """Chức năng 2: Duyệt danh sách và tính lương đa hình (Không dùng if/else)."""
    print("\n--- BẢNG LƯƠNG NHÂN VIÊN ---")
    if not employee_list:
        print("Hệ thống trống, không thể tính lương.")
        return
    for employee in employee_list:
        salary = employee.calculate_salary()
        # Định nghĩa chuỗi hiển thị tiền tệ chuẩn: f"{salary:,.0f} VND"
        print(f"{employee.employee_id:<5} | {employee.name:<15} | Lương: {salary:,.0f} VND")


# ===================================================================
# 3. LUỒNG ĐIỀU KHIỂN CHƯƠNG TRÌNH CHÍNH (MAIN FUNCTION)
# ===================================================================
def main():
    # Khởi tạo Mock Data chuẩn theo yêu cầu bài toán
    employees = [
        FullTimeEmployee("E001", "Nguyen Van A", 15000000, 3000000),
        PartTimeEmployee("E002", "Tran Thi B", 80, 50000),
        InternEmployee("E003", "Le Van C", 3000000)
    ]

    while True:
        print("\n=== EMPLOYEE SALARY MANAGER ===")
        print("1. Xem danh sách nhân viên")
        print("2. Tính lương toàn bộ nhân viên")
        print("3. Thoát chương trình")
        print("================================")
        
        choice = input("Chọn chức năng (1-3): ").strip()

        if choice == "1":
            display_employees(employees)
        elif choice == "2":
            display_salaries(employees)
        elif choice == "3":
            print("\nCảm ơn bạn đã sử dụng Employee Salary Manager!")
            break
        else:
            print("\nLựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == "__main__":
    # Khối lệnh kiểm tra an toàn: Đảm bảo class Employee không thể bị tạo object trực tiếp
    try:
        invalid_instance = Employee("E000", "Ghost") # type: ignore
    except TypeError:
        pass # Chặn thành công lỗi kiến trúc ở tầng runtime
        
    main()