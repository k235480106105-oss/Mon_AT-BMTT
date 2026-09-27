# 1. Tìm hiểu thuật toán mã hóa DES và AES

## 1.1. Tổng quan về mã hóa đối xứng

Mã hóa đối xứng (Symmetric Encryption) là phương pháp mã hóa trong đó cùng một khóa bí mật được sử dụng cho quá trình mã hóa và giải mã dữ liệu.

Quy trình tổng quát:

                 Khóa bí mật
                     │
                     ▼
Plaintext ──► Mã hóa đối xứng ──► Ciphertext
                                      │
                                      ▼
                              Mã hóa đối xứng
                                      │
                                      ▲
                                 Khóa bí mật
                                      │
                                      ▼
                                  Plaintext
Ưu điểm của mã hóa đối xứng là tốc độ xử lý nhanh và phù hợp để mã hóa lượng dữ liệu lớn.
Hai thuật toán mã hóa đối xứng quan trọng là DES và AES

## 1.2. Thuật toán DES
### 1.2.1 Khái niệm
DES (Data Encryption Standard) là một thuật toán mã hóa đối xứng được phát triển từ thuật toán Lucifer và được sử dụng rộng rãi trong các hệ thống bảo mật trước khi các thuật toán hiện đại hơn xuất hiện.
DES mã hóa dữ liệu theo từng khối có kích thước 64 bit.
Mặc dù khóa DES được biểu diễn với độ dài 64 bit, trong đó 8 bit được sử dụng cho mục đích kiểm tra parity. Do đó, độ dài khóa hiệu dụng của DES là 56 bit.
### 1.2.2 Các đặc điểm chính của DES
| Đặc điểm                  | DES                      |
| ------------------------- | ------------------------ |
| Tên đầy đủ                | Data Encryption Standard |
| Loại                      | Mã hóa đối xứng          |
| Kích thước block          | 64 bit                   |
| Kích thước khóa biểu diễn | 64 bit                   |
| Kích thước khóa hiệu dụng | 56 bit                   |
| Số vòng                   | 16                       |
| Cấu trúc                  | Feistel Network          |
### 1.2.3 Cấu trúc của DES
DES sử dụng cấu trúc Feistel Network
Quy trình mã hóa tổng quát:
Plaintext 64 bit
       │
       ▼
Initial Permutation
       │
       ▼
   L0      R0
    \      /
     \    /
      16 vòng
       │
       ▼
Final Permutation
       │
       ▼
Ciphertext 64 bit
Sau phép hoán vị ban đầu, khối dữ liệu 64 bit được chia thành hai phần:
L0 = 32 bit
R0 = 32 bit
Sau đó dữ liệu được xử lý qua 16 vòng.
### 1.2.4 Một vòng DES
Ở vòng thứ i, DES thực hiện:
Li = R(i-1)
Ri = L(i-1) XOR F(R(i-1), Ki)
Trong đó:
Li là nửa trái của vòng hiện tại.
Ri là nửa phải của vòng hiện tại.
Ki là khóa con của vòng.
F là hàm biến đổi của DES.
Hàm F gồm các bước:
R(i-1)
   │
   ▼
Expansion
32 bit → 48 bit
   │
   ▼
XOR với Round Key
   │
   ▼
S-Boxes
48 bit → 32 bit
   │
   ▼
Permutation
   │
   ▼
Kết quả hàm F
DES thực hiện tổng cộng 16 vòng
### 1.2.5 Sinh khóa con trong DES 
Từ khóa ban đầu, DES thực hiện quá trình Key Schedule để tạo ra 16 khóa con.
Mỗi khóa con có kích thước 48 bit
DES Key
   │
   ▼
Key Schedule
   │
   ├── K1
   ├── K2
   ├── K3
   ├── ...
   └── K16
Mỗi vòng sử dụng một khóa con khác nhau.
### 1.2.6 Quy trình mã hóa DES
Quy trình mã hóa DES gồm các bước chính:
1. Nhận plaintext có kích thước 64 bit.
2. Thực hiện Initial Permutation.
3. Chia dữ liệu thành hai phần L0 và R0, mỗi phần 32 bit.
4. Thực hiện 16 vòng Feistel.
5. Ở mỗi vòng sử dụng một round key tương ứng.
6. Sau vòng thứ 16 thực hiện phép hoán vị cuối.
7. Thu được ciphertext 64 bit.
### 1.2.7 Quy trình giải mã DES
DES có ưu điểm của cấu trúc Feistel là quá trình giải mã sử dụng cấu trúc tương tự quá trình mã hóa.
Điểm khác biệt chính là thứ tự sử dụng các khóa con được đảo ngược:
Mã hóa:
K1 → K2 → K3 → ... → K16

