query = '''create table {}({} {},
{} {},
{} {},
{} {},
{} {},
{} {})'''

insrt_query = '''insert into data_warehouse.claims2024(claim_id,
name ,gender,clm_eff_date,clm_term_date,status)  values(%s,%s,%s,%s,%s,%s);'''
count = '''select count(*) from information_schema.columns 
where table_schema = "data_warehouse" and table_name = "claims2024";'''

