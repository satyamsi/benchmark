#!/usr/bin/python 

class benchmark():
    def __init__(self):
        self.parse_args()

    def parse_args(self):
        import argparse
        self.parser = argparse.ArgumentParser(description='System load generator')
        
        self.parser.add_argument('--test-type',          dest='test',     default='files',              help='test type')
        self.parser.add_argument('--file',               dest='filename', default='foo.txt',            help='file name')
        self.parser.add_argument('--num-repitions',      dest='reps',     default=1000000,              help='number of reps')
        
        self.args = self.parser.parse_args()

    # File tests 
    def file_orwc(self):
        fh = open(self.args.filename, "r+")
        s = fh.read(1024)        
        fh.write(s)
        fh.close()

    def file_orwc_loop(self):
        for i in range(0, self.args.reps):
            self.file_orwc()

    # CPU tests 
    def cpu(self):
        for i in range(0, self.args.reps/1000):
            pass

    def cpu_loop(self):
        for i in range(0, self.args.reps):
            self.cpu()

    # Execute tests
    def execute_test(self):
        import datetime
        tstart = datetime.datetime.now()
        print 'Executing: ' + self.args.test + ' - ' + str(tstart)

        if self.args.test == 'files':
            self.file_orwc_loop()
        elif self.args.test == 'cpu':
            self.cpu_loop()
        else:
            pass
        tend = datetime.datetime.now()
        print 'Completed: ' + self.args.test + ' - ' + str(tend) + ' (' + str(tend-tstart) + ')'


# ---------------------------------
# Main 
# ---------------------------------
b = benchmark()

b.execute_test()
