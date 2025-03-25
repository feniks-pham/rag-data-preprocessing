# Tổng quan container

Để lưu trữ dữ liệu của bạn trong một project, bạn cần tạo một container và tải các object lên container đó. Container là đối tượng chứa dữ liệu (Object) trong vStorage có thể hiểu đối tượng này tương đương một thư mục trong hệ điều hành. Bạn có thể quản lý tệp và thư mục bằng các công cụ và API được cung cấp.

Trong một project sẽ có thể khởi tạo một hoặc nhiều container có vai trò như 1 directory chứa dữ liệu tuy nhiên container sẽ khác với directory ở mặt container là 1 phân cấp cho phép người dùng hoặc nhà cung cấp dịch vụ đưa ra các tính năng và thực thi chúng từ phân cấp này trở xuống. Ví dụ chúng tôi cung cấp các tính năng quota, lifecycle, ACLs,... cho mỗi container trong một project.

Về mặt triển khai, các project, container, object là tài nguyên của vStorage và chúng tôi cũng cung cấp API để bạn quản lý chúng. Ví dụ: bạn có thể tạo một project, container và tải các object lên bằng cách sử dụng API. Bạn cũng có thể sử dụng giao diện quản trị mà chúng tôi cung cấp hoặc các 3rd party softwares để thực hiện các thao tác này.&#x20;

Phần này mô tả cách làm việc với các container. Để biết thông tin về cách làm việc với các container, hãy xem [Làm việc với container](./).

\
