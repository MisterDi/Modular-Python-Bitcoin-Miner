# Modular Python Bitcoin Miner
# Copyright (C) 2012 Michael Sparmann (TheSeven)
#
#     This program is free software; you can redistribute it and/or
#     modify it under the terms of the GNU General Public License
#     as published by the Free Software Foundation; either version 2
#     of the License, or (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program; if not, write to the Free Software
#     Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# Please consider donating to 1PLAPWDejJPJnY2ppYCgtw5ko8G5Q4hPzh if you
# want to support further development of the Modular Python Bitcoin Miner.



##################################################
# Dummy (single work source) block chain manager #
##################################################



class DummyBlockchain(object):


  def __init__(self, core):
    # Initialize job list (protected by global job queue lock)
    self.jobs = []
    
    
  def add_job(self, job):
    if not job in self.jobs: self.jobs.append(job)
  

  def remove_job(self, job):
    while job in self.jobs: self.jobs.remove(job)
    
    
  def add_work_source(self, worksource):
    pass


  def remove_work_source(self, worksource):
    pass


  def handle_block(self):
    for job in self.jobs: job.cancel()
    self.jobs = []
    self.core.notify_job_canceled()
