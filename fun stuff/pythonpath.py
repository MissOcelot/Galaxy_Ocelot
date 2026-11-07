from pyscript import document
from pyodide.ffi import create_proxy

current_path = "start"
event_handlers = []

def add_click(button, callback):
    proxy = create_proxy(lambda event: callback())
    event_handlers.append(proxy)
    button.addEventListener("click", proxy)

def show_step(step):
    global current_path

    options_div = document.getElementById("options")
    options_div.innerHTML = ""
  
    
    if "results" in step:
      for name in step["results"]:
            item = document.createElement("p")
            item.id = "results"
            item.className = name.lower().replace(" ", "-")
            item.innerText = name
            options_div.appendChild(item)
      results_container = document.createElement("div")
      results_container.id = "results-container"
      heading = document.createElement("h2")
      heading.innerText = "You got..."
      heading.id = "result-heading"
      aflink = document.createElement("h2")
      aflink.innerText = "ArtFight Page \n Character Page"
      results_container.appendChild(heading)
      options_div.appendChild(results_container)
      

      return

    current_path = step["path"]

    for option in step["options"]:
        button = document.createElement("button")
        button.innerText = option
        add_click(button, lambda answer=option: handle_choice(answer))
        options_div.appendChild(button)


def handle_choice(choice):
    show_step(Characterpicker(current_path, choice))


def Characterpicker(path, choice):
    if path == "start":
        if choice == "Animal":
              return{"options": ["Mammal","Bird","Fish"],
                    "path": "animal"}
        else:
              return{"options": ["Warrior Cats", "Animal Jam", "WildCraft", "MaraPets", "Fer.al"],
                    "path": "Fandom"}
    elif path == "animal":
          if choice == "Mammal":
                return{"options": ["Canine", "Feline", "Rodent", "Mythical", "Hybrid"],
                      "path": "Mammal"}
          elif choice == "Bird":
                return{"results": ["Lennie"]}
          else:
                return{"results": ["Sunny", "Rainy"]}
    elif path == "Mammal":
          if choice == "Canine":
                return{"options":["Fox", "Dog"],
                       "path":"Canine"}
          elif choice == "Feline":
                return{"options": ["Big cats", "Small cats"],
                       "path": "Feline"}
          elif choice == "Rodent":
                return{"results": ["Azara"]}
          elif choice == "Mythical":
                return{"results": ["Ecosia", "Evosia"]}
          else:
                return{"results": ["Kaliau", "Kavik"]}
    elif path == "Canine":
          if choice == "Fox":
                return{"results": ["Honeydew", "Yukichas"]}
          else:
                return{"results": ["Harley", "Mika", "Maybell", "Sandy"]}
    elif path == "Feline":
          if choice == "Big cats":
                return{"options": ["Snow Leopard", "Sabertooth Tiger", "Lynx"],
                       "path": "Big cats"}
          else:
                return{"options": ["Realistic", "Not Realistic"],
                       "path": "Small cats"}
    elif path == "Small cats":
          if choice == "Realistic":
                return{"options": ["Tabby","Tuxedo","Tortishell","Calico","Black","Ticked"],
                       "path": "Realistic"}
          if choice == "Not Realistic":
                return {"options": ["Winged", "No wings"],
                        "path": "Not Realistic"}
    elif path == "Big cats":
          if choice == "Snow Leopard": 
                return{"results": ["Mycil", "Lightning"]}
          if choice == "Sabertooth Tiger":
                return{"results":["Celise"]}
          if choice == "Lynx":
                return{"results": ["Chaske"]}
    elif path == "Realistic": 
          if choice == "Tabby":
                return{"options":["Grey Tabby", "Brown Tabby", "Orange Tabby"],
                       "path": "Tabby"}
          if choice == "Black":
                return{"results": ["Johnny", "Mazy", "Jax"]}
          if choice == "Tuxedo":
                return{"results": ["EmberTail", "Max"]}
          if choice == "Tortishell":
                return{"results": ["HazelMist"]}
          if choice == "Calico":
                return{"results": ["Calie", "Esme"]}
          if choice == "Ticked":
                return{"results": ["Siouxwu"]}
    elif path == "Tabby":
          if choice == "Grey Tabby":
                return{"results": ["WhisperSong"]}
          if choice == "Brown Tabby":
                return{"results": ["EmberTail"]}
          if choice == "Orange Tabby":
                return{"results":["Miyoni"]}
    elif path == "Not Realistic":
          if choice == "Winged":
                return{"results": ["Anglais", "ColorZip"]}
          if choice == "No wings":
                return{"options": ["Mostly greyscale", "Colorful"],
                       "path": "No wings"}
    elif path == "No wings":
          if choice == "Mostly greyscale":
                return{"results": ["Damore", "Smear", "Mintie"]}
          else: 
                return{"results": ["Celise", "Hex", "Qiztote", "Duskstep"]}
    elif path == "Fandom":
          if choice == "Warrior Cats":
                return{"options": ["Clan cats", "Kittypets"],
                       "path": "Warrior Cats"}
          if choice == "Animal Jam":
                return{"options": ["Squirrel", "Snow Leopard"],
                       "path": "Animal Jam"}
          if choice == "MaraPets":
                return{"options": ["Hybrid", "Fox"],
                       "path": "MaraPets"}
          if choice == "WildCraft":
                return{"results": ["Chaske"]}
          if choice == "Fer.al":
                return{"results": ["Ecosia", "Evosia"]}
    elif path == "Warrior Cats":
        if choice == "Clan cats":
              return{"options": ["Medicine Cat", "Warrior"],
               "path": "Clan cats"}
        if choice == "Kittypets":
              return{"results": ["Mazy", "Johnny", "Jax", "Max"]}
    elif path == "Clan cats":
        if choice == "Warrior":
              return{"results": ["HazelMist", "EmberTail"]}
        if choice == "Medicine Cat":
              return{"results": ["WhisperSong"]}
    elif path == "Animal Jam":
        if choice == "Squirrel":
              return{"results": ["Azara"]}
        if choice == "Snow Leopard":
              return{"results": ["Lightning"]}
    elif path == "MaraPets":
        if choice == "Hybrid":
              return{"results": ["Kaliau"]}
        if choice == "Fox":
              return{"results":["Yukichas"]}
    else:
        return {"results": ["Uh oh. Something went wrong. How did you get here? Refresh and try again. Call ocelot i guess."]}

def start_over():
    show_step({
        "options": ["Animal", "Fandom"],
        "path": "start"
    })

restart_button = document.getElementById("restart-button")
add_click(restart_button, start_over)

start_over()
    