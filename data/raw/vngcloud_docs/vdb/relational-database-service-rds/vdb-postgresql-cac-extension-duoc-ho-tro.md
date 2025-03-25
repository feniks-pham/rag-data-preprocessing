# vDB PostgreSQL - Các extension được hỗ trợ

PostgreSQL nổi tiếng với tính linh hoạt. Bạn hoàn toàn có thể mở rộng các core-function của Postgresql bằng các Extensions.

Mặc định, khi khởi tạo một database với vDB PostgreSQL, bạn đã được bật sẵn một số extension (danh sách bên dưới), ngoài ra bạn cũng có thể chủ động bật thêm một số extension khác tùy theo nhu cầu (danh sách bên dưới).

## **1.Danh sách các extension được bật sẵn:** <a href="#vdbpostgresql-cacextensionduochotro-1.danhsachcacextensionduocbatsan" id="vdbpostgresql-cacextensionduochotro-1.danhsachcacextensionduocbatsan"></a>

Đối với PostgreSQL, các database được tạo mới sẽ được bật sẵn các Extension như trong database **template1.**&#x20;

Sau khi tạo database, bạn có thể dùng lệnh:

|  `\dx` |
| ------ |

hoặc

| `select * from pg_extension;`  |
| ------------------------------ |

để xem danh sách các extension đã được bật trên database.

\


Dưới đây là danh sách các extension đã được bật sẵn:

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>No</strong></td><td><strong>Name</strong></td><td><strong>Description</strong></td><td><strong>Version Postgresql hỗ trợ</strong></td><td><strong>Version</strong></td></tr><tr><td>1</td><td>btree_gin</td><td>support for indexing common datatypes in GIN</td><td>TBU</td><td>1.2</td></tr><tr><td>2</td><td>btree_gist</td><td>support for indexing common datatypes in GiST</td><td>TBU</td><td>1.5</td></tr><tr><td>3</td><td>chkpass</td><td>data type for auto-encrypted passwords</td><td>TBU</td><td>1</td></tr><tr><td>4</td><td>citext</td><td>data type for case-insensitive character strings</td><td>TBU</td><td>1.4</td></tr><tr><td>5</td><td>cube</td><td>data type for multidimensional cubes</td><td>TBU</td><td>1.2</td></tr><tr><td>6</td><td>dict_int</td><td>text search dictionary template for integers</td><td>TBU</td><td>1</td></tr><tr><td>7</td><td>dict_xsyn</td><td>text search dictionary template for extended synonym processing</td><td>TBU</td><td>1</td></tr><tr><td>8</td><td>hstore</td><td>data type for storing sets of (key, value) pairs</td><td>TBU</td><td>1.4</td></tr><tr><td>9</td><td>isn</td><td>data types for international product numbering standards</td><td>TBU</td><td>1.1</td></tr><tr><td>10</td><td>lo</td><td>Large Object maintenance</td><td>TBU</td><td>1.1</td></tr><tr><td>11</td><td>ltree</td><td>data type for hierarchical tree-like structures</td><td>TBU</td><td>1.1</td></tr><tr><td>12</td><td>pg_trgm</td><td>text similarity measurement and index searching based on trigrams</td><td>TBU</td><td></td></tr><tr><td>13</td><td>plpgsql</td><td>PL/pgSQL procedural language</td><td>TBU<br></td><td>1</td></tr><tr><td>14</td><td>postgis</td><td>PostGIS geometry, geography, and raster spatial types and functions</td><td>TBU</td><td>2.5.4</td></tr><tr><td>15</td><td>postgres_fdw</td><td>foreign-data wrapper for remote PostgreSQL servers</td><td>TBU</td><td></td></tr><tr><td>16</td><td>unaccent</td><td>text search dictionary that removes accents</td><td>TBU</td><td></td></tr><tr><td>17</td><td>vector</td><td>vector data type and ivfflat and hnsw access methods</td><td>14, 15</td><td>0.8.0</td></tr></tbody></table>

**Lưu ý:** N**ế**u bạn muốn tạo database trắng hoàn toàn, hãy dùng **template0.**

VD:

| `CREATE DATABASE dbname TEMPLATE template0;` |
| -------------------------------------------- |

## **2. Danh sách các extension bạn có thể tự bật:** <a href="#vdbpostgresql-cacextensionduochotro-2.danhsachcacextensionbancothetubat" id="vdbpostgresql-cacextensionduochotro-2.danhsachcacextensionbancothetubat"></a>

Bạn có thể tự bật một Extension bằng cách chạy lệnh:

| create extension \<extension\_name>; |
| ------------------------------------ |

