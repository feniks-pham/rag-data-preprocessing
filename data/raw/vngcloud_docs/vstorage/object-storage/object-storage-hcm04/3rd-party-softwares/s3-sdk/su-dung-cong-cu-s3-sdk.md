# Sử dụng công cụ S3 SDK

## Một số use case thông thường (ví dụ đối với ngôn ngữ: Java & thư viện AWS SDK) <a href="#sudungcongcus3sdk-motsousecasethongthuong-vidudoivoingonngu-java-and-thuvienawssdk" id="sudungcongcus3sdk-motsousecasethongthuong-vidudoivoingonngu-java-and-thuvienawssdk"></a>

**Tạo một bucket mới**

> s3Client.createBucket(\<CONTAINER-NAME>);

**Lấy danh sách tất cả object trong một bucket**

> ObjectListing objectListing = s3Client.listObjects(\<CONTAINER-NAME>);\
> for (S3ObjectSummary os : objectListing.getObjectSummaries()) {\
> System.out.println(os.getKey());\
> }

**Tải lên tệp tin vào một bucket** &#x20;

> s3Client.putObject(\<CONTAINER-NAME>, \<KEY-NAME>, new File(\<PATH-TO-LOCAL-FILE>));

**Xóa một object trong một bucket**

> s3Client.deleteObject(\<CONTAINER-NAME>, \<KEY-NAME>);

**Xóa một bucket**

> ObjectListing objectListing = s3Client.listObjects(\<CONTAINER-NAME>);
>
> if (CollectionUtils.isNotEmpty(objectListing.getObjectSummaries())) {\
> String\[] objkeyArr = objectListing.getObjectSummaries().stream().map(S3ObjectSummary::getKey)\
> &#x20; .toArray(String\[]::new);\
> DeleteObjectsRequest delObjReq = new DeleteObjectsRequest(bucket).withKeys(objkeyArr);\
> s3Client.deleteObjects(delObjReq);\
> }
>
> s3Client.deleteBucket(bucket);

**Di chuyển một object**

> s3Client.copyObject(\<SOURCE-CONTAINER-NAME>, \<SOURCE-KEY-NAME>,\
> \<DEST-CONTAINER-NAME>, \<DEST-KEY-NAME>);\
> s3Client.deleteObject(\<SOURCE-CONTAINER-NAME>, \<SOURCE-KEY-NAME>);

***

## Một số use case nâng cao <a href="#sudungcongcus3sdk-motsousecasenangcao" id="sudungcongcus3sdk-motsousecasenangcao"></a>

**Chuyển chế độ công khai bucket**

> s3Client.setBucketAcl(\<CONTAINER-NAME>, CannedAccessControlList.PublicRead);

**Chuyển chế độ riêng tư bucket**

> s3Client.setBucketAcl(\<CONTAINER-NAME>, CannedAccessControlList.Private);

#### Chú ý khi sử dụng S3 SDK <a href="#sudungcongcus3sdk-chuykhisudungs3sdk" id="sudungcongcus3sdk-chuykhisudungs3sdk"></a>

{% hint style="info" %}
**Chú ý:**

* Khi bạn sử dụng S3 SDK để tải lên tệp tin lớn (multipart upload), tệp tin được chia thành nhiều segment để tải lên hệ thống vStorage. Trong quá trình tải của tệp tin, có thể có một số segment được tải lên, một số segment không được tải lên do gặp lỗi như network có vấn đề, hệ thống vStorage đang quá tải, ứng dụng của bạn bị dừng chạy, treo, v.v. Tệp tin khi đó được xem như tải lên không thành công, các segment đã được tải lên được xem như là các incomplete segment hay là segment rác và đang chiếm dụng dung lượng lưu trữ của bạn. Chúng tôi khuyến cáo bạn nên chủ động xóa các segment rác này trong ứng dụng của bạn để tối ưu chi phí và dung lượng lưu trữ của project mà bạn đang sử dụng.
{% endhint %}
