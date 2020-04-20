import git
from datetime import datetime



git.Git("./freebsd_"+datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")).clone("https://github.com/freebsd/freebsd")
