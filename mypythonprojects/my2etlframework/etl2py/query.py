# query = '''select count(*) from employee.emp_details'''

# query = '''insert into data_warehouse.LZ_product(PID,PNAME,QTY,PRICE)
# values(%s,%s,%s,%s)'''

temp = '''create temporary table data_warehouse.temp_product(
PID int, PNAME varchar(100), QTY varchar(50), PRICE int
)'''

insrt_temp = '''insert into data_warehouse.temp_product(PID,PNAME,QTY,PRICE)
values(%s,%s,%s,%s)'''

dell = '''delete from data_warehouse.LZ_product'''

pre_process = '''insert into data_warehouse.LZ_product
select pid,pname,if(qty=0,'out of stock',qty) as QTY,price from data_warehouse.temp_product;'''

