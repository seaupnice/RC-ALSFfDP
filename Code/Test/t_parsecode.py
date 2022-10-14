from os import path, getcwd
import sys
sys.path.append(path.join(getcwd(), 'Code'))

from parsecode.token_vec import TokenV


if __name__ == '__main__':
    filepath = path.join(getcwd(), 'Data', 'tomcat', 'java', 'org', 'apache', 'AnnotationProcessor.java')
    tv = TokenV(filepath)
    print(tv.getTV())