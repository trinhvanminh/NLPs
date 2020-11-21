import re
str = '''
<li class="task-list-item">
    <input checked="" class="task-list-item-checkbox" disabled="" id="" type="checkbox">
        Increasing the training set size generally does not hurt an algorithm’s performance, and it may help significantly.
    </input>
</li>
'''

a = re.findall(r'(?<=>\t).*(?=\n\t</input>)',str)

print(a)