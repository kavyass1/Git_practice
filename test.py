import argparse
parser=argparse.ArgumentParser()
parser.add_argument('name', type=str, help="Pass the name of the employee")
parser.add_argument('job', type=str, help = "Pass the Designation of the employee")
args = parser.parse_args()
print('Hello,', args.name)
print('Designation,', args.job)
