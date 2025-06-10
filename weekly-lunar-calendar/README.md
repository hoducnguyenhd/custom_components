# Weekly Lunar Calendar

Lovelace Custom card hiển thị lịch tuần, bao gồm cả ngày âm lịch cho Home Assistant. Phương pháp tính ngày Âm lịch được kế thừa từ thư viện của Hồ Ngọc Đức.

![Weekly-Lunar-Calendar](https://raw.githubusercontent.com/lesydat/weekly-calendar/master/preview.png)

## Hướng dẫn cài đặt:

Thêm  dòng code sau vào phần resource trong lovelace

```yaml
- url: https://raw.githubusercontent.com/lesydat/weekly-lunar-calendar/master/weekly-lunar-calendar.js
  type: module
```

Thêm một custom card vào lovelace 
```yaml
- type: custom:weekly-lunar-calendar
```
