import cv2

# Địa chỉ IP của camera trên điện thoại
camera_ip = "http://192.168.100.141:8080/"  # Thay đổi địa chỉ IP này bằng địa chỉ IP của camera trên điện thoại của bạn

# Kết nối đến camera
cap = cv2.VideoCapture(f"{camera_ip}/video")

# Kiểm tra xem camera có kết nối thành công không
if not cap.isOpened():
    print("Không thể kết nối đến camera.")
    exit()

# Vòng lặp để hiển thị hình ảnh từ camera
while True:
    ret, frame = cap.read()  # Đọc frame từ camera

    # Kiểm tra xem việc đọc frame có thành công không
    if not ret:
        print("Không thể nhận được frame từ camera.")
        break

    cv2.imshow("Camera", frame)  # Hiển thị frame

    # Đợi một phím bấm để thoát
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Giải phóng các tài nguyên
cap.release()
cv2.destroyAllWindows()
