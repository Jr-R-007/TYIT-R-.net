#Table Driven Agent
table ={
    ("A", "Clean"): ("Suck"),
    ("A", "Dirty"): ("Right"),
    ("B", "Clean"): ("Suck"),
    ("B", "Dirty"): ("Left")
      }

def table_driven_agent(percept):
    return table.get(percept)
                    
                     