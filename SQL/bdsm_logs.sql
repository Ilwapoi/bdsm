create sequence bdsm_id_sequence start 1;

create table bdsm_logs
(
  id  integer unique NOT NULL default nextval('bdsm_id_sequence')
, test_value text
)