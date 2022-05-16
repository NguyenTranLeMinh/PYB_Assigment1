"# PYB_Assigment1"

Cho tọa độ 3 đỉnh A, B, C của hình tam giác trong mặt phẳng không gian Oxy. Bài tập yêu cầu học viên tính toán các thông số của hình tam giác từ đơn giản đến phức tạp thông qua ngôn ngữ lập trình Python như:

- Xét xem A, B, C có đủ điều kiện tạo thành tam giác ABC hay không.

- Tính toán độ dài các cạnh và độ lớn các góc của tam giác ABC.

- Đưa ra kết luận tam giác ABC là tam giác nhọn, tam giác vuông hay tam giác tù.

- Đưa ra kết luận tam giác ABC là tam giác cân, tam giác đều, tam giác vuông cân hay tam giác bình thường.

- Tính diện tích của tam giác ABC.

- Tính độ dài các đường cao của tam giác ABC xuất phát từ các đỉnh A, B, C.

- Tính tọa độ trọng tâm và trực tâm của tam giác ABC.


Hướng dẫn:
input: Tọa độ của 3 điểm A, B, C ở hệ trục tọa độ Oxy theo format ở dạng list như sau: 

[Ax, Ay, Bx, By, Cx, Cy] (ví dụ: [1, 1, 2, 2, 3, 1])

a. Viết hàm kiemtra_tamgiac(input) kiểm tra xem 3 điểm A, B, C có đủ điều kiện hợp thành tam giác ABC hay không.

- Nếu đủ điều kiện, trả về “True”.

- Nếu không đủ điều kiện, trả về “False”.

Note: 3 điểm A, B, C hợp thành một tam giác trong hệ trục tọa độ Oxy nếu 3 điểm A, B, C không thẳng hang.

b. Viết hàm goccanh_tamgiac(input) tính toán các cạnh và góc của tam giác ABC:

- Tính toán các cạnh và số đo các góc của tam giác ABC, kết quả trả về là một list với độ dài các cạnh theo thứ tự [AB, BC, CA, góc A, góc B, góc C].

- Kết quả các cạnh và góc làm tròn kết quả đến chữ số thập phân thứ 2. 

c. Viết hàm xet_tamgiac(input) xét xem tam giác ABC thuộc loại tam giác nào:

- Xét xem tam giác ABC là tam giác vuông, tam giác nhọn hay tam giác tù, tại đỉnh nào.

- Xét xem tam giác ABC là tam giác bình thường, tam giác cân hay tam giác đều, tại đỉnh nào.

 Trả về kết quả:

o Nếu là tam giác vuông cân thì trả về kết quả: “ABC la tam giac vuong can tai dinh A(B/C)”.

o Nếu là tam giác đều thì trả về kết quả: “ABC là tam giac deu”.

o Nếu là tam giác tù và cân thì trả về kết quả: “ABC la tam giac tu va can tai dinh A/B/C”.

o Nếu chỉ là tam giác vuông, cân hoặc tù thì trả về: kết quả: “ABC là tam giac vuong/can/tu tai dinh A/B/C”.

o Nếu không phải các trường hợp trên, trả về kết quả: “ABC la tam giac binh thuong”.

d. Viết hàm dientich_tamgiac(input) để tính diện tích của tam giác ABC.

- Trả về diện tích của tam giác ABC, kết quả được làm tròn đến chữ số thập phân thứ 2.

e. Viết hàm duongcao_tamgiac(input) để tính độ dài của các đường cao của tam giác ABC:

- Trả về độ dài 3 đường cao của tam giác ABC xuất phát từ các đỉnh A, B và C theo dạng list [dcA, dcB. dcC], kết quả được làm tròn đến chữ số thập phân thứ 2.

f. Viết hàm trungtuyen_tamgiac(input) để tính độ dài từ các đỉnh A, B, C đến trọng tâm của tam giác ABC:

