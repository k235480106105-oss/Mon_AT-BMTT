# 1. RSA là gì?
RSA (Rivest–Shamir–Adleman) là một thuật toán mật mã bất đối xứng.
Khác với AES

RSA sử dụng hai khóa khác nhau nhưng có quan hệ toán học với nhau:
                    RSA
                     │
             ┌───────┴───────┐
             │               │
       Public Key        Private Key
       Khóa công khai    Khóa bí mật

Public Key
Có thể dùng công khai cho mọi người

Private Key
Phải giữ bí mật, chỉ sở hữu được phép sử dụng.
# 2. Nguyên lý toán học của RSA
RSA dựa trên tính chất của số nguyên tố và số học modulo, đặc biệt là việc phân tích một số rất lớn thành tích của hai số nguyên tố lớn là bài toán khó về mặt tính toán.
Quy trình sinh khóa:
 Chọn p, q
   ↓
Tính n = p × q
   ↓
Tính φ(n)
   ↓
Chọn e
   ↓
Tính d
   ↓
┌──────────────────┐
│ Public Key       │
│ (e, n)            │
└──────────────────┘

┌──────────────────┐
│ Private Key      │
│ (d, n)            │
└──────────────────┘
## 2.1. Bước 1 - Chọn hai số nguyên tố p và q
Đầu tiên chọn hai số nguyên tố khác nhau:
p và q

Trong hệ thống thực tế p,q phải là các số nguyên tố rất lớn và được sinh ngâu nhiên.
Để minh họa, ta dùng số nhỏ:

p= 61
q= 53

## 2.2. Bước 2 - Tính n
Tính: n = p x q

Với ví dụ: n = 61 x 53 = 3233

Giá trị n được sử dụng trong cả Public Key và Private Key.

## 2.3. Bước 3 - Tính Euler's Totient φ(n)
Vì: n = p × q

với p, q là hai số nguyên tố khác nhau, ta có:

φ(n) = (p - 1)(q - 1)

Thay số:

φ(n) = (61 - 1)(53 - 1) = 60 × 52  = 3120

## 2.4. Bước 4 - Chọn e

Tiếp theo chọn số nguyên e sao cho:

1 < e < φ(n)

và:

gcd(e, φ(n)) = 1

Nói cách khác, e và φ(n) phải nguyên tố cùng nhau.

Trong ví dụ:

e = 17

Kiểm tra:

gcd(17, 3120) = 1

Vậy e = 17 hợp lệ.

## 2.5 Bước 5 - Tính d

Ta cần tìm d sao cho:

e × d ≡ 1 (mod φ(n))

Hay:

17 × d ≡ 1 (mod 3120)

Kết quả:

d = 2753

Kiểm tra:

17 × 2753 = 46801

và:

46801 mod 3120 = 1

Do đó d = 2753 hợp lệ.

Trong thực tế, d được tính bằng Extended Euclidean Algorithm hoặc hàm tương đương để tìm modular inverse.

## 2.6. Sinh cặp khóa 

Sau khi có:

n = 3233
e = 17
d = 2753

ta có:

Public Key
Public Key = (e, n)

           = (17, 3233)
Private Key
Private Key = (d, n)

            = (2753, 3233)

Sơ đồ:

                 RSA KEY GENERATION

              p = 61       q = 53
                 │            │
                 └─────┬──────┘
                       ▼
                  n = p × q
                       │
                       ▼
                    n = 3233
                       │
                       ▼
                  φ(n) = 3120
                       │
              ┌────────┴────────┐
              │                 │
          Chọn e = 17      Tính d = 2753
              │                 │
              └────────┬────────┘
                       │
              ┌────────┴────────┐
              ▼                 ▼
        Public Key          Private Key
        (17, 3233)          (2753, 3233)
# 3. RSA mã hóa và giải mã
 
Sau khi có cặp khóa, RSA có thể sử dụng khóa công khai và khóa bí mật để thực hiện các phép toán mật mã.

Giả sử thông điệp sau khi chuyển thành số là:

m
Mã hóa

Sử dụng Public Key:

c = m^e mod n

Trong đó:

m: plaintext
e: public exponent
n: modulus
c: ciphertext

Giải mã

Sử dụng Private Key:

m = c^d mod n

Trong đó:

c: ciphertext
d: private exponent
n: modulus
m: plaintext ban đầu

Sơ đồ:

                 PUBLIC KEY
                    (e,n)
                       │
                       ▼
Plaintext ───────► RSA Encrypt
                       │
                       ▼
                  Ciphertext
                       │
                       ▼
                 RSA Decrypt
                       ▲
                       │
                 PRIVATE KEY
                    (d,n)
                       │
                       ▼
                   Plaintext