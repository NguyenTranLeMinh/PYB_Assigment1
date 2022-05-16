import typing
import numpy as np
from math import sqrt, asin, degrees


# additional function # AF1
def check_input(stdin: str) -> bool:
    err_message = 'Invalid Input'
    out = True
    
    ABC = stdin.split()
    # Đủ 6 tọa độ
    if len(ABC) != 6:
        err_message = 'Vui lòng nhập vừa đủ 6 tọa độ.'
        out = False
    else:
        # Numeric
        try:
            ABC = list(map(float, ABC))
        except ValueError as e:
            err_message = e
            out = False
    print(f'Info: {err_message}\n')
    return out


# additional function # AF2
def canh(ABC: typing.List[float]) -> typing.List[float]:
    Ax, Ay, Bx, By, Cx, Cy = ABC
    BC = sqrt((Bx-Cx)**2 + (By-Cy)**2) # Đoạn BC
    CA = sqrt((Cx-Ax)**2 + (Cy-Ay)**2) # Đoạn CA
    AB = sqrt((Ax-Bx)**2 + (Ay-By)**2) # Đoạn AB
    return [AB, BC, CA]


# 1
def kiemtra_tamgiac(ABC: typing.List[float]) -> bool:
    AB, BC, CA = canh(ABC) # unpacking
    return True if abs(BC-CA) < AB < BC + CA else False


# 4
def dientich_tamgiac(ABC: typing.List[float]) -> float:
    AB, BC, CA = canh(ABC)
    p = (AB + BC + CA) / 2
    return round(sqrt(p*(p - AB)*(p - BC)*(p - CA)), 2)


# 2
def goccanh_tamgiac(ABC: typing.List[float]) -> typing.List[float]:
    AB, BC, CA = canh(ABC)
    S = dientich_tamgiac(ABC)
    A = degrees(asin(2*S / (CA*AB))) if CA**2 + AB**2 > BC**2 else 180. - degrees(asin(2*S / (CA*AB)))
    B = degrees(asin(2*S / (AB*BC))) if AB**2 + BC**2 > CA**2 else 180. - degrees(asin(2*S / (CA*AB)))
    C = degrees(asin(2*S / (BC*CA))) if BC**2 + CA**2 > AB**2 else 180. - degrees(asin(2*S / (CA*AB)))
    return list(map(lambda x: round(x, 2), [AB, BC, CA, A, B, C]))


# 3
def xet_tamgiac(ABC: typing.List[float]) -> str:
    out = None
    AB, BC, CA, A, B, C = goccanh_tamgiac(ABC)
    # tam giác đều
    if AB == BC and BC == CA:
        out = 'ABC la tam giac deu'
    # tam giác cân
    elif AB == BC:
        if B == 90:
            out = 'ABC la tam giac vuong can tai dinh B'
        elif B > 90:
            out = 'ABC la tam giac tu va can tai dinh B'
        else:
            out = 'ABC là tam giac can tai dinh B'
    elif BC == CA:
        if C == 90:
            out = 'ABC la tam giac vuong can tai dinh C'
        elif C > 90:
            out = 'ABC la tam giac tu va can tai dinh C'
        else:
            out = 'ABC là tam giac can tai dinh C'
    elif CA == AB:
        if A == 90:
            out = 'ABC la tam giac vuong can tai dinh A'
        elif A > 90:
            out = 'ABC la tam giac tu va can tai dinh A'
        else:
            out = 'ABC là tam giac can tai dinh A'
    # độ dài 3 cạnh khác nhau đôi một
    else:
        if A == 90:
            out = 'ABC la tam giac vuong tai dinh A va la tam giac binh thuong'
        elif A > 90:
            out = 'ABC la tam giac tu tai dinh A va la tam giac binh thuong'
        elif B == 90:
            out = 'ABC la tam giac vuong tai dinh B va la tam giac binh thuong'
        elif B > 90:
            out = 'ABC la tam giac tu tai dinh B va la tam giac binh thuong'
        elif C == 90:
            out = 'ABC la tam giac vuong tai dinh C va la tam giac binh thuong'
        elif C > 90:
            out = 'ABC la tam giac tu tai dinh C va la tam giac binh thuong'
        else:
            out = 'ABC la tam giac binh thuong'
    
    return out


# 5
def duongcao_tamgiac(ABC: typing.List[float]) -> typing.List[float]:
    AB, BC, CA = canh(ABC)
    dcA = 2*dientich_tamgiac(ABC) / BC
    dcB = 2*dientich_tamgiac(ABC) / CA
    dcC = 2*dientich_tamgiac(ABC) / AB
    return list(map(lambda x: round(x, 2), [dcA, dcB, dcC]))


# 6
def trungtuyen_tamgiac(ABC: typing.List[float]) -> typing.List[float]:
    Ax, Ay, Bx, By, Cx, Cy = ABC
    Gx = (Ax + Bx + Cx) / 3
    Gy = (Ay + By + Cy) / 3
    ttA = sqrt((Gx - Ax)**2 + (Gy - Ay)**2)
    ttB = sqrt((Gx - Bx)**2 + (Gy - By)**2)
    ttC = sqrt((Gx - Cx)**2 + (Gy - Cy)**2)
    return list(map(lambda x: round(x, 2), [ttA, ttB, ttC]))


