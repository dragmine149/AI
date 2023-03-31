# Calendar Creation

This was a mini project and below is the documentation. I wanted to translate my data into something more readable and usable (although already pretty good). The data consisted of 2 months worth of entry of different styles although repeated thoughout.
Yes i probably could have made a simple program which took less time, but i wanted to see what the ai thought about.

NOTE: this was done using ChatGPT 3.5

The full chat log that this program uses can be found [here](./Chatlog.txt). The most up to date version can be viewed [here](https://chat.openai.com/chat/0c328ad8-e571-4fc9-be06-547d6b1dfbf6) (that will also include more information if i do decide to update this, and also an easier viewable form).

## Part 1

Converting the data into python and a calendar.

### The original plan by the AI

So i gave the AI the below input

```txt
Here is some data:
30/01/23
L1 - alright, nice and peacful. did maths ME1, fixed some isues with EXP001
L2 - Did some more ME1, checked what i did (Still confused on some stuff). Released version 1.2.6 of PythonFunctions
L3 - Ooh regex intresting. Thought it was more usless stuff
L4 - AAAA, makes sense but annoying
L5 - It coursework, went well got a good amount done.

31/01/23
L1 - Tried to get some work done but computer and phone had failed to connect how i wanted it to. Finally fixed it and did some maths for a while
L2 - Explored the issue of PythonFunctions install cryptography using [google] and (hopefully) fixed that. Also did more maths
L3 - Maths lesson, alright notcied some very stupid mistakes (didn't answer question etc. Got set homework to do to finish going through my paper)
L4 - More maths, something intresting. Took a while to understand why things are how they are but after a while got the basics down.
L5 - Binary, just made some stuff using bits


Make a program to convert this into a calendar format.
```

and well, at first it wanted to make it hard coded, with for an expanding dataset would not have been useful.

#### Output

Here's a program that converts the provided data into a calendar format:

```python
# Define a function to convert date strings into datetime objects
from datetime import datetime

def parse_date(date_str):
    return datetime.strptime(date_str, '%d/%m/%y')

# Define a dictionary to map day labels to integer values
day_map = {'L1': 0, 'L2': 1, 'L3': 2, 'L4': 3, 'L5': 4}

# Define a list of tuples containing the date, day, and activity for each entry
entries = [
    (parse_date('30/01/23'), 'L1', 'alright, nice and peaceful. did maths ME1, fixed some issues with EXP001'),
    (parse_date('30/01/23'), 'L2', '
```

I cancled it whist it was typing, i did not want to hard code the data.

### The second plan

Sticking with the original data, this time not in a file, it carried on generating new code. This time however, i don't know what it was doing. The file it produced is [noclass.py](./noclass.py) which even apon running it, gives an index error. At the time of asking the AI this, i did not actually run that file, i just asked it to put it into a class instead.

### Classes have been introduced

Now using classes, something new starts. Makes it more readable (i think) as well. This time [v1.py](./V1.py) was generated which cased an error. The same error as [noclass.py](./noclass.py) generated eariler.

```py
Traceback (most recent call last):
  File "/mnt/d/Code/AI/CalendarCreate/noclass.py", line 19, in <module>
    day = parts[1]
IndexError: list index out of range
```

The error above, is the error generated.

After telling the error, generating [V2.py](./V2.py), giving the same error. It gave me debug which i didn't do as i wanted it to get most of the errors instead of me having to do some debug. I asked what it thinks [data.txt](./data.txt) should look like.

### Updating data.txt

After asking what the data should look like, it gave this response.

```text
30/01/23 - L1 - alright, nice and peacful. did maths ME1, fixed some isues with EXP001
30/01/23 - L2 - Did some more ME1, checked what i did (Still confused on some stuff). Released version 1.2.6 of PythonFunctions
30/01/23 - L3 - Ooh regex intresting. Thought it was more usless stuff
30/01/23 - L4 - AAAA, makes sense but annoying
30/01/23 - L5 - It coursework, went well got a good amount done.
31/01/23 - L1 - Tried to get some work done but computer and phone had failed to connect how i wanted it to. Finally fixed it and did some maths for a while
31/01/23 - L2 - Explored the issue of PythonFunctions install cryptography using [google] and (hopefully) fixed that. Also did more maths
31/01/23 - L3 - Maths lesson, alright notcied some very stupid mistakes (didn't answer question etc. Got set homework to do to finish going through my paper)
31/01/23 - L4 - More maths, something intresting. Took a while to understand why things are how they are but after a while got the basics down.
31/01/23 - L5 - Binary, just made some stuff using bits
```

It fixed itself and generated [V3.py](./V3.py) which instead of running straight away, i asked it to make it into a program where i could run the below in another file:

```py
from Calendar import Activities
Activities('data.txt')
```

Out of this, [calendar1.py](./calendar1.py) and [main1.py](./main1.py) was generated, and it used an intresting technique to me, `f.read().splitlines()`. I asked it the differences and it's quite surprising at first.

#### Input

```txt
on line 14 of 'calendar.py' what is the difference between your way and f.readlines()?
```

#### Output

```txt
On line 14 of calendar.py, I used the f.read().splitlines() method to read the contents of the file and split it into a list of lines, whereas you could also use f.readlines() to get a list of lines directly.

Both methods will give you a list of lines, but the f.read().splitlines() method has the advantage of automatically removing any trailing newline characters ('\n') from the end of each line, which can be convenient when parsing text data like in this case.

On the other hand, the f.readlines() method does not remove the trailing newline characters, so you would need to call the strip() method on each line separately to remove them, as I did on line 16.

In general, both methods are valid ways to read a file into a list of lines, and the choice between them depends on the specific needs of your program.
```

Now that i run [calendar1.py](./calendar1.py) i see that it produced an error, i belived it was due to the other types of data format not original included, so i gave it some more to process.

### More data to be processed

```txt
I added more data to data.txt including data as such below.
Now i get an error on line 25

10/03/23 - Snow day, no school. Online work

17/02/23
L1/L2 - IT not much happened. Learing Aim B
L3/L4 - Not much happened again, did some developing played games, some editing.
L5 - did me own stuff

01/02/23 -- Teacher strike day (1)
L1 - Did some work on PythonFunctions.Searching outside, quite nice just a bit too cold to spend a whole day out there at the moment.
L2 - Did some more work on PythonFunctions.Searching after finding a place to work
Break - Played osu! Lazer
L3 - Did some IT work on laptop from what i could recall from memory, also installed nodejs.
L4 - Finished first part of posts. Probably redraft it tomorrow on the computers. Someone spraied in the PS16 room, it smells now. Need to check powerpoint for more of the brief which i can't access at the moment. So just going to leave the rest for another day. Should be doing more, but still have a week to do so. Continued to play and made some changes to PythonFunctions.
Lunch - Went to find a new spot, couldnt find anything so headed back to original spot.
L5 - WOOL. Finished v1.3.0 of PythonFunctions. Went through (finished) maths trig paper we did in class. Done that homework.
```

Above is what i told the ai, the produced error and some extra data. I made it seemed like i wanted to add more data which caused the error and well, it gave an intresting response. Out comes [calendar2.py](./calendar2.py) which not only gave me an error, but didn't look the cleanest as well. As so, my next input was to try and fix both of these issues.

```text
Apprently there is an invalid line format here in line 2.
Data: L1 - alright, nice and peacful. did maths ME1, fixed some isues with EXP001

I also don't want more than 4 indents per function
I also don't want the use of 'else'
Could we also use 'enumerate' instead of range(len())?
```

After doing so, [calendar3.py](./calendar3.py) was produced, fixed the extra issues (mostly, other than an elif), and worked. After running it, we are actually geting somewhere. However the output just looked terrible. Produced way over 500 lines of output when i ran the program (which can't really be shown here so i have put it in [outputs/1.txt](./outputs/1.txt)). Not only was it terrible, it was also super excessive. so back to asking the ai.

### Reformating the output

```txt
The new program, needs to have support for reading from a file.
The data stored in that file can be one of the groups below (seperated by ------)
The program must print out the date, label and description in the following format (seperated by =====)

=====
dd/mm/yy
Label - activity
=====

----
30/01/23
L1 - alright, nice and peacful. did maths ME1, fixed some isues with EXP001
L2 - Did some more ME1, checked what i did (Still confused on some stuff). Released version 1.2.6 of PythonFunctions
L3 - Ooh regex intresting. Thought it was more usless stuff
L4 - AAAA, makes sense but annoying
L5 - It coursework, went well got a good amount done.
----
01/02/23 -- Teacher strike day (1)
L1 - Did some work on PythonFunctions.Searching outside, quite nice just a bit too cold to spend a whole day out there at the moment.
L2 - Did some more work on PythonFunctions.Searching after finding a place to work
Break - Played osu! Lazer
L3 - Did some IT work on laptop from what i could recall from memory, also installed nodejs.
L4 - Finished first part of posts. Probably redraft it tomorrow on the computers. Someone spraied in the PS16 room, it smells now. Need to check powerpoint for more of the brief which i can't access at the moment. So just going to leave the rest for another day. Should be doing more, but still have a week to do so. Continued to play and made some changes to PythonFunctions.
Lunch - Went to find a new spot, couldnt find anything so headed back to original spot.
L5 - WOOL. Finished v1.3.0 of PythonFunctions. Went through (finished) maths trig paper we did in class. Done that homework.
----
17/02/23
L1/L2 - IT not much happened. Learing Aim B
L3/L4 - Not much happened again, did some developing played games, some editing.
L5 - did me own stuff
----
10/03/23 - Snow day, no school. Online work
```

Above is the next input i gave it, this time i added an example of what i wanted, which kind of came back and bit me in the back later (you'll see). This new input gave one of the smallest program so far [Activites.py](./Activites.py) uppon running although it looked cleaner, not the desired output. (The output is shown in [outputs/2.txt](./outputs/2.txt)). This new data, being over 600 lines definitly had some duplication which was the goal to fix. The next couple of inputs are below because i stoped it half way during one to correct it. (Mine -> AI -> Mine)

```txt
I would like to change the desire output to the below format.

dd/mm/yy
=======
Label - activity

Keep going with Label - activity until the start of a new day
```

```txt
Sure, here's an updated version of the code that formats the output in the new desired format:

python

from datetime import datetime

class Activities:
    def __init__(self, filename):
        self.filename = filename
        self.activities = []
        self.read_data()
        self.print_activities()

    def read_data(self):
        with open(self.filename, 'r') as f:
            data = f.read().split('----\n')
            for day in data:
                day = day.strip()
                if day:
                    activities = day.split('\n')
                    date_str = activities.pop(0)
                    date = datetime.strptime(date_str, '%d/%m/%y')
                    for i, activity in enumerate(activities):
                        label, desc = activity.split(' - ')
                        self.activities.append({'date': date, 'label':

```

```
I'm sorry for what i said eariler, but my file does not contain `----`.
```

After correcting it with the '----' issue, [Activites2.py](./Activites2.py) was generated, this time printing less but giving this error message.

```py
Traceback (most recent call last):
  File "/mnt/d/Code/AI/CalendarCreate/Activites2.py", line 27, in <module>
    activities('data.txt')
  File "/mnt/d/Code/AI/CalendarCreate/Activites2.py", line 20, in activities
    label, desc = activity.split(' - ')
ValueError: not enough values to unpack (expected 2, got 1)
```

After telling it the error, a holw new category of files was created out of this.

### Parse Data files

The first file generated was, [ParseData.py](./ParseData.py) and after asking some questions back and forth due to basic things that got missed, i finally got an output. (The questions was just, missing this, error here, how do i run it).
[outputs/3.txt](./outputs/3.txt) shows the output. Now this is getting closer to a goal, got to take it in steps here. However as noticed, the Label was being duplciated multiple times and sometimes it was just outright breaking.

After generating [ParseData2.py](./ParseData2.py) not only did i gain an error, but the output was terrible. (Show in [outputs/4.txt](./outputs/4.txt)) Less data got ouputed but did run into an error. This time we had a bit of discussion (shown below) before heading back to make programs. (I start first, we alternate.)

```txt
This has just made it worser
```

```txt
I apologize for that. Can you please give me more details on the issue you're facing now?
```

```txt
Not the output i was excepting
```

```txt
I apologize for the incorrect output. Can you please clarify the desired output format again so I can assist you better?
```

```txt
EXCEPTED OUTPUT:

dd/mm/yy
=======
Label - activity
Label - activity
label - activity

EXAMPLE OUTPUT:
```

```txt
I apologize for the confusion. Here's the updated expected output for the function parse_data:
01/02/23

L1 - Did some work on PythonFunctions.Searching outside, quite nice just a bit too cold to spend a whole day out there at the moment.
L2 - Did some more work on PythonFunctions.Searching after finding a place to work
L3 - Did some IT work on laptop from what i could recall from memory, also installed nodejs.
L4 - Finished first part of posts. Probably redraft it tomorrow on the computers. Someone spraied in the PS16 room, it smells now. Need to check powerpoint for more of the brief which i can't access at the moment. So just going to leave the rest for another day. Should be doing more, but still have a week to do so. Continued to play and made some changes to PythonFunctions.
L5 - WOOL. Finished v1.3.0 of PythonFunctions. Went through (finished) maths trig paper we did in class. Done that homework.
17/02/23

L1/L2 - IT not much happened. Learing Aim B
L3/L4 - Not much happened again, did some developing played games, some editing.
L5 - did me own stuff
10/03/23

Snow day, no school. Online work
```

(Note, the last output ^^ the dates are in bold in the actual output)

After clarifing this, [ParseData3.py](./ParseData3.py) was made which gave an output, still not the one excepted. Shown in [outputs/5.txt](./outputs/5.txt). It was definitly better than the eariiler attempts but seperated data a bit too much, even though it had the correct output during the eariler test.

After generating [ParseData4.py](./ParseData4.py), reporting an error that occured, [ParseData5.py](./ParseData5.py), [ParseData6.py](./ParseData6.py) was generated still with the same error and seemed to be getting worse, so i just instead went back to [ParseData2.py](./ParseData2.py) and told it to fix the error. Out comes [ParseData7.py](./ParseData7.py) which of cause, gave me the same error. Then [ParseData8.py](./ParseData8.py) which fixed all the previous errors. (Other than the fact i messed up my own formatting in [data.txt](./data.txt) somehow)

But this was shown as a function, not what i original wanted (i asked for classes). I get that there hard been a lot of text and it might have forgot, so after promoting it came the new era of files of polloshing the code.

### Polloshing the code (and finishing touches)

```txt
Turn the program into a class, with dictionaries.
I want to then be able to call a function and pass in a specifiy date to get the infromation for that day
```

Out came [Calendar.py](./Calendar.py) translated it into a class and added some extra functions to do just the job. It even explained how to use the class which i just added in the file. Now at first run, it gave the same issue as most of `ParseData` gave me. Here the AI started to slightly break down (reason unknown), but i got my first error with the AI and it stoped generating, forcing me to use the second option. [ActivityCalendar.py](./ActivityCalendar.py).

### Back to fixing that error

Starting with [ActivityCalendar.py](./ActivityCalendar.py) i gave it a full stack trace of the error to try and work with.

```py
# The error still occurs, here is a full stack trace. Please fix

Traceback (most recent call last):
  File "/mnt/d/Code/AI/CalendarCreate/ActivityCalendar.py", line 33, in <module>
    calendar = ActivityCalendar('data.txt')
  File "/mnt/d/Code/AI/CalendarCreate/ActivityCalendar.py", line 7, in __init__
    self.load_data(filename)
  File "/mnt/d/Code/AI/CalendarCreate/ActivityCalendar.py", line 17, in load_data
    current_date = datetime.datetime.strptime(
  File "/usr/lib/python3.10/_strptime.py", line 568, in _strptime_datetime
    tt, fraction, gmtoff_fraction = _strptime(data_string, format)
  File "/usr/lib/python3.10/_strptime.py", line 352, in _strptime
    raise ValueError("unconverted data remains: %s" %
ValueError: unconverted data remains:  -- Teacher strike day (1)
```

After making [ActivityCalendar2.py](./ActivityCalendar2.py) and some modifications (just modifiy the function, no point in making a whole new file) we finally got back to something working.

### Okay, now we can continue the polish

So originally i asked it to rewrite without using `elif` or `else` and i suppose i didn't specify enough here because it started to rewrite that function. So instead i just gave it the whole program and started again.

I also added in to use docstrings where necessary

After [ActivityCalendar2.py](./Activites2.py) was rewritten, out comes [ActivityCalendar3.py](./ActivityCalendar3.py) The furthest we have been since the begining, After a bit of back and forth, fixing some issues we come to [ActivityCalendar4.py](./ActivityCalendar4.py) which previously had different docstrings but changed shortly afterwards. This program worked and just needed some refining.

This refining consisted of adding types and docstrings (because it removed the docstrings when i told id to add the types.) and pretty much, it was done except for one thing.

### Using user input instead of hardcoded data

Ah yeah, user input. Easy question easy answer. After also asking it to move the `__main__.py` statements, we come to [ActivityCalendar4.py](./ActivityCalendar4.py) and [main2.py](./main2.py) these allow for the user input and keeps it seperated from the actual file itself.

## Part 1 end

And that concludes this part. A program which lets me select any day and get the output for it, also allows for easy expandablitly.

## Part 2 - UI

So i attempted to add ui to this program, i might contain i might not but these attempts so far have not been promosing.

### The first generation

Meet [ui.py](./ui.py) the first attempt which already failed, Tried to use something that does not exist. And then i corrected it, and it used different none-existant modules. I might attempt to make it use a UI at some point in the future but for now i will leave it here.
