# 1. Mô hình 1 — Xác thực người gửi

Đây là mô hình chữ ký số RSA.

Giả sử:

Alice = người gửi
Bob   = người nhận

Alice có:

Alice Private Key
Alice Public Key
Quy trình

Alice:

Message
   │
   ▼
Hash
   │
   ▼
Sign bằng Alice Private Key
   │
   ▼
Signature

Alice gửi:

Message + Signature

Bob nhận được:

Message
Signature
Alice Public Key

Bob:

Message
   │
   ▼
Hash
   │
   ├───────────────┐
   │               │
   ▼               ▼
Hash           Verify Signature
                   ▲
                   │
            Alice Public Key
                   │
                   ▼
                 PASS

Nếu chữ ký hợp lệ:

- Đúng người sở hữu Private Key của Alice
- Dữ liệu không bị thay đổi

Đây chính là mô hình xác thực người gửi và đảm bảo toàn vẹn dữ liệu.

# 2. Mô hình 2 — Gửi dữ liệu cho người nhận

Giả sử:

Alice → Bob

Bob công khai:

Bob Public Key

Alice sử dụng:

Bob Public Key

để mã hóa dữ liệu.

                 Bob Public Key
                       │
                       ▼
Message ───────► RSA Encryption
                       │
                       ▼
                  Ciphertext
                       │
                       ▼
                 Bob Private Key
                       │
                       ▼
                  Plaintext

Chỉ người sở hữu:

Bob Private Key

mới có thể giải mã ciphertext tương ứng.

Ý nghĩa

Mô hình này đảm bảo:

- Tính bí mật
- Dữ liệu được mã hóa cho khóa của Bob

Mã hóa bằng Public Key của người nhận giúp đảm bảo tính bí mật đối với người sở hữu Private Key tương ứng; để xác thực danh tính người nhận cần có cơ chế tin cậy đối với Public Key.

# 3. Mô hình 3 — Xác thực cả hai

Alice muốn:

Bob chắc chắn dữ liệu đến từ Alice.
Chỉ Bob đọc được dữ liệu.

Quy trình:

                         ALICE
                           │
                      Plaintext
                           │
                           ▼
                  Hash + Sign
                           │
                    Alice Private Key
                           │
                           ▼
                  Digital Signature
                           │
                           ▼
                Encrypt for Bob
                           │
                    Bob Public Key
                           │
                           ▼
                  Encrypted Message
                           │
                           ▼
                          BOB
                           │
                  Bob Private Key
                           │
                           ▼
                       Decrypt
                           │
                  ┌────────┴────────┐
                  │                 │
               Message          Signature
                  │                 │
                  │           Alice Public Key
                  │                 │
                  └────────┬────────┘
                           ▼
                        Verify
                           │
                           ▼
                    ✓ Authentication
                    ✓ Confidentiality
                    ✓ Integrity

Trong thực tế, cách triển khai cụ thể cần tuân theo giao thức và thư viện chuẩn, không tự thiết kế protocol tùy ý.

# 4. So sánh tốc độ AES và RSA

RSA không được thiết kế để mã hóa dữ liệu lớn. Vì vậy không nên lấy:

1 MB
10 MB
100 MB

rồi bắt RSA mã hóa trực tiếp như AES.

RSA phù hợp hơn để mã hóa dữ liệu nhỏ, đặc biệt là khóa AES.

Benchmark hợp lý

Ta sẽ đo:

AES
1 KB
10 KB
100 KB
1 MB
RSA

Dùng dữ liệu nhỏ phù hợp với RSA-OAEP, ví dụ:

32 bytes
64 bytes
128 bytes

với RSA-2048 + OAEP/SHA-256.

Kết luận:

AES:
- nhanh
- xử lý dữ liệu lớn
- phù hợp mã hóa nội dung

RSA:
- chậm hơn
- xử lý dữ liệu nhỏ
- phù hợp trao đổi/bảo vệ khóa

Kết quả thực nghiệm cho thấy chữ ký RSA-PSS được xác minh thành công bằng Public Key của Alice. Khi nội dung thông điệp bị thay đổi, quá trình xác minh thất bại và thông điệp bị từ chối. Điều này chứng minh chữ ký số RSA có thể được sử dụng để xác thực nguồn gửi và kiểm tra tính toàn vẹn của dữ liệu.

# 5. Kết quả benchmark

AES-256-GCM:
      1024 bytes | Encrypt: 0.00000198 s | Decrypt: 0.00000191 s
     10240 bytes | Encrypt: 0.00000521 s | Decrypt: 0.00000662 s
    102400 bytes | Encrypt: 0.00002786 s | Decrypt: 0.00002615 s
   1048576 bytes | Encrypt: 0.00057777 s | Decrypt: 0.00049693 s

RSA-2048-OAEP:
        32 bytes | Encrypt: 0.00003329 s | Decrypt: 0.00093646 s
        64 bytes | Encrypt: 0.00003315 s | Decrypt: 0.00073062 s
       128 bytes | Encrypt: 0.00004860 s | Decrypt: 0.00062878 s

Kết quả thực nghiệm cho thấy AES-256-GCM có tốc độ xử lý rất nhanh và có khả năng xử lý dữ liệu có kích thước lớn. Khi kích thước dữ liệu tăng từ 1 KB lên 1 MB, AES vẫn hoàn thành quá trình mã hóa và giải mã trong thời gian rất ngắn.

Trong khi đó, RSA-2048-OAEP có chi phí tính toán cao hơn đáng kể, đặc biệt ở quá trình giải mã. RSA cũng bị giới hạn về kích thước dữ liệu có thể mã hóa trực tiếp. Vì vậy, RSA không phù hợp để mã hóa trực tiếp các dữ liệu lớn.

Từ kết quả trên có thể thấy AES phù hợp để mã hóa nội dung dữ liệu, còn RSA phù hợp hơn cho việc trao đổi hoặc bảo vệ khóa mã hóa đối xứng.

# 6. Cách dùng kết hợp sức mạnh của RSA và AES

Mục tiêu của chương trình:

Alice
  │
  │ Plaintext
  ▼
AES-256-GCM
  │
  ├──────────────► Ciphertext
  │
  ▼
AES Key
  │
  ▼
RSA-2048-OAEP
  │
  │ Bob Public Key
  ▼
Encrypted AES Key

Bob nhận:

Ciphertext
Encrypted AES Key
Nonce

Sau đó:

Encrypted AES Key
       │
       ▼
Bob Private Key
       │
       ▼
   AES Key
       │
       ▼
AES-256-GCM
       │
       ▼
Plaintext

Chương trình sinh AES-256 key và nonce ngẫu nhiên cho mỗi lần mã hóa. AES-GCM sử dụng AES key để mã hóa plaintext, sau đó RSA-OAEP sử dụng Public Key của người nhận để mã hóa AES key. Người nhận sử dụng Private Key để khôi phục AES key và thực hiện giải mã ciphertext.