
def main():
    fp = open('/tmp/file_created_by_python_script.txt', 'w')
    fp.write('first line')
    fp.close()

if __name__ == "__main__":
    main()
