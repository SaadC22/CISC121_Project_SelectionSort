# Selection Sort Visualizer

Step 1  Algorithm Choice
Algorithm Chosen: Selection Sort  
Reason: It was the first sorting algorithm I learnt in Grade 10 CS class, and it stuck with me throughout the years as where I started my journey in CS, so I decided to stick with an old reliable when doing this project.

Step 2  Computational Thinking
Decomposition: Loop through list, find minimum, swap, repeat.  
Pattern Recognition: Repeated comparisons, one swap per pass.  
Abstraction: Show current index, minimum, swaps, list changes; hide Python internals.  
Algorithm Design: User input → convert to list → sort with logs → show output in GUI.

Flowchart:

           ┌───────────────────────────┐
           │ User enters numbers                 │
           └───────────────────────────┘
                          ↓
             ┌────────────────────────┐
             │ Convert to list (ints)          │
             └────────────────────────┘
                           ↓
          ┌────────────────────────────────┐
          │ Start i at 0 (start of array) 			    │
          └────────────────────────────────┘
                                     ↓
         ┌────────────────────────────────────┐
         │ Set min_index = i                 			    │
         └────────────────────────────────────┘
                            ↓
       ┌──────────────────────────────────────────┐
       │ Loop j from i+1 to end of list           				  │
       │ If arr[j] < arr[min_index] update min    				  │
       └──────────────────────────────────────────┘
                               ↓
         ┌───────────────────────────────────────┐
         │ Swap arr[i] and arr[min_index]        				│
         └───────────────────────────────────────┘
                                ↓
           ┌────────────────────────────────────┐
           │ i = i + 1                          			  │
           └────────────────────────────────────┘
                               ↓
                 ┌──────────────────────────┐
                 │ Repeat until end of list           │
                 └──────────────────────────┘
                                ↓
                ┌──────────────────────────┐
                │ Return sorted list + log 			 │
                └──────────────────────────┘

Step 3 Implementation
Selection Sort implemented in Python with step-by-step logging (`selection_sort_steps` function).

Step 4  UI
Gradio interface with input box and step-by-step output.

Step 5  Testing (An Image will be given during the submission)
Tested with:
- `5,2,9,1` → `[1,2,5,9]`
- `1,2,3,4` → `[1,2,3,4]` (already sorted)
- `9,8,7` → `[7,8,9]`
- `5` → `[5]` (single element)
- `5,a,9` → Error message  

All outputs matched expected results.

Step 6  Author & Acknowledgment
Created by Abusaad Cheema for CISC 121.
