# Author: Prabhu Ramachandran <prabhu_r at users dot sf dot net>
# Copyright (c) 2006, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import Instance
from enthought.tvtk.api import tvtk

# Local imports
from enthought.mayavi.filters.cell_to_point_data import CellToPointData
from enthought.mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `PointToCellData` class.
######################################################################
class PointToCellData(CellToPointData):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.PointDataToCellData, args=(), allow_none=False, listen=True)
    
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['point'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['cell'],
                               attributes=['any'])

