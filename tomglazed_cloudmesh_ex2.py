>>> print cloudmesh.shell("cloud list")
TBD
+--------------+--------+
| cloud        | active |
+--------------+--------+
| aws          |        |
| azure        |        |
| devstack     |        |
| dreamhost    |        |
| hp           |        |
| hp_east      |        |
| india        |        |
| india_havana |        |
+--------------+--------+

>>> print cloudmesh.shell("cloud on india")
Refreshing tomglazed servers india ->
Refresh time: 0.231638261212
Store time: 0.4352647142912

>>> print cloudmesh.shell("cloud list")
TBD
+--------------+--------+
| cloud        | active |
+--------------+--------+
| aws          |        |
| azure        |        |
| devstack     |        |
| dreamhost    |        |
| hp           |        |
| hp_east      |        |
| india        |        |
| india_havana | True   |
+--------------+--------+
