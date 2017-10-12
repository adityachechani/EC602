"""this is the main part of the assignment"""
# Copyright 2017 Aditya adityac@bu.edu
# Copyright 2017 Aditya aditya28@bu.edu
# Copyright 2017 Abhi abhivora@bu.edu

import unittest
import subprocess
		
#please change this to valid author emails
AUTHORS = ['adityac@bu.edu', 'aditya28@bu.edu', 'abhivora@bu.edu']

PROGRAM_TO_TEST = "collisionc_0"

def runprogram(program, args, inputstr):
    coll_run = subprocess.run(
        [program, *args],
        input=inputstr.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, timeout = 0.2)

    ret_code = coll_run.returncode
    program_output = coll_run.stdout.decode()
    program_errors = coll_run.stderr.decode()
    return (ret_code, program_output, program_errors)


class CollisionTestCase(unittest.TestCase):
    "empty class - write this"
	    


    def test_initial(self):
        strin = "one 10 0 1 0\ntwo 21 0 0 0"
        correct_out = "2\none 11 0 0 0\ntwo 22 0 1 0\n"          
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2"],strin)
        outarray= out.split("\n")
        correct_outarray= correct_out.split("\n")
        self.assertEqual(rc,0)
        self.assertEqual(outarray[0],correct_outarray[0])
        self.assertEqual(outarray[1:],correct_outarray[1:])
        #self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")



    def test_long_inputs(self):
        strin = "one 1000000000000 0 1 0\ntwo 2100000000000 0 0 0"
        correct_out = "21000000\none 1.000021e+12 0 1 0\ntwo 2.1e+12 0 0 0\n"          
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["21000000"],strin)
        outarray= out.split("\n")
        correct_outarray= correct_out.split("\n")
        self.assertEqual(rc,0)
        self.assertEqual(outarray[0],correct_outarray[0])
        self.assertEqual(outarray[1:],correct_outarray[1:])
        #self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")


    def test_multiple_times(self):
        strin = "one 10 0 1 0\ntwo 21 0 0 0"
        correct_out = "2\none 11 0 0 0\ntwo 22 0 1 0\n5\none 11 0 0 0\ntwo 25 0 1 0\n"         
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2","5"],strin)
        outarray= out.split("\n")
        correct_outarray= correct_out.split("\n")
        self.assertEqual(rc,0)
        self.assertEqual(outarray[0],correct_outarray[0])
        self.assertEqual(outarray[1:],correct_outarray[1:])
        #self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")


    # def test_multiple_times_reversed(self):
    #     strin = "one 10 0 1 0\ntwo 21 0 0 0"
    #     correct_out = "5\none 11 0 0 0\ntwo 25 0 1 0\n2\none 11 0 0 0\ntwo 27 0 1 0\n"         
    #     (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["5","2"],strin)
    #     outarray= out.split("\n")
    #     correct_outarray= correct_out.split("\n")
    #     self.assertEqual(rc,0)
    #     self.assertEqual(outarray[0],correct_outarray[0])
    #     self.assertEqual(outarray[1:],correct_outarray[1:])
    #     #self.assertEqual(out,correct_out)
    #     self.assertEqual(errs,"")





    # def test_single_input(self):
    #     strin = "one 10 0 1 0"
    #     #correct_out = "2\none 11 0 0 0\ntwo 22 0 1 0\n"          
    #     (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2"],strin)
    #     self.assertEqual(rc,2)
        #self.assertEqual(out,correct_out)
        #self.assertEqual(errs,"")

    def test_decimal(self):	
        strin = "one 1.2 2.5 1 0\ntwo 13.8 8.9 -1 0"
        correct_out = "3\none 3.5601545 1.9670556 -0.1808 -0.98351988\ntwo 11.439845 9.4329444 0.1808 0.98351988\n"          
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        outarray= out.split("\n")
        correct_outarray= correct_out.split("\n")
        self.assertEqual(rc,0)
        self.assertEqual(outarray[0],correct_outarray[0])
        self.assertEqual(outarray[1:],correct_outarray[1:])
        #self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
        #if out == ("3\none 3.560155 1.967056 -0.181 -0.9835199\ntwo 11.43985 9.432944 0.181 0.9835199\n"):
        	#self.assertEqual(rc,0)

    	#else if (out == "3\none 3.56016 1.96706 -0.181 -0.98352\ntwo 11.4399 9.43294 0.181 0.9835200\n"):
        	#self.assertEqual(rc,0)

    	#else if out == ("3\none 3.560 1.967 -0.181 -0.984\ntwo 11.440 9.433 0.181 0.984\n"):
        	#self.assertEqual(rc,0)

    	#else (out == "3\none 3.56 1.97 -0.18 -0.98\ntwo 11.44 9.43 0.18 0.98\n"):
        
    def test_one_char_input(self):	
        strin = "one a 2.5 1 0\ntwo 13.8 b -1 0"
        #correct_out = "3\none 3.5601545 1.9670556 -0.1808 -0.98351988\ntwo 11.439845 9.4329444 0.1808 0.98351988\n"          
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,1)
        # outarray= out.split("\n")
        # correct_outarray= correct_out.split("\n")
        # #self.assertEqual(rc,0)
        # self.assertEqual(outarray[0],correct_outarray[0])
        # self.assertEqual(outarray[1:],correct_outarray[1:])
        # self.assertEqual(out,correct_out)
        # self.assertEqual(errs,"")

        # self.assertEqual(out,correct_out)
        # self.assertEqual(errs,"")

    # def test_double_decimal_point(self):	
    #     strin = "one 1..2 2.5 1 0\ntwo 13.8 8.9 -1 0"
    #     (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
    #     self.assertEqual(rc,1)
    
    def test_char_timer(self):	
        strin = "one 1 2 0 1\ntwo 13 9 -2 -1"         
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["i"],strin)
        self.assertEqual(rc,2)
        #outarray= out.split("\n")
        # correct_outarray= correct_out.split("\n")
        # #self.assertEqual(rc,0)
        # self.assertEqual(outarray[0],correct_outarray[0])
        # self.assertEqual(outarray[1:],correct_outarray[1:])
        # #self.assertEqual(out,correct_out)
        # self.assertEqual(errs,"")


    def test_extra_input(self):	
        strin = "one 1 2 0 1 0\ntwo 13 9 -2 -1"         
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
        self.assertEqual(rc,1)
        # outarray= out.split("\n")
        # correct_outarray= correct_out.split("\n")
        # #self.assertEqual(rc,0)
        # self.assertEqual(outarray[0],correct_outarray[0])
        # self.assertEqual(outarray[1:],correct_outarray[1:])
        # #self.assertEqual(out,correct_out)
        # self.assertEqual(errs,"")


    # def test_time_long(self):
    #     strin = "one 1000 1000 0 0\ntwo 10000 1000 -1 0"         
    #     correct_out = "1000\none 1000 1000 0 0\ntwo 9000 1000 -1 0\n"
    #     (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1000"],strin)
    #     outarray= out.split("\n")
    #     correct_outarray= correct_out.split("\n")
    #     self.assertEqual(rc,0)
    #     self.assertEqual(outarray[0],correct_outarray[0])
    #     self.assertEqual(outarray[1:],correct_outarray[1:])
    #     #self.assertEqual(out,correct_out)
    #     self.assertEqual(errs,"")



    # def test_time_long_collide(self):
    #     strin = "one 1000 1000 0 0\ntwo 5000 1000 -1 0"         
    #     correct_out = "6000\none -1010 1000 -1 0\ntwo 1010 1000 0 0\n"          
    #     (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["6000"],strin)
    #     outarray= out.split("\n")
    #     correct_outarray= correct_out.split("\n")
    #     self.assertEqual(rc,0)
    #     self.assertEqual(outarray[0],correct_outarray[0])
    #     self.assertEqual(outarray[1:],correct_outarray[1:])
    #     #self.assertEqual(out,correct_out)
    #     self.assertEqual(errs,"")



    # def test_programname(self):
    #     self.assertTrue(PROGRAM_TO_TEST.startswith('col'),"wrong program name")

def main():
    "show how to use runprogram"

    # print(runprogram('./test_program.py', ["4", "56", "test"], "my input"))
    unittest.main()

if __name__ == '__main__':
    main()
