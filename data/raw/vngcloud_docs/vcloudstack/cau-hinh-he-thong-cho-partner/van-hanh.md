# Vận hành

## <mark style="color:blue;">RESET PASSWORD VM</mark>

#### Bước 1: Cần xác định vm đang ở compute nào:

```
openstack server show <uuid_vm> | grep OS-EXT-SRV-ATTR:host
```

#### Bước 2: SSH đến compute chứa vm và thực hiện:



```
docker exec -it nova_libvirt bash -c virsh
set-user-password --user <user_name> --password <password> <uuid_vm>
```

***

## <mark style="color:blue;">Enable Disable interface</mark>

#### Bước 1: List các port được gắn trên VM

```
openstack port list --server <uuid_vm>
```

#### Bước 2: Thực hiện Disable port

```
openstack port set --disable <port_uuid>
```

***

## <mark style="color:blue;">Migrate Host</mark>

#### Bước 1: Thực hiện Stop vm

```
nova stop <uuid_vm>
```

#### Bước 2: Migrate vm sang host khác

```
openstack server migrate <uuid_vm>
```

#### Bước 3: Xác nhận migrate

```
nova resize-confirm <uuid_vm> 
```

#### Bước 4: Start vm kiểm tra

```
nova start <uuid_vm>
```
