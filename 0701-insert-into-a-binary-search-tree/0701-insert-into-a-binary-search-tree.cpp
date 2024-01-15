/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (root == nullptr) {
            return new TreeNode(val);
        }

        TreeNode* current = root;
        while (current != nullptr) {
            if (current->val < val) {
                if (current->right == nullptr) {
                    current->right = new TreeNode(val);
                    break;
                } else {
                    current = current->right;
                }
            } else if (current->val > val) {
                if (current->left == nullptr) {
                    current->left = new TreeNode(val);
                    break;
                } else {
                    current = current->left;
                }
            }
        }

        return root;
    }
};
