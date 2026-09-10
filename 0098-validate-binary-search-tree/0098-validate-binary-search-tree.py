class Solution(object):

  def isValidBST(self, root):
    def validate(node, low=float('-inf'), high=float('inf')):
      if not node:
        return True

      # Node value must be strictly within bounds
      if not (low < node.val < high):
        return False

      # Left child must be < node.val; Right child must be > node.val
      return validate(node.left, low, node.val) and validate(
          node.right, node.val, high
      )

    return validate(root)
        