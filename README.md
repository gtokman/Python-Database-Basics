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

New Terms

```
TextField()
```
* a field that holds a blob of text of any size

```
DateTimeField()
```
* a field for holding a date and a time

```
OrderedDict
 ```
* a handy container from the collections module that works like a dict but maintains the order that keys are added

```
.__doc__
```
* a magic variable that holds the docstring of a function, method, or class
 
``` 
sys
```
* a Python module that contains functionality for interacting with the system

```
sys.stdin
```
* a Python object that represents the standard input stream. In most cases, this will be the keyboard

```
.where()
```
* method that lets us filter our .select() results

```
.contains()
```
 * method that specifies the input should be inside the specified field
 
* os - Python module that lets us integrate with the underlying OS
* os.name - attribute that holds a name for the style of OS
* os.system() - method to allow Python code to call OS-level programs

* **/usr/bin/env what?**

If you're not sure what to put after /usr/bin/env, test it out in your terminal program.

Type in /usr/bin/env python and you should get a Python shell like normal. If it says 2.7 or something other than the 3.4 you should be expecting, try /usr/bin/env python3. Whichever of these gets you the correct Python shell is the one you should put at the top of your file.

# Links

[Peewee query methods](http://docs.peewee-orm.com/en/latest/peewee/querying.html)
[Time](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)