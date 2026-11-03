ROADMAP = ["Learn Coding Basics", "Learn Linux", "Learn Git", "Build a Bookbot",
           "Learn Object Oriented Programming", "Build an AI Agent",
           "Learn Statistics for Programmers", "Learn Retrieval Augmented Generation"]


def next_course(done):
    for course in ROADMAP:
        if course not in done:
            return course
    return "all done"


my_done = set()  # e.g. {"Learn Coding Basics"}
print("Next up:", next_course(my_done))