Giải mã:
K16 → K15 → K14 → ... → K1
Sau khi thực hiện quá trình giải mã, plaintext ban đầu được khôi phục.
### 1.2.8 Nhược điểm của DES 
Nhược điểm lớn nhất của DES là khóa hiệu dụng chỉ có 56 bit.
Số lượng khóa có thể có là: 2^56
Với năng lực tính toán hiện đại, không gian khóa này không còn đủ lớn để chống lại các cuộc tấn công brute-force.
Do đó DES không còn được khuyến nghị sử dụng cho các hệ thống bảo mật hiện đại.
DES đã được thay thế bởi các thuật toán có độ dài khóa lớn hơn, trong đó AES là một trong những thuật toán quan trọng nhất.
## 1.3 Thuật toán AES 
### 1.3.1 Khái niệm AES
AES (Advanced Encryption Standard) là một thuật toán mã hóa đối xứng hiện đại được sử dụng rộng rãi để bảo vệ dữ liệu.
AES được thiết kế để thay thế DES và cung cấp mức độ bảo mật cao hơn với kích thước khóa lớn hơn.
AES sử dụng block có kích thước cố định là 128 bit.
AES hỗ trợ ba kích thước khóa:
AES-128
AES-192
AES-256
### 1.3.2 Các đặc điểm chính của AES
| Đặc điểm   | AES-128 | AES-192 | AES-256 |
| ---------- | ------: | ------: | ------: |
| Block size | 128 bit | 128 bit | 128 bit |
| Key size   | 128 bit | 192 bit | 256 bit |
| Số vòng    |      10 |      12 |      14 |
### 1.3.3 Cấu trúc AES
AES sử dụng cấu trúc Substitution-Permutation Network.
Dữ liệu được biểu diễn dưới dạng một ma trận trạng thái (State) gồm 16 byte:
┌────┬────┬────┬────┐
│    │    │    │    │
├────┼────┼────┼────┤
│    │    │    │    │
├────┼────┼────┼────┤
│    │    │    │    │
├────┼────┼────┼────┤
│    │    │    │    │
└────┴────┴────┴────┘
       4 × 4 byte
       = 128 bit
AES thực hiện nhiều vòng biến đổi trên State 
### 1.3.4 Quy trình mã hóa AES
Đối với AES-256, quy trình tổng quát:
Plaintext
    │
    ▼
AddRoundKey
    │
    ▼
Round 1
    │
    ├── SubBytes
    ├── ShiftRows
    ├── MixColumns
    └── AddRoundKey
    │
    ▼
Round 2
    │
   ...
    │
    ▼
Round 13
    │
    ├── SubBytes
    ├── ShiftRows
    ├── MixColumns
    └── AddRoundKey
    │
    ▼
Final Round
    │
    ├── SubBytes
    ├── ShiftRows
    └── AddRoundKey
    │
    ▼
Ciphertext
AES-256 có tổng cộng 14 vòng.
### 1.3.5 Quy trình giải mã AES
Để giải mã ciphertext, AES sử dụng các phép biến đổi nghịch đảo:
InvShiftRows
InvSubBytes
InvMixColumns
AddRoundKey

Quy trình tổng quát:
Ciphertext
    │
    ▼
Inverse AddRoundKey
    │
    ▼
InvShiftRows
    │
    ▼
InvSubBytes
    │
    ▼
InvMixColumns
    │
   ...
    │
    ▼
Plaintext
Các Round Key được sử dụng theo thứ tự phù hợp với quá trình giải mã.

# 2. So sánh DES và AES
| Tiêu chí                   | DES                      | AES                              |
| -------------------------- | ------------------------ | -------------------------------- |
| Tên                        | Data Encryption Standard | Advanced Encryption Standard     |
| Loại                       | Đối xứng                 | Đối xứng                         |
| Block size                 | 64 bit                   | 128 bit                          |
| Key hiệu dụng              | 56 bit                   | 128/192/256 bit                  |
| Số vòng                    | 16                       | 10/12/14                         |
| Cấu trúc                   | Feistel Network          | Substitution-Permutation Network |
| Mức độ bảo mật hiện nay    | Không còn an toàn        | Được sử dụng rộng rãi            |
| Khả năng chống brute-force | Thấp                     | Cao hơn nhiều                    |
| Sử dụng hiện nay           | Không khuyến nghị        | Phổ biến                         |

Có thể kết luận rằng AES có mức độ bảo mật cao hơn DES nhờ kích thước khóa lớn hơn và thiết kế hiện đại hơn. DES hiện nay không còn phù hợp để bảo vệ dữ liệu nhạy cảm.

# 3. Kết quả thực nghiệm trên ngôn ngữ python
Dữ liệu đầu vào: 
Hello! This is my Information Security project.
Kết quả thực nghiệm
Plaintext:
Hello! This is my Information Security project.

AES Key:
361b167f16c7b35871b887a2f355d00ba9be21bb86cb10edb96bb3523249424d

Nonce:
b2f1308af615471e68a9f710

Ciphertext:
37139e5c65f77226c154d30d2b6e0d73793ce95ead34e6bb7f04f33b87ad1677a7bd05a1ca804c79c05c99a60dc46ca58c72ba0423197295c532afe19f3361

Decrypted plaintext:
Hello! This is my Information Security project.

Verification:
SUCCESS - Decryption matches original plaintext.

Kết quả cho thấy dữ liệu sau khi giải mã giống với plaintext ban đầu, chứng minh chương trình AES hoạt động chính xác.

# 4. Kết luận
DES và AES đều là các thuật toán mã hóa đối xứng, tuy nhiên DES sử dụng khóa hiệu dụng 56 bit nên hiện nay không còn đủ an toàn.
AES sử dụng block 128 bit và hỗ trợ khóa 128, 192 hoặc 256 bit. Trong đó AES-256 cung cấp không gian khóa lớn và được sử dụng rộng rãi trong các hệ thống bảo mật hiện đại.
Trong phạm vi bài thực hành, AES-256-GCM được triển khai bằng Python thông qua thư viện cryptography. Chương trình thực hiện thành công quá trình mã hóa plaintext thành ciphertext và giải mã ciphertext trở lại plaintext ban đầu.