\


<table data-header-hidden><thead><tr><th></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Description</strong></td><td><strong>Version</strong></td></tr><tr><td>address_standardizer</td><td>Used to parse an address into constituent elements. Generally used to support geocoding address normalization step.</td><td>2.5.4</td></tr><tr><td>address_standardizer_data_us</td><td>Address Standardizer US dataset example</td><td>2.5.4</td></tr><tr><td>amcheck</td><td>functions for verifying relation integrity</td><td>1</td></tr><tr><td>autoinc</td><td>functions for autoincrementing fields</td><td>1</td></tr><tr><td>earthdistance</td><td>calculate great-circle distances on the surface of the Earth</td><td>1.1</td></tr><tr><td>fuzzystrmatch</td><td>determine similarities and distance between strings</td><td>1.1</td></tr><tr><td>insert_username</td><td>functions for tracking who changed a table</td><td>1</td></tr><tr><td>intagg</td><td>integer aggregator and enumerator (obsolete)</td><td>1.1</td></tr><tr><td>intarray</td><td>functions, operators, and index support for 1-D arrays of integers</td><td>1.2</td></tr><tr><td>moddatetime</td><td>functions for tracking last modification time</td><td>1</td></tr><tr><td>pageinspect</td><td>inspect the contents of database pages at a low level</td><td>1.6</td></tr><tr><td>pg_buffercache</td><td>examine the shared buffer cache</td><td>1.3</td></tr><tr><td>pg_freespacemap</td><td>examine the free space map (FSM)</td><td>1.2</td></tr><tr><td>pg_prewarm</td><td>prewarm relation data</td><td>1.1</td></tr><tr><td>pg_stat_statements</td><td>track execution statistics of all SQL statements executed</td><td>1.6</td></tr><tr><td>pg_trgm</td><td>text similarity measurement and index searching based on trigrams</td><td>1.3</td></tr><tr><td>pg_visibility</td><td>examine the visibility map (VM) and page-level visibility info</td><td>1.2</td></tr><tr><td>pgcrypto</td><td>cryptographic functions</td><td>1.3</td></tr><tr><td>pgrouting</td><td>pgRouting Extension</td><td>3.0.0</td></tr><tr><td>pgrowlocks</td><td>show row-level locking information</td><td>1.2</td></tr><tr><td>pgstattuple</td><td>show tuple-level statistics</td><td>1.5</td></tr><tr><td>postgis_sfcgal</td><td>PostGIS SFCGAL functions</td><td>2.5.4</td></tr><tr><td>postgis_tiger_geocoder</td><td>PostGIS tiger geocoder and reverse geocoder</td><td>2.5.4</td></tr><tr><td>postgis_topology</td><td>PostGIS topology spatial types and functions</td><td>2.5.4</td></tr><tr><td>refint</td><td>functions for implementing referential integrity (obsolete)</td><td>1</td></tr><tr><td>sslinfo</td><td>information about SSL certificates</td><td>1.2</td></tr><tr><td>tablefunc</td><td>functions that manipulate whole tables, including crosstab</td><td>1</td></tr><tr><td>tcn</td><td>Triggered change notifications</td><td>1</td></tr><tr><td>timetravel</td><td>functions for implementing time travel</td><td>1</td></tr><tr><td>tsm_system_rows</td><td>TABLESAMPLE method which accepts number of rows as a limit</td><td>1</td></tr><tr><td>tsm_system_time</td><td>TABLESAMPLE method which accepts time in milliseconds as a limit</td><td>1</td></tr><tr><td>unaccent</td><td>text search dictionary that removes accents</td><td>1.1</td></tr><tr><td>uuid-ossp</td><td>generate universally unique identifiers (UUIDs)</td><td>1.1</td></tr></tbody></table>

bạn có thể dùng lệnh sau để kiểm tra danh sách các extension đang được hỗ trợ trên vDB của mình:

| `select * from pg_available_extensions;` |
| ---------------------------------------- |

Nếu bạn cần extension nào chưa được hỗ trợ, vui lòng liên hệ với **VNG Cloud Support** để được hỗ trợ.



## **3. Lưu ý:** <a href="#vdbpostgresql-cacextensionduochotro-2.danhsachcacextensionbancothetubat" id="vdbpostgresql-cacextensionduochotro-2.danhsachcacextensionbancothetubat"></a>

\+ Extension vector chỉ available cho các vDB khởi tạo từ 08/01/2024.&#x20;

\+ Để sử dụng trên các vDB đã khởi tạo trước đó, bạn vui lòng liên hệ VNG Cloud Support để được hỗ trợ enable.