- Trả về độ dài từ các đỉnh A, B, C đến trọng tâm của tam giác ABC theo dạng list [ttA, ttB, ttC], kết quả được làm tròn đến chữ số thập phân thứ 2.

g. (Yêu cầu nâng cao) Viết hàm tam_tamgiac(input) trả về tọa độ của trọng tâm và trực tâm của tam giác ABC.

-  Trả về tọa độ của trọng tâm và trực tâm của tam giác ABC ở dạng list theo thứ tự sau: [trongtam_x, trongtam_y, tructam_x, tructam_y]

h. Viết hàm giaima_tamgiac(input) trả về tất cả các kết quả ở trên theo thứ tự sau:

- Check 3 điểm A, B, C có tạo thành 1 tam giác hay không sử dụng hàm kiemtra_tamgiac(input):

+ Nếu đủ điều kiện, trả về đoạn text: “A, B, C hop thanh mot tam giac” và tiếp tục chương trình.

+ Nếu không đủ điều kiện, trả về đoạn text: “A, B, C khong hop thanh mot tam giac” và kết thúc chương trình.

- Trả về độ dài các cạnh và góc của tam giác ABC sử dụng hàm goccanh_tamgiac(input). Kết quả trả về là các đoạn text ở format sau:

+ “1. So do co ban cua tam giac:”

 “Chieu dai canh AB: AB” (Cần thay AB ở cuối bằng độ dài của cạnh AB).

 “Chieu dai canh BC: BC” (Cần thay BC ở cuối độ dài của cạnh BC).

 “Chieu dai canh CA: CA” (Cần thay CA ở cuối độ dài của cạnh BC).

 “ Goc A: BAC” (Cần thay BAC ở cuối bằng độ lớn của góc A).

“ Goc B: ABC” (Cần thay ABC ở cuối bằng độ lớn của góc B).

“ Goc C: BCA” (Cần thay BCA ở cuối bằng độ lớn của góc C).

- Trả về tính chất của tam giác ABC sử dụng hàm xet_tamgiac(input), kết quả trả về giống hệt với output của hàm.

- Trả về diện tích của tam giác ABC sử dụng hàm dientich_tamgiac(input), kết quả trả về là đoạn text ở format sau:

+ “2. Dien tich cua tam giac ABC: SABC” (Cần thay SABC bằng diện tích của tam giác ABC).

- Trả về độ dài các đường cao và khoảng cách từ 3 điểm A, B, C đến trọng tâm của tam giác sử dụng các hàm duongcao_tamgiac(input) và trungtuyen_tamgiac(input). Kết quả trả về là các đoạn text ở format sau:

+ “3. So do nang cao tam giac ABC:”

 “ Do dai duong cao tu dinh A: hA” (Thay hA bằng độ đài đường cao từ A).

 “ Do dai duong cao tu dinh B: hB” (Thay hB bằng độ đài đường cao từ B).

 “ Do dai duong cao tu dinh C: hC” (Thay hC bằng độ đài đường cao từ C).

 “ Khoang cach den trong tam tu dinh A: tA” (Thay tA bằng độ đài đến trọng tâm từ A).

 “ Khoang cach den trong tam tu dinh B: tB” (Thay tB bằng độ đài đến trọng tâm từ B).

 “ Khoang cach den trong tam tu dinh C: tC” (Thay tC bằng độ đài đến trọng tâm từ C).

- Trả về tọa độ của trọng tâm và trực tâm của tam giác ABC sử dụng hàm tam_tamgiac(input). Kết quả trả về là các đoạn text ở format sau:

+ “4. Toa do mot so diem dac biet cua tam giac ABC:”

 “Toa do trong tam: [x_trongtam, y_tructam]” (thay [x_trongtam, y_trong tam] bằng tòa độ của trọng tâm tam giác ABC).

 “Toa do truc tam: [x_tructam, y_tructam]” (thay [x_tructam, y_tructam] bằng tòa độ của trực tâm tam giác ABC).