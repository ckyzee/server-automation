import git
from datetime import datetime

datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")
git.Git("./freebsd_"+datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")).clone("https://github.com/freebsd/freebsd")
