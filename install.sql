--
-- This script will install and configure the spatial database for
-- use with the sdp web application.
--

create database template_postgis with encoding='UTF8';

\c template_postgis;
\i /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql;
\i /usr/share/postgresql/9.1/contrib/postgis-1.5/spatial_ref_sys.sql;

\c postgres;
update pg_database set datistemplate='t', datallowconn='f' where datname='template_postgis';
create role sdp with login password '12345';
create database sdp with encoding='UTF8' owner=sdp template=template_postgis;

\c sdp
alter table spatial_ref_sys owner to sdp;
alter table geometry_columns owner to sdp;
alter view geography_columns owner to sdp;
create schema sdp authorization sdp;
