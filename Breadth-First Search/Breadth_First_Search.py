from Graph import Graph
from Node import Node

dinner = ["Steve Guttenberg",
          "Daniel Stern",
          "Mickey Rourke",
          "Kevin Bacon",
          "Tim Daly",
          "Ellen Barkin",
          "Paul Reiser",
          "Kathryn Dowling",
          "Michael Tucker",
          "Jessica James",
          "Colette Blonigan",
          "Kelle Kipp",
          "Clement Fowler",
          "Claudia Cron"]
footloose = ["Kevin Bacon",
             "Lori Singer",
             "Dianne Wiest",
             "John Lithgow",
             "Sarah Jessica Parker",
             "Chris Penn",
             "Frances Lee McCain",
             "Jim Youngs",
             "John Laughlin",
             "Lynne Marta",
             "Douglas Dirkson"]
flatliners = ["Kiefer Sutherland",
              "Julia Roberts",
              "Kevin Bacon",
              "William Baldwin",
              "Oliver Platt",
              "Kimberly Scott",
              "Joshua Rudoy",
              "Benjamin Mouton",
              "Hope Davis",
              "Patricia Belcher",
              "Beth Grant"]
eatPrayLove = ["Julia Roberts",
               "Javier Bardem",
               "Billy Crudup",
               "Richard Jenkins",
               "Viola Davis",
               "James Franco",
               "Sophie Thompson",
               "Mike O 'Malley",
               "Christine Hakim",
               "Arlene Tur",
               "Hadi Subiyanto",
               "Gita Reddy",
               "Tuva Novotny",
               "Luca Argentero",
               "Rushita Singh"]
spotlight = ["Mark Ruffalo",
             "Michael Keaton",
             "Rachel McAdams",
             "Liev Schreiber",
             "John Slattery",
             "Brian d'Arcy James",
             "Stanley Tucci",
             "Gene Amoroso",
             "Jamey Sheridan",
             "Billy Crudup",
             "Maureen Keiller",
             "Richard Jenkins",
             "Paul Guilfoyle",
             "Len Cariou",
             "Neal Huff",
             "Michael Cyril Creighton",
             "Laurie Heineman",
             "Tim Progosh"]

movies = [dinner, footloose, flatliners, eatPrayLove, spotlight]
movieTitles = ["Dinner", "Footloose", "Flatliners", "Eat Pray Love", "Spotlight"]
graph = Graph()

for num in range(len(movieTitles)):
    movieNode = Node(movieTitles[num])
    graph.addNode(movieNode)

    for actor in movies[num]:
        actorNode = graph.getNode(actor)
        if actorNode is None:
            actorNode = Node(actor)

        movieNode.addEdge(actorNode)
        graph.addNode(actorNode)

start = graph.setStart("Rachel McAdams")
end = graph.setEnd("Kevin Bacon")

queue = []

start.searched = True
queue.append(start)

while len(queue) > 0:
    current = queue.pop(0)
    print(current.value)
    if current == end:
        print("found")
        break;

    for node in current.edges:
        if not node.searched:
            node.searched = True
            node.parent = current
            queue.append(node)

path = [end.value]
next = end.parent

while next is not None:
    path.append(next.value)
    next = next.parent

path.reverse()
print(path)


