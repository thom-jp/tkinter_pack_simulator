# tkinter_pack_simulator
This is python tkinter GUI pack method simulator

# How to Use
1. Run script by python3
```bash
python packsim.py
```
(for my environment, "python" indicates python3)

2. Configure items by bottom control panel

![image](https://user-images.githubusercontent.com/11180273/152720220-4496b305-90c9-4b73-a8d9-b908f8757751.png)

|Control|Type|Explanation|
|---|---|---|
|pack|Checkbox|An item will be created on simulation window when checked it.<br>Every other configurations of an item are meaningless when it's unchecked.<br>By default, 4 items are selected.|
|side|Combobox|An item will be packed on a selected side|
|fill|Combobox|An item will try to be filled selected direction.<br>It's limited by occupied area.|
|expand|Checkbox|An item will try to expand occupied area.|

That's all.
It'll be nice if it helps someone confusing about "pack" layout method of tkinter.

# Note
Packing order is always start from youngest number of items regardless your configuration operation.
When you change something, actually all items are once deleted and re-packed again.

# About what I didn't implement
Sorry I was lazy to implement configuration reset feature.
I knwo that reset feature wll be quite helpful but I think this is not an application used repeatedly after user understand how pack works.
So, instead of taking effort on this, I'd like to focus on something more effective.
