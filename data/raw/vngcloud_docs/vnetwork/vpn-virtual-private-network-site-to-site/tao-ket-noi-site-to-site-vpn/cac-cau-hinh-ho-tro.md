# Các cấu hình hỗ trợ

Hiện tại Dịch vụ VPN đang hỗ trợ đa số các loại Cấu hình phổ biến có thể tương thích một các rộng rãi. Người dùng có thể tham khảo ở đây

### Authenticated Encryption (AEAD) Algorithms <a href="#authenticated_encryption_aead_algorithms" id="authenticated_encryption_aead_algorithms"></a>

<table><thead><tr><th width="183">Keyword</th><th width="390">Description</th><th>Note</th></tr></thead><tbody><tr><td>aes256gcm128</td><td>256 bit AES-GCM with 128 bit ICV</td><td>default value</td></tr><tr><td>aes192gcm128</td><td>192 bit AES-GCM with 128 bit ICV</td><td></td></tr><tr><td>aes128gcm128</td><td>128 bit AES-GCM with 128 bit ICV</td><td></td></tr><tr><td>aes256gcm96</td><td>256 bit AES-GCM with 96 bit ICV</td><td></td></tr><tr><td>aes192gcm96</td><td>192 bit AES-GCM with 96 bit ICV</td><td></td></tr><tr><td>aes128gcm96</td><td>128 bit AES-GCM with 96 bit ICV</td><td></td></tr><tr><td>aes256gcm64</td><td>256 bit AES-GCM with 64 bit ICV</td><td></td></tr><tr><td>aes192gcm64</td><td>192 bit AES-GCM with 64 bit ICV</td><td></td></tr><tr><td>aes128gcm64</td><td>128 bit AES-GCM with 64 bit ICV</td><td></td></tr><tr><td>aes256ccm128</td><td>256 bit AES-CCM with 128 bit ICV</td><td></td></tr><tr><td>aes192ccm128</td><td>192 bit AES-CCM with 128 bit ICV</td><td></td></tr><tr><td>aes128ccm128</td><td>128 bit AES-CCM with 128 bit ICV</td><td></td></tr><tr><td>aes256ccm96</td><td>256 bit AES-CCM with 96 bit ICV</td><td></td></tr><tr><td>aes192ccm96</td><td>192 bit AES-CCM with 96 bit ICV</td><td></td></tr><tr><td>aes128ccm96</td><td>128 bit AES-CCM with 96 bit ICV</td><td></td></tr><tr><td>aes256ccm64</td><td>256 bit AES-CCM with 64 bit ICV</td><td></td></tr><tr><td>aes192ccm64</td><td>192 bit AES-CCM with 64 bit ICV</td><td></td></tr><tr><td>aes128ccm64</td><td>128 bit AES-CCM with 64 bit ICV</td><td></td></tr><tr><td>aes256</td><td>256 bit AES-CBC</td><td></td></tr><tr><td>aes192</td><td>192 bit AES-CBC</td><td></td></tr><tr><td>aes128</td><td>128 bit AES-CB</td><td></td></tr></tbody></table>

### Integrity Algorithms (Hashing) <a href="#integrity_algorithms" id="integrity_algorithms"></a>

_Hash is ignored with GCM algorithms_

<table><thead><tr><th>Keyword</th><th width="389">Description</th><th>isDefault</th></tr></thead><tbody><tr><td>sha2_256</td><td>SHA2_256_128 HMAC (128 bit)</td><td>default value</td></tr><tr><td>sha2_384</td><td>SHA2_384_192 HMAC (192 bit)</td><td></td></tr><tr><td>sha2_512</td><td>SHA2_512_256 HMAC (256 bit)</td><td></td></tr><tr><td>sha</td><td>SHA1 HMAC (96 bit)</td><td>weak security</td></tr><tr><td>md5</td><td>MD5 HMAC (96 bit)</td><td>weak security</td></tr></tbody></table>

### Diffie Hellman Groups

<table><thead><tr><th>Keyworkd</th><th width="392">Description</th><th>Note</th></tr></thead><tbody><tr><td>modp8192</td><td>18 (8192 bit)</td><td></td></tr><tr><td>modp6144</td><td>17 (6144 bit)</td><td></td></tr><tr><td>modp4096</td><td>16 (4096 bit)</td><td></td></tr><tr><td>modp3072</td><td>15 (3072 bit)</td><td></td></tr><tr><td>modp2048</td><td>14 (2048 bit)</td><td>default value</td></tr><tr><td>modp1536</td><td>5 (1536 bit)</td><td>weak security</td></tr><tr><td>modp1024</td><td>2 (1024 bit)</td><td>weak security</td></tr><tr><td>modp768</td><td>1 (768 bit)</td><td>weak security</td></tr></tbody></table>

### &#x20;