# additional function # AF3
def ptdt_vuonggoc(diem_x: float, diem_y: float, L: typing.List[float]) -> typing.List[float]:
    # Phương trình tổng quát đường thẳng d trong Oxy là (d): ax + by + c = 0
    # Giá trị trả về là đường thẳng d biểu diễn bởi 1 List: ptd = [a, b, c]  
    # Tìm phương trình đường vuông góc L đi qua (diem_x, diem_y)
    x1, y1, x2, y2 = L
    # TH1: L // Ox
    if y1 == y2: 
        #ptL = [0., 1., y1]                  
        ptdtvg = [1., 0., -1. * diem_x - 0. * diem_y]
    # TH2: L // Oy
    elif x1 == x2: 
        #ptL = [1., 0., x1] 
        ptdtvg = [0., 1., -0. * diem_x - 1. * diem_y]
    # TH3: (L): y = ax + b (a != 0) 
    else:
        matrix1 = np.array([[x1, 1], [x2, 1]]).astype(np.float32)
        matrix2 = np.array([[y1], [y2]]).astype(np.float32)
        ptBC = np.linalg.pinv(matrix1) @ matrix2 # inner_product(matrix1 ^-1, matrix2),  Shape 2 x 1
        a_L, _ = ptBC.reshape((2,)) # [a_L, b_L]
        # Theo format ax + by + c = 0, ở đây là ax - y + b = 0
        ptdtvg = [-1./a_L, -1., diem_y - -1./a_L * diem_x]
    return ptdtvg


# 7
def tam_tamgiac(ABC: typing.List[float]) -> typing.List[float]:
    Ax, Ay, Bx, By, Cx, Cy = ABC
    _, _, _, A, B, C = goccanh_tamgiac(ABC)
    
    trongtam_x = (Ax + Bx + Cx) / 3
    trongtam_y = (Ay + By + Cy) / 3
    
    if A == 90:
        tructam_x, tructam_y = Ax, Ay
    elif B == 90:
        tructam_x, tructam_y = Bx, By
    elif C == 90:
        tructam_x, tructam_y = Cx, Cy
    else:
        # dt di qua A vuong goc BC: aA.x + bA.y + cA = 0
        aA, bA, cA = ptdt_vuonggoc(Ax, Ay, [Bx, By, Cx, Cy])
        # dt di qua B vuong goc CA: aB.x + bB.y + cB = 0
        aB, bB, cB = ptdt_vuonggoc(Bx, By, [Cx, Cy, Ax, Ay])

        m1 = np.array([[aA, bA], [aB, bB]])
        m2 = np.array([[-cA], [-cB]])
        truc_tam = np.linalg.pinv(m1) @ m2
        tructam_x, tructam_y = truc_tam.reshape((2,))

    return list(map(lambda x: round(x, 2), [trongtam_x, trongtam_y, tructam_x, tructam_y]))


# 8
def giaima_tamgiac(ABC: typing.List[float]) -> None:
    if not kiemtra_tamgiac(ABC):
        print('A, B, C khong hop thanh mot tam giac')
        return
    print('A, B, C hop thanh mot tam giac')

    AB, BC, CA, A, B, C = goccanh_tamgiac(ABC)
    print('1. So do co ban cua tam giac:')
    print('Chieu dai canh AB:', AB)
    print('Chieu dai canh BC:', BC)
    print('Chieu dai canh CA:', CA)
    print('Goc A:', A)
    print('Goc B:', B)
    print('Goc C:', C)
    print(xet_tamgiac(ABC))
    print('2. Dien tich cua tam giac ABC:', dientich_tamgiac(ABC))

    hA, hB, hC = duongcao_tamgiac(ABC)
    tA, tB, tC = trungtuyen_tamgiac(ABC)
    print('3. So do nang cao tam giac ABC:')
    print('Do dai duong cao tu dinh A:', hA)
    print('Do dai duong cao tu dinh B:', hB)
    print('Do dai duong cao tu dinh C:', hC)
    print('Khoang cach den trong tam tu dinh A:', tA)
    print('Khoang cach den trong tam tu dinh B:', tB)
    print('Khoang cach den trong tam tu dinh C:', tC)

    x_trongtam, y_trongtam, x_tructam, y_tructam = tam_tamgiac(ABC)
    print('4. Toa do mot so diem dac biet cua tam giac ABC:')
    print(f'Toa do trong tam: [{x_trongtam}, {y_trongtam}]')
    print(f'Toa do truc tam: [{x_tructam}, {y_tructam}]')



if __name__ == "__main__":
    # input
    input_mess = 'Nhập tọa độ các đỉnh A, B, C (cách nhau bởi khoảng trắng, theo thứ tự Ax, Ay, Bx, By, Cx, Cy): '
    stdin = input(input_mess)
    while not check_input(stdin):
        stdin = input(input_mess)
    
    # parameters
    ABC = list(map(float, stdin.split())) # Ax, Ay, Bx, By, Cx, Cy

    giaima_tamgiac(ABC)
