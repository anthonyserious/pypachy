# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2
import google.protobuf.wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import pypachy.pfs_pb2 as pfs__pb2


class APIStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateRepo = channel.unary_unary(
        '/pfs.API/CreateRepo',
        request_serializer=pfs__pb2.CreateRepoRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.InspectRepo = channel.unary_unary(
        '/pfs.API/InspectRepo',
        request_serializer=pfs__pb2.InspectRepoRequest.SerializeToString,
        response_deserializer=pfs__pb2.RepoInfo.FromString,
        )
    self.ListRepo = channel.unary_unary(
        '/pfs.API/ListRepo',
        request_serializer=pfs__pb2.ListRepoRequest.SerializeToString,
        response_deserializer=pfs__pb2.RepoInfos.FromString,
        )
    self.DeleteRepo = channel.unary_unary(
        '/pfs.API/DeleteRepo',
        request_serializer=pfs__pb2.DeleteRepoRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.StartCommit = channel.unary_unary(
        '/pfs.API/StartCommit',
        request_serializer=pfs__pb2.StartCommitRequest.SerializeToString,
        response_deserializer=pfs__pb2.Commit.FromString,
        )
    self.ForkCommit = channel.unary_unary(
        '/pfs.API/ForkCommit',
        request_serializer=pfs__pb2.ForkCommitRequest.SerializeToString,
        response_deserializer=pfs__pb2.Commit.FromString,
        )
    self.FinishCommit = channel.unary_unary(
        '/pfs.API/FinishCommit',
        request_serializer=pfs__pb2.FinishCommitRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ArchiveCommit = channel.unary_unary(
        '/pfs.API/ArchiveCommit',
        request_serializer=pfs__pb2.ArchiveCommitRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.InspectCommit = channel.unary_unary(
        '/pfs.API/InspectCommit',
        request_serializer=pfs__pb2.InspectCommitRequest.SerializeToString,
        response_deserializer=pfs__pb2.CommitInfo.FromString,
        )
    self.ListCommit = channel.unary_unary(
        '/pfs.API/ListCommit',
        request_serializer=pfs__pb2.ListCommitRequest.SerializeToString,
        response_deserializer=pfs__pb2.CommitInfos.FromString,
        )
    self.DeleteCommit = channel.unary_unary(
        '/pfs.API/DeleteCommit',
        request_serializer=pfs__pb2.DeleteCommitRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.FlushCommit = channel.unary_unary(
        '/pfs.API/FlushCommit',
        request_serializer=pfs__pb2.FlushCommitRequest.SerializeToString,
        response_deserializer=pfs__pb2.CommitInfos.FromString,
        )
    self.ListBranch = channel.unary_unary(
        '/pfs.API/ListBranch',
        request_serializer=pfs__pb2.ListBranchRequest.SerializeToString,
        response_deserializer=pfs__pb2.Branches.FromString,
        )
    self.SquashCommit = channel.unary_unary(
        '/pfs.API/SquashCommit',
        request_serializer=pfs__pb2.SquashCommitRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ReplayCommit = channel.unary_unary(
        '/pfs.API/ReplayCommit',
        request_serializer=pfs__pb2.ReplayCommitRequest.SerializeToString,
        response_deserializer=pfs__pb2.Commits.FromString,
        )
    self.PutFile = channel.stream_unary(
        '/pfs.API/PutFile',
        request_serializer=pfs__pb2.PutFileRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetFile = channel.unary_stream(
        '/pfs.API/GetFile',
        request_serializer=pfs__pb2.GetFileRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_wrappers__pb2.BytesValue.FromString,
        )
    self.InspectFile = channel.unary_unary(
        '/pfs.API/InspectFile',
        request_serializer=pfs__pb2.InspectFileRequest.SerializeToString,
        response_deserializer=pfs__pb2.FileInfo.FromString,
        )
    self.ListFile = channel.unary_unary(
        '/pfs.API/ListFile',
        request_serializer=pfs__pb2.ListFileRequest.SerializeToString,
        response_deserializer=pfs__pb2.FileInfos.FromString,
        )
    self.DeleteFile = channel.unary_unary(
        '/pfs.API/DeleteFile',
        request_serializer=pfs__pb2.DeleteFileRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.DeleteAll = channel.unary_unary(
        '/pfs.API/DeleteAll',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ArchiveAll = channel.unary_unary(
        '/pfs.API/ArchiveAll',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class APIServicer(object):

  def CreateRepo(self, request, context):
    """Repo rpcs
    CreateRepo creates a new repo.
    An error is returned if the repo already exists.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InspectRepo(self, request, context):
    """InspectRepo returns info about a repo.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListRepo(self, request, context):
    """ListRepo returns info about all repos.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteRepo(self, request, context):
    """DeleteRepo deletes a repo.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartCommit(self, request, context):
    """Commit rpcs
    StartCommit creates a new write commit from a parent commit.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ForkCommit(self, request, context):
    """Fork creates a commit on a new branch.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FinishCommit(self, request, context):
    """FinishCommit turns a write commit into a read commit.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ArchiveCommit(self, request, context):
    """ArchiveCommit marks commits as archived, it will be excluded from ListCommit.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InspectCommit(self, request, context):
    """InspectCommit returns the info about a commit.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListCommit(self, request, context):
    """ListCommit returns info about all commits.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteCommit(self, request, context):
    """DeleteCommit deletes a commit.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FlushCommit(self, request, context):
    """FlushCommit waits for downstream commits to finish
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListBranch(self, request, context):
    """ListBranch returns info about the heads of branches.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SquashCommit(self, request, context):
    """Squash returns the head of the commit of the merge
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReplayCommit(self, request, context):
    """Replay returns the head of the commit of the merge
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PutFile(self, request_iterator, context):
    """File rpcs
    PutFile writes the specified file to pfs.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFile(self, request, context):
    """GetFile returns a byte stream of the contents of the file.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InspectFile(self, request, context):
    """InspectFile returns info about a file.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListFile(self, request, context):
    """ListFile returns info about all files.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteFile(self, request, context):
    """DeleteFile deletes a file.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteAll(self, request, context):
    """DeleteAll deletes everything
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ArchiveAll(self, request, context):
    """ArchiveAll archives everything
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_APIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateRepo': grpc.unary_unary_rpc_method_handler(
          servicer.CreateRepo,
          request_deserializer=pfs__pb2.CreateRepoRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'InspectRepo': grpc.unary_unary_rpc_method_handler(
          servicer.InspectRepo,
          request_deserializer=pfs__pb2.InspectRepoRequest.FromString,
          response_serializer=pfs__pb2.RepoInfo.SerializeToString,
      ),
      'ListRepo': grpc.unary_unary_rpc_method_handler(
          servicer.ListRepo,
          request_deserializer=pfs__pb2.ListRepoRequest.FromString,
          response_serializer=pfs__pb2.RepoInfos.SerializeToString,
      ),
      'DeleteRepo': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteRepo,
          request_deserializer=pfs__pb2.DeleteRepoRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'StartCommit': grpc.unary_unary_rpc_method_handler(
          servicer.StartCommit,
          request_deserializer=pfs__pb2.StartCommitRequest.FromString,
          response_serializer=pfs__pb2.Commit.SerializeToString,
      ),
      'ForkCommit': grpc.unary_unary_rpc_method_handler(
          servicer.ForkCommit,
          request_deserializer=pfs__pb2.ForkCommitRequest.FromString,
          response_serializer=pfs__pb2.Commit.SerializeToString,
      ),
      'FinishCommit': grpc.unary_unary_rpc_method_handler(
          servicer.FinishCommit,
          request_deserializer=pfs__pb2.FinishCommitRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ArchiveCommit': grpc.unary_unary_rpc_method_handler(
          servicer.ArchiveCommit,
          request_deserializer=pfs__pb2.ArchiveCommitRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'InspectCommit': grpc.unary_unary_rpc_method_handler(
          servicer.InspectCommit,
          request_deserializer=pfs__pb2.InspectCommitRequest.FromString,
          response_serializer=pfs__pb2.CommitInfo.SerializeToString,
      ),
      'ListCommit': grpc.unary_unary_rpc_method_handler(
          servicer.ListCommit,
          request_deserializer=pfs__pb2.ListCommitRequest.FromString,
          response_serializer=pfs__pb2.CommitInfos.SerializeToString,
      ),
      'DeleteCommit': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteCommit,
          request_deserializer=pfs__pb2.DeleteCommitRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'FlushCommit': grpc.unary_unary_rpc_method_handler(
          servicer.FlushCommit,
          request_deserializer=pfs__pb2.FlushCommitRequest.FromString,
          response_serializer=pfs__pb2.CommitInfos.SerializeToString,
      ),
      'ListBranch': grpc.unary_unary_rpc_method_handler(
          servicer.ListBranch,
          request_deserializer=pfs__pb2.ListBranchRequest.FromString,
          response_serializer=pfs__pb2.Branches.SerializeToString,
      ),
      'SquashCommit': grpc.unary_unary_rpc_method_handler(
          servicer.SquashCommit,
          request_deserializer=pfs__pb2.SquashCommitRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ReplayCommit': grpc.unary_unary_rpc_method_handler(
          servicer.ReplayCommit,
          request_deserializer=pfs__pb2.ReplayCommitRequest.FromString,
          response_serializer=pfs__pb2.Commits.SerializeToString,
      ),
      'PutFile': grpc.stream_unary_rpc_method_handler(
          servicer.PutFile,
          request_deserializer=pfs__pb2.PutFileRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetFile': grpc.unary_stream_rpc_method_handler(
          servicer.GetFile,
          request_deserializer=pfs__pb2.GetFileRequest.FromString,
          response_serializer=google_dot_protobuf_dot_wrappers__pb2.BytesValue.SerializeToString,
      ),
      'InspectFile': grpc.unary_unary_rpc_method_handler(
          servicer.InspectFile,
          request_deserializer=pfs__pb2.InspectFileRequest.FromString,
          response_serializer=pfs__pb2.FileInfo.SerializeToString,
      ),
      'ListFile': grpc.unary_unary_rpc_method_handler(
          servicer.ListFile,
          request_deserializer=pfs__pb2.ListFileRequest.FromString,
          response_serializer=pfs__pb2.FileInfos.SerializeToString,
      ),
      'DeleteFile': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteFile,
          request_deserializer=pfs__pb2.DeleteFileRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'DeleteAll': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAll,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ArchiveAll': grpc.unary_unary_rpc_method_handler(
          servicer.ArchiveAll,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pfs.API', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BlockAPIStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PutBlock = channel.stream_unary(
        '/pfs.BlockAPI/PutBlock',
        request_serializer=pfs__pb2.PutBlockRequest.SerializeToString,
        response_deserializer=pfs__pb2.BlockRefs.FromString,
        )
    self.GetBlock = channel.unary_stream(
        '/pfs.BlockAPI/GetBlock',
        request_serializer=pfs__pb2.GetBlockRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_wrappers__pb2.BytesValue.FromString,
        )
    self.DeleteBlock = channel.unary_unary(
        '/pfs.BlockAPI/DeleteBlock',
        request_serializer=pfs__pb2.DeleteBlockRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.InspectBlock = channel.unary_unary(
        '/pfs.BlockAPI/InspectBlock',
        request_serializer=pfs__pb2.InspectBlockRequest.SerializeToString,
        response_deserializer=pfs__pb2.BlockInfo.FromString,
        )
    self.ListBlock = channel.unary_unary(
        '/pfs.BlockAPI/ListBlock',
        request_serializer=pfs__pb2.ListBlockRequest.SerializeToString,
        response_deserializer=pfs__pb2.BlockInfos.FromString,
        )


class BlockAPIServicer(object):

  def PutBlock(self, request_iterator, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBlock(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteBlock(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InspectBlock(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListBlock(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BlockAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PutBlock': grpc.stream_unary_rpc_method_handler(
          servicer.PutBlock,
          request_deserializer=pfs__pb2.PutBlockRequest.FromString,
          response_serializer=pfs__pb2.BlockRefs.SerializeToString,
      ),
      'GetBlock': grpc.unary_stream_rpc_method_handler(
          servicer.GetBlock,
          request_deserializer=pfs__pb2.GetBlockRequest.FromString,
          response_serializer=google_dot_protobuf_dot_wrappers__pb2.BytesValue.SerializeToString,
      ),
      'DeleteBlock': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteBlock,
          request_deserializer=pfs__pb2.DeleteBlockRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'InspectBlock': grpc.unary_unary_rpc_method_handler(
          servicer.InspectBlock,
          request_deserializer=pfs__pb2.InspectBlockRequest.FromString,
          response_serializer=pfs__pb2.BlockInfo.SerializeToString,
      ),
      'ListBlock': grpc.unary_unary_rpc_method_handler(
          servicer.ListBlock,
          request_deserializer=pfs__pb2.ListBlockRequest.FromString,
          response_serializer=pfs__pb2.BlockInfos.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pfs.BlockAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
