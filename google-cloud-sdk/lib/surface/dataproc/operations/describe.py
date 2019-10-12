# -*- coding: utf-8 -*- #
# Copyright 2015 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Describe operation command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.dataproc import dataproc as dp
from googlecloudsdk.api_lib.dataproc import util
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.dataproc import flags


class Describe(base.DescribeCommand):
  """View the details of an operation.

  View the details of an operation.

  ## EXAMPLES

  To view the details of an operation, run:

    $ {command} operation_id
  """

  @staticmethod
  def Args(parser):
    flags.AddOperationFlag(parser, 'describe')

  def Run(self, args):
    dataproc = dp.Dataproc(self.ReleaseTrack())

    operation_ref = util.ParseOperation(args.operation, dataproc)

    request = dataproc.messages.DataprocProjectsRegionsOperationsGetRequest(
        name=operation_ref.RelativeName())

    operation = dataproc.client.projects_regions_operations.Get(request)
    return operation
