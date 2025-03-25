# API developers

## 1. Authentication&#x20;

* Đầu tiên, bạn truy cập vào ứng dụng Figma, chọn menu **App management** sau đó chọn tab **Credential:**

<figure><img src="../../../.gitbook/assets/image (672).png" alt=""><figcaption></figcaption></figure>

* Tiếp theo, bạn nhập **Username** và chọn **Group** nhóm quyền tương ứng (ở đây bạn nhóm quyền **Sigma Livestream Full**):

<figure><img src="../../../.gitbook/assets/image (671).png" alt=""><figcaption></figcaption></figure>

* Sau khi bạn chọn **Submit**, hệ thống **Sigma** sẽ sinh ra **Username** và **Secret Key**, quý khách cần lưu mật khẩu này lại hoặc tải xuống tệp tin **credentail** bằng cách chọn **Download as .env file**.

<figure><img src="../../../.gitbook/assets/image (673).png" alt=""><figcaption></figcaption></figure>

* Sau khi đã có **Username** và **Secret** **Key**, Quý khách dùng tool **Base64Encode** để tạo **token** cho header **Authorization** theo cú pháp như sau:

```actionscript
Authorization: Basic Base64Encode(<Username>:<Secret Key>)
```

* Cuối cùng, quý khách lấy thông tin **App ID** bằng cách chọn menu **App management,** chọn tab **General** sau đó quý khách có thể thấy thông tin **App ID** như hình sau

<figure><img src="../../../.gitbook/assets/image (674).png" alt=""><figcaption></figcaption></figure>

&#x20;

## 2.    API Tạo kênh live transcode

Để tạo một kênh live transcode với các setting sau:

* Ultra-low-latency
* Có sẵn 03 profile 1080p, 720p, 480p
* Catchup buổi live lưu vào S3 storage _(Lưu ý: nhập lại tên channel và cấu hình S3)_

bạn có thể sử dụng API sau:

```json
curl --location 'https://api.sigma.video/api/livestream/channels' \
--header 'X-App-Id: <app_id>' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic <token>' \
--data '{
    "name": "<channel_name>",
    "description": null,
    "tags": [],
    "transcodeProfile": [
        "fbffbd08-ed7f-4a51-aabd-3132ac863bb5",
        "54a3d4db-a827-45ae-b6be-1faa21c2e7c6",
        "33a26869-0a1b-49a4-8303-1284ac8fd034"
    ],
    "type": "transcode",
    "mode": "ultra-low-latency",
    "stopTimeout": 30,
    "catchup": true,
    "record": false,
    "outputFormat": "hls",
    "machine": {
        "enabled": true,
        "machineId": "94e98078-b9cb-4d44-b16e-369fdb81da35",
        "machineType": "SIGMA_MACHINE"
    },
    "destinationCatchup": {
        "type": "s3",
        "s3": {
            "accessKey": "<s3_access_key>",
            "bucket": "<bucket_name>",
            "endpoint": "<s3_end_point>",
            "secretKey": "<s3_secrect_key>",
            "region": "<s3_region>",
            "segmentPrefix": null
        }
    }
}'

```

Nếu kết quả call API thành công, mã **HTTP Response** sẽ là **201**, cùng với response body là một json object trong đó có thông tin quan trọng nhất là id của channel vừa tạo như ví dụ bên dưới. **ID** này được dùng trong các API start/stop livesession hoặc delete channel

```json
{
    "id": "42efeee4-e94e-4444-b0a6-90850413519d",
    "name": "Channel_02",
    "description": null,
    …
}

```

## 3.   Get thông tin của một channel

Sau khi tạo kênh, quý khách có thể lấy thông tin chi tiết của một channel bằng cách gọi API sau:

```json
curl --location 'https://api.sigma.video/api/livestream/channels/<channel_id>' \
--header 'X-App-Id: <app_id>' \
--header 'Authorization: Basic <token>'
```

Nếu kết quả call API thành công, mã HTTP Response sẽ là **200**. Trong đó có một số thông tin quan trọng như:

