# Weekly Lunar Calendar

Lovelace Custom card hiển thị lịch tuần, bao gồm cả ngày âm lịch cho Home Assistant. Phương pháp tính ngày Âm lịch được kế thừa từ thư viện của Hồ Ngọc Đức.

![Weekly-Lunar-Calendar](https://github.com/hoducnguyenhd/custom_components/blob/main/weekly-lunar-calendar/preview.png)

## Hướng dẫn cài đặt:

Chọn sửa bảng điều khiển trên góc phải -> chọn dấu "..." -> chọn Quản lý tài nguyên -> chọn Thêm tài nguyên:
Url: copy link bên dưới
Loại tài nguyên: Mô-đun JavaScript 
```yaml
https://github.com/hoducnguyenhd/custom_components/blob/main/weekly-lunar-calendar/weekly-lunar-calendar.js
```
Thêm một custom card vào lovelace 
```yaml
type: custom:weekly-lunar-calendar
```
