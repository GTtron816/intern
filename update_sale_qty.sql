create or replace procedure updatesale(saleid int,prid int,dailys int,dd date,c_id int)
language plpgsql
as $$
begin
insert into sale values(saleid,prid,dailys,dd,c_id);
update item set qty=qty-(select dailysale from sale where sale_id=saleid) where item_id=prid;
commit;
end;$$;