* `currentSessionId`: nếu channel đang trong phiên livestream thì ta sẽ nhận được id của phiên.
* Với kênh có cấu hình catchup for VOD lưu vào S3 thì endpoint truy cập đến file master.m3u8 sẽ có dạng như sau: `<s3>/sigma-livestream/<session_id>/catchup/master-catchup.m3u8`
* `rtmpServer`: rtmp url để push stream.
* `streamToken`: stream key.
* `liveStreamUrl`: URL để xem live.

Data nhận được sẽ như ví dụ sau:

```json
{
    "id": "42efeee4-e94e-4444-b0a6-90850413519d",
    "name": "Channel_02",
    "description": null,
    "tags": [],
    "appId": "0c787e24-87a3-47da-a131-e8310f35aff7",
    "inputId": "e5418288-37be-4d0f-8221-f0c5e99efe5b",
    "transcodeProfile": […],
    "type": "transcode",
    "mode": "ultra-low-latency",
    "stopTimeout": 30,
    "catchup": true,
    "destinationCatchup": {
        "type": "s3",
        "s3": { … }
    },
    "record": false,
    "outputFormat": "hls",
    "status": "active",
    "machine": { … },
    "createdAt": "2024-07-22T10:34:36.772Z",
    "updatedAt": "2024-07-23T06:15:31.729Z",
    "currentSessionId": "977cc345-d771-4223-9306-07c2b9d49a34",
    "input": {
        "streamToken":"42efe-a050270cbbab47cbfacd-3519d",
        "rtmpServer":"rtmp://103.245.251.51:1935/livestream"
    },
    "liveStreamUrl": http://103.245.251.51:8080/manifest/42efeee4-e94e-4444-b0a6-90850413519d/master.m3u8,

} 
```

## 4.   API start live channel

Sử dụng API như sau để start một live channel:

```json
curl --location --request PATCH 'https://api.sigma.video/api/livestream/channels/<channel_id>/start' \
--header 'X-App-Id: <app_id>' \
--header 'Authorization: Basic <token>'
```

Nếu kết quả call API thành công, mã HTTP Response sẽ là **200**.

## 5.   API stop live channel

Sử dụng API như sau để stop một live channel:

```json
curl --location --request DELETE 'https://api.sigma.video/api/livestream/channels/<channel_id>/stop' \
--header 'X-App-Id: <app_id>' \
--header 'Authorization: Basic <token>'
```

Nếu kết quả call API thành công, mã HTTP Response sẽ là **200**.

## 6.   Xóa một channel

Để xóa channel, sử dụng API như sau:

```json
curl --location 'https://api.sigma.video/api/livestream/sessions?q={"channelId":"<channel_id>"}&sort=updatedAt|desc&page=1&perPage=100' \
--header 'X-App-Id: <app_id>' \
--header 'Authorization: Basic <token>'

```

Nếu kết quả call API thành công, mã HTTP Response sẽ là **200**.

## 7.   Liệt kê danh sách live session của một channel

Mỗi phiên livestream của một channel sẽ được tracking lại thành một session. Chúng ta có thể dùng API như sau để lấy danh sách session của một channel:

```json
curl --location 'https://api.sigma.video/api/livestream/sessions?q={"channelId":"<channel_id>"}&sort=updatedAt|desc&page=1&perPage=100' \
--header 'X-App-Id: <app_id>' \
--header 'Authorization: Basic <token>'

```

Nếu kết quả call API thành công, mã HTTP Response sẽ là 200. Kết quả nhận được như ví dụ mẫu sau:

