# New Terms

```
.create()
```
* creates a new instance all at once

```
.select()
```
* finds records in a table

```
.save()
```
* updates an existing row in the database

```
.get()
```
* finds a single record in a table

```
.delete_instance()
```
* deletes a single record from the table

```
.order_by()
```
* - specify how to sort the records

```
if __name__ == '__main__'
```
* a common pattern for making code only run with the script is run and not when it's imported

```
db.close()
```
* not a method we used, but often a good idea. Explicitly closes the connection to the database.

```
.update()
```
* also something we didn't use. Offers a way to update a record without .get() and .save(). Example: Student.update(points=student['points']).where(Student.username == student['username']).execute()

# Links

[Peewee query methods](http://docs.peewee-orm.com/en/latest/peewee/querying.html)