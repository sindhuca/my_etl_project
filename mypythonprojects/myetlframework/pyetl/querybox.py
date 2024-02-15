query='''
select a.emp_id,a.emp_name,b.sl_number,b.product_name,
    case b.sl_number when b.sl_number=a.emp_id then "active" else "inactive" end as curr_ind from employee.product b left join employee.emp_details a on 
    b.sl_number=a.emp_id;'''

insert = '''insert into data_warehouse.LZ_product(PID,PNAME,QTY,PRICE) values(%s,%s,%s,%s)'''