```json
{
    "data": [
        {
            "name": "Channel_02_2024-07-22-11:33:50",
            "status": "ended",
            "appId": "0c787e24-87a3-47da-a131-e8310f35aff7",
            "recordUrls": [],
            "clientInfo": {
                "action": "on_publish",
                "stream": "42efe-a050270cbbab47cbfacd-3519d",
                "ip": "103.245.252.19",
                "client_id": "y1799srf",
                "param": "",
                "tcUrl": "rtmp://103.245.251.51:1935/livestream",
                "ips": [],
                "app": "livestream",
                "stream_id": "vid-4024822"
            },
            "duration": 40,
            "isCreateTask": true,
            "channelId": "42efeee4-e94e-4444-b0a6-90850413519d",
            "channel": {
                "id": "42efeee4-e94e-4444-b0a6-90850413519d",
                "name": "Channel_02",
                ...
            },
            "id": "5017085c-d828-491d-837f-2160df3e07c1",
            "events": [],
            "createdAt": "2024-07-22T11:33:50.903Z",
            "updatedAt": "2024-07-22T11:35:02.898Z",
            "startedAt": "2024-07-22T11:34:20.064Z",
            "finishedAt": "2024-07-22T11:35:02.898Z"
        },
        {
            "name": "Channel_02_2024-07-22-11:32:35",
            "status": "ended",
            "appId": "0c787e24-87a3-47da-a131-e8310f35aff7",
            "recordUrls": [],
            "clientInfo": {
                "action": "on_publish",
                "stream": "42efe-a050270cbbab47cbfacd-3519d",
                "ip": "103.245.252.19",
                "client_id": "ii05j356",
                "param": "",
                "tcUrl": "rtmp://103.245.251.51:1935/livestream",
                "ips": [],
                "app": "livestream",
                "stream_id": "vid-2wx9608"
            },
            "duration": 10,
            "isCreateTask": true,
            "channelId": "42efeee4-e94e-4444-b0a6-90850413519d",
            "channel": {
                "id": "42efeee4-e94e-4444-b0a6-90850413519d",
                "name": "Channel_02"
				...
            },
            "events": [],
            "createdAt": "2024-07-22T11:32:35.675Z",
            "updatedAt": "2024-07-22T11:33:19.362Z",
            "startedAt": "2024-07-22T11:33:05.117Z",
            "finishedAt": "2024-07-22T11:33:19.362Z"
        }
    ],
    "total": 2,
    "count": 2,
    "page": 1,
    "perPage": 100
}

```

## 8.   Xem status của một session

Chúng ta có thể lấy trạng thái hoạt động của một live session bằng cách gọi API sau:

```json
curl --location 'https://api.sigma.video/api/livestream/sessions/<session_id>/status' \
--header 'X-App-Id: <app_id>' \
--header 'Authorization: Basic <token>'
```

Nếu kết quả call API thành công, mã HTTP Response sẽ là 200. Kết quả nhận được như ví dụ mẫu sau:

```json
{"status":"live"}
```

## 9.   Liệt kê danh sách event của một session

Trong quá trình hoạt động của một session các action như: khởi tạo, stop, start, tín hiệu bị gián đoạn, tín hiệu đã phục hồi, v.v… sẽ sinh ra và tracking thành các events. Ta có thể dùng API như bên dưới để lấy danh sách các event:

```json
curl --location 'https://api.sigma.video/api/livestream/events?q={"$and":[{"sessionId":"<session_id>"}]}&sort=updatedAt|desc&page=1&perPage=100' \
--header 'X-App-Id: <app_id>' \
--header 'Authorization: Basic <token>'

```

Nếu kết quả call API thành công, mã HTTP Response sẽ là 200. Kết quả nhận được như ví dụ mẫu sau:

```json
{
    "data": [
        {
            "actor": "user",
            "action": "ended",
            "sessionId": "5017085c-d828-491d-837f-2160df3e07c1",
            "id": "3b393448-65a8-4258-a418-2bfaa8cda40d",
            "createdAt": "2024-07-22T11:35:02.901Z",
            "updatedAt": "2024-07-22T11:35:02.901Z",
            "message": "Kênh đã kết thúc"
        },
        {
            "action": "stable",
            "sessionId": "5017085c-d828-491d-837f-2160df3e07c1",
            "id": "66df86b4-c0ed-4db7-868c-a12ca1830c58",
            "createdAt": "2024-07-22T11:34:20.063Z",
            "updatedAt": "2024-07-22T11:34:20.063Z",
            "message": "Kênh ổn định"
        }
	]
}

```
