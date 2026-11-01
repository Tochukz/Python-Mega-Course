contents = ["Learn python to work DevOps, Machine Learning and Artificial intelligence",
            "Learn System design to design complex scalable and resilient cloud native system",
            "Learn payment systems to work in FinTech and " # broken line string
            "build system that support millions"]
filenames = ["python.txt", "system.txt", "payment.txt"]

for filename, content in zip(filenames, contents):
    file = open(f"outputs/{filename}", "w")
    file.write(content)
    file.close()


# Multi-line string
to_learn = "Learn python" \
    "for machine learning" \
    "and AI"

print(to_learn)