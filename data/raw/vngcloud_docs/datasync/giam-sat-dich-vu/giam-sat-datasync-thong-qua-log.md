# Giám sát DataSync thông qua Log

#### Log là gì? <a href="#giamsatdatasyncthongqualog-loglagi" id="giamsatdatasyncthongqualog-loglagi"></a>

Log là các sự kiện được thu thập tại nhiều thời điểm khác nhau. Các sự kiện này thường được tạo ra bởi các application hoặc các service và chứa đầy đủ các thông tin về ngữ cảnh tại thời điểm sự kiện xảy ra.

***

#### Tại sao log lại hữu ích? <a href="#giamsatdatasyncthongqualog-taisaologlaihuuich" id="giamsatdatasyncthongqualog-taisaologlaihuuich"></a>

Log là một yếu tố quan trọng của an ninh mạng. Khi được thực thi đúng cách, ghi log có thể cung cấp cho chúng ta cái nhìn rõ ràng về những gì đang xảy ra hoặc đã xảy ra trong hệ thống của chúng ta, cho phép chúng ta chứng thực các sự kiện với độ chính xác cao hơn và thực hiện các điều chỉnh khi cần thiết.

***

#### Giám sát DataSync thông qua DataSync log trên hệ thống vMonitor Platform <a href="#giamsatdatasyncthongqualog-giamsatdatasyncthongquadatasynclogtrenhethongvmonitorplatform" id="giamsatdatasyncthongqualog-giamsatdatasyncthongquadatasynclogtrenhethongvmonitorplatform"></a>

Giám sát DataSync thông qua log thật dễ dàng khi bạn sử dụng hệ thống vMonitor Platform. Hãy yên tâm là vMonitor Platform cũng là một sản phẩm thuộc hệ sinh thái của VNG Cloud. Bạn có thể sử dụng vMonitor Platform để cấu hình các tính năng giám sát dựa trên logs của DataSync. Dĩ nhiên để có thể thực hiện giám sát được thì bạn cần mua gói log quota của dịch vụ vMonitor Platform. Chi tiết bạn có thể tham khảo tại [vMonitor Platform](../../vmonitor/).&#x20;

Nội dung logs được đẩy về hệ thống gồm các thông tin như sau:

<table data-header-hidden><thead><tr><th width="102"></th><th width="212"></th><th></th></tr></thead><tbody><tr><td>STT</td><td>Fields</td><td>Ý nghĩa</td></tr><tr><td>STT</td><td>Fields</td><td>Ý nghĩa</td></tr><tr><td>1</td><td>@timestamp</td><td>Thời gian sự kiện bắt đầu tương tự nội dung field "time"</td></tr><tr><td>2</td><td>rootUserAccountID</td><td>Account ID của tài khoản DataSync.</td></tr><tr><td>3</td><td>size</td><td>Kích cỡ file được transfer, đơn vị byte.</td></tr><tr><td>4</td><td>object</td><td>Tên file được transfer.</td></tr><tr><td>5</td><td>sourceObject</td><td></td></tr><tr><td>6</td><td>bucket</td><td>Tên bucket nguồn.</td></tr><tr><td>7</td><td>region</td><td>Region nguồn.</td></tr><tr><td>8</td><td>endpoint</td><td>Endpoint nguồn.</td></tr><tr><td>9</td><td>labels</td><td></td></tr><tr><td>10</td><td>taskid</td><td>Mã Task ID: được sinh ra trong mỗi chạy chạy một Transfer Job.</td></tr><tr><td>11</td><td>jobid</td><td>Mã Transfer Job ID: mã transfer job id mà bạn tạo từ DataSync Portal.</td></tr><tr><td>12</td><td>statusCode</td><td>Mã trạng thái transfer thành công hay thất bại.</td></tr><tr><td>13</td><td>source</td><td>Mặc định "datasync/access_log".</td></tr><tr><td>14</td><td>level</td><td>Mặc định "info".</td></tr><tr><td>15</td><td>host</td><td>Mặc định "VNGCLOUD"</td></tr><tr><td>16</td><td>time</td><td><br></td></tr><tr><td>17</td><td>objectType</td><td>Mặc định "*s3.Object".</td></tr><tr><td>18</td><td>destinationObject</td><td></td></tr><tr><td>19</td><td>bucket</td><td>Tên container đích nhận dữ liệu trên vStorage.</td></tr><tr><td>20</td><td>region</td><td>Region nhận dữ liệu</td></tr></tbody></table>
