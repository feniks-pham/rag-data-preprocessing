# Pull và Push image với docker

_\*Yêu cầu máy tính đã cài Docker engine (như Docker Desktop)_

## Push Image

Đầu tiên để có thể push image thì ta cần có sẵn 1 Repository trên vCR, ví dụ ta đã tạo sẵn 1 repo như sau:

<figure><img src="../../.gitbook/assets/image (13) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Để push image lên Repo, trước tiên ta cần gắn tag cho image

| “docker tag SOURCE\_IMAGE\[:TAG] vcr.vngcloud.vn/96000-sdkimage/IMAGE\[:TAG]” docker tag 09042024/hello-world vcr.vngcloud.vn/96000-sdkimage/hello-world:first |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- |

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Login bằng user/pass Repo

| docker login vcr.vngcloud.vn -u 96000-khaivt |
| -------------------------------------------- |

Với user là 96000-khaivt (xem trên portal) và pass là secret key khi tạo user

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Push image lên Repo:

| ![](file:///C:/Users/LAP14383-local/AppData/Local/Packages/oice_16_974fa576_32c1d314_3436/AC/Temp/msohtmlclip1/01/clip_image005.gif)    docker push vcr.vngcloud.vn/96000-sdkimage/IMAGE\[:TAG] docker push vcr.vngcloud.vn/96000-sdkimage/hello-world:first |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

<figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Pull Image

Đầu tiên ta cũng cân login bằng user và password như lúc push, sau đó thực hiện pull bằng lệnh sau:

| docker pull vcr.vngcloud.vn/96000-sdkimage/IMAGE\[:TAG] docker pull vcr.vngcloud.vn/96000-sdkimage/hello-world:first |
| -------------------------------------------------------------------------------------------------------------------- |

<figure><img src="../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
