from functools import partial, reduce

lines = read("example_log.txt")
# ip_addresses = list(map(lambda x: x.split()[0], lines))
extract_ips = partial(map, lambda x: x.split()[0])
# iltered_ips = list(filter(lambda x: int(x.split('.')[0]) <= 20, ip_addresses))
extract_filtered = partial(filter, lambda x: int(x.split(".")[0]) <= 20)

my_count = partial(reduce, lambda x, _: 2 if isinstance(x, str) else x + 1)
ratio = count_filtered / count_all
composed = compose(extract_ips, extract_filtered, my_count)
counted = composed(lines)


log = open("example_log.txt")


def parse_log(log):
    for line in log:
        split_line = line.split()
        remote_addr = split_line[0]
        time_local = parse_time(split_line[3] + " " + split_line[4])
        request_type = strip_quotes(split_line[5])
        request_path = split_line[6]
        status = int(split_line[8])
        body_bytes_sent = int(split_line[9])
        http_referrer = strip_quotes(split_line[10])
        http_user_agent = strip_quotes(" ".join(split_line[11:]))
        yield (
            remote_addr,
            time_local,
            request_type,
            request_path,
            status,
            body_bytes_sent,
            http_referrer,
            http_user_agent,
        )


first_line = next(parse_log(log))

import itertools


def build_csv(lines, header=None, file=None):
    def open_file(f):
        # If it's a string, then open the file
        # and return the opened file.
        if isinstance(f, str):
            f = open(f, "w")
        return f

    file = open_file(file)  # add inner function.
    if header:
        lines = itertools.chain([header], lines)
    writer = csv.writer(file, delimiter=",")
    writer.writerows(lines)
    file.seek(0)
    return file


csv_file = build_csv(lines, file="example.csv")

# Iteration 2
import csv


# def count_unique_request(csv_file):
#     reader = csv.reader(csv_file)
#     header = next(reader)
#     idx = header.index("request_type")

#     uniques = {}
#     for line in reader:

#         if not uniques.get(line[idx]):
#             uniques[line[idx]] = 0
#         uniques[line[idx]] += 1
# return uniques


log = open("example_log.txt")
parsed = parse_log(log)
file = open("temporary.csv", "r+")
csv_file = build_csv(
    parsed,
    header=[
        "ip",
        "time_local",
        "request_type",
        "request_path",
        "status",
        "bytes_sent",
        "http_referrer",
        "http_user_agent",
    ],
    file=file,
)
uniques = count_unique_request(csv_file)


def count_unique_request(csv_file):
    reader = csv.reader(csv_file)
    header = next(reader)
    idx = header.index("request_type")

    uniques = {}
    for line in reader:

        if not uniques.get(line[idx]):
            uniques[line[idx]] = 0
        uniques[line[idx]] += 1
    return ((k, v) for k, v in uniques.items())


log = open("example_log.txt")
parsed = parse_log(log)
file = open("temporary.csv", "r+")
csv_file = build_csv(
    parsed,
    header=[
        "ip",
        "time_local",
        "request_type",
        "request_path",
        "status",
        "bytes_sent",
        "http_referrer",
        "http_user_agent",
    ],
    file=file,
)
uniques = count_unique_request(csv_file)
summarized_file = open("summarized.csv", "r+")
summarized_csv = build_csv(
    uniques, header=["request_type", "count"], file=summarized_file
)
print(summarized_csv.readlines